from flask import Flask, render_template, request, redirect, url_for
import shelve , Cart , PaymentInfo
from paymentForm import PaymentForm
from storeForms import ItemForm
from product import Product
import datetime
import base64

app = Flask(__name__, static_url_path='/static')



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def store():
    db = shelve.open('storage.db', 'r')
    inventory = db['inventory']
    db.close()

    product_list = []
    fruit_list = []
    vegetable_list = []
    other_list = []

    for key in inventory:
        product = inventory.get(key)
        product_list.append(product)
        if product.get_type() == "fruit":
            fruit_list.append(product)
        elif product.get_type() == "vegetable":
            vegetable_list.append(product)
        else:
            other_list.append(product)

    return render_template('store.html', product_list=product_list, fruit_list=fruit_list, vegetable_list=vegetable_list, other_list=other_list)

@app.route('/store_create', methods=["GET", "POST"])
def store_admin_create():
    itemForm = ItemForm(csrf_enabled=False)
    if itemForm.validate_on_submit():
        inventory = {}
        db = shelve.open('storage.db', 'c')

        try:
            inventory = db['inventory']
        except:
            print('Error in retrieving inventory from storage.db.')
        if len(inventory) == 0:
            product_id = 1
        else:
            product_id = max(inventory.keys())+1
        img_raw = itemForm.img.data
        img_encoded = base64.b64encode(img_raw.read())
        img_string = img_encoded.decode('utf-8')
        product = Product(product_id, itemForm.name.data, img_string, itemForm.type.data, float(itemForm.price.data), str(itemForm.unitNo.data) + " " + str(itemForm.unitType.data), itemForm.stock.data, itemForm.description.data)
        inventory[product.get_product_id()] = product
        db['inventory'] = inventory
        db.close()
        return redirect(url_for('store_admin'))
    return render_template('store_create.html', form=itemForm)


@app.route('/store_update/<int:id>/', methods=['GET', 'POST'])
def store_admin_update(id):
    updateForm = ItemForm(csrf_enabled=False)
    if request.method == 'POST' and updateForm.validate():
        inventory = {}
        db = shelve.open('storage.db', 'w')
        inventory = db['inventory']
        product = inventory.get(id)
        product.set_name(updateForm.name.data)
        img_raw = updateForm.img.data
        img_encoded = base64.b64encode(img_raw.read())
        img_string = img_encoded.decode('utf-8')
        product.set_image(img_string)
        product.set_type(updateForm.type.data)
        product.set_price(updateForm.price.data)
        product.set_unit(str(updateForm.unitNo.data) + " " + str(updateForm.unitType.data))
        product.set_stock(updateForm.stock.data)
        product.set_description(updateForm.description.data)
        db['inventory'] = inventory
        db.close()

        return redirect(url_for('store_admin'))
    else:
        inventory = {}
        db = shelve.open('storage.db', 'r')
        inventory = db['inventory']
        db.close()

        product = inventory.get(id)
        updateForm.name.data = product.get_name()
        updateForm.type.data = product.get_type()
        updateForm.price.data = product.get_price()
        updateForm.unitNo.data = product.get_unitNo()
        updateForm.unitType.data = product.get_unitType()
        updateForm.stock.data = product.get_stock()


        return render_template('store_update.html', form=updateForm)


@app.route('/store_delete/<int:id>/', methods=["POST"])
def store_delete(id):
    inventory = {}
    db = shelve.open('storage.db', 'w')
    inventory = db['inventory']
    inventory.pop(id)
    db['inventory'] = inventory
    db.close()
    return redirect(url_for('store_admin'))
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/sign_up')
def log_in():
    return render_template('sign_up.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/home2')
def home2():
    db = shelve.open('storage.db', 'c')
    try:
        cartDict = db[db['activeUser']+"Cart"]
    except:
        cartDict = {}
    db.close()
    cartList = []
    totalcost = 0
    for key in cartDict:
        cartt = cartDict.get(key)
        cartList.append(cartt)
    for i in cartList:
        totalcost += i.get_cost()
    countcart = len(cartList)
    return render_template('home2.html', countcart = countcart)

