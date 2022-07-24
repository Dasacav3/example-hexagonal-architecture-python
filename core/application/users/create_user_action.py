from uuid import uuid4
from core.domain.entities.user.user import User
from core.domain.ports.dynamo_db.user_repository import IUserRepository


class CreateUserAction:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.__user_repository = user_repository

    def execute(self, user_data: dict) -> None:
        user = self.__create_user(user_data)

        return self.__user_repository.save(user)

    def __create_user(self, user_data: dict) -> User:
        return User(
            id=uuid4().__str__(),
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password']
        )
