from flask_cors import CORS
from flask_caching import Cache
from api import create_app
from api.config import DevConfig 
from api.db import db
from api.mail import mail
from api.cache import cache



app = create_app()
CORS(app, resources={r"/*": {"origins": ["http://localhost:8080"]}}, allow_headers=['Content-Type', 'Authorization', 'Cache-Control'], supports_credentials=True)

db.init_app(app)
cache.init_app(app)
mail.init_app(app)
#app.app_context().push()


with app.app_context():
    cache.clear()
    db.create_all()

if __name__ == '__main__':
    app.run()