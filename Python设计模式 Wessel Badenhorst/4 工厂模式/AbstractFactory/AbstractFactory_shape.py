import abc
"""
python 内置的abc模块,它让我们可以自定义一个抽象基类.
"""


class AbstratFactory(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def make_obj(self):
		return

class ShapeFactory(AbstratFactory):
	def make_obj(self):
		# do something
		shape = "do something"
		return shape

class ColorFactory(AbstratFactory):
	def make_obj(self):
		# do something
		color = "do something"
		return color