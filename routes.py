"""
# Docstring.
"""
# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
from template_app.views import BaseHandlerView, base_template


# Global Vars
# -N/A


def load_app_routes(app):
	"""

	Args:
		app:

	Returns:

	"""
	app.add_url_rule('/', view_func=BaseHandlerView.as_view('index'))


def load_app_test_routes(app):
	"""

	Args:
		app:

	Returns:

	"""
	app.add_url_rule('/testing/base', 'base', base_template)
