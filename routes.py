"""
# Docstring.
"""
# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
from food_print.views import *
from prototype.views import *


# Global Vars
# -N/A


def load_app_routes(app):
	"""

	Args:
		app:

	Returns:

	"""
	app.add_url_rule('/', view_func=HomePageHandlerView.as_view('login'))
	app.add_url_rule('/createuser',
	                 view_func=CreateUserView.as_view('createuser')
	                 )
	app.add_url_rule('/upload', view_func=UploadHandlerView.as_view('upload'))
	app.add_url_rule('/mobile', view_func=MobileHandlerView.as_view('mobile'))
	app.add_url_rule(
		'/lifestyle', view_func=LifestyleHandlerView.as_view('lifestyle')
	)
	app.add_url_rule('/diary', view_func=DiaryHandlerView.as_view('diary'))
	app.add_url_rule('/review', view_func=ReviewHandlerView.as_view('review'))
	app.add_url_rule('/all', view_func=ListAllHandlerView.as_view('all'))
	app.add_url_rule('/update', view_func=UpdateHandlerView.as_view('update'))
	app.add_url_rule('/delete', view_func=DeleteHandlerView.as_view('delete'))
	app.add_url_rule(
		'/checklastday',
		view_func=CheckLastDayHandlerView.as_view('checklastday')
	)
	app.add_url_rule('/admin', view_func=AdminHandlerView.as_view('admin'))
	app.add_url_rule('/todo', view_func=TodoHandlerView.as_view('todo'))


def load_app_test_routes(app):
	"""

	Args:
		app:

	Returns:

	"""
	app.add_url_rule('/testing/base', 'base', base_template)
	app.add_url_rule(
		'/testing/create_test_user',
		view_func=CreateTestUserView.as_view('create_test_user')
	)
	app.add_url_rule(
		'/testing/create_lifestyle',
		view_func=CreateLifeStyleView.as_view('create_lifestyle')
	)
	app.add_url_rule(
		'/testing/create_food', view_func=CreateFoodView.as_view('create_food')
	)
	app.add_url_rule(
		'/testing/blobstore',
		view_func=BlobstoreUploadHandlerView.as_view('test_blobstore')
	)
	app.add_url_rule('/testing/view', view_func=TestView.as_view('test_view'))
