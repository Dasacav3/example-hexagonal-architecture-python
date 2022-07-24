from datetime import datetime


class User:
    __id: str
    __name: str
    __email: str
    __password: str
    __created_at: str
    __updated_at: str

    def __init__(self, id: str, name: str, email: str, password: str, created_at: str = '', updated_at: str = '') -> None:
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__created_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") if created_at == '' else created_at
        self.__updated_at = '' if updated_at == '' else updated_at

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_password(self) -> str:
        return self.__password

    def get_created_at(self) -> str:
        return self.__created_at

    def get_updated_at(self) -> str:
        return self.__updated_at
