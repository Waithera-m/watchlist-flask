from flask import Flask
from .config import DevConfig

#Initialize application, creat application instance
#We pass in instance_relative_config which allow us to connect to the instance/folder when the app instance is created
app = Flask(__name__,instance_relative_config=True)

# Setting up configuration
#The app.config.from_pyfile('config.py') connects to the config.py file and all its contents are appended to the app.config.
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views

#most flask extensions have to be initialized in this file before they can be used
from flask_bootstrap import Bootstrap

#Initialize boostrap
bootstrap = Bootstrap(app)