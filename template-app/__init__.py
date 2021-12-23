"""
# Docstring.
"""
# Python Modules
import logging
import logging.config

# 3rd Party Modules
# -N/A


# Project Modules
# -N/A

# Global Vars
# Instantiates a client
logging.config.fileConfig("config/logging.conf")


def get_app_logger(logger_name, level=None):
	"""
	Get the python logger with name: `logger_name`.

	Args:
		logger_name (:str): Name of python logger to be displayed on console.
		level (:str): Required log level, currently supports only "Debug".

	Returns: instance of `logging.getLogger`.
	"""
	_logger = logging.getLogger(logger_name)
	if level is not None:
		if level.startswith("Debug"):
			_logger.level = logging.DEBUG
	return _logger
