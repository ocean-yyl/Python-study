import logger
import logger_class
logger.warn("this is a warning")

log_obj = logger_class.Logger("log_file/log.log")
log_obj.error("this is erro")
