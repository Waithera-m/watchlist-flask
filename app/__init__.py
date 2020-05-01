from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE

csrf = CSRFProtect()
mail = Mail()
simple = SimpleMDE()

#flask_login facilitates user authentication system management

#UploadSet class defines the type of files to be uploaded
photos = UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
#login_manager.session_protection provides different security levels. Strong security level monitors the changes in a user's request header and logs them out.
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):

    '''
    funtion to create app instance, configurations, and initialize flask extensions
    '''
    #Initialize application, creat application instance
    #We pass in instance_relative_config which allow us to connect to the instance/folder when the app instance is created
    app = Flask(__name__)

    #app configurations
    app.config.from_object(config_options[config_name])
    
    #UploadSet configuration
    configure_uploads(app,photos)

    #initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    simple.init_app(app)

    #register blueprint

    from .Main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    # url_prefix argument adds a prefix to all the routes registered with the auth blueprint

    

    #set configuration
    from .request import configure_request
    configure_request(app)

    return app

    





