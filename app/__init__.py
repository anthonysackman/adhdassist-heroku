from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.mainlogger import LogInit, logging_level_codes

app = Flask(__name__)

logger = LogInit(log_name=__name__, log_level=logging_level_codes['INFO'])
logger._log_init()

from app.config import Config
_config = Config()
_config.set_config()
app.config.from_object(_config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models