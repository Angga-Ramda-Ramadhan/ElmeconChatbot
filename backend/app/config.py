import os 

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MYSQL_HOST = os.environ.get('DB_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASS = os.environ.get('MYSQL_PASS')
    MYSQL_DB = os.environ.get('MYSQL_DB')
    
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"

class DevConfig(Config):

    DEBUG=True


config = {
    'default':DevConfig
}