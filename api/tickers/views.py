from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import tickers
from ..models import Tickers


@tickers.route('/tickers', endpoint='get_tickers',methods=['GET'])
@jwt_required()
def get_tickers():
    current_user = get_jwt_identity()
    try:
        Tickers.serialize_model(current_user, ID=True)
    except Exception as e:
        print(str(e))
        return "Unsuccessful", 400
    else: 
        return jsonify(Tickers.serialize_model(current_user, ID=True))



@tickers.route('/tickers', endpoint='add_tickers', methods=['POST'])
@jwt_required()
def add_tickers():
    if not request.is_json:
        return "Invalid format", 400
    data = request.get_json()
    #validation handled at the front-end
    for record in data: 
        record['user_id'] = get_jwt_identity()
        ticker = Tickers(**record)
        try:
            ticker.save()
        except Exception as e:
            print(f'Theres been a problem:  {e}')
            continue
    return "Success", 200