@app.route('/store2', methods=['GET', 'POST'])
def store2():

    return render_template('store2.html')


@app.route('/contact_us2')
def contact_us2():
    return render_template('contact_us2.html')

@app.route('/sign_out')
def sign_out():
    return render_template('sign_out.html')




@app.route('/home_admin')
def admin_home():
    return render_template('home_admin.html')

@app.route('/store_admin')
def store_admin():
    db = shelve.open('storage.db', 'r')
    inventory = db['inventory']
    db.close()

    product_list = []
    for key in inventory:
        product = inventory.get(key)
        product_list.append(product)
    return render_template('store_admin.html', product_list=product_list)

@app.route('/order_admin')
def admin_order():
    return render_template('order_admin.html')

@app.route('/admin_voucher')
def admin_voucher():
    return render_template('voucher_admin.html')

@app.route('/offers_admin')
def offers_admin():
    return render_template('offers_admin.html')

@app.route('/voucher')
def voucher():
    return render_template('voucher.html')

@app.route('/admin_statistics')
def statistics():
    return render_template('Statistics.html')


@app.route('/corders')
def corders():
    return render_template('corders.html')

@app.route('/after_login')
def after():
    db = shelve.open('storage.db', 'c')
    try:
        cartDict = db[db['activeUser']+"Cart"]
    except:
        cartDict = {}
    db.close()
    cartList = []
    totalcost = 0
    for key in cartDict:
        cartt = cartDict.get(key)
        cartList.append(cartt)
    for i in cartList:
        totalcost += i.get_cost()
    countcart = len(cartList)
    return render_template('after_login.html', countcart = countcart)

@app.route('/after_admin')
def afteradmin():
    return render_template('after_login_admin.html')

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/event2')
def event2():
    db = shelve.open('storage.db', 'c')
    try:
        cartDict = db[db['activeUser']+"Cart"]
    except:
        cartDict = {}
    db.close()
    cartList = []
    totalcost = 0
    for key in cartDict:
        cartt = cartDict.get(key)
        cartList.append(cartt)
    for i in cartList:
        totalcost += i.get_cost()
    countcart = len(cartList)
    return render_template('event2.html', countcart = countcart)

@app.route('/event_admin')
def event_admin():
    return render_template('event_admin.html')

@app.route('/staff_directory')
def staff_directory():
    return render_template('staff_directory.html')

@app.route('/sign_out_admin')
def sign_out_admin():
    return render_template('sign_out.html')

@app.route('/after_edit_images')
def edit_images():
    return render_template('after_edit_images.html')

@app.route('/retrieveCart')
def retrieveCart():
    cartDict = {}
    db = shelve.open('storage.db', 'c')
    try:
        cartDict = db[db['activeUser']+"Cart"]
    except:
        cartDict = {}
    db.close()
    cartList = []
    totalcost = 0
    for key in cartDict:
        cartt = cartDict.get(key)
        cartList.append(cartt)
    for i in cartList:
        totalcost += i.get_cost()
    countcart = len(cartList)
    if countcart == 0:
        return redirect(url_for('store'))
    else:
        return render_template('cart.html',cartList=cartList, countcart = countcart, totalcost = totalcost)
#def cart():
#    return render_template('cart.html')


@app.route('/deleteItem/<int:id>', methods=['POST'])
def deleteItem(id):
    cartDict = {}
    db = shelve.open('storage.db', 'w')
    cartDict = db[db['activeUser']+"Cart"]
    print('yes')
    print(cartDict)
    print(cartDict[id].get_name())

    cartDict.pop(id)

    db[db['activeUser']+"Cart"] = cartDict
    db.close()

    return redirect(url_for('retrieveCart'))

