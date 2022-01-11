from sqlalchemy import create_engine
from app import app
from app.base_log import _logger
class SqlEngine:
    def __init__(self) -> None:
        self._log = _logger._log(__name__)
        self.engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        self._log.info("SqlEngine initialized")