"""
# test the routes of the main app.
"""
# Python Modules
import unittest

# 3rd Party Modules
# -N/A

# Project Modules
from main import app
from template_app import get_app_logger

# Global Vars
test_logger = get_app_logger(__name__)


class ViewsTestCase(unittest.TestCase):
	"""
	All test cases related to `template_app` views.
	"""
	def setUp(self):
		self.app = app

	def tearDown(self):
		"""
		Teardowns all the initialized objects/structures.
		"""
		with self.app.app_context():
			# remove all app specific objects .....
			pass

	def test_index(self):
		"""

		:return:
		"""
		# Test setup
		test_logger.info("\nTesting Route: `/`")
		test_query_params = {
			"num_of_user": 2, "site": "b", "group": "0"
		}
		request_url = "/"
		with self.app.test_client() as tc:
			test_logger.info("Established connection....")
			test_logger.info("Query Params are: {}".format(test_query_params))
			test_logger.info("Url is: {}".format(request_url))
			actual_response = tc.get(request_url)
			self.assertEqual(actual_response.status_code, 200)

	def test_404(self):
		"""

		:return:
		"""
		# Test setup
		test_logger.info("\nTesting Route: `/not_exists`")
		request_url = "/not_exists"
		with self.app.test_client() as tc:
			test_logger.info("Established connection....")
			test_logger.info("Url is: {}".format(request_url))
			actual_response = tc.get(request_url)
			self.assertEqual(actual_response.status_code, 404)
