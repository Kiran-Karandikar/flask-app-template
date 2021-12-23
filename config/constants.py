"""
Script to store all constants.
"""
# Python Modules

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
APPLICATION_DIR = "flask-app-template"
APP_NAME = "template-app"

# Extension: Flask-cors
# Following defines all required response headers for CORS
CORS_RESOURCES = {
	r"/*": {
		"origins": "*",
		"allow_headers": "*",
		"methods": ["GET", "POST"],
	}
}
TEST_FOLDER = "tests"
TEST_PATTERN = '*_test.py'
# Extension: Flask-Toastr notification options
TOAST_OPTIONS = {
	'TOASTR_TIMEOUT': 15000,
	'TOASTR_EXTENDED_TIMEOUT': 1000,
	'TOASTR_POSITION_CLASS': 'toast-top-right',
	'TOASTR_PREVENT_DUPLICATES': 'false',
	'TOASTR_NEWS_ON_TOP': 'true'
}
UPLOAD_FOLDER = '/tmp'
