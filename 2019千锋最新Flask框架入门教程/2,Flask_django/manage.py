#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-30 15:17
# software: PyCharm

from App import create_app
from App.ext import init_ext
from App.views.manage_db import DB
from App.views.views import init_route,first_bp
from App.views.views_blue2 import second_blue



def init_app():
	# env = "develop"
	import os
	env = os.environ.get("FLASK_ENV","develop")
	app = create_app(env) # 创建app

	init_ext(app) # 加载models

	init_views(app) # 加载路由

	app.run(debug=True) # 启动app


# 加载views路由
def init_views(app):
	init_route(app)  # 加载路由
	app.register_blueprint(first_bp)  # 加载blue-print 的路由
	app.register_blueprint(second_blue)  # 加载blue-print 的路由
	app.register_blueprint(DB)


# manager.run()
if __name__ == '__main__':
	init_app()
