from core.domain.ports.shared.filesystem_repository import IFilesystemRepository


class S3FilesystemRepository(IFilesystemRepository):
    def __init__(self, s3_client: object, bucket: str) -> None:
        super().__init__()
        self.__s3_client = s3_client
        self.__bucket = bucket

    def put(self, key: str, value: str) -> None:
        self.__s3_client.put_object(
            Bucket=self.__bucket,
            Key=key,
            Body=value
        )

    def get(self, key: str) -> str:
        response = self.__s3_client.get_object(
            Bucket=self.__bucket,
            Key=key
        )

        return response['Body'].read().decode('utf-8')

    def delete(self, key: str) -> None:
        self.__s3_client.delete_object(
            Bucket=self.__bucket,
            Key=key
        )
