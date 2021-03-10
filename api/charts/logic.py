import yfinance as yf
import pandas as pd
import datetime as dt
import json
from ..models import Tickers


class Chart:
    def __init__(self, ticker_symbol, period="1d", interval="30m"):
        self.ticker=ticker_symbol
        self.period=period
        self.interval=interval
        self.df_data = None

    def get_timeseries(self):
        try:
            ts = yf.Ticker(self.ticker)
            self.df_data = ts.history(period=self.period, interval=self.interval)
        except Exception as e:
            raise RuntimeError(f"YahooFinance exception while requesting daily data for {self.ticker}") from e
        else:
            self.df_data.index.name = "Date"

    def serialize(self, df):
        return {column: df[column].values.tolist() for column in df.columns.tolist()}

class DailyChart(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(args, kwargs)

    def datetime2str(self, df, datetime_c):
        #print(df)
        df[datetime_c]=df[datetime_c].dt.strftime('%Y-%m-%d %H:%M:%S')

    def process_daily_timeseries(self):
        ###############to test
        if self.df_data.empty:
            try:
                self.df_data = ts.history(start=dt.date.today(), interval=self.interval) 
            except Exception as e:
                print(str(e))
                raise Exception from e
            else:
                if self.df_data.empty:
                    raise Exception('Cant download data for today')
                return self.process_daily_timeseries()
        #####################
        data = self.df_data[['Close']]
        data.reset_index(inplace=True)
        data = data.round(decimals=2)
        self.datetime2str(data, data.columns[0])
        #return self.serialize(data)
        serialized = self.serialize(data)
        serialized['last_update']=data.Date.values[-1]
        serialized['symbol']=self.ticker
        #print(serialized)
        return serialized

class CandleChart(DailyChart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.candle = ['Open', 'High', 'Low', 'Close']

    def date2str(self, df, date_c):
        df[date_c]=df[date_c].dt.strftime('%Y-%m-%d')

    def process_long_timeseries(self):
        data = self.df_data[self.candle]
        data.reset_index(inplace=True)
        data = data.round(decimals=2)
        if self.period in ['1m','3m','1y','5y']:
            self.date2str(data, data.columns[0])
        elif self.interval in ['1d','5d','1wk','1mo','3mo']:
            self.date2str(data, data.columns[0])
        else:
            self.datetime2str(data, data.columns[0])
        return self.serialize(data)
        
if __name__ == "__main__":
    chart = CandleChart("EZJ.L", period="1wk", interval="15m")
    chart.get_timeseries()
    ts = chart.process_long_timeseries()
    # print(ts)
    chart = DailyChart("EZJ.L")
    ts = chart.get_timeseries()
    # print(ts)