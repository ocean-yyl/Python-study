#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:24544
# datetime:2019-11-04 13:22
# software: PyCharm
from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()
# 扩展库init
def init_ext(app):
	models.init_app(app)
