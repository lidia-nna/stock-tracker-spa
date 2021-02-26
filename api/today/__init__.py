from flask import Blueprint

today = Blueprint('today', __name__)

from . import views