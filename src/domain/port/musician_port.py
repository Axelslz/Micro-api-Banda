from abc import ABC, abstractmethod
from src.domain.entities.musician import Musician

class MusicianRepository(ABC):
    @abstractmethod
    def add(self, musician: Musician):
        pass

