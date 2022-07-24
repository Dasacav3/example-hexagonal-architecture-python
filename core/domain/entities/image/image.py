from datetime import datetime


class Image:
    __id: str
    __name: str
    __type: str
    __size: int
    __category: str
    __uri: str
    __created_at: str
    __updated_at: str

    def __init__(self, id: str, name: str, type: str, size: int, category: str, uri: str, created_at: str = '', updated_at: str = ''):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__size = size
        self.__category = category
        self.__uri = uri
        self.__created_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") if created_at == '' else created_at
        self.__updated_at = None if updated_at == '' else updated_at

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_type(self) -> str:
        return self.__type

    def get_size(self) -> int:
        return self.__size

    def get_category(self) -> str:
        return self.__category

    def get_uri(self) -> str:
        return self.__uri

    def get_created_at(self) -> str:
        return self.__created_at

    def get_updated_at(self) -> str:
        return self.__updated_at
