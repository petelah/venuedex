from datetime import datetime
from vd import db, login_manager
from flask import current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(10), nullable=False)
    business_name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    menu = db.Column(db.String(100), nullable=True)

    food = db.Column(db.Boolean, nullable=True)
    booze = db.Column(db.Boolean, nullable=True)
    pickup = db.Column(db.Boolean, nullable=True)
    selfd = db.Column(db.Boolean, nullable=True)
    uber = db.Column(db.Boolean, nullable=True)
    deliveroo = db.Column(db.Boolean, nullable=True)
    bopple = db.Column(db.Boolean, nullable=True)

    instagram = db.Column(db.String(100), nullable=True)
    facebook = db.Column(db.String(200), nullable=True)

    email = db.Column(db.String(120), unique=True, nullable=False)
    spinfo = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(1024), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    approved = db.Column(db.Boolean, nullable=True, default=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return f"Post('{self.business_name}', '{self.date_posted}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.User}')"

class BlogPost(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"BlogPost('{self.User}')"
