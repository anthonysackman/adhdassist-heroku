from flask import Flask, request, jsonify , render_template
import json


app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def index(user=None):
    user_set = user or 'Stranger'
    return render_template('index.html', user=user_set)
    
@app.route('/api/', methods=['POST'])
def post():
    value = json.loads(request.data)
    return json.dumps(value)

if __name__ == '__main__': 
    app.run()
