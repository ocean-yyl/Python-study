#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-30 16:24
# software: PyCharm

from flask import Blueprint
from App.models import models
from App.models import Student

DB = Blueprint("create_db", __name__)

#访问 127.0.0.1:5000/createDB
@DB.route('/createDB')
def create():
	models.create_all()
	return "DB创建成功"

@DB.route('/addStu')
def addStu():
	stu = Student()
	stu.name = "yyl"
	models.session.add(stu)
	models.session.commit()

	return "创建成功"

@DB.route('/dropdb')
def dropdb():
	models.drop_all()

	return "删除成功"