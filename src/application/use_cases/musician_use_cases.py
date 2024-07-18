from src.domain.entities.musician import Musician
from src.domain.port.musician_port import MusicianRepository
from src.infrastructure.rabbitmq.musician_publisher import publish_musician_created

class RegisterMusicianUseCase:
    def __init__(self, repository: MusicianRepository):
        self.repository = repository

    def execute(self, data: dict) -> Musician:
        """
        Execute the use case to register a musician.

        :param data: A dictionary with musician data.
        :return: The registered Musician entity.
        """
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

        # Publicar mensaje en RabbitMQ
        publish_musician_created(musician)

        return musician
