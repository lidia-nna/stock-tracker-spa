from api.models import Tickers
import json
from flask_jwt_extended import jwt_required, get_jwt_identity


def test_login_fail(client, init_databse):
    r = client.post('/auth', 
        data = dict(email='play.python.test@gmail.com',
            password='testing1#', follow_redirects=True)
    )
    assert r.status_code != 200

def test_register_pass(client, init_databse):
    r = client.post('/register', 
        data = dict(email='lid.mijas@gmail.com',
        password='testing1#', follow_redirects=True)
    )
    assert r.status_code == 200

def test_unconfirmed_account(client, init_databse):
    r = client.post('/auth', 
        data = dict(username='lid.mijas',
            password='testing1#', follow_redirects=True)
    )
    assert r.status_code == 403

def test_get_summary(client, init_databse):

    r = client.get('/summary')
    assert r.status == 200

    
# def test_post_json_file(client, init_databse):
#     file_name = "test/test_file.json"
#     with open(file_name, 'rb') as f:
#         r = client.post('/tickers', json = json.load(f))

#     assert r.status_code == 200

# def test_post_json(client, init_databse):
#     test_ticker = { 
#             'ticker': 'AAPL',
#             'name' : 'Apple Inc.',
#             'share_price': 100,
#             'upper_threshold': 0.5,
#             'lower_threshold': 0.3,
#             'share_count': 1000
#         }
#     r=client.post('/ticker', json = test_ticker)
#     assert r.status_code == 200 

# def test_get_daily_chart(client):
#     r = client.get('/charts/daily', query_string={'ticker':'AAPL'})
#     assert r.status_code == 200
#     r = client.get('/charts/daily', query_string={'symbol':'AAPL'})
#     assert b"Invalid query parameter" in r.data
#     r = client.get('/charts/daily')
#     assert b"No ticker info" in r.data

# def test_get_historical_chart(client):
#     r = client.get('/charts/alltime', query_string={'ticker':'AAPL'})
#     assert r.status_code == 200
#     r = client.get('/charts/alltime', query_string={'symbol':'AAPL'})
#     assert b"Invalid query parameter" in r.data
#     r = client.get('/charts/alltime')
#     assert b"No ticker info" in r.data

# def test_get_weekly_chart(client):
#     r = client.get('/charts/week', query_string={'ticker':'AAPL'})
#     assert r.status_code == 200
#     r = client.get('/charts/week', query_string={'symbol':'AAPL'})
#     assert b"Invalid query parameter" in r.data
#     r = client.get('/charts/week')
#     assert b"No ticker info" in r.data







