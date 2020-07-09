# application/__init__.py
import config
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
bootstrap = Bootstrap()
UPLOAD_FOLDER = 'application/static/images'


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    login_manager.init_app(app)
    login_manager.login_message = "You must be login to access this page."
    login_manager.login_view = "frontend.login"

    bootstrap.init_app(app)

    with app.app_context():
        from .frontend import frontend_blueprint
        app.register_blueprint(frontend_blueprint)

        return app
