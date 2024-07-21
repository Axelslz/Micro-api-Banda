import bcrypt
from src.domain.port.musician_port import MusicianRepository

class LoginMusicianUseCase:
    def __init__(self, repository: MusicianRepository):
        self.repository = repository

    def execute(self, email: str, password: str) -> dict:
        musician = self.repository.find_by_email(email)
        if not musician or not bcrypt.checkpw(password.encode('utf-8'), musician.password.encode('utf-8')):
            return {"message": "Invalid email or password"}
        
        return {"message": "Login successful", "musician": musician.to_dict()}
