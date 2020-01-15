from flask import Flask, render_template, request, redirect, url_for, session, g
from Forms import CreateUserForm, UserLogin, CreateEventForm
from passlib.hash import sha256_crypt
import shelve, User
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
currentuser = ['', '', '']


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = "True"
        print(g.user)


@app.route('/')
def home():
    userType = currentuser[2]
    is_login = g.user
    return render_template('home.html', userType=userType,is_login=g.user, user=currentuser[0])


@app.route('/contactUs', )
def contactUs():
    userType = currentuser[2]
    if g.user:
        if userType == "A":
            print(g.user)
            return render_template('contactUs.html',userType=userType,is_login=g.user, user=currentuser[0])

    return redirect(url_for('home'))


@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    userType = currentuser[2]
    createUserForm = CreateUserForm(request.form)
    if request.method == 'POST' and createUserForm.validate():

        usersDict = {}
        db = shelve.open('storage.db', 'c')

        try:
            usersDict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        user = User.User(createUserForm.userName.data, createUserForm.email.data,
                         sha256_crypt.hash(createUserForm.password.data), createUserForm.cfmPassword.data,
                         createUserForm.userType.data)
        inside = False
        for key in usersDict:
            user_stored = usersDict.get(key)
            if user.get_userName() == user_stored.get_userName():
                inside = True
                break
        if inside == False:
            if createUserForm.password.data == createUserForm.cfmPassword.data:
                usersDict[user.get_userID()] = user
                db['Users'] = usersDict
                db.close()
                return redirect(url_for('home'))
        else:
            ok = "username already exists!"
            return render_template('createUser.html', form=createUserForm, ok=ok,userType=userType,is_login=g.user, user=currentuser[0])

    return render_template('createUser.html', form=createUserForm, userType=userType,is_login=g.user, user=currentuser[0])


@app.route('/login', methods=['GET', 'POST'])
def login():
    userType = currentuser[2]
    userLogin01 = UserLogin(request.form)
    if request.method == 'POST' and userLogin01.validate():
        session.pop('user', None)
        db = shelve.open('storage.db', 'r')

        try:
            userDict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        for key in userDict:
            user = userDict.get(key)
            if user.get_userName() == userLogin01.userName.data:
                if sha256_crypt.verify(userLogin01.password.data, user.get_password()):
                    currentuser[0] = user.get_userID()
                    currentuser[1] = user.get_userName()
                    currentuser[2] = user.get_userType()
                    session['user'] = currentuser
                    print(currentuser)
                    print(session['user'])
                    print(session['user'][2])

                    return redirect(url_for('home'))
                else:
                    print(user.get_userName() + " password or username is incorrect")
            else:
                print(user.get_userName() + " password or username is incorrect")

    return render_template('login.html', userloginform=userLogin01 ,userType=userType,is_login=g.user, user=currentuser[0] )


@app.route('/updatePassword/<int:id>/', methods=['GET', 'POST'])
def updatePassword(id):
    userType = currentuser[2]
    updateUserForm = CreateUserForm(request.form)
    if request.method == 'POST' and updateUserForm.validate():
        db = shelve.open('storage.db', 'w')
        userDict = db['Users']

        user = userDict.get(id)
        user.set_userName(updateUserForm.userName.data)
        user.set_email(updateUserForm.email.data)
        user.set_password(sha256_crypt.hash(updateUserForm.password.data))
        user.set_cfmPassword(updateUserForm.cfmPassword.data)

        db['Users'] = userDict
        db.close()

        return redirect(url_for('home'))
    else:
        return render_template('updatePassword.html', form=updateUserForm,userType=userType,is_login=g.user, user=currentuser[0])


@app.route('/logOut')
def dropsession():
    session.pop('user', None)
    currentuser[0] = ''
    currentuser[1] = ''
    currentuser[2] = ''

    return redirect(url_for('home'))


@app.route('/createEvents', methods=['GET', 'POST'])
def createEvent():
    userType = currentuser[2]
    createEventForm = CreateEventForm(request.form)
    if request.method == 'POST' and createEventForm.validate():
        eventsDict = {}
        db = shelve.open('eventstorage.db', 'c')
        try:
            eventsDict = db['Users']
        except:
            print("Error in retrieving Users from eventstorage.db.")
        event = User.Event(createEventForm.eventName.data, createEventForm.date.data, createEventForm.details.data,
                           createEventForm.requirements.data, createEventForm.remarks.data)
        eventsDict[event.get_eventID()] = event
        db['Users'] = eventsDict

        db.close()

        return redirect(url_for('home'))
    return render_template('createEvents.html', form=createEventForm,userType=userType,is_login=g.user, user=currentuser[0])


@app.route('/retrieveEvents')
def retrieveEvents():
    userType = currentuser[2]
    eventsDict = {}
    db = shelve.open('eventstorage.db', 'r')
    eventsDict = db['Users']
    db.close()

    eventsList = []
    for key in eventsDict:
        event = eventsDict.get(key)
        eventsList.append(event)
    return render_template('retrieveEvents.html', eventsList=eventsList, count=len(eventsList),userType=userType,is_login=g.user, user=currentuser[0])


@app.route('/updateEvents/<int:id>/', methods=['GET', 'POST'])
def updateUser(id):
    userType = currentuser[2]
    updateUserForm = CreateEventForm(request.form)
    if request.method == 'POST' and updateUserForm.validate():
        db = shelve.open('eventstorage.db', 'w')
        eventDict = db['Users']

        event = eventDict.get(id)
        event.set_eventName(updateUserForm.eventName.data)
        event.set_date(updateUserForm.date.data)
        event.set_details(updateUserForm.details.data)
        event.set_requirements(updateUserForm.requirements.data)
        event.set_remarks(updateUserForm.remarks.data)

        db['Users'] = eventDict
        db.close()

        return redirect(url_for('retrieveEvents'))
    else:
        eventDict = {}
        db = shelve.open('eventstorage.db', 'r')
        eventDict = db['Users']
        db.close()

        event = eventDict.get(id)
        updateUserForm.eventName.data = event.get_eventName()
        updateUserForm.date.data = event.get_date()
        updateUserForm.details.data = event.get_details()
        updateUserForm.requirements.data = event.get_requirements()
        updateUserForm.remarks.data = event.get_remarks()

        return render_template('updateEvents.html', form=updateUserForm,userType=userType,is_login=g.user, user=currentuser[0])


@app.route('/deleteEvent/<int:id>', methods=['POST'])
def deleteEvent(id):
    eventsDict = {}
    db = shelve.open('eventstorage.db', 'w')
    eventsDict = db['Users']

    eventsDict.pop(id)

    db['Users'] = eventsDict
    db.close()

    return redirect(url_for('retrieveEvents'))


@app.route('/events')
def events():
    userType = currentuser[2]
    eventsDict = {}
    db = shelve.open('eventstorage.db', 'r')
    eventsDict = db['Users']
    db.close()

    eventsList = []
    for key in eventsDict:
        event = eventsDict.get(key)
        eventsList.append(event)
    return render_template('Events.html', eventsList=eventsList, count=len(eventsList),userType=userType,is_login=g.user, user=currentuser[0])


if __name__ == '__main__':
    app.run(debug=True)
