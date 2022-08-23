from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.model import db
from models.model import Barberies, Barbers, User

from conf import settings

def create():
    app = Flask(__name__)
    admin = Admin(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    admin.add_view(ModelView(Barberies,db.session))
    admin.add_view(ModelView(Barbers,db.session))
    admin.add_view(ModelView(User,db.session))
    return app