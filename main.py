"""
Script to route the requests.
"""
# Python Modules
# -N/A

# Project Modules
from app_config import app
from config.error_handlers import init_error_handler
from config.request_handlers import init_request_processing
from routes import *

# 3rd Party Modules
# -N/A

# Global Vars
# -N/A
###############################################################################
# Register the @app.before_request and @app.after_request
init_request_processing(app)
###############################################################################
# Register HTTP error handling
init_error_handler(app)
###############################################################################
# Add all App routes
load_app_routes(app)
load_app_test_routes(app)
###############################################################################

if __name__ == '__main__':
	app.run()
