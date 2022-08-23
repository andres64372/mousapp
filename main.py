from flask import Response, request
from flask_cors import CORS
from flask_socketio import SocketIO

import json

from manage import create

from repos.barberies import get_barberies, get_barbers
from repos.users import validate_user, create_user

from domain.login import Login
from domain.signup import SignUp

app = create()

CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/barberies')
def barberies():
  response = get_barberies(request.args.get('City'))
  return Response(json.dumps(response.data), status=response.status, content_type='application/json')

@app.route('/barbers')
def barbers():
  response = get_barbers(request.args.get('City'))
  return Response(json.dumps(response.data), status=response.status, content_type='application/json')

@app.route('/login', methods=['POST'])
def login():
  data = Login.from_dict(request.json)
  response = validate_user(data)
  return Response(json.dumps(response.data), status=response.status, content_type='application/json')

@app.route('/signup', methods=['POST'])
def signup():
  data = SignUp.from_dict(request.json)
  response = create_user(data)
  return Response(json.dumps(response.data), status=response.status, content_type='application/json')

if __name__ == '__main__':
    socketio.run(app, port=8000, host='0.0.0.0', debug=True)