from core.infrastructure.services.application_container import ApplicationContainer

application_container = ApplicationContainer()


def create_user(user_data: dict):
    print(user_data)
    application_container.user_container().create_user_action().execute(user_data)


def save_image(image_data: dict):
    print(image_data)
    application_container.image_container().save_image_action().execute(
        image_data['content'], image_data['name']
    )


if __name__ == '__main__':

    print('''
    This is a sample application implementating hexagonal architecture.

    You can use this application to create a new user to dynamodb or to upload an image to s3.

    Select an option:
    1. Create a new user
    2. Upload an image
    ''')
    option = int(input('Enter option: '))

    if option == 1:
        user_name = input('Enter your name: ')
        user_email = input('Enter your email: ')
        user_password = input('Enter your password: ')

        user_data = {
            'name': user_name,
            'email': user_email,
            'password': user_password
        }

        create_user(user_data)
    elif option == 2:
        image_name = input('Enter your image name: ')
        image_content = input('Enter your image content: ')
        mime_type = input('Enter your image mime type: ')
        size = input('Enter your image size: ')

        image_data = {
            'name': image_name,
            'content': image_content,
            'mime_type': mime_type,
            'size': size
        }

        save_image(image_data)
