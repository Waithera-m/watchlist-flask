import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    '''
    Class facilitates the creation of test units to test the User class' behavior
    '''
    def setUp(Self):

        '''
        Function runs before every test case
        '''
        self.new_user = User(password = 'banana')

    def test_password_setter(self):

        '''
        Function checks if password is hashed when pass_secure has a value
        '''
        self.assertTrue(self.new_user.pass_secure is not None)
    
    def test_no_access_password(self):

        '''
        Function checks if the app raises attribute error if users try to access password property
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password
        
    def test_password_verification(self):

        '''
        Function checks if program can verify correct passwords
        '''
        self.assertTrue(self.new_user.verify_password('banana'))