from models.model import db
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from conf import settings
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)