@app.route('/minusItem/<int:id>', methods=['GET','POST'])
def minusItem(id):
    cartDict = {}
    db = shelve.open('storage.db', 'c')
    cartDict = db[db['activeUser']+"Cart"]

    cart = cartDict.get(id)
    if cart.get_uType() == "g":
        cart.set_quantity(cart.get_quantity()-cart.get_unit())
        if cart.get_quantity() <= 0:
            cartDict.pop(id)
        cart.set_cost(cart.get_price(),cart.get_quantity(),cart.get_unit(),cart.get_uType())
    elif cart.get_uType() == "per packet" or cart.get_uType() == "per box" or cart.get_uType() == "kg":
        cart.set_quantity(cart.get_quantity()-cart.get_unit())

        if cart.get_quantity() <= 0:
            cartDict.pop(id)
        cart.set_cost(cart.get_price(),cart.get_quantity(),cart.get_unit(),cart.get_uType())

    db[db['activeUser']+"Cart"] = cartDict
    db.close()
    return redirect(url_for('retrieveCart'))

@app.route('/plusItem/<int:id>', methods=['GET','POST'])
def plusItem(id):
    cartDict = {}
    db = shelve.open('storage.db', 'w')
    cartDict = db[db['activeUser']+"Cart"]
    inventory = db['inventory']
    product = inventory.get(id)
    cart = cartDict.get(id)
    if cart.get_uType() == "g":
        cart.set_quantity(cart.get_quantity()+cart.get_unit())
        if cart.get_quantity()/cart.get_unit() > product.get_stock():
            cart.set_quantity(cart.get_quantity()-cart.get_unit())
        cart.set_cost(cart.get_price(),cart.get_quantity(),cart.get_unit(),cart.get_uType())
    elif cart.get_uType() == "per packet" or cart.get_uType() == "per box" or cart.get_uType() == "kg":
        cart.set_quantity(cart.get_quantity()+cart.get_unit())
        if cart.get_quantity()/cart.get_unit() > product.get_stock():
            cart.set_quantity(cart.get_quantity()-cart.get_unit())
        cart.set_cost(cart.get_price(),cart.get_quantity(),cart.get_unit(),cart.get_uType())

    #cart.set_cost(cart.get_price(),cart.get_quantity()+100)
    #if cart.get_quantity() <= 0:
    #    cartDict.pop(id)
    db[db['activeUser']+"Cart"] = cartDict
    db.close()
    return redirect(url_for('retrieveCart'))

@app.route('/payment', methods=['GET', 'POST'])
def checkout():
    cartDict = {}
    db = shelve.open('storage.db', 'r')
    cartDict = db[db['activeUser']+"Cart"]
    db.close()
    cartList = []
    totalcost = 0
    for key in cartDict:
        cartt = cartDict.get(key)
        print(cartt.get_quantity())
        cartList.append(cartt)
    for i in cartList:
        #print(i.get_cost)
        totalcost += i.get_cost()
        print(totalcost)
    countcart = len(cartList)
    paymentForm = PaymentForm(request.form)
    if request.method == 'POST' and paymentForm.validate():
        print("helllooooooo")
        #get the items in cart

        ########################################################################
        #add the cart into previous purchases and the overall sales and pending( i guess)
        prevDict = {}
        addPurchase = {}
        addPending = {}
        db = shelve.open('storage.db', 'c')
        try:
            name = db['activeUser']
            prevDict = db[name+'prev']
            addPurchase = db['allPurchases']
            addPending = db['pendingOrders']
        except:
            print("Error in retrieving from storage.db.")
        print("pppppppppppppppppppp")
        print(len(addPurchase))
        print("pppppppppppppppppppp")
        print(addPurchase)
        print(len(addPurchase)+1)
        date = datetime.datetime.now()
        date = str(date.day) +'/'+ str(date.month) +"/"+ str(date.year)
        print(date)
        payment = PaymentInfo.PaymentInfo(paymentForm.name.data,paymentForm.email.data,
                                          paymentForm.address.data,paymentForm.country.data,
                                          paymentForm.city.data,paymentForm.zip.data,
                                          paymentForm.cardName.data,paymentForm.cardNum.data,
                                          paymentForm.expmonth.data,paymentForm.expyear.data,
                                          paymentForm.cvv.data, totalcost, date)

        prevDict[len(addPurchase)+1] = [cartDict,payment]
        addPending[len(addPurchase)+1] = [cartDict,payment]
        addPurchase[len(addPurchase)+1] = [cartDict,payment]

        db[db['activeUser']+'prev'] = prevDict
        db['allPurchases']=  addPurchase
        db['pendingOrders'] = addPending
        db[db['activeUser']+"Cart"] = len(addPurchase)
        print(cartList)
        print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')
        inventory = db['inventory']
        for p in cartList:
            prod = inventory.get(p.get_itemId())
            print(p.get_unit())
            print(p.get_quantity())
            print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            prod.set_stock(prod.get_stock()-int(p.get_quantity()/p.get_unit()))
            #print(p.get_itemId())
            #inventory[p.get_itemId()].set_stock()
            #print(product)
            #inventory[p.get_itemId()] = product.subtract_stock(p.get_quantity())
        db['inventory'] = inventory
        print(db['allPurchases'])
        db.close()
        print (addPurchase)
        return redirect(url_for('receipt'))

    if cartList == []:
        return redirect(url_for('retrieveCart'))
    else:
        return render_template('payment.html', form=paymentForm, cartList = cartList , totalcost = totalcost, countcart = countcart)

