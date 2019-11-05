#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-30 15:17
# software: PyCharm
from flask_sqlalchemy import SQLAlchemy
from App.ext import models

class Student(models.Model):
	id =  models.Column(models.Integer,primary_key=True)
	name = models.Column(models.String(20))

class grades(models.Model):
	id =  models.Column(models.Integer,primary_key=True)
	sex = models.Column(models.String(20))