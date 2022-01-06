from flask import request, render_template
import json
from app import app


@app.route('/')
@app.route('/<user>')
def index(user=None):
    user_set = user or 'Stranger'
    return render_template('index.html', user=user_set)
    
@app.route('/api/', methods=['POST'])
def post():
    value = json.loads(request.data)
    return json.dumps(value)