@app.route('/ppurchase')
def ppurchase():
    pendingDict = {}
    completedDict = {}
    prevDict = {}
    db = shelve.open('storage.db', 'c')
    try:
        prevDict = db[db['activeUser']+'prev']
    except:
        prevDict = {}
    try:
        pendingDict = db["pendingOrders"]
    except:
        pendingDict = {}
    try:
        completedDict = db["completedOrders"]
    except:
        completedDict = {}
    db.close()
    prevList = []
    ordernumList = []
    statusList = []
    for key in prevDict:
        o = prevDict.get(key)
        prevList.insert(0,o)
        if key in completedDict:
            statusList.append('On the way')
        elif key in pendingDict:
            statusList.append('Preparing')
        ordernumList.insert(0,key)
        #print(key)
    db = shelve.open('storage.db', 'c')
    try:
        cartDict = db[db['activeUser']+"Cart"]
    except:
        cartDict = {}
    db.close()
    cartList = []
    totalcost = 0
    for key in cartDict:
        cartt = cartDict.get(key)
        cartList.append(cartt)
    for i in cartList:
        totalcost += i.get_cost()
    countcart = len(cartList)

    return render_template('ppurchase.html',prevList=prevList, count=len(prevList), ordernumList = ordernumList, statusList = statusList, countcart = countcart)



@app.route('/receipt')
def receipt():
    cartDict = {}
    cartList = []
    #totalcost = 0
    db = shelve.open('storage.db', 'c')
    orderNo = db[db['activeUser']+"Cart"]
    print("small pp")
    print(orderNo)
    cartDict = db['allPurchases'][int(orderNo)]
    print(cartDict)
    for o in cartDict[0]:
        cartt = cartDict[0].get(o)
        print(cartt.get_quantity())
        cartList.append(cartt)
    db[db['activeUser']+"Cart"] = {}
    db.close()
    countcart = 0

    return render_template('receipt.html',orderNo = orderNo, cartDict = cartDict, cartList = cartList,countcart=countcart)




@app.route('/doneOrders/<int:id>', methods=['GET','POST'])
def doneOrders(id):
    pendingDict = {}
    completedDict = {}
    db = shelve.open('storage.db', 'c')
    try:
        pendingDict = db["pendingOrders"]
        completedDict = db["completedOrders"]
    except:
        print("got error la")
    print(pendingDict)
    print(pendingDict[id])
    print(id)
    completedDict[id] =pendingDict[id]
    pendingDict.pop(id)
    db["pendingOrders"] = pendingDict
    db["completedOrders"] = completedDict
    db.close()
    return redirect(url_for('retrievePending'))

