from wtforms import Form, StringField, validators, RadioField, TextAreaField
from flask_wtf import FlaskForm


class CreateUserForm(Form):

    userName = StringField('User Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = StringField('Password', [validators.Length(min=8, max=150),validators.DataRequired()])
    cfmPassword = StringField('Confirm Password', [validators.Length(min=8, max=150), validators.DataRequired()])
    userType = RadioField('User Type',
                          choices=[('Hr', 'Human resource'),('A', 'Admin'), ('D', 'Design'), ('L', 'Logistic'),
                                   ('F', 'Finance'), ('C', 'Customer')], default='C')


class UserLogin(Form):

    userName = StringField('User Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = StringField('Password', [validators.Length(min=8, max=150), validators.DataRequired()])


class CreateEventForm(Form):

    eventName = StringField('Event Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    date = StringField('Date', [validators.Length(min=1, max=150), validators.DataRequired()])
    details = StringField('Details', [validators.Length(min=1, max=150), validators.DataRequired()])
    requirements = TextAreaField('Requirements', [validators.Optional()])
    remarks = TextAreaField('Remarks', [validators.Optional()])
