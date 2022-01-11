import os
from dotenv import load_dotenv
from app.base_log import _logger
#from app.base_log import _log
# environmental variable configuration file
class Config(object):
    def __init__(self) -> None:
        self._log = _logger._log(__name__)
        self._log.info("Config init")
        # heavy performance loss, defaulting to false
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.ENV_VAR = os.environ.get('ENV_VAR')
        
    # set config, defaults to prod config if no value found, config set in related function below
    def set_config(self):
        if self.ENV_VAR == 'local':
            self.local_config()
        else:
            self.prod_config()
        self._log.info("Config set", extra={'env_var':self.ENV_VAR})
    
    def prod_config(self):
        try:    
            self.SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABAsE_URI']
        except Exception as er:
           self. _log.error("config failed, exiting...", extra={'error':er})
           exit()
            
    def local_config(self):
        load_dotenv() # only needed to load .env locally
        try:    
            self.SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
        except Exception as er:
           self. _log.error("config failed, exiting...", extra={'error':er})
           exit()
            
        