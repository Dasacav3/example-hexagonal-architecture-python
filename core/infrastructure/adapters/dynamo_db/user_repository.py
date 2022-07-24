from core.domain.ports.dynamo_db.user_repository import IUserRepository
from core.domain.entities.user.user import User


class UserRepository(IUserRepository):
    def __init__(self, dynamodb_client: object, table_name: str):
        self.__dynamodb_client = dynamodb_client
        self.__table_name = table_name

    def save(self, user: User) -> None:
        try:
            self.__dynamodb_client.put_item(
                TableName=self.__table_name,
                Item={
                    'model': {'S': 'user'},
                    'id': {'S': user.get_id()},
                    'name': {'S': user.get_name()},
                    'email': {'S': user.get_email()},
                    'password': {'S': user.get_password()},
                    'created_at': {'S': user.get_created_at()},
                    'updated_at': {'S': user.get_updated_at()}
                }
            )
        except Exception as e:
            print(f'Error: {e}')

        return 'User created successfully'

    def find_by_id(self, id: str):
        try:
            response = self.__dynamodb_client.get_item(
                TableName=self.__table_name,
                Key={
                    'model': {'S': 'user'},
                    'id': {'S': id}
                }
            )

            item = response['Item']

        except Exception as e:
            print(f'Error: {e}')

        return User(
            id=item['id']['S'],
            name=item['name']['S'],
            email=item['email']['S'],
            password=item['password']['S'],
            created_at=item['created_at']['S'],
            updated_at=item['updated_at']['S']
        )
