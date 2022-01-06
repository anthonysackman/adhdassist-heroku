import os
from dotenv import load_dotenv

class Config(object):
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI is None:
        SQLALCHEMY_DATABASE_URI = os.getenv('SQL_DATABASE_URL')
    # heavy performance loss
    SQLALCHEMY_TRACK_MODIFICATIONS = False