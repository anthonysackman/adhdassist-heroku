import os
from dotenv import load_dotenv
from app.mainlogger import LogInit as li
from app import mainlogger

_log = mainlogger.logging

class Config(object):
    def __init__(self) -> None:
        _log.warning("file {name_var} initialized".format(name_var=__name__, self_var=self))
        # heavy performance loss, defaulting to false
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.ENV_VAR = os.environ.get('ENV_VAR')
        
    def set_config(self):
        #FIXME log env var selected 
        if self.ENV_VAR == 'local':
            self.local_config()
        else:
            self.prod_config()
    
    def prod_config(self):
        try:    
            self.SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
        except KeyError:
            #FIXME add log for failed environmental variable
            print(KeyError)
            
    def local_config(self):
        load_dotenv()
        try:    
            self.SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
        except KeyError:
            #FIXME add log for failed environmental variable
            print(KeyError)
            
        