from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Barberies(db.Model):
    id = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    distance = db.Column(db.String(5), nullable=False)
    stars = db.Column(db.String(5), nullable=False)
    url = db.Column(db.String(150), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(80), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return '<User %s>' % self.title

class Barbers(db.Model):
    id = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    stars = db.Column(db.String(5), nullable=False)
    url = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return '<User %s>' % self.id