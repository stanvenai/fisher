# coding:utf-8
# @Time    : 2019/2/7 16:56
# @Author  : huangai
# @email   : stanvenai@163.com
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from flask import jsonify, request	

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
	# q=request.args['q']
	# page=request.args['page']

	form = SearchForm(request.args)
	if form.validate():
		q = form.q.data.strip()
		page = form.page.data
		isbn_or_key = is_isbn_or_key(q)
		if isbn_or_key == 'isbn':
			result = YuShuBook.search_by_isbn(q)
		else:
			result = YuShuBook.search_by_keyword(q, page)
		return jsonify(result)  # flask专用
	else:
		return jsonify(form.errors)
# return json.dumps(result),200,{'content-type':'application/json'}


# @web.route('/hello')
# def hello_world():
# 	return 'Hello World!'
# app.add_url_rule('/hello',view_func=hello_world)
