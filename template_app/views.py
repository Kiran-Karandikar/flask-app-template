"""
Temporary Script to hold all view request for app `template_app`.
"""
# Python Modules
from collections import namedtuple
from flask import (
	 make_response, render_template, request,flash
)
from flask_cors import cross_origin
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
			"post": 'template_app/loggedIN.html',
		}
		return templates.get(method)

	@cross_origin()
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
		vlogger.info("Request payload is : {}".format(payload))
		user_name = payload.get("login-user_name")
		password = payload.get("login-password")
		content_type = self.request.headers.get('Content-Type')
		vlogger.info("User id: {}".format(user_name))
		vlogger.info("Password : {}".format(password))
		vlogger.info("Requested Content Type: {}".format(content_type))
		if user_name is not None and password is not None:
			user = None
			try:
				# Fetch user details from the database here.....
				# set `user` to the fetched user from database
				USER = namedtuple('User', ['name', 'password'])
				user = USER(user_name, password)
			except Exception as e:
				vlogger.exception(
					"Exception while fetching entity: `User`"
					"\n\n Actual Error: ", exc_info=e
				)
			if user is not None and user.password == str(password):
				vlogger.info("Requested User is: {}".format(user))
				vlogger.info("Successfully logged in ... ")
				context.update(
					{"success": True}
				)
				flash("Logged in for User:{}".format(user_name), 'success')
				response = make_response(
					render_template(self.get_template_name("post"), **context),
					200
				)
				return response
		flash("Not able to log in.....", 'error')
		flash("Sign Up, Not supported...", 'warning')
		flash("Log in using any username and password", 'info')
		vlogger.error("Requested user not found, returning .....")
		return render_template(self.get_template_name("get"), **context)


def base_template():
	flash("Base template loaded", "info")
	flash("This is warning message of flash", "warning")
	flash("This is error message of flash", "error")
	flash("This is success message of flash", "success")
	return render_template("base.html")
