from flask import Response
from flask_cors import CORS
from flask_socketio import SocketIO

import json

from manage import create
from models.model import Barberies, Barbers, db

app = create()

CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

dummyList = {
  "barberies": [
    {"key": "a", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "b", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "c", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "d", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "e", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "f", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "g", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "h", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "i", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "j", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "k", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "l", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "m", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},
    {"key": "n", "title": "CAVALIERE", "location": "Laureles", "distance": "9.8", "stars": "4.3", "url": "https://blog.agendapro.com/hubfs/Barberia.png", "longitude": -75.590640, "latitude": 6.248037},

  ],
  "barbers": [
    {"key": "a", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "b", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "c", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "d", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "e", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "f", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "g", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "h", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "i", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "j", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
    {"key": "k", "title": "Andres", "stars": "4.3", "url": "https://cms.modumb.com/storage/carreras/mundo-barberia-149.png"},
  ]
}

@app.route('/barberies')
def barberies():
  # from secrets import token_hex
  # for i in range(10):
  #   id = token_hex(8)
  #   insert = Barberies(
  #     id=id,
  #     title="Cavaliere",
  #     location="Laureles",
  #     distance="9.8",
  #     stars="4.3",
  #     url="https://blog.agendapro.com/hubfs/Barberia.png",
  #     longitude=-75.590640,
  #     latitude=6.248037,
  #     city="Medellín"
  #   )
  #   db.session.add(insert)
  # for i in range(15):
  #   id = token_hex(8)
  #   insert = Barbers(
  #     id=id,
  #     first_name="Andres",
  #     last_name="Herrera",
  #     stars="4.3",
  #     url="https://cms.modumb.com/storage/carreras/mundo-barberia-149.png",
  #     city="Medellín"
  #   )
  #   db.session.add(insert)
  # db.session.commit()
  data = []
  barberies = Barberies.query.filter_by(city="Medellín").all()
  for barbery in barberies:
    data.append({
      "key": barbery.id, 
      "title": barbery.title, 
      "location": barbery.location, 
      "distance": barbery.distance, 
      "stars": barbery.stars, 
      "url": barbery.url, 
      "longitude": barbery.longitude, 
      "latitude": barbery.latitude
    })

  return Response(json.dumps(data), status=200, content_type='application/json')

@app.route('/barbers')
def barbers():
  data = []
  barbers = Barbers.query.filter_by(city="Medellín").all()
  for barber in barbers:
    data.append({
      "key": barber.id, 
      "title": f"{barber.first_name} {barber.last_name}", 
      "stars": barber.stars, 
      "url": barber.url, 
    })
  return Response(json.dumps(data), status=200, content_type='application/json')

if __name__ == '__main__':
    socketio.run(app)