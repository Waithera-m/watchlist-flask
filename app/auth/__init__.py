from flask import Blueprint

#create blueprint instance
auth = Blueprint('auth',__name__)

from . import views