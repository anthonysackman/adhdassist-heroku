from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.base_log import _logger
from app.config import Config
from flask_login import LoginManager
from flask_mail import Mail

# flask app init
app = Flask(__name__)
# set login/session object, loginview sets default login page for protected endpoints
login = LoginManager(app)
login.login_view = 'login'
# load/set logging_config.yml for logging
_logger.log_config()
_log = _logger._log(__name__)
# Configure flask_mailer
mail = Mail(app)
# load enviromental variables, attaches to flasp app object
_config = Config()
_config.set_config()
app.config.from_object(_config)
# create db and db migration objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models