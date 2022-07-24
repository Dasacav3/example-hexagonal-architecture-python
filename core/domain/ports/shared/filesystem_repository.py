from abc import ABC, abstractmethod


class IFilesystemRepository(ABC):
    @abstractmethod
    def put(self, key: str, value: str) -> None:
        pass

    @abstractmethod
    def get(self, key: str) -> str:
        pass

    @abstractmethod
    def delete(self, key) -> None:
        pass
