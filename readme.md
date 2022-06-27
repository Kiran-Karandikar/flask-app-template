<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[contributors-shield]: https://img.shields.io/github/contributors/kiran-karandikar/flask-app-template?style=for-the-badge

[contributors-url]: https://github.com/Kiran-Karandikar/flask-app-template/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Kiran-Karandikar/flask-app-template?style=for-the-badge

[forks-url]: https://github.com/Kiran-Karandikar/flask-app-template/network

[stars-shield]: https://img.shields.io/github/stars/Kiran-Karandikar/flask-app-template?style=for-the-badge

[stars-url]: https://github.com/Kiran-Karandikar/flask-app-template/stargazers

[issues-shield]: https://img.shields.io/github/issues/Kiran-Karandikar/flask-app-template?style=for-the-badge

[issues-url]: https://github.com/Kiran-Karandikar/flask-app-template/issues

[license-shield]: https://img.shields.io/github/license/Kiran-Karandikar/flask-app-template?style=for-the-badge

[license-url]: https://github.com/Kiran-Karandikar/flask-app-template/blob/master/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/kiran-karandikar

---------


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">flask-app-template</h3>
  <p align="center">
    Simple, reusable, minimalistic, configurable flask app.    
    <br />    
    <a href="https://kiran-karandikar.github.io/flask-app-template"><strong>Preview</strong></a>
    <br />
    <a href="https://github.com/kiran-karandikar/flask-app-template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kiran-karandikar/flask-app-template">View Demo</a>
    ·
    <a href="https://github.com/kiran-karandikar/flask-app-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/kiran-karandikar/flask-app-template/issues">Request Feature</a>
  </p>
</div>

<!-- BADGES.MD Finish -->
<!-- BADGES.MD Finish -->
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

### Other projects

Check out the other stuff I've worked upon.

- ___AI/ML/Data Science___

  - **AML-Home-Credit-Default-Risk** : [Predicting how capable each applicant is of repaying a loan \(Kaggle Challenge\).](https://github.com/Kiran-Karandikar/AML-Home-Credit-Default-Risk)

  - **Exercise-performance-analysis** : [Prototype exercise volume prediction using machine learning models.](https://github.com/Kiran-Karandikar/Exercise-performance-analysis)

- ___Web Development___

  - **flask-app-template** : [Simple, reusable, minimalistic, configurable flask app.](https://github.com/Kiran-Karandikar/flask-app-template)

  - **flask-oauth2-wrike-api** : [A sample Flask app to authenticate with Wrike as a third-party OAuth2 provider.](https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api)

> Section `Other projects` is auto-updated using [Github actions](https://github.com/features/actions). 
<!-- CONTACT -->
## Contact

- [Kiran Karandikar: khkarandikar at gmail dot com](mailto:khkarandikar@gmail.com)
