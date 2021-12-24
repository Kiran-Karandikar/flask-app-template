"""
# This script holds all config keys related to app `food_print`.
"""
# Python Modules
import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_toastr import Toastr
from werkzeug.debug import DebuggedApplication

# Project Modules
from config.constants import *

# 3rd Party Modules
# -N/A

# Global Vars
sys.path.append(os.path.join(os.path.dirname(__file__), APP_NAME))
###############################################################################
# App configuration
###############################################################################
app = Flask(__name__)
app.config ['UPLOAD_FOLDER'] = UPLOAD_FOLDER
##############################################################################
# Set up the environment specific parameters.
# feature - debugging Application The toolbar will automatically be
#  injected into HTML responses when debug mode is on. In production,
#  setting app.debug = False will disable the toolbar.
##############################################################################
FLASK_CONF = os.getenv('FLASK_CONF').strip()
if FLASK_CONF != "PROD":
	if FLASK_CONF == 'TEST':
		app.config.from_object('config.settings.Testing')
	elif FLASK_CONF == 'DEV' or (
			'SERVER_SOFTWARE' in os.environ and
			os.environ ['SERVER_SOFTWARE'].startswith('Dev')
	):
		# Development settings
		app.config.from_object('config.settings.Development')
	toolbar = DebugToolbarExtension(app)
	app.wsgi_app = DebuggedApplication(
		app.wsgi_app, evalex=True, pin_security=False, pin_logging=False
	)
elif FLASK_CONF == "PROD":
	# todo - check the environment specific variables....
	# Production in the standard environment
	app.config.from_object('config.settings.Production')
else:
	raise OSError(
		"Unable to detect the server configuration please check the "
		"environment variables. "
	)
##############################################################################
# Flask Extensions
##############################################################################
# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
# Flask-cors: CORS specific
cors = CORS(app, resources=CORS_RESOURCES)
app.config ['CORS_HEADERS'] = 'Content-Type'
# Flask-Toastr: Notification specific
toast = Toastr(app)
app.config.update(TOAST_OPTIONS)
