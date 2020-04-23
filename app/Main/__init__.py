from flask import Blueprint
#initialize blueprint
main = Blueprint('main', __name__)
from . import views, error