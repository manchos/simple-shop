from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap



app = Flask(__name__)


app.config.from_object('app.config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

Bootstrap(app)

from app import routes, models