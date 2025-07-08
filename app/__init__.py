from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'

# ✅ Correct order — set config before initializing db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}

# ✅ Now initialize database
db = SQLAlchemy(app)

# ✅ Login manager setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# ✅ Import routes at the end to avoid circular imports
from app import routes
