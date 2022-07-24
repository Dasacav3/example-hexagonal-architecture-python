import os
from dependency_injector import providers, containers
from core.application.users.create_user_action import CreateUserAction
from core.infrastructure.adapters.dynamo_db.user_repository import UserRepository
from core.infrastructure.services.aws_container import AwsContainer


class UserContainer(containers.DeclarativeContainer):

    aws_container = providers.Container(
        AwsContainer
    )

    user_repository = providers.Singleton(
        UserRepository,
        dynamodb_client=aws_container().dynamodb_client,
        table_name=os.getenv('DYNAMODB_TABLE')
    )

    create_user_action = providers.Singleton(
        CreateUserAction,
        user_repository=user_repository
    )
