from Tools.base_request import BaseRequest

BASE_URL_OPEN_BREWERY = 'https://api.openbrewerydb.org/v1/breweries'


class OpenBreweryAPI(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_OPEN_BREWERY)

    def get_single_brewery(self, obdb_id, expected_error=False):
        response = self.get(obdb_id, expected_error)
        return response

    def get_list_breweries(self, per_page=1, **kwargs):
        if per_page:
            request = f'?per_page={per_page}&'
        else:
            request = '?'
        if kwargs.get('city'):
            request = request + f'by_city={kwargs.get("city")}'
        if kwargs.get('dist'):
            request = request + f'by_dist={kwargs.get("dist")}'
        if kwargs.get('ids'):
            request = request + f'by_ids={kwargs.get("ids")}'
        if kwargs.get('name'):
            request = request + f'by_name={kwargs.get("name")}'
        if kwargs.get('state'):
            request = request + f'by_state={kwargs.get("state")}'
        if kwargs.get('postal'):
            request = request + f'by_postal={kwargs.get("postal")}'
        if kwargs.get('type'):
            request = request + f'by_type={kwargs.get("type")}'
        response = self.get(request)
        return response

    # def get_list_breweries(self, per_page, expected_error=False):
    #     response = self.get(f'?per_page={per_page}', expected_error)
    #     return response

    def get_list_breweries_by_city(self, city, expected_error=False):
        response = self.get(f'?by_city={city}', expected_error)
        return response

    def get_list_breweries_by_dist(self, dist, expected_error=False):
        response = self.get(f'?by_dist={dist}', expected_error)
        return response

    def get_list_breweries_by_ids(self, _id, expected_error=False):
        response = self.get(f'?by_ids={_id}', expected_error)
        return response

    def get_list_breweries_by_name(self, name, expected_error=False):
        response = self.get(f'?by_name={name}', expected_error)
        return response

    def get_list_breweries_by_state(self, state, expected_error=False):
        response = self.get(f'?by_state={state}', expected_error)
        return response

    def get_list_breweries_by_postal(self, postal, expected_error=False):
        response = self.get(f'?by_postal={postal}', expected_error)
        return response

    def get_list_breweries_by_type(self, type, expected_error=False):
        response = self.get(f'?by_type={type}', expected_error)
        return response
