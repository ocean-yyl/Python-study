#prototype 原型,标准,模范
from abc import ABCMeta,abstractmethod

class Prototype(metaclass=ABCMeta):
	@abstractmethod
	def clone(self):
		pass