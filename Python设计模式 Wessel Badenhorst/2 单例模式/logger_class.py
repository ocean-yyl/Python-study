#encoding=utf-8

class Logger(object):
	"""
	A file-based message logger with the following properties
	
	Attributes:
		file_name : a string representing the full path of the log ...
	"""
	
	def __init__(self,filename):
		"""实例化类"""
		self.file_name = filename

	def _write_log(self,level,msg):
		with open(self.file_name,"a") as log_file:
			log_file.write("[{0}] {1}\n".format(level,msg))
	
	def critical(self,msg):
		self._write_log("CRITICAL", msg)
	
	def error(self,msg):
		self._write_log("ERROR", msg)
	
	def warn(self,msg):
		self._write_log("WARN", msg)
	
	def info(self,msg):
		self._write_log("INFO", msg)
	
	def debug(self,msg):
		self._write_log("DBUG", msg)

