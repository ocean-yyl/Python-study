#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-29 23:40
# software: PyCharm

from flask import Flask
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app=app)

@app.route("/")
def index():
	return "<h1>hello world</h1>"


if __name__ == '__main__':
	# app.run(debug=True)
	manager.run()