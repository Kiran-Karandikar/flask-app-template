# Flask App Template
> Tested with python version 3.8

Simple, reusable, minimalistic, configurable flask app.

## Table of Contents
- [Features](#features)
- [Environment](#environment)
- [First Run](#first_run)
- [Configuration](#configuration)
---
### Features
- `Flask-cors, flask-debuggedtoolbar, flask-toastr` included
- configurable environment specific app configuration.
- unit test stub
- templates: partials, macros.

> #### What's not included
- Any database specific implementation.
- flask blueprints
---
### Environment
- clone this repo in your working directory
- install all required packages
  - packages included: `flask, flask-cors, Flask-DebugToolbar, Flask-Toastr, mock`
```shell
# required to test app locally
pip install -r requirements.txt 
```
---
### First run
- generate `secret_keys.py` to hold secrets: `CSRF_SECRET_KEY, SESSION_KEY`
  - `python config/generate_secrete_keys.py`
- run following commands in shell
```shell
set FLASK_APP=main.py 
set FLASK_ENV=development
set FLASK_CONF=DEV 
flask run
```
---
### Configuration
#### Change the default app name and working directory from `config/constants.py`
- change `APPLICATION_DIR` to `project_dir`
- change `APP_NAME` to `your_flask_app`
- sample app `template_app` is included in this repo.
  - This can be configured based on your demands.
---
## Local unit Testing
- update default test_folder location and test pattern defined in `config/constants.py`
```python
TEST_PATTERN = "*_test.py"
TEST_FOLDER = "tests"
```
- run the test suite.
```shell
python app_test.py 
```
- for test coverage
```shell
coverage run app_test.py
```
- coverage report
```shell
coverage report template_app/*.py
```