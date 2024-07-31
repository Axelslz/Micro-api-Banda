import bcrypt
from src.domain.entities.musician import Musician
from src.domain.port.musician_port import MusicianRepository

class RegisterMusicianUseCase:
    def __init__(self, repository: MusicianRepository):
        self.repository = repository

    def execute(self, data: dict) -> dict:
        # Verifica si ya existe un músico con el mismo email
        existing_musician = self.repository.find_by_email(data['email'])
        if existing_musician:
            raise ValueError(f"El músico con el correo electrónico {data['email']} ya existe")

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        musician = Musician(
            name=data['name'],
            email=data['email'],
            password=hashed_password.decode('utf-8'),  # Asegúrate de usar la contraseña hasheada
            phone=data.get('phone'),
            location=data.get('location'),
            description=data.get('description'),
            repertoire=data.get('repertoire'),
            experience=data.get('experience'),
            videos=data.get('videos'),
            photos=data.get('photos'),
            contact_name=data.get('contact_name'),
            contact_email=data.get('contact_email'),
            contact_phone=data.get('contact_phone'),
            social_links=data.get('social_links'),
        )

        self.repository.add(musician)
        return musician.to_dict()

class FindMusicianByIdUseCase:
    def __init__(self, repository: MusicianRepository):
        self.repository = repository

    def execute(self, musician_id: int) -> dict:
        musician = self.repository.find_by_id(musician_id)
        if not musician:
            return {"message": f"Músico con ID {musician_id} no encontrado"}

        return {
            "name": musician.name,
            "location": musician.location,
            "description": musician.description,
            "experience": musician.experience,
            "contact_name": musician.contact_name,
            "contact_email": musician.contact_email,
            "contact_phone": musician.contact_phone
        }
