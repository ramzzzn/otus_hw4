from Tools.base_request import BaseRequest

BASE_URL_JSONPLACEHOLDER = 'https://jsonplaceholder.typicode.com'


class JsonPlaceholderAPI(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_JSONPLACEHOLDER)

    def get_resource(self, route, resource_id, expected_error=False):
        response = self.get(route, resource_id, expected_error)
        return response

    def create_resource(self, route, title: str, body: str, user_id: int, expected_error=False):
        data = {
            'title': title,
            'body': body,
            'userId': user_id,
        }
        return self.post(data, route, is_json=True, expected_error=expected_error)

    def update_comment(self, route, resource_id: int, title: str, body: str, user_id: int, expected_error=False):
        data = {
            'postId': user_id,
            'id': resource_id,
            'name': title,
            'body': body,
        }
        return self.put(data, route, endpoint_id=resource_id, is_json=True, expected_error=expected_error)

    def patch_resource(self, route, resource_id: int, title: str, body: str, expected_error=False):
        data = {
            'title': title,
            'body': body,
        }
        return self.patch(data, route, endpoint_id=resource_id, is_json=True, expected_error=expected_error)

    def delete_resource(self, route, resource_id):
        response = self.delete(route, resource_id)
        return response



    def get_nested_resource(self, route, resource_id, nested_route):
        response = self.get(route, f'{resource_id}/{nested_route}')
        return response
