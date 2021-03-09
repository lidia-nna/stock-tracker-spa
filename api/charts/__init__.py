from flask import Blueprint
from ..limiter import limiter

charts = Blueprint('charts', __name__)
limiter.limit("100/hour")(charts)

from . import views