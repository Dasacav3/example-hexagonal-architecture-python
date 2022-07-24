import base64
from core.domain.ports.shared.filesystem_repository import IFilesystemRepository


class SaveImageAction:
    def __init__(self, filesystem_repository: IFilesystemRepository) -> None:
        self.__filesystem_repository = filesystem_repository

    def execute(self, content: str, image_name: str) -> None:
        self.__filesystem_repository.put(
            image_name,
            base64.b64decode(content)
        )
