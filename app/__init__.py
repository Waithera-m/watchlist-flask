from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    '''
    funtion to create app instance, configurations, and initialize flask extensions
    '''
    #Initialize application, creat application instance
    #We pass in instance_relative_config which allow us to connect to the instance/folder when the app instance is created
    app = Flask(__name__)

    #app configurations
    app.config.from_object(config_options[config_name])
    

    #initialize flask extensions
    bootstrap.init_app(app)

    #register blueprint

    from .Main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #set configuration
    from .request import configure_request
    configure_request(app)

    return app

    





