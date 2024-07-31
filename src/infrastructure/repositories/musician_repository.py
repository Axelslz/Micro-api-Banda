import datetime
from src.domain.port.musician_port import MusicianRepository
from src.domain.entities.musician import Musician
from src.domain.entities.profile_visit import ProfileVisit
from src.infrastructure.database.mysql.connection import db

class MusicianRepositoryImpl(MusicianRepository):
    def add(self, musician: Musician):
        db.session.add(musician)
        db.session.commit()

    def find_by_id(self, musician_id):
        return db.session.query(Musician).filter_by(id=musician_id).first()

    def find_by_email(self, email):
        return db.session.query(Musician).filter_by(email=email).first()
    
    def record_profile_visit(self, musician_id):
        visit = ProfileVisit(musician_id=musician_id)
        db.session.add(visit)
        db.session.commit()

    def get_profile_visits(self, musician_id):
        visits = ProfileVisit.query.filter_by(musician_id=musician_id).all()
        return [visit.timestamp for visit in visits]

    def get_last_profile_visit(self, musician_id):
        return ProfileVisit.query.filter_by(musician_id=musician_id).order_by(ProfileVisit.timestamp.desc()).first()

    def update(self, profile_visit):
        db.session.add(profile_visit)
        db.session.commit()