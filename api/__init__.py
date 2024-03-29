from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from .config import DevConfig
from .today import today
from .ticker import ticker
from .tickers import tickers
from .charts import charts
from .users import users
from .db import db
from .limiter import limiter



def create_app(cfg = DevConfig):
    app = Flask(__name__)
    CORS(app)
    jwt = JWTManager(app)
    app.config.from_object(cfg)
    limiter.init_app(app)
    app.register_blueprint(today)
    app.register_blueprint(ticker)
    app.register_blueprint(tickers)
    app.register_blueprint(charts)
    app.register_blueprint(users)

  
    
    @app.route('/')
    def index():
        #return 'Running API'
        return render_template('index.html')

    return app
    

   

    


            


    # @app.route('/ticker', methods=['PUT'])
    # def update_ticker():
    #     data = request.form
    #     #validation handled in the front-end
    #     for record in ticker_db:
    #         if data.get('ID') == record.get('ID'):
    #             for k, v in data.items():
    #                 record[k] = v
    #         else:
    #             return "No record to update", 404
    #     return 200

   