import json

from Tools.base_request import BaseRequest, BASE_URL_DOG_CEO


class DogAPI(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_DOG_CEO)

    def get_list_all_breeds(self):
        response = self.get('list', 'all')
        return response

    def get_image(self):
        response = self.get('list', 'all')
        return response
