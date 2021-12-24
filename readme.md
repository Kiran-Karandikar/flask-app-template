# Flask App Template

Simple and reusable flask app.
Minimalistic, minimalistic, configurable flask app.

## Table of Contents
- [Configuration](#configuration)
- [Start](#start)
- [Team](#team)

---
### Configuration
> Tested with python version 2.7, needs testing for latest python
- [ ] issues : Bump python version to latest

> Current Python version is 2.7

config/constants.py

- change `APPLICATION_DIR`
- change `APP_NAME`
- generate `secret_keys`

```shell
# required to test app locally
pip install -r requirements.txt 
set FLASK_APP=main.py 
set FLASK_ENV=development
set FLASK_CONF=DEV 
flask run
```

## Local unit Testing

- setup the flask config variables

```shell
set FLASK_APP=main.py
set FLASK_ENV=test
set FLASK_CONF=TEST
```

- check the test_suite path and test_pattern
# todo - check for sdk_path and test_path in app_test.py
```shell
python app_test.py 
# or
python gcloudsdk.py --sdk_path --test_path --test-pattern
```
- test coverage
```shell
coverage run app_test.py
```