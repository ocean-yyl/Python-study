#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:24544
# datetime:2019-11-04 13:50
# software: PyCharm

class Config(object):
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(Config):
	DEBUG = True

	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:123456@127.0.0.1:3306/flasksqlalchemy"

class TestConfig(Config):
	TESTING = True

	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:123456@127.0.0.1:3306/flasksqlalchemy"

class StagingConfig(Config):# 演示环境
	DEBUG = True

	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:123456@127.0.0.1:3306/flasksqlalchemy"

class ProductConfig(Config):
	DEBUG = True

	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:123456@127.0.0.1:3306/flasksqlalchemy"

envs = {
	"develop":DevelopConfig,
	"testing":TestConfig,
	"staging":StagingConfig,
	"product":ProductConfig,
	"default":DevelopConfig
}