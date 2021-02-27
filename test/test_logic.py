import pandas as pd
from api.models import Tickers, UserModel
from api.users.emailtoken import Token
import datetime as dt
import numpy as np
from flask_sqlalchemy import SQLAlchemy


def test_users(init_databse):
    user = UserModel('testemail@email')
    user.set_password('testing1#')
    user.save_to_db()
    myuser = UserModel.check_user(email='testemail@email')
    assert myuser.username == 'testemail'
    record = UserModel.find_user_record(user_id=1)
    assert record.username == 'testemail'

def test_email_token():
    t = Token()
    token = t.generate_confirmation_token(email='play.python.test@gmail.com')
    email = t.confirm_token(token=token)
    assert email == 'play.python.test@gmail.com'


    
    
# def test_uniq_tickers(init_databse):
#     # file_name = "test/test_file.json"
#     # with open(file_name, 'rb') as f:
#     #     client.post('/tickers', json = json.load(f))
#     tickers = Tickers.list_uniq_tickers()
#     assert tickers == [
#         "EZJ.L",
#         "BWY.L",
#         "SBRY.L",
#         "IXI.L",
#         "NCR",
#         "AAPL"
#     ]
# def test_serialize(init_databse):
#     ticker_record = Tickers.query.first()
#     record = Tickers.serialize(ticker_record) 
#     assert record.get('id') == None
#     assert record['ticker'] in Tickers.list_uniq_tickers()

# def test_get_db_df(summary):
#     summary.get_db_df()
#     db_ixico_stocks = [stock.share_price for stock in Tickers.query.filter(Tickers.name=='IXICO')]
#     df_ixico_stocks = summary.db[summary.db.name == "IXICO"]['share_price'].values
#     assert isinstance(summary.db, pd.DataFrame) == True
#     assert summary.db.columns.all() in Tickers.get_column_names()
#     assert tuple(df_ixico_stocks) == tuple(db_ixico_stocks)

# def test_get_live_data(summary):
#     summary.get_tickers()
#     summary.get_live_data()
#     assert tuple(summary.live_data.columns) == ('live','open', 'low', 'high')
#     assert np.datetime64('today') in summary.live_data.index.get_level_values(0)

# def test_compile_summary(summary):
#     if summary.prepare(): 
#         assert summary.summary.empty == False
#         df = summary.summary
#         apple_record = df[df.ticker == "AAPL"]
#         print(apple_record)
#         assert apple_record.total_earnings.values == apple_record.live.values * 10 - 1000
#         assert apple_record.margin.values == (apple_record.live.values-100.0)/100.0
    

