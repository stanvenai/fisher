#coding:utf-8
# @Time    : 2019/2/10 18:23
# @Author  : huangai
# @email   : stanvenai@163.com
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint

web=Blueprint('web',__name__)
from app.web import book
from app.web import user
