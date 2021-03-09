from flask import Blueprint
from ..limiter import limiter

today = Blueprint('today', __name__)
limiter.limit("100/hour")(today)

from . import views