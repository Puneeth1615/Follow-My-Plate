import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_very_secret_and_complex_key_that_you_should_change_immediately_12345') #

uri = os.environ.get("DATABASE_URL", "").strip() #
if uri.startswith("postgres://"): #
    uri = uri.replace("postgres://", "postgresql://", 1) #

app.config['SQLALCHEMY_DATABASE_URI'] = uri #
print("DATABASE_URL from os.environ:", repr(uri), file=sys.stderr) #

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True} #

db = SQLAlchemy(app) #
login_manager = LoginManager(app) #
login_manager.login_view = 'login' #

migrate = Migrate(app, db)

from app import routes, models #