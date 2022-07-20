from datetime import datetime
from email.policy import default
from enum import unique
from project import db
from flask_login import UserMixin
from . import login_manager


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.BigInteger, unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    email_verified = db.Column(db.Boolean, default=0)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f"User('{self.name}','{self.email}','{self.phone}','{self.password}')"

    def get_id(self):
        return (self.user_id)

    def update(self):
        db.session.commit()
