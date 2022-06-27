# studiologging 

'''
direct run

from function.pipeline import logger 
reload(logger)
logger.AutoRigLogger.info('asdasdasd')

logger.AutoRigLogger.set_propagate(False)


'''
import logging
import sys

class Logger(object):
	# class level variable
	LOGGER_NAME = 'Noman'

	FORMAT_DEFAULT = "[%(name)s][%(levelname)s]%(message)s"

	LEVEL_DEFAULT = logging.DEBUG

	PROPAGATE_DEFAULT = True # make not double with maya

	_logger_obj = None

	# function decorator
	@classmethod # constructor
	def logger_obj(cls):
		if not cls._logger_obj: 
			if cls.logger_exists():
				# if exists
				cls._logger_obj = logging.getLogger(cls.LOGGER_NAME)
			else:
				# if not exists
				cls._logger_obj = logging.getLogger(cls.LOGGER_NAME)

				cls._logger_obj.setLevel(cls.LEVEL_DEFAULT)

				cls._logger_obj.propagate = cls.PROPAGATE_DEFAULT # make not double with maya

				fmt = logging.Formatter(cls.FORMAT_DEFAULT)

				stream_handler = logging.StreamHandler(sys.stderr)
				# stream_handler = logging.StreamHandler(sys.stdout) # get rid hastag

				stream_handler.setFormatter(fmt)
				cls._logger_obj.addHandler(stream_handler)

		return cls._logger_obj

	@classmethod
	def logger_exists(cls):
		return cls.LOGGER_NAME in logging.Logger.manager.loggerDict.keys()

	@classmethod
	def set_level(cls, level):
		lg = cls.logger_obj()
		lg.setLevel(level)


	@classmethod
	def set_propagate(cls, propagate): # make not double with maya
		lg = cls.logger_obj()
		lg.propagate = propagate


	@classmethod
	def debug(cls, msg, *args, **kwargs):
		lg = cls.logger_obj()
		lg.debug(msg, *args, **kwargs)

	@classmethod
	def info(cls, msg, *args, **kwargs):
		lg = cls.logger_obj()
		lg.info(msg, *args, **kwargs)

	@classmethod
	def warning(cls, msg, *args, **kwargs):
		lg = cls.logger_obj()
		lg.warning(msg, *args, **kwargs)

	@classmethod
	def error(cls, msg, *args, **kwargs):
		lg = cls.logger_obj()
		lg.error(msg, *args, **kwargs)

	@classmethod
	def critical(cls, msg, *args, **kwargs):
		lg = cls.logger_obj()
		lg.critical(msg, *args, **kwargs)

	@classmethod
	def log(cls, level, msg, *args, **kwargs):
		lg = cls.logger_obj()
		lg.log(level, msg, *args, **kwargs)

	@classmethod
	def exception(cls,  msg, *args, **kwargs):
		lg = cls.logger_obj()
		lg.exception( msg, *args, **kwargs)

	@classmethod
	def write_to_file(cls, path, level=logging.WARNING):
		file_handler = logging.FileHandler(path)
		file_handler.setLevel(level)

		# Formatter
		fmt = logging.Formatter("[%(asctime)s][%(levelname)s]%(message)s")
		file_handler.setFormatter(fmt)
		lg = cls.logger_obj()
		lg.addHandler(file_handler)






class MayaLogger(Logger):

	LOGGER_NAME = "MayaLogger"

	FORMAT_DEFAULT = "[%(levelname)s][%(name)s]%(message)s"

	PROPAGATE_DEFAULT = False



class AutoRigLogger(MayaLogger):

	LOGGER_NAME = "AutoRig"
	FORMAT_DEFAULT = "[%(levelname)s][%(name)s]%(message)s"
	PROPAGATE_DEFAULT = False






'''
if __name__ == "__main__":
	Logger.set_propagate(False)# make not double with maya

	Logger.set_level(logging.WARNING)
	Logger.write_to_file("D:/testLogger.log")
	Logger.debug("debug message")
	Logger.info("info message")
	Logger.warning("warning message")
	Logger.error("error message")
	Logger.critical("critical message")
	Logger.log(5,"log message")
'''