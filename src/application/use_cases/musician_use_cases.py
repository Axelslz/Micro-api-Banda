from src.domain.entities.musician import Musician
from src.domain.port.musician_port import MusicianRepository
from src.infrastructure.rabbitmq.musician_publisher import publish_musician_created, publish_musician_request

class RegisterMusicianUseCase:
    def __init__(self, repository: MusicianRepository):
        self.repository = repository

    def execute(self, data: dict) -> str:
        musician = Musician(
            name=data['name'],
            email=data['email'],
            password=data['password'],  # Consider hashing this password before storage
            phone=data.get('phone', None),
            location=data['location'],
            description=data.get('description', ''),
            repertoire=data.get('repertoire', ''),
            experience=data.get('experience', 0),
            videos=data.get('videos', ''),
            photos=data.get('photos', ''),
            contact_name=data['contact_name'],
            contact_email=data['contact_email'],
            contact_phone=data.get('contact_phone', None),
            social_links=data.get('social_links', '')
        )

        self.repository.add(musician)
        publish_musician_created(musician)
        return "Músico registrado exitosamente"

class FindMusicianByIdUseCase:
    @staticmethod
    def execute(musician_id: int):
        publish_musician_request(musician_id)
        return {"message": "Solicitud enviada a RabbitMQ para buscar el músico por ID"}