from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

ticker_db = [
{
    'ID': 1,
    'Ticker':'EZJ.L',
    "Name": "Easyjet",
    'Bought': 509.54,
    'Upper limit': 0.3,
    'Lower limit': 0.2,
    'No shares': 97,
},
{
    'ID': 2,
    'Ticker':'BWY.L',
    "Name": "Bellway",
    'Bought': 2603.42,
    'Upper limit': 0.3,
    'Lower limit': 0.2,
    'No shares': 19,
},
{
    'ID': 3,
    'Ticker':'BWY.L',
    "Name": "Bellway",
    'Bought': 2506.35,
    'Upper limit': 0.3,
    'Lower limit': 0.2,
    'No shares': 20,
},
{   
    'ID': 4,
    "Ticker": "SBRY.L", 
    "Name": "Sainsburys",
    'Upper limit': 0.3,
    'Lower limit': 0.2,  
    "Bought":  196.40, 
    "No shares": 127,  
}, 
{
    'ID': 5,
    'Ticker':'IXI.L',
    "Name": "IXICO",
    'Upper limit': 0.3,
    'Lower limit': 0.2,         
    "Bought":    63.0, 
    "No shares": 7500, 
},
{   
    'ID': 6,
    'Ticker':'NCR',
    "Name": "NCR", 
    'Upper limit': 0.3,
    'Lower limit': 0.2,         
    "Bought":   17.78, 
    "No shares": 302,  

}
]

last_id = ticker_db[-1]['ID']

import pandas as pd
dfdb = pd.DataFrame(ticker_db)
dfdb.set_index("Ticker", inplace=True)