from flask import request, render_template
import json
from app import app
from app.base_log import _logger

_log = _logger._log(__name__)

@app.route('/')
@app.route('/<user>')
def index(user="stranger"):
    _log.debug("INDEX DEBUG", extra={'request':request.__dict__})
    return render_template('index.html', user_val=user)
    
@app.route('/api/', methods=['POST'])
def post():
    _log.debug("POST DEBUG", extra={'request':request.__dict__})
    value = json.loads(request.data)
    return json.dumps(value)
