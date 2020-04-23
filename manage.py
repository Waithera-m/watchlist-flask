from app import create_app
from flask_script import Manager,Server
# Manager class from flask-script that will initialize the extension and the Server class will launch the server.

#call function and pass configuration_options development key
app = create_app('development')

#initialize manager and pass app instance: create command line to dictate how the application will be run
manager = Manager(app)

#command 'server' will launch the application server
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()