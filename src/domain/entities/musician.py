from sqlalchemy import Column, Integer, String
from src.infrastructure.database.mysql.connection import db

class Musician(db.Model):
    __tablename__ = 'musicians'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    location = Column(String(100), nullable=True)
    description = Column(String(255), nullable=True)
    repertoire = Column(String(255), nullable=True)
    experience = Column(Integer, nullable=False, default=0)
    videos = Column(String(255), nullable=True)
    photos = Column(String(255), nullable=True)
    contact_name = Column(String(50), nullable=False)
    contact_email = Column(String(50), nullable=False)
    contact_phone = Column(String(20), nullable=True)
    social_links = Column(String(255), nullable=True)

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
