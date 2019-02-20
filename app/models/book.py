# coding:utf-8
# @Time    : 2019/2/13 11:00
# @Author  : huangai
# @email   : stanvenai@163.com
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(50), nullable=False)
	author = Column(String(30), default='匿名')
	binding = Column(String(20))
	publisher = Column(String(50))
	price = Column(String(20))
	pages = Column(Integer)
	pubdate = Column(String(20))
	isbn = Column(String(15), nullable=False, unique=True)
	summary = Column(String(1000))
	image = Column(String(50))
