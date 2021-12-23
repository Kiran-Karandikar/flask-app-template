"""
# This script holds all config keys related to app `food_print`.
"""
# Python Modules
import json
import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_toastr import Toastr
from werkzeug.debug import DebuggedApplication

# Project Modules
from config import gcloudsdk
from config.constants import *
from config.request_handlers import CustomResponse, InterceptRequestMiddleware

# 3rd Party Modules
# -N/A

# Global Vars
sys.path.append(os.path.join(os.path.dirname(__file__), APP_NAME))
ID_FILE_PATH = os.path.join(os.path.dirname(__file__), ID_FILE_NAME)
###############################################################################
# App configuration
###############################################################################
app = Flask(__name__)
# todo -- do we need to use google cloud specific tmp folder ??
app.config ['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.wsgi_app = InterceptRequestMiddleware(app.wsgi_app)
# Fix: werkzeug has  no module `middleware`
# from werkzeug.middleware.proxy_fix import ProxyFix
# app.wsgi_app = ProxyFix(app.wsgi_app, x_host=1, x_proto=1)
app.response_class = CustomResponse
##############################################################################
# Set up the environment specific parameters.
# feature - debugging Application The toolbar will automatically be
#  injected into HTML responses when debug mode is on. In production,
#  setting app.debug = False will disable the toolbar.
##############################################################################
if os.getenv('FLASK_CONF') == 'TEST':
	app.config.from_object('config.settings.Testing')
	toolbar = DebugToolbarExtension(app)
	app.wsgi_app = DebuggedApplication(
		app.wsgi_app, evalex=True, pin_security=False, pin_logging=False
	)
	# Importing the App Engine SDK so that modules can use google.appengine.*
	# APIs..
	gcloudsdk.setup_cloudsdk_path(GOOGLE_SDK_PATH, APPLICATION_DIR)
elif os.getenv('FLASK_CONF') == 'DEV' or (
		'SERVER_SOFTWARE' in os.environ and
		os.environ ['SERVER_SOFTWARE'].startswith('Dev')
):
	# Development settings
	app.config.from_object('config.settings.Development')
	toolbar = DebugToolbarExtension(app)
	app.wsgi_app = DebuggedApplication(
		app.wsgi_app, evalex=True, pin_security=False, pin_logging=False
	)
	# Importing the App Engine SDK so that modules can use google.appengine.*
	# APIs
	gcloudsdk.setup_cloudsdk_path(GOOGLE_SDK_PATH, APPLICATION_DIR)
elif os.getenv('GAE_ENV', '').startswith('standard'):
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
##############################################################################
# `data/idv2.json`: has following structure:
# {
# 	"user_id": "user_study",
# 	.......
# }
with open(ID_FILE_PATH, 'r') as dataFile:
	ID_DATA = json.loads(dataFile.read())
