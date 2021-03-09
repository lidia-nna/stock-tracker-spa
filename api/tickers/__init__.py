from flask import Blueprint
from ..limiter import limiter

tickers = Blueprint('tickers', __name__)
limiter.limit("200/hour")(tickers)
from . import views