from .connection import db

class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    repertoire = db.Column(db.Text, nullable=True)
    experience = db.Column(db.Integer, nullable=True)
    videos = db.Column(db.Text, nullable=True)
    photos = db.Column(db.Text, nullable=True)
    contact_name = db.Column(db.String(255), nullable=False)
    contact_email = db.Column(db.String(255), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=True)
    social_links = db.Column(db.Text, nullable=True)
