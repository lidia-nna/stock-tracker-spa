import yfinance as yf
import pandas as pd
import datetime as dt
import json
from ..models import Tickers

class Summary:
    def __init__(self, user):
        self.user = user
        self.tickers = None
        self.db = None
        self.today = dt.date.today()
        self.live_data = None
        self.summary = pd.DataFrame()

    def get_tickers(self):
        print(self.user)
        self.tickers = Tickers.list_uniq_tickers(user_id=self.user)
        #self.tickers = []


    def get_db_df(self):
        db_dict = Tickers.serialize_model(self.user, ID=True)
        dfdb = pd.DataFrame(db_dict)
        dfdb.set_index("ticker", inplace=True)
        self.db = dfdb


    def get_live_data(self):
        try:
            today = yf.download(tickers=self.tickers, period='1d') #start=self.today)
        except Exception as e:
            raise RuntimeError from e
        if len(self.tickers) > 1:
            today = today.stack().drop(['Adj Close', 'Volume'], axis=1)#.droplevel('Date', axis=0)
        else:
            today = today.drop(['Adj Close', 'Volume'], axis=1)#.droplevel('Date', axis=0)
            today['Ticker'] = self.tickers[0]
            today.reset_index(inplace=True)
            today.set_index(['Date', 'Ticker'], inplace=True)
        today.rename(columns = {"Date":"date", "Ticker":"ticker","Close":"live", "Open": "open", "High": "high", "Low": "low"}, inplace=True)
        today.index.set_names(["date","ticker"], inplace=True)
        today = today[['live','open', 'low', 'high']]
        self.live_data = today

    
    def compile_summary(self):
        #combine live and db data
        summary = self.live_data.join(self.db, on="ticker")

        #add simple stats
        summary['upper_threshold'] = (summary['upper_threshold']/100 + 1) * summary["share_price"]
        summary['lower_threshold'] = (summary['lower_threshold']/100 - 1) * summary["share_price"] * (-1)
        summary['margin'] = (summary['live'] - summary['share_price'])*100/summary['share_price'] 
        summary['total_earnings'] = (summary['live'] - summary['share_price'])*summary['share_count']/100
        summary['reset_threshold'] = summary.apply(lambda x: x['live'] > x['upper_threshold'] or x['live'] < x['lower_threshold'], axis=1)

        #add multiindex for the tickers who have more than one record 
        summary['stock_nr'] = summary.groupby(summary.index).cumcount() + 1
        #summary.set_index([summary.index,'name','stock_nr'], inplace=True)
        summary.reset_index(inplace = True)

        #round results to two decimal places
        summary=summary.round(decimals=2)

        #change date-time object to string
        summary.date = summary.date.dt.strftime('%Y-%m-%d %H:%M:%S')
        self.summary = summary
        


    def prepare(self):
        try:
            self.get_tickers()
            self.get_db_df()
            self.get_live_data()
            self.compile_summary()
        except Exception as e:
            print(str(e))
            raise Exception from e
            # print(f"Retrieval unsuccessful!\n{e}")
            # return False
        else:
            print("Success")


    def get_report(self):
        try:
            self.prepare()
        except Exception as e:
            print(str(e))
            raise Exception from e
        else: 
            return json.loads(self.summary.to_json(orient="records"))


        
import pytest 
def test_daily_chart():
    chart = DailyChart("EZJ.L")
    ts = chart.get_timeseries()
    df = chart.df_data
    assert chart.period == "1d"
    assert chart.interval == "30m"
    # assert ts.index.name == "Datetime"
    assert df.Close.empty == False
    assert df.columns.size == 2
    assert isinstance(ts, dict) == True
    assert tuple(ts.keys()) == tuple(df.columns.tolist())
    #assert dt.datetime.strptime(ts%Y-%m-%d %H:%M:%S)


if __name__ == "__main__":
    user=''
    summary = Summary(user)
    print(summary.prepare())