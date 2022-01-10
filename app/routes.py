from flask import request, render_template
import json
from app import app

# from app.mainlogger import MainLogger as ml
from app.mainlogger import LogInit as li, logging_level_codes

# initialize logger
#_log = li().logger

@app.route('/')
@app.route('/<user>')
def index(user="stranger"):
    _log.warning(f"request {request.url}")
    return render_template('index.html', user_val=user)
    
@app.route('/api/', methods=['POST'])
def post():
    value = json.loads(request.data)
    return json.dumps(value)
