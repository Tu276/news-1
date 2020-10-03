from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app

# We update our app/__init__.py to create our application
# factory function. We import import the config_options from
# the the config.py file that we updated. We then create the bootstrap instance.
# We create a create_app() function that takes the configuration setting key as an argument.
# This is because we might want to create the application instance under different configurations.
#  We then create the Flask app instance. We then import the configuration settings directly to the
# application using the from_object()method. We remove the app.config.from_pyfile("config.py") statement
# because all our secret configuration settings will be stored as environment variables.
# We call the init_app() on an extension to complete on their initialization.Finally we return app.
