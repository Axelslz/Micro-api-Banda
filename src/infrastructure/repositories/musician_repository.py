from src.domain.port.musician_port import MusicianRepository
from src.domain.entities.musician import Musician
from src.infrastructure.database.mysql.connection import db

class MusicianRepositoryImpl(MusicianRepository):
    def add(self, musician: Musician):
        db.session.add(musician)
        db.session.commit()

    def find_by_id(self, musician_id):
        return db.session.query(Musician).filter_by(id=musician_id).first()

    def find_by_email(self, email):
        return db.session.query(Musician).filter_by(email=email).first()