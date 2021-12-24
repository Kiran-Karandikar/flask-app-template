"""
# Docstring.
"""
# Python Modules
from flask import json, jsonify, make_response, render_template
from werkzeug.exceptions import HTTPException

# Project Modules
from template_app import get_app_logger

# 3rd Party Modules
# -N/A

# Global Vars
e_logger = get_app_logger("HTTP_ERRORS")


# define an error handling function
def init_error_handler(flask_app):
	# catch every type of exception
	@flask_app.errorhandler(Exception)
	def handle_exception(e):
		e_logger.exception(
			"Exception occurred while serving the request......\n"
			"The actual Error is:\n", exc_info=e
		)
		# return json response of error
		if isinstance(e, HTTPException):
			response = e.get_response()
			# replace the body with JSON
			# Check here for e.code then decide probably
			response.data = json.dumps(
				{"code": e.code, "name": e.name, "description": e.description}
			)
		else:
			# build error response
			response = make_response(
				jsonify(
					{
						"message": 'Something went wrong in code check the '
						           'error log, This is not HTTPException',
					}
				), 500
			)
		return response

	@flask_app.errorhandler(404)
	def page_not_found(e):
		return render_template('404.html', err_msg=e), 404

	@flask_app.errorhandler(500)
	def server_error(e):
		return render_template('500.html', err_msg=e), 500
