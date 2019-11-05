from Singleton.logger_singleton import Logger_singleton

logger = Logger_singleton()
logger.file_name = "../log_file/log.log"
logger.error("error test 2019")


logger = Logger_singleton()
logger.warn("error test2 2019")