from http.client import FORBIDDEN
from xml.dom import NotFoundErr
from flask import request, render_template, flash, redirect, url_for
import json
from app import app, db
from app.base_log import _logger
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import user_account, user_email_auth
from werkzeug.urls import url_parse

_log = _logger._log(__name__)

#login_required redirects to /login if auth fails
@login_required
@app.route('/')        
@app.route('/<user>')
def index(user="stranger"):
    _log.debug("INDEX DEBUG", extra={'request':request.__dict__})
    return render_template('index.html', user_val=user)

# Login Page using flask-wtf for form validation
@app.route('/login', methods=['GET', 'POST'])
def login():
    # creates login form object, validate_on_submit will only run on submit() POST within login.html
    # validate_on_submit checks user form against form and returns errors/ends request if validation fails
    # GET requests return false and login.html is rendered and returned
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # check if user_account record with this email exists and user password_hash matched
        user = user_account.query.filter_by(email=login_form.email.data).first()
        if user is None or not user.check_password(login_form.password.data):
            #flash passes data into next request
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        # next page checks to see if user was redirected to login and returns them if so
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        new_user = user_account(email=register_form.email.data)
        new_user.set_password(register_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        new_email_auth = user_email_auth(user_account_id=new_user.id)
        new_email_auth.set_url_hash()
        db.session.add(new_email_auth)
        db.session.commit()
        flash('Registration Email Sent!')
        return redirect(url_for('login'))
    return render_template('register.html', form=register_form)

@login_required
@app.route('/validate-email/<validationHash>', methods=['GET', 'POST'])
def validate_email(validationHash=None):
    _url_hash = user_email_auth(id=current_user.id)
    if validationHash is None:
        raise NotFoundErr
    if _url_hash.first().url_hash == validationHash:
        return "test"
    

# end user session
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/api/', methods=['POST'])
def post():
    _log.debug("POST DEBUG", extra={'request':request.__dict__})
    value = json.loads(request.data)
    return json.dumps(value)
