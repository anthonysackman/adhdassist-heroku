import os
from dotenv import load_dotenv

class Config(object):
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # heavy performance loss
    SQLALCHEMY_TRACK_MODIFICATIONS = False