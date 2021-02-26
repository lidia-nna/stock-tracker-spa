from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.cache import cache
from . import ticker
from ..models import Tickers


@ticker.route('/ticker', endpoint='add_update_ticker', methods=['POST', 'PUT'])
@jwt_required()
def add_update_ticker():
    # data = request.form
    if not request.is_json:
        return "Invalid format", 400
    data = request.get_json()
    #validation handled in the front-end
    #check if record already exists
    data['user_id'] = get_jwt_identity()
    if request.method == "PUT":
        if data.get('id') is None:
            return "Record ID is missing in the body; cannot identify the record", 400
        elif not Tickers.find_record_by_id(_id=data['id'], user_id = data['user_id']):
            return f"Record ID of {data['id']} not found", 400
        else:
            try:
                print('data',data)
                Tickers.update(data)
                return "Success", 200
            except Exception as e:
                print(str(e))
                return "PUT failure", 500

    elif request.method == "POST":
        ticker = Tickers(**data)
        if data.get('id') and Tickers.find_record_by_id(data['id'], data['user_id']):
            return "Record already exists", 400
        try:
            ticker.save()
        except Exception as e:
            print(f'Theres been a problem:  {e}')
            return "Fail", 500
    return "Success", 200

@ticker.route('/ticker', endpoint='delete_ticker', methods=["DELETE"])
@jwt_required()
def delete_ticker():
    if not request.args:
        return "No record info", 400
    if request.args.get('id') is None:
        return "Invalid query parameter", 400
    ticker_id = request.args['id']
    user_id = get_jwt_identity()
    ticker = Tickers.find_record_by_id(ticker_id,user_id).first()
    symbol = ticker.ticker
    try:
        ticker.delete()
    except Exception as e:
        print(str(e))
        return 'Failed', 500
    else:
        #print(cache.get(symbol))
        #cache.set(symbol, '')
        return "Success", 200