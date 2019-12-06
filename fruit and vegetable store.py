from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def store():
    return render_template('store.html')

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
    return render_template('after_login_admin.html')

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/event2')
def event2():
    return render_template('event2.html')

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

if __name__ == '__main__':
    app.run()
