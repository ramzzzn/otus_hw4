import requests
import pprint


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(
            self, url, request_type, data=None, is_json=False,
            expected_error=False
    ):
        pprint.pprint(f'Request to: {url}')
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                if is_json:
                    response = requests.post(url, json=data)
                else:
                    response = requests.post(url, data=data)
            elif request_type == 'PUT':
                if is_json:
                    response = requests.put(url, json=data)
                else:
                    response = requests.put(url, data=data)
            elif request_type == 'PATCH':
                if is_json:
                    response = requests.patch(url, json=data)
                else:
                    response = requests.patch(url, data=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200 or 201:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        # # log part
        # pprint.pprint(f'{request_type} example')
        # pprint.pprint(response.url)
        # pprint.pprint(response.status_code)
        # pprint.pprint(response.reason)
        # pprint.pprint(response.text)
        # pprint.pprint(response.json())
        # pprint.pprint('**********')
        return response

    def get(self, endpoint, endpoint_id=None, expected_error=False):
        if endpoint_id:
            url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        else:
            url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, body, endpoint, endpoint_id=None, is_json=False, expected_error=False):
        if endpoint_id:
            url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        else:
            url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'POST', data=body, is_json=is_json, expected_error=expected_error)
        return response

    def put(self, body, endpoint, endpoint_id=None, is_json=False, expected_error=False):
        if endpoint_id:
            url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        else:
            url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'PUT', data=body, is_json=is_json, expected_error=expected_error)
        return response

    def patch(self, body, endpoint, endpoint_id=None, is_json=False, expected_error=False):
        if endpoint_id:
            url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        else:
            url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'PATCH', data=body, is_json=is_json, expected_error=expected_error)
        return response

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response


if __name__ == '__main__':
    base_request = BaseRequest('https://dog.ceo/api')
    pet_info = base_request.get('list', 'all')
    pprint.pprint(pet_info)
    pass
