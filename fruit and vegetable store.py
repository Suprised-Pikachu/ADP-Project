from flask import Flask, render_template, request, url_for, redirect, session, g, flash
from form import CreateStaffForm
from werkzeug.utils import secure_filename

# import shelve, staff, User
import shelve
import staff

import os

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)


def allowed_file(filename):
    pass


def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route('/')
def home():
    return render_template('home.html',user=userlogin)

@app.route('/store')
def store():
    return render_template('store.html',user=userlogin)

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html',user=userlogin)

@app.route('/sign_out')
def sign_out():
    global userlogin
    userlogin = "false"
    return render_template('sign_out.html',user=userlogin)

@app.route('/cart')
def cart():
    return render_template('cart.html',user=userlogin)

@app.route('/payment')
def payment():
    return render_template('payment.html',user=userlogin)

@app.route('/receipt')
def receipt():
    return render_template('receipt.html',user=userlogin)

@app.route('/ppurchase')
def ppurchase():
    return render_template('ppurchase.html',user=userlogin)

@app.route('/home_admin')
def admin_home():
    return render_template('home_admin.html')

@app.route('/store_admin')
def admin_store():
    return render_template('store_admin.html')

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
    return render_template('voucher.html',user=userlogin)

@app.route('/admin_statistics')
def statistics():
    return render_template('Statistics.html')

@app.route('/porders')
def porders():
    return render_template('porders.html',user=userlogin)

@app.route('/corders')
def corders():
    return render_template('corders.html',user=userlogin)

@app.route('/after_admin')
def afteradmin():
    return render_template('after_login_admin.html')

@app.route('/event')
def event():
    return render_template('event.html',user=userlogin)

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
    return render_template('after_edit_images.html',user=userlogin)

@app.route('/addStaff', methods=['GET','POST'])
def addStaff():
    # global staffDict
    print('AddStaff...1...')
    createStaffForm = CreateStaffForm(request.form)
    print('AddStaff...2...')
    if request.method == 'POST' and createStaffForm.validate():
            # usersDict = {}
            staffDict = {}
            db = shelve.open('storage.db', 'c')

            try:
               staffDict = db['Staffs']
            except:
               print("Error in retrieving Users from storage.db.")
            user = staff.Staff(createStaffForm.firstName.data,
                         createStaffForm.lastName.data,
                         createStaffForm.membership.data,
                         createStaffForm.gender.data,
                         createStaffForm.remarks.data)
            staffDict[user.get_staffID()] = user
            db['Staffs'] = staffDict
            db.close()
            return redirect(url_for('testing'))
    print('AddStaff...3...')
    return render_template('addStaff.html', form=createStaffForm)


@app.route('/retrieveStaff')
def retrieveStaff():
    staffDict = {}
    db = shelve.open('storage.db','r')
    staffDict = db['Staffs']
    db.close()

    usersList = []
    for key in staffDict:
        staff = staffDict.get(key)
        usersList.append(staff)

    return render_template('staff_directory(test).html',usersList=usersList,count=len(usersList))

@app.route('/successful')
def successful():
    return render_template('successful.html',user=userlogin)


@app.route('/signin')
def s():
    global userlogin
    userlogin = "true"
    return render_template('testing_signin.html',user=userlogin)

@app.route('/testing')
def testing():
    print("00001")
    staffDict = {}
    print("00002")
    db = shelve.open('storage.db','c')
    print("00003...db("+str(db)+")")


    # staffDict = db['Staffs']
    # print("1...Test staffDict("+staffDict+")")


    # try:
    #     staffDict = db['Staffs']
    #     user = s.Staff("myFirstName", "myLastName", "S", "M", "myRemarks")
    #     staffDict[user.get_staffID()] = user
    #     db['Staffs'] = staffDict
    # except:
    #     print("Error in retrieving Users from storage.db.")


    # db.close()
    # print("00004")

    try:
        staffList = []
        print("2!!!!")
        staffDict = db['Staffs']
        print("1...Test staffDict("+staffDict+")")

        for key in staffDict:
            print("3...Test key("+key+")")
            staff = staffDict.get(key)
            staffList.append(staff)
        return render_template('staff_directory(test).html',staffList=staffList, count=len(staffList))
    except:
        print("no such record!!!!")
    finally:
        db.close()
        print("00004")

    return render_template('staff_directory(test).html',staffList=staffList, count=len(staffList))


@app.route('/updateStaff/<int:id>/', methods=['GET','POST'])
def updateStaff(id):
    updateStaffForm = CreateStaffForm(request.form)
    if request.method == 'POST' and updateStaffForm.validate():
        staffDict = {}
        db = shelve.open('storage,db','w')
        staffDict = db['Staffs']

        staff = staffDict.get(id)
        staff.set_firstName(updateStaffForm.firstName.data)
        staff.set_lastName(updateStaffForm.lastName.data)
        staff.set_membership(updateStaffForm.membership.data)
        staff.set_gender(updateStaffForm.gender.data)
        staff.set_remarks(updateStaffForm.remarks.data)

        db['Staffs'] = staffDict
        db.close()

        return redirect(url_for('testing'))

    else:
        staffDict = {}
        db = shelve.open('storage.db','r')
        staffDict = db['Staffs']
        db.close()

        staff = staffDict.get(id)
        updateStaffForm.firstName.data = staff.get_firstName()
        updateStaffForm.lastName.data = staff.get_lastName()
        updateStaffForm.membership.data = staff.get_membership()
        updateStaffForm.gender.data = staff.get_gender()
        updateStaffForm.remarks.data = staff.get_remarks()
        return render_template('updateStaff.html',form=updateStaffForm)


@app.route('/deleteStaff/<int:id>', methods=['POST'])
def deleteStaff(id):
    staffDict = {}
    db = shelve.open('storage.db','w')
    staffDict = db['Staffs']


    staffDict.pop(id)

    db['Staffs']= staffDict
    db.close()

    return redirect(url_for('testing'))
userlogin = "false"

if __name__ == '__main__':
    app.run()

