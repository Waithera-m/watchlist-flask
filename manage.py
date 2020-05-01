from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Review
from flask_migrate import Migrate, MigrateCommand
# Manager class from flask-script that will initialize the extension and the Server class will launch the server.

#call function and pass configuration_options development key
app = create_app('development')

#initialize manager and pass app instance: create command line to dictate how the application will be run
manager = Manager(app)

#initialize migrate class
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#command 'server' will launch the application server
manager.add_command('server',Server)

#create a shell context
@manager.shell
def make_shell_context():

    '''
    Function facilitates the passing of properties to the shell
    '''
    return dict(app = app,db = db,User = User,Role = Role)


@manager.command
def test():

    '''
    Run test cases
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()