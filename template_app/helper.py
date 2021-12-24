"""
Helper function related app `template_app`.
"""
# Python Modules
# -N/A

# Project Modules
from . import get_app_logger

# 3rd Party Modules
# -N/A

# Global Vars
hlogger = get_app_logger(__name__)


def template_app_helper(*args, **kargs):
	"""

	:param args:
	:param kargs:
	:return:
	"""
	# do something here ..
	hlogger.info("Function call ......")
	print ("Hi there !!!, from `template_app_helper")
	hlogger.info("Returning to caller.")
