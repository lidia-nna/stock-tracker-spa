import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base config"""
    SECRET_KEY = "lidias_secret"
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    PORT = 5000
    UPLOAD_EXTENSIONS = ['.json']
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    CACHE_TYPE='simple'
    JWT_SECRET_KEY="thiskeyisserious"
    JWT_TOKEN_LOCATION=["headers"]
    # JWT_COOKIE_CSRF_PROTECT=False
    # JWT_CSRF_IN_COOKIES=False
    # JWT_ACCESS_COOKIE_PATH=['/tickers','/summary','/ticker']
    # JWT_REFRESH_COOKIE_PATH=['/token/refresh','/auth']
    #JWT_REFRESH_CSRF_COOKIE_PATH=['/token/refresh','/auth']
    JWT_ACCESS_TOKEN_EXPIRES=600
    #JWT_COOKIE_SAMESITE=None
    #JWT_COOKIE_SECURE=True
    MAIL_SERVER="smtp.gmail.com"
    MAIL_PORT=465
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('SECURITY_PASSWORD_SALT')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

class TestConfig(DevConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../test/test.db')
    SECURITY_PASSWORD_SALT=os.environ.get('SECURITY_PASSWORD_SALT')
    PORT = 5500


class ProdConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod.db')
    PORT = 5000
    UPLOAD_EXTENSIONS = ['.json']
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    CACHE_TYPE='simple'
    JWT_SECRET_KEY=""
    JWT_TOKEN_LOCATION=["headers"]
    JWT_ACCESS_TOKEN_EXPIRES=600
    # JWT_COOKIE_CSRF_PROTECT=False
    # JWT_CSRF_IN_COOKIES=False
    # JWT_ACCESS_COOKIE_PATH=['/tickers','/summary','/ticker']
    # JWT_REFRESH_COOKIE_PATH=['/token/refresh','/auth']
    #JWT_REFRESH_CSRF_COOKIE_PATH=['/token/refresh','/auth']
    #JWT_COOKIE_SAMESITE=None
    #JWT_COOKIE_SECURE=True
    MAIL_SERVER="smtp.gmail.com"
    MAIL_PORT=465
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_USERNAME="play.python.test@gmail.com"
    #MAIL_PASSWORD=os.environ["MAIL_PASSWORD"]
    MAIL_DEFAULT_SENDER='play.python.test@gmail.com'
    # DB_HOST = os.environ["DB_HOST"]
    # DB_PORT = os.environ.get("DB_PORT", 3306)
    # DB_DATABASE = os.environ["DB_DATABASE"]
    # DB_USER = os.environ["DB_USER"]
    # DB_PASSWORD = os.environ["DB_PASSWORD"]
    # SQLALCHEMY_DATABASE_URI = (
    #     f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    # )
