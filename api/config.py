import os
#from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env')) #doesn't seem to work

class Config:
    """Base config"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG=False
    TESTING = False
    MAIL_SERVER="smtp.gmail.com"
    MAIL_PORT=465
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SECURITY_PASSWORD_SALT=os.environ.get('SECURITY_PASSWORD_SALT')
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True

class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    PORT = 5000
    UPLOAD_EXTENSIONS = ['.json']
    CACHE_TYPE='simple'
    JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION=["headers"]
    JWT_ACCESS_TOKEN_EXPIRES=600
    CORS_ORIGINS="http://localhost:8080" #process.env.VUE_SERVER
    CORS_HEADERS=['Content-Type', 'Authorization', 'Cache-Control']
    CORS_SUPPORTS_CREDENTIALS=True
   


class TestConfig(DevConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../test/test.db')
    PORT = 5500


class ProdConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod.db')
    PORT = 5000
    # DB_HOST = os.environ["DB_HOST"]
    # DB_PORT = os.environ.get("DB_PORT", 3306)
    # DB_DATABASE = os.environ["DB_DATABASE"]
    # DB_USER = os.environ["DB_USER"]
    # DB_PASSWORD = os.environ["DB_PASSWORD"]
    # SQLALCHEMY_DATABASE_URI = (
    #     f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    # )
