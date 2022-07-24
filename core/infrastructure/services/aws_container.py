import boto3
import os
import dotenv
from dependency_injector import providers, containers


dotenv.load_dotenv()


class AwsContainer(containers.DeclarativeContainer):

    dynamodb_client = providers.Factory(
        boto3.client,
        service_name='dynamodb',
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    s3_client = providers.Factory(
        boto3.client,
        service_name='s3',
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
