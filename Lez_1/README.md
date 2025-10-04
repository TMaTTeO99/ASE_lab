# LESSON 1
The current directory contains a simple Flask web service.
The focus of this lesson is on the integration and use of the Roo-Code extension to build a simple web server.

## WINDOWS RUN INSTRUCTIONS

### STEPS:

1. python -m venv env_name
2. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
3. .\env_name\Scripts\Activate.ps1
4. pip install flask
5. $env:FLASK_APP = 'Controllers.base_operations:get_app'
6. flask run --host=0.0.0.0 --port=5005