@app.route('/pendOrders/<int:id>', methods=['GET','POST'])
def pendOrders(id):
    pendingDict = {}
    completedDict = {}
    db = shelve.open('storage.db', 'c')
    try:
        pendingDict = db["pendingOrders"]
        completedDict = db["completedOrders"]
    except:
        print("got error la")

    print(id)
    pendingDict[id] = completedDict[id]
    completedDict.pop(id)
    db["pendingOrders"] = pendingDict
    db["completedOrders"] = completedDict
    db.close()
    return redirect(url_for('retrieveCompleted'))

@app.route('/retrievePending')
def retrievePending():
    pendingDict = {}
    db = shelve.open('storage.db', 'c')
    try:
        pendingDict = db["pendingOrders"]
    except:
        pendingDict = {}
    db.close()
    pendingList = []
    ordernumList = []
    for key in pendingDict:
        o = pendingDict.get(key)
        print(o)
        print(key)
        pendingList.append(o)
        ordernumList.append(key)
    print(pendingList)

    return render_template('porders.html',pendingList=pendingList, count=len(pendingList), ordernumList = ordernumList, pendingDict = pendingDict)

@app.route('/retrieveCompleted')
def retrieveCompleted():
    completedDict = {}
    db = shelve.open('storage.db', 'c')
    try:
        completedDict = db["completedOrders"]
    except:
        completedDict = {}
    db.close()
    completedList = []
    ordernumList = []
    for key in completedDict:
        o = completedDict.get(key)
        print(o)
        print(key)
        completedList.insert(0,o)
        ordernumList.insert(0,key)
    print(completedList)

    return render_template('corders.html',completedList=completedList, count=len(completedList), ordernumList = ordernumList, comletedDict = completedDict)



@app.route('/addCart/<int:id>', methods=['GET','POST'])
def addCart(id):
    cartDict = {}
    db = shelve.open('storage.db', 'c')
    #
    db['activeUser'] = "zele"
    inventory = db['inventory']
    #discount = db['Discounts']
    try:
        cartDict = db[db['activeUser']+"Cart"]
    except:
        print("Error in retrieving Users from storage.db.")
    product = inventory.get(id)

    #if id in discount:
    #    ok = Cart.Cart(id,product.get_name(),product.get_unitNo(),discount.get(id).get_discounted_price(),product.get_type(),product.get_unitNo(),product.get_unitType(),product.get_image())
    #else:

    #(itemId,name,quantity,price,type,unit,uType,image):
    ok = Cart.Cart(product.get_product_id(),product.get_name(),product.get_unitNo(),product.get_price(),product.get_type(),product.get_unitNo(),product.get_unitType().strip(),product.get_image())
    print(product.get_unitType())
    print(product.get_unitType().strip())
    print("looooooooooooooooooooooooooool")
    #ok = Cart.Cart('122','apple',6,10.00,'veg',6,'kg')
    if ok.get_itemId() in cartDict:
        print('alr have la')
    else:
    #cart.set_cost(cart.get_price(),cart.get_quantity()+100)
    #if cart.get_quantity() <= 0:
    #    cartDict.pop(id)
        cartDict[ok.get_itemId()] = ok
        print(ok.get_itemId())
        db[db['activeUser']+"Cart"] = cartDict
        print(cartDict)
    db.close()
#
#
#
#
    #db = shelve.open('storage.db', 'c')
    #
    #db['activeUser'] = "zele"
    #
   # try:
  #      cartDict = db[db['activeUser']+"Cart"]
  #  except:
 #       print("Error in retrieving Users from storage.db.")
#    ok = Cart.Cart('123','opple',5,6.00,'veg',5,'g')

    #cart.set_cost(cart.get_price(),cart.get_quantity()+100)
    #if cart.get_quantity() <= 0:
    #    cartDict.pop(id)
#    if ok.get_itemId() in db[db['activeUser']+"Cart"]:
#        print('alr have la')
#    else:
#        cartDict[ok.get_itemId()] = ok
#        print(ok.get_itemId())
#        db[db['activeUser']+"Cart"] = cartDict
#        print(cartDict)
#    db.close()
    return redirect(url_for('store'))

if __name__ == '__main__':
    app.run(debug = True)
