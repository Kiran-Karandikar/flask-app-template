"""
Configuration for Flask app.
"""
# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
try:
	from secret_keys import CSRF_SECRET_KEY, SESSION_KEY
except ImportError:
	raise ImportError(
		"Secret_keys.py file does not exist.  Use `generate_secrete_keys.py` "
		"locally to generate one and upload to server."
	)


class Config(object):
	# Flask-Cache settings
	# CACHE_TYPE = 'gaememcached'
	# Set secret keys for CSRF protection
	SECRET_KEY = CSRF_SECRET_KEY
	CSRF_SESSION_KEY = SESSION_KEY


class Development(Config):
	# Flask-DebugToolbar settings
	DEBUG = True
	CSRF_ENABLED = False
	DEBUG_TB_PROFILER_ENABLED = True
	DEBUG_TB_INTERCEPT_REDIRECTS = False


class Testing(Config):
	CSRF_ENABLED = False
	TESTING = True
	DEBUG = True


class Production(Config):
	DEBUG = False
	CSRF_ENABLED = True
