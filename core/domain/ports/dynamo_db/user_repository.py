from abc import ABC, abstractmethod
from core.domain.entities.user.user import User


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> User:
        pass
