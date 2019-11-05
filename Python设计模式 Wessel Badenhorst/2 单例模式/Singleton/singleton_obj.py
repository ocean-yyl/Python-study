#encoding=utf-8
# 单例模式源码
"""
单例模式:
	保证一个类仅有一个实例，并提供一个访问它的全局访问点。
	如果已经存在一个创建好的对象,则获取它;如果不存在,才创建一个新的对象.
"""

class SingletonObj(object):
	class __SingletonObj():
		def __init__(self):
			self.val = None

		def __str__(self):
			return "{0!r} {1}".format(self,self.val)

		"""
		the rest of the class definition will follow here,as per the previous
		"""

	instance = None

	def __new__(cls, *args, **kwargs):
		if not SingletonObj.instance:
			SingletonObj.instance = SingletonObj.__SingletonObj()

		return SingletonObj.instance

	def __getattr__(self, item):
		return getattr(self.instance,item)

	def __setattr__(self, key, value):
		return setattr(self.instance,key,value)