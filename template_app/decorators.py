"""
Decorators for URL handlers.
"""
# Python Modules
from functools import wraps

# 3rd Party Modules
# -N/A

# Project Modules
from . import get_app_logger

# Global Vars
dlog = get_app_logger(__name__)


def inspect_call(func):
	"""
	Decorator to inspect any function call.

	Args:
		func: name of function to be inspected.

	Returns: Decorated `func`.
	"""

	@wraps(func)
	def decorated_view(*args, **kargs):
		dlog.info("**********************************************************")
		dlog.info("Function called : {}".format(func.__name__))
		self_object = args [0]
		dlog.info("Args are : {}".format(*args))
		if hasattr(self_object, "request"):
			dlog.info("Request object is : {}".format(self_object.request))
		if hasattr(self_object, "response"):
			dlog.info("response object is : {}".format(self_object.response))
		for _ in kargs:
			dlog.info("Keyword args are: {} = {}".format(_, kargs.get(_)))
		return_value = func(*args, **kargs)
		dlog.info("**********************************************************")
		return return_value

	return decorated_view
