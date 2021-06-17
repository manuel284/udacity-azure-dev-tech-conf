import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL=os.environ.get('POSTGRES_URL')
    POSTGRES_USER=os.environ.get('POSTGRES_USER')
    POSTGRES_PW=os.environ.get('POSTGRES_PW')
    POSTGRES_DB=os.environ.get('POSTGRES_DB')
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SERVICE_BUS_CONNECTION_STRING =os.environ.get('SERVICE_BUS_CONNECTION_STRING')
    SERVICE_BUS_QUEUE_NAME =os.environ.get('SERVICE_BUS_QUEUE_NAME')

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False