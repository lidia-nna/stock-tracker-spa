from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.cache import cache
from . import today
from .logic import Summary



@today.route('/summary', endpoint='get_summary', methods=['GET'])
@jwt_required()
#@cache.cached(timeout=15*60, query_string=True) #15 mins
def get_summary():
    current_user = get_jwt_identity()
    #current_user = 1
    summary = Summary(current_user)
    try:
        summary.get_report()
    except Exception as e:
        if 'No stocks found' in str(e):
            return str(e)
        return "Error generating greport", 500
    return jsonify(summary.get_report())    