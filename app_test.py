"""
# Docstring.
"""
# Python Modules
import os
import sys
import unittest

# Project Modules
from config import gcloudsdk
from config.constants import (
	APPLICATION_DIR, GOOGLE_SDK_PATH, TEST_FOLDER,
	TEST_PATTERN,
)

# 3rd Party Modules
# -N/A

# Global Vars
# -N/A


if __name__ == '__main__':
	# set the flask environment variables
	if not os.getenv("FLASK_APP"):
		os.environ ["FLASK_APP"] = "main.py"
	if not os.getenv("FLASK_ENV") or not os.getenv("FLASK_CONF"):
		os.environ ["FLASK_ENV"] = "test"
		os.environ ["FLASK_CONF"] = "TEST"
	gcloudsdk.setup_cloudsdk_path(GOOGLE_SDK_PATH, APPLICATION_DIR)
	test_path = os.path.join(os.getcwd(), TEST_FOLDER)
	suite = unittest.loader.TestLoader().discover(test_path, TEST_PATTERN)
	result = unittest.TextTestRunner(verbosity=2).run(suite)
	if not result.wasSuccessful():
		sys.exit(1)
