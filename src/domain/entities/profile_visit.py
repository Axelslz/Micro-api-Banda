from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from src.infrastructure.database.mysql.connection import db

class ProfileVisit(db.Model):
    __tablename__ = 'profile_visits'

    id = Column(Integer, primary_key=True, autoincrement=True)
    musician_id = Column(Integer, ForeignKey('musicians.id'), nullable=False)
    timestamp = Column(DateTime, default=func.now(), nullable=False)
    graph_path = Column(String(255))  