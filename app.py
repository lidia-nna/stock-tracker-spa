from flask_caching import Cache
from api import create_app
from api.db import db
from api.mail import mail
from api.cache import cache
import os


cfg="api.config." + os.environ.get('CONFIG')
app = create_app(cfg=cfg)

db.init_app(app)
cache.init_app(app)
mail.init_app(app)
#app.app_context().push()


with app.app_context():
    cache.clear()
    db.create_all()

if __name__ == '__main__':
    app.run()