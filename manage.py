from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.model import db
from models.model import Barberies, Barbers

def create():
    app = Flask(__name__)
    admin = Admin(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://eyxfxcbtjdttob:c5381b6c675238d33864d72cb78c30c557a758bc409438b6d6add524e714256a@ec2-107-22-122-106.compute-1.amazonaws.com:5432/d5ju17hotgn0hc"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '8gv$4fg143G34g85$g4GHE54h45Rgeg54wt'
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    admin.add_view(ModelView(Barberies,db.session))
    admin.add_view(ModelView(Barbers,db.session))
    return app