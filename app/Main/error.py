from flask import render_template
from . import main

# decorator app.errorhandler() passes in the received error
@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    method to render the 404 error page if the wrong address is entered
    '''
    return render_template('fourOwfour.html'),404