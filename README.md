# Virtual Classroom using VR and Deep Learning
### To set up the environment and project!

To install and use virtual env

    * Run "pip install virtualenv" to install virtual env.
    * Run "python -m virtualenv venv" to create a virtualenv of name venv.
    * Run "venv\Scripts\activate" to activate the virtualenv.

Run "pip install -r requirements.txt" in command prompt first in a virtual env and run the project.

To run flask :
FOR WINDOWS - 
```
set FLASK_APP=app 
set FLASK_ENVIRONMENT=development 
```
FOR UBUNTU -
```
export FLASK_APP=app 
export FLASK_ENVIRONMENT=development 
```
In the end: 
flask run

### About the Project
This project is developed for more interactive and fun learning classes, boring subjects like Data Structures, Computer Vision and etc, can be bought alive in the classes. 
Some of the features of the project are dashboard for both student and teacher are:
1. Login and Signup
2. Updating user profile. 

Using Speech Recognisation, the teacher augments a object in VR space. 
![Image of Cube Spawning](https://github.com/kkneha/vrcl/tree/master/screenshots/cube.png)

More fun things like, Hand Tracking, Customised models can be added in this. The basic idea in this project is to use VR in such a way that it makes more fun and realistic class. 
