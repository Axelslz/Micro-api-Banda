from src.domain.port.musician_port import MusicianRepository
from src.infrastructure.database.mysql.connection import db
from src.infrastructure.database.mysql.models import Musician

class MusicianRepositoryImpl(MusicianRepository):
    def add(self, musician):
        new_musician = Musician(name=musician.name, email=musician.email, password=musician.password, phone=musician.phone, location=musician.location, description=musician.description, repertoire=musician.repertoire, experience=musician.experience, videos=musician.videos, photos=musician.photos, contact_name=musician.contact_name, contact_email=musician.contact_email, contact_phone=musician.contact_phone, social_links=musician.social_links)
        db.session.add(new_musician)
        db.session.commit()
