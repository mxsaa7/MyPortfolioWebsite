from enum import unique
from sqlalchemy.orm import backref, relationship
from flaskportfolio import db
from datetime import datetime, timedelta


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    message = db.Column(db.Text, nullable=False)

def __repr__(self):
    return f"Message('{self.subject}', '{self.message}')"