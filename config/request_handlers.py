"""
# Docstring.
"""
# Python Modules
from flask import make_response, request

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def init_request_processing(flask_app):
	def _build_cors_preflight_response():
		response = make_response()
		response.headers.add('Access-Control-Allow-Credentials', 'true')
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
		response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
		response.headers.add(
			'Access-Control-Allow-Methods',
			"GET, POST, OPTIONS, PUT, PATCH, DELETE"
		)
		response.headers.add(
			'Access-Control-Expose-Headers',
			"Content-Type,Content-Length,Authorization,X-Pagination"
		)
		return response

	@flask_app.before_request
	def before_request():
		if request.method == 'OPTIONS':
			origin = request.headers.get('Origin')
			response = _build_cors_preflight_response()
			if origin:
				response.headers.add('Access-Control-Allow-Origin', origin)
			return response, 200

	@flask_app.after_request
	def after_request_func(response):
		origin = request.headers.get('Origin')
		response.headers.add('Access-Control-Allow-Credentials', 'true')
		response.headers.add(
			'Access-Control-Expose-Headers',
			'Content-Type,Content-Length,Authorization,X-Pagination '
		)
		if origin:
			response.headers.add('Access-Control-Allow-Origin', origin)
		return response
