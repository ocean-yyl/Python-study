#encoding=utf-8
# 单例模式源码
"""
单例模式:
	保证一个类仅有一个实例，并提供一个访问它的全局访问点。
	如果已经存在一个创建好的对象,则获取它;如果不存在,才创建一个新的对象.
"""

class Logger_singleton(object):
	class __SingletonObj():
		def __init__(self):
			self.file_name = None

		def __str__(self):
			return "{0!r} {1}".format(self,self.file_name)

		"""
		the rest of the class definition will follow here,as per the previous
		"""
		def _write_log(self, level, msg):
			with open(self.file_name, "a") as log_file:
				log_file.write("[{0}] {1}\n".format(level, msg))

		def critical(self, msg):
			self._write_log("CRITICAL", msg)

		def error(self, msg):
			self._write_log("ERROR", msg)

		def warn(self, msg):
			self._write_log("WARN", msg)

		def info(self, msg):
			self._write_log("INFO", msg)

		def debug(self, msg):
			self._write_log("DBUG", msg)

	instance = None

	def __new__(cls, *args, **kwargs):
		if not Logger_singleton.instance:
			Logger_singleton.instance = Logger_singleton.__SingletonObj()

		return Logger_singleton.instance

	def __getattr__(self, item):
		return getattr(self.instance,item)

	def __setattr__(self, key, value):
		return setattr(self.instance,key,value)