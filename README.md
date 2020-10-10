# arcl
To install and use virtual env

    * Run "pip install virtualenv" to install virtual env.
    * Run "python -m virtualenv venv" to create a virtualenv of name venv.
    * Run "venv\Scripts\activate" to activate the virtualenv.

Run "pip install -r requirements.txt" in command prompt first in a virtual env and run the project.

To run flask :
  FOR WINDOWS - set FLASK_APP=app
                set FLASK_ENVIRONMENT=development
  FOR UBUNTU - export FLASK_APP=app
               export FLASK_ENVIRONMENT=development
               
  flask run
