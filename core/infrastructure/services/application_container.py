import dotenv
from dependency_injector import providers, containers
from core.infrastructure.services.image_container import ImageContainer
from core.infrastructure.services.user_container import UserContainer


dotenv.load_dotenv()


class ApplicationContainer(containers.DeclarativeContainer):

    user_container = providers.Container(
        UserContainer
    )

    image_container = providers.Container(
        ImageContainer
    )
