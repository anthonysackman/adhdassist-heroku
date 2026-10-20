from app import app
import smtplib
from email.message import EmailMessage

class Emailer:
    def __init__(self) -> None:
        self.msg['From'] = app.config.get('EMAIL_FROM')
        
        # FIXME https://docs.python.org/3/library/email.examples.html