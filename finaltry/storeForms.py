from wtforms import StringField, RadioField, DecimalField, validators, IntegerField, TextAreaField, SelectField, FloatField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, file_required

class ItemForm(FlaskForm):
    name = StringField('Product Name', [validators.length(min=1, max=100), validators.data_required()])
    img = FileField("Product Image", validators=[file_required()])
    type = RadioField('Product type', choices=[('fruit', 'Fruits'), ('vegetable', 'Vegetables'), ('other', 'Others')], default="other")
    price = FloatField('Product Price ($)', [validators.NumberRange(0, 1000), validators.data_required()])
    unitNo = IntegerField('Unit Number', [validators.number_range(0, 1000), validators.data_required()])
    unitType = SelectField('Unit Type', [validators.data_required()], choices=[('kg', 'kg'), ('g', 'g'), ('per packet', 'per packet'), ('per box', 'per box')])
    stock = IntegerField('Number of stocks', [validators.NumberRange(0, 9999), validators.data_required()])
    description = TextAreaField('Product description', [validators.Optional()])
