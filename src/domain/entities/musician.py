import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.infrastructure.database.mysql.connection import db

class Musician(db.Model):
    __tablename__ = 'musicians'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(20))
    location = Column(String(100))
    description = Column(String(255))
    repertoire = Column(String(255))
    experience = Column(Integer)
    videos = Column(String(255))
    photos = Column(String(255))
    contact_name = Column(String(50))
    contact_email = Column(String(100))
    contact_phone = Column(String(20))
    social_links = Column(String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'location': self.location,
            'description': self.description,
            'repertoire': self.repertoire,
            'experience': self.experience,
            'videos': self.videos,
            'photos': self.photos,
            'contact_name': self.contact_name,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'social_links': self.social_links
        }
