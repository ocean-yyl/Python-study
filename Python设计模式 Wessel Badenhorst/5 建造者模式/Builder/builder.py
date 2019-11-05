#encoding=utf-8
from abc import ABCMeta,abstractmethod

class Director(object,mecontaclass=ABCMeta):
	def __init__(self):
		self._builder = None

	@abstractmethod
	def construct(self):
		pass

	def get_constructed_object(self):
		return self._builder.constracted_object


class Builder(object,metaclass=ABCMeta):
	def __init__(self,constracted_object):
		self.constracted_object = constracted_object


class Product(object):
	def __init__(self):
		pass
	def __repr__(self):
		pass

class ConcreteBuilder(Builder):
	pass

class ConcreteDirector(Director):
	pass