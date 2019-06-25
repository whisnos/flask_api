from wtforms import StringField, IntegerField, Form
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForms(Form):
	q = StringField(validators=[Length(min=1, max=30,message='q必填'),DataRequired()]) # DataRequired() 防止传入空格
	page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)
