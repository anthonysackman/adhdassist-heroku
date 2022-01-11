import logging
import logging.config
from yaml import safe_load

# python logging configuration and log setter 
# __init__.py runs log_config() and does not need to be run again
# can be used anywhere in the app
# configured to stream output in JSON
# to uss include "from app.base_log import _logger"
# create _log object "_log = _logger._log(__name__)"
# _log can now be used anywhere in the file
# _log.info("error message text", extra={'custom_key':'custom_value'})
# any dictionary key/value pairs included in extra will create tags automatically in log anaylitics
# extra does not need to be included
class _logger:
    def __init__(self) -> None:
        self.name = self.__name__
        
    def _log(name=__name__):
        logger = logging.getLogger(name)
        return logger
    
    def log_config():
        with open('logging_config.yaml', 'r') as f:
            config = safe_load(f.read())
            logging.config.dictConfig(config)



