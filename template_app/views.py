"""
Temporary Script to hold all view request for app `template_app`.
"""
# Python Modules
from __future__ import with_statement
from flask import (
	jsonify, make_response, render_template, request,flash
)
from flask.views import MethodView

# 3rd Party Modules
# -N/A

# Project Modules
from . import get_app_logger
from .decorators import inspect_call

# Global Vars
vlogger = get_app_logger(__name__)
cors_log = get_app_logger('flask_cors', "Debug")


# route - `/*`
class BaseHandlerView(MethodView):
	"""
	Handle `Get` and `Post` request for route `/*`.
	"""
	methods = ["GET", "POST"]

	def __init__(self):
		self.request = request

	def get_template_name(self, method):
		"""
		Placeholder to define the template used in `BaseHandlerView`.
		"""
		templates = {
			"get": 'template_app/index.html',
			"post": 'food_print/diary_update.html',
		}
		return templates.get(method)

	def get(self):
		vlogger.info("Get method of /BaseHandlerView")
		context = {}
		flash("This is test of flashing messages", "info")
		return render_template(self.get_template_name("get"), **context)

	@inspect_call
	def post(self):
		vlogger.info("Post method of /BaseHandlerView")
		context = {"success": False}
		payload = self.request.values.to_dict()
		userid = payload.get("userid")
		password = payload.get("password")
		content_type = self.request.headers.get('Content-Type')
		vlogger.info("User id: {}".format(userid))
		vlogger.info("Password : {}".format(password))
		vlogger.info("Requested Content Type: {}".format(content_type))
		if userid is not None and password is not None:
			user = None
			try:
				user = User.query(User.name == str(userid)).get()
			except Exception as e:
				vlogger.exception(
					"Exception while fetching entity: `User`"
					"\n\n Actual Error: ", exc_info=e
				)
			if user is not None and user.password == str(password):
				vlogger.info("Requested User is: {}".format(user))
				vlogger.info("Successfully logged in ... ")
				context.update(
					{"success": True, "user_group": user.group,
					 "monitor_other_name": user.monitor_other_name}
				)
				response = make_response(jsonify(context))
				response.headers.add('Content-Type', 'application/json')
				##############################################################
				# returning the json response instead of rendering template
				# `update` since the dev_app.js uses the json data to verify
				# login.
				#############################################################
				return response
		vlogger.error("Requested user not found, returning .....")
		return render_template(self.get_template_name("get"), **context)


def base_template():
	flash("Base template loaded", "info")
	flash("This is warning message of flash", "warning")
	flash("This is error message of flash", "error")
	flash("This is success message of flash", "success")
	return render_template("base.html")
