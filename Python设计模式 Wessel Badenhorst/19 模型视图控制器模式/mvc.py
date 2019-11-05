#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-29 14:25
# software: PyCharm

import sys


# 控制器->逻辑
"""
控制器是该模式的核心,这个部分是调度所有其他类的。
用户会与控制器交互并且通过它来与整个系统进行交互。
控制器会接收用户输入,处理所有的业务逻辑,从模型获取数据,
并且将数据发送到视图以转换成要返回给用户的表示形式。
"""
class GenericController(object):
	def __init__(self):
		self.model = GenericModel()
		self.view = GenericView()

	def handle(self, request):
		data = self.model.get_data(request)
		self.view.generate_response(data)

# 模型->数据
"""
模型是处理数据的:
获取数据,设置数据,更新数据以及删除数据。
就是这样。通常会看到模型所做的远多于此,而那是错误的。
我们的模型应该是通向数据的程序侧接口,它要抽离直接与数据存储交互的需要,
允许从基于文件的存储切换到一些键值存储或者完全的关系型数据库系统。
"""
class GenericModel(object):
	def __init__(self):
		pass

	def get_data(self, request):
		return {"request": request}

# 视图->show
"""
就像模型一样,我们不希望视图中包含任何业务逻辑。
视图应该仅仅处理输出或者将传递到它的数据呈现成某种要返回到用户的格式,
例如输出到控制台的打印语句或者呈现给游戏玩家的3D渲染。
输出的格式对于视图的处理机制而言并没有太大的区别。
我们也会忍不住将逻辑添加到视图,这是一种滑坡谬误,并且不应该是我们所要采用的路径。
"""
class GenericView(object):
	def __init__(self):
		pass

	def generate_response(self, data):
		print(data)


def main(name):
	req_handler = GenericController()
	req_handler.handle(name)


if __name__ == '__main__':
	main(sys.argv[1])
