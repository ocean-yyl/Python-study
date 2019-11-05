#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-30 15:17
# software: PyCharm
from flask import render_template

def init_route(app):
	@app.route("/")
	def index():
		return "<h1>hello world</h1>"


from flask import Blueprint
first_bp = Blueprint("first_bp",__name__)

#访问 127.0.0.1:5000/index2
@first_bp.route('/index2/')
def index2():
	return render_template('we.html', my_msg="传递参数my_msg")