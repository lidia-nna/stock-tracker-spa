from flask_caching import Cache
from api import create_app
from api.db import db
from api.mail import mail
from api.cache import cache
from api.models import UserModel
import os
import datetime


cfg="api.config." + os.environ.get('CONFIG')
app = create_app(cfg=cfg)

db.init_app(app)
cache.init_app(app)
mail.init_app(app)
#app.app_context().push()


with app.app_context():
    cache.clear()
    db.create_all()
    #create demo user
    if not UserModel.check_user(username='demo'):
        user = UserModel(
            username='demo',
            email=os.environ.get('MAIL_USERNAME'),
            confirmed=True,
            confirmed_on=datetime.datetime.utcnow(),
            registered_on=datetime.datetime.utcnow()
        )
        user.set_password('11111111')
        db.session.add(user)
        db.session.commit()

if __name__ == '__main__':
    app.run()