import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Fix: sanitize newline or old-style URI
uri = os.environ.get("DATABASE_URL", "").strip()  # removes '\n'
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri


print("DATABASE_URL from os.environ:", repr(uri), file=sys.stderr)  # for debug

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes

