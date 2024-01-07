from Tools.base_request import BaseRequest

BASE_URL_DOG_CEO = 'https://dog.ceo/api'


class DogAPI(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_DOG_CEO)

    def get_list_all_breeds(self, expected_error=False):
        response = self.get('breeds/list/all', expected_error)
        return response

    def get_random_image(self, number_of_images: int, expected_error=False):
        if number_of_images:
            response = self.get('breeds/image/random', number_of_images, expected_error)
        else:
            response = self.get('breeds/image/random', expected_error)
        return response

    def get_all_images_by_breed(self, breed_name: str, expected_error=False):
        response = self.get('breed', f'{breed_name}/images/', expected_error)
        return response

    def get_images_by_breed(self, breed_name: str, number_of_images: int, expected_error=False):
        if number_of_images:
            response = self.get('breed', f'{breed_name}/images/random/{number_of_images}', expected_error)
            # if len(response['message']) < number_of_images:
            #     print('The number of images on the server is less than the requested number of images')
        else:
            response = self.get('breed', f'{breed_name}/images/random/', expected_error)
        return response

    def list_all_sub_breeds(self, breed_name: str, expected_error=False):
        response = self.get(f'breed/{breed_name}', 'list', expected_error)
        return response

    def list_all_sub_breeds_images(self, breed_name: str, sub_breed_name: str, expected_error=False):
        response = self.get(f'breed/{breed_name}', f'{sub_breed_name}/images', expected_error)
        return response

    def list_random_image_by_sub_breed(self, breed_name: str, sub_breed_name: str, number_of_images: int,
                                       expected_error=False):
        if number_of_images:
            response = self.get(f'breed/{breed_name}', f'{sub_breed_name}/images/random/{number_of_images}',
                                expected_error)
        else:
            response = self.get(f'breed/{breed_name}', f'{sub_breed_name}/images/random/',
                                expected_error)
        return response
