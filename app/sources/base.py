from abc import ABC, abstractmethod
from app.models.jobs import Job


class JobSource(ABC):

    @abstractmethod
    def search(self, url: str) -> list[Job]:
        pass