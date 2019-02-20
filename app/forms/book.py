#coding:utf-8
# @Time    : 2019/2/11 18:05
# @Author  : huangai
# @email   : stanvenai@163.com
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
	q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
	page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)