import os

from flask import Flask
from flask import Flask, render_template, request
import json
from datetime import datetime
from . import model, auth, teacher, stream

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'userdata.sqlite') 
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
        
    model.init_app(app)
   
    app.register_blueprint(auth.bp)
    app.register_blueprint(stream.bp)
    app.register_blueprint(teacher.bp)
    return app

    """
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import en_de
    app.register_blueprint(en_de.bp)

    from . import model
    app.register_blueprint(model.bp)
    return app """



