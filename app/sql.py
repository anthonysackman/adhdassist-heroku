from sqlalchemy import create_engine
from app import app

class SqlEngine:
    def __init__(self) -> None:
        self.engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])