from flask import Flask, request, jsonify 
import json


app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'foo': 'bar',
                       'baz': 'damn'})
    
@app.route('/test', methods=['POST'])
def post():
    value = json.loads(request.data)
    return json.dumps(value)

if __name__ == '__main__': 
    app.run()
