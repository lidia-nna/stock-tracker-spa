from flask import Blueprint

tickers = Blueprint('tickers', __name__)
from . import views