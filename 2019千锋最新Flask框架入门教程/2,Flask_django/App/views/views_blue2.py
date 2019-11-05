#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-30 15:42
# software: PyCharm

from flask import Blueprint
second_blue = Blueprint("second_blue",__name__)

#访问 127.0.0.1:5000/index3
@second_blue.route('/index3')
def index3():
	return "<h1>Flask test-> blue-print</h1>"
