#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-30 15:22
# software: PyCharm
from flask import Flask
from App.settings import envs

def create_app(env):
	app = Flask(__name__)

	# uri: 数据库+驱动://用户名:密码@主机:端口/数据库名称
	app.config.from_object(envs.get(env))

	return app