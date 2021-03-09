from flask import Blueprint
from ..limiter import limiter

users = Blueprint('users', __name__, template_folder='templates')
limiter.limit("200/hour")(users)
from . import views