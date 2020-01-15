from wtforms import Form, StringField, validators

class PaymentForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=1, max=150), validators.DataRequired()])
    country = StringField('Country', [validators.Length(min=1, max=150), validators.DataRequired()])
    city = StringField('City', [validators.Length(min=1, max=150), validators.DataRequired()])
    zip = StringField('Zip', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardName = StringField('Name on card', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardNum = StringField('Credit card number', [validators.Length(min=1, max=150), validators.DataRequired()])
    expmonth = StringField('Exp month', [validators.Length(min=1, max=150), validators.DataRequired()])
    expyear = StringField('Exp year', [validators.Length(min=1, max=150), validators.DataRequired()])
    cvv = StringField('CVV', [validators.Length(min=1, max=150), validators.DataRequired()])

    #membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    #gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    #remarks = TextAreaField('Remarks', [validators.Optional()])

