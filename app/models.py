from app import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
# UserMixin impliments standard database configurations for user session tracking (used specifically for flask_login package)
class user_account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=True)
    #is_email_validated = db.Column(db.Boolean, nullable=False)
    email_auth_codes = db.relationship('user_email_auth', backref='user_account', lazy=True)

    def __repr__(self):
        return '<user_account {}>'.format(self.email)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return user_account.query.get(int(id))

class user_email_auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_account_id = db.Column(db.Integer, db.ForeignKey('user_account.id'))
    url_hash = db.Column(db.String(120), nullable=False)
    created_date = db.Column(func.DateTime(timezone=True), default=func.current_time())