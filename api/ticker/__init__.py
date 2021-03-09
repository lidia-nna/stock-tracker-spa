from flask import Blueprint
from ..limiter import limiter

ticker = Blueprint('ticker', __name__)
limiter.limit("100/hour")(ticker)

from . import views