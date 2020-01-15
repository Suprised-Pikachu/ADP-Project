from flask import Flask, render_template, request, redirect, url_for, jsonify
import shelve
from storeForms import ItemForm
from product import Product
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
    return render_template('home2.html')


@app.route('/store2')
def store2():
    return render_template('store2.html')


@app.route('/contact_us2')
def contact_us2():
    return render_template('contact_us2.html')


@app.route('/sign_out')
def sign_out():
    return render_template('sign_out.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/receipt')
def receipt():
    return render_template('receipt.html')


@app.route('/ppurchase')
def ppurchase():
    return render_template('ppurchase.html')


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


@app.route('/porders')
def porders():
    return render_template('porders.html')


@app.route('/corders')
def corders():
    return render_template('corders.html')


@app.route('/after_login')
def after():
    return render_template('after_login.html')


@app.route('/after_admin')
def afteradmin():
    role = 'logistics'
    return render_template('after_login_admin.html', role=role)


@app.route('/event')
def event():
    return render_template('event.html')


@app.route('/event2')
def event2():
    return render_template('event2.html')


@app.route('/event_admin')
def eve_admin():
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


if __name__ == '__main__':
    app.run()
