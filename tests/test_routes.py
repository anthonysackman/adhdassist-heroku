from app import app, routes
from flask import Flask, request
import json

def test_index_type(client):
    index = client.get('/test')
    content_type = str(index.headers).split(';')[0]
    assert content_type == 'Content-Type: text/html'
    name = str(index.data).split('<h1>')[1].split('<')[0]
    assert "test" in name
    _index = client.get('/')
    _name = str(_index.data).split('<h1>')[1].split('<')[0]
    assert "stranger" in _name

def test_api(client):
    api = client.post('/api/', data=json.dumps({"test":"data"}))
    print(type(api.data))
    api_data = json.loads(api.data)
    assert api_data['test'] == 'data'