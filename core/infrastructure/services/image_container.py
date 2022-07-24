import os
from dependency_injector import providers, containers
from core.application.images.save_image_action import SaveImageAction
from core.infrastructure.services.aws_container import AwsContainer
from core.infrastructure.adapters.shared.s3_filesystem_repository import S3FilesystemRepository


class ImageContainer(containers.DeclarativeContainer):

    aws_container = providers.Container(
        AwsContainer
    )

    filesystem_repository = providers.Singleton(
        S3FilesystemRepository,
        s3_client=aws_container().s3_client,
        bucket=os.getenv('BUCKET_NAME')
    )

    save_image_action = providers.Singleton(
        SaveImageAction,
        filesystem_repository=filesystem_repository
    )
