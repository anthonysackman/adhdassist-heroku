import logging

logging_level_codes = {
    'CRITICAL': 50,
    'ERROR': 40,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
    'NOTSET': 0
}

class MainLogger(object):
    def __init__(self, log_name, log_level) -> None:
        # create logger
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)
        
    def _log_controller(self, format=None):
        # create handler and set handler logging level 
        self._log_handler()
        self._log_formatter()
        return self.logger
        
    def _log_handler(self):
        # create handler and set handler logging level 
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(self.logger.level)
        self.logger.addHandler(self.console_handler)
        
    def _log_formatter(self, format=None):
        if format:
            self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - stuff')
        else:
            self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.console_handler.setFormatter(self.formatter)
        
class LogInit(MainLogger):
    def __init__(self, log_name=__name__, log_level=logging_level_codes['DEBUG'], ):
        super().__init__(log_name, log_level)
    
    def _log_init(self):
        self._log_var = self._log_controller()
        return self._log_var