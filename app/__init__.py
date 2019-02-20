# coding:utf-8
# @Time    : 2019/2/10 18:22
# @Author  : huangai
# @email   : stanvenai@163.com
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask
from app.models.book import db


def create_app():
	app = Flask(__name__)
	app.config.from_object('app.secure')
	app.config.from_object('app.setting')
	register_blueprint(app)

	db.init_app(app)
	db.create_all(app=app)
	return app


def register_blueprint(app):
	from app.web import web
	app.register_blueprint(web)
