from flask import render_template
from app import app

# decorator app.errorhandler() passes in the received error
@app.errorhandler(404)
def four_Ow_four(error):
    '''
    method to render the 404 error page if the wrong address is entered
    '''
    return render_template('fourOwfour.html'),404