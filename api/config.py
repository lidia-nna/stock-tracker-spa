import os

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
    CACHE_TYPE='simple'
    JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION=["headers"]
    JWT_ACCESS_TOKEN_EXPIRES=600
    UPLOAD_EXTENSIONS = ['.json']

class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    PORT = 5000
    CORS_ORIGINS="http://localhost:8080" 
    CORS_HEADERS=['Content-Type', 'Authorization', 'Cache-Control', 'X-Forwarded-For']
    CORS_SUPPORTS_CREDENTIALS=True
   


class TestConfig(DevConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../test/test.db')
    PORT = 5500


class ProdConfig(Config):
    ENV = 'production'
    #CORS_ORIGINS=os.environ.get('VUE_URL')
    #CORS_RESOURCES='r”/*”'
    #CORS_HEADERS=['Content-Type', 'Authorization', 'Cache-Control']
    #CORS_SUPPORTS_CREDENTIALS=True
    PROJECT_ID = os.environ.get('PROJECT_ID')
    BUCKET_NAME = os.environ.get('BUCKET_NAME')
    DB_NAME = os.environ.get('DB_FILE_NAME')
    DB_TMP_PATH = os.environ.get('DB_LOCAL_PATH')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(os.environ.get('DB_LOCAL_PATH'))
    #DB_NAME = os.environ.get("DB_NAME")
    #DB_INSTANCE_NAME = os.environ.get('DB_INSTANCE_NAME')
    #DB_INSTANCE_REGION = os.environ.get("DB_INSTANCE_REGION")
    #DB_PUBLIC_PI_ADDRESS = os.environ.get("DB_PUBLIC_PI_ADDRESS")
    #DB_USER = os.environ.get("DB_USER")
    #DB_PASSWORD = os.environ.get("DB_PASSWORD")
    #SQLALCHEMY_DATABASE_URI = (
    #    f"postgres+pg8000://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?unix_sock=/cloudsql/{PROJECT_ID}:{DB_INSTANCE_REGION}:{DB_INSTANCE_NAME}/.s.PGSQL.5432"
    #)
