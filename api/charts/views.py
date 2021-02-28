from flask import request, jsonify
from api.cache import cache
from . import charts
from .logic import DailyChart, CandleChart

@charts.route('/charts/daily')
@cache.cached(timeout=15*60, query_string=True) #15min
def get_daily_chart():
    if not request.args:
        return "No ticker info", 400
    if request.args.get('ticker') is None:
        return "Invalid query parameter", 400
    chart = DailyChart(ticker_symbol=request.args['ticker'], interval='15m')
    try:
        chart.get_timeseries()
        ts = chart.process_daily_timeseries()
    except RuntimeError as e:
        print(str(e))
        return "Error retreiving data from yfinance api", 500
    else:
        return jsonify(ts)

@charts.route('/charts/alltime')
@cache.cached(timeout=240*60, query_string=True) #4hours
def get_historical_data():
    if not request.args:
        return "No ticker info", 400
    if request.args.get('ticker') is None:
        return "Invalid query parameter", 400
    chart = CandleChart(request.args['ticker'], period="1y", interval="1d")
    try:
        chart.get_timeseries()
        ts = chart.process_long_timeseries()
    except RuntimeError as e:
        print(str(e))
        return "Error retreiving data from yfinance api", 500
    else:
        return jsonify(ts)


@charts.route('/charts/week')
@cache.cached(timeout=240*60, query_string=True) #4hours
def get_weekly_data():
    if not request.args:
        return "No ticker info", 400
    if request.args.get('ticker') is None:
        return "Invalid query parameter", 400
    chart = CandleChart(request.args['ticker'], period="1wk", interval="15m")
    try:
        chart.get_timeseries()
        ts = chart.process_long_timeseries()
    except RuntimeError as e:
        print(str(e))
        return "Error retreiving data from yfinance api", 500
    else:
        return jsonify(ts)