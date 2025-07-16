
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # CHANGE THIS LINE: Increase the length from 128 to a larger value
    password_hash = db.Column(db.String(255)) # Changed from 128 (or whatever it was)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    goal = db.Column(db.String(20))
    food_entries = db.relationship('FoodEntry', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'

class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    calories = db.Column(db.Float, nullable=False)
    meal_type = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<FoodEntry {self.description} ({self.calories} kcal) on {self.date_posted.strftime("%Y-%m-%d")}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))