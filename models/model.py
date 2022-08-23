from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Barberies(db.Model):
    id = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    location = db.Column(db.String(80), nullable=True)
    stars = db.Column(db.String(5), nullable=True)
    url = db.Column(db.String(150), nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    city = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean, default=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    barber = db.relationship('Barbers', backref='barberies')

    def __repr__(self):
        return '<User %s>' % self.title

class Schedule(db.Model):
    id = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    day = db.Column(db.String(3), nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)
    barber_id = db.Column(db.String(16), db.ForeignKey('barbers.id'))

    def __repr__(self):
        return '<User %s>' % self.day

class Bookings(db.Model):
    id = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=True)
    start = db.Column(db.Time, nullable=True)
    end = db.Column(db.Time, nullable=True)
    barber_id = db.Column(db.String(16), db.ForeignKey('barbers.id'))
    user_id = db.Column(db.String(16), db.ForeignKey('user.id'))
    service_id = db.Column(db.String(16), db.ForeignKey('services.id'))

    def __repr__(self):
        return '<User %s>' % self.day

class Barbers(db.Model):
    id = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    barbery_id = db.Column(db.String(16), db.ForeignKey('barberies.id'))
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    stars = db.Column(db.String(5), nullable=True)
    url = db.Column(db.String(150), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=True, unique=True)
    password = db.Column(db.String(80), nullable=True)
    status = db.Column(db.Boolean, default=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    schedule = db.relationship('Schedule', backref='barbers')
    service = db.relationship('Services', backref='barbers')
    booking = db.relationship('Bookings', backref='barbers')

    def __repr__(self):
        return '<User %s>' % self.last_name

class Services(db.Model):
    id = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    barbery_id = db.Column(db.String(16), db.ForeignKey('barbers.id'))
    name = db.Column(db.String(80), nullable=True)
    cost = db.Column(db.Float, nullable=True)   
    span = db.Column(db.Time, nullable=False) 
    booking = db.relationship('Bookings', backref='services')

    def __repr__(self):
        return '<User %s>' % self.name

class User(db.Model):
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    status = db.Column(db.Boolean, default=False)
    booking = db.relationship('Bookings', backref='user')

    def __repr__(self):
        return '<User %s>' % self.email