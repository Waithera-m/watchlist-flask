from flask import render_template
from . import auth

@auth.route('/login')
def login():

    '''
    View function returns login template and its contents
    '''
    return render_template('auth/login.html')