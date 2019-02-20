# coding:utf-8
# @Time    : 2019/2/7 15:51
# @Author  : huangai
# @email   : stanvenai@163.com
# @Site    : 
# @File    : http_web.py
# @Software: PyCharm

import requests

class HTTP:
	@staticmethod
	def get(url, return_json=True):
		r = requests.get(url)
		print(r)
		if r.status_code != 200:
			return {} if return_json else ''
		return r.json() if return_json else r.text

