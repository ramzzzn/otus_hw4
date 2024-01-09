import pytest
from hamcrest import *


class TestOpenBreweryApi:
    @pytest.mark.parametrize('obdb_id',
                             [
                                 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'
                             ])
    def test_single_brewery(self, open_brewery_api, obdb_id):
        single_brewery = open_brewery_api.get_single_brewery(obdb_id)
        assert_that(single_brewery, is_not(empty()), 'Не получен ответ от сервера')
        assert_that(single_brewery['id'], equal_to(obdb_id), 'Полученный идентификатор не соответствует запрашиваемому')

    @pytest.mark.parametrize('per_page',
                             [
                                 1, None, 200
                             ])
    def test_list_breweries_with_per_page(self, open_brewery_api, per_page):
        list_breweries = open_brewery_api.get_list_breweries(per_page=per_page)
        assert_that(list_breweries, is_not(empty()), 'Не получен ответ от сервера')
        if per_page:
            assert_that(len(list_breweries), equal_to(per_page), 'Неверное количество записей')
        else:
            assert_that(len(list_breweries), equal_to(50), 'Неверное количество записей')

    @pytest.mark.parametrize('city',
                             [
                                 'Norman',
                                 'San Diego',
                                 'Jung-gu',
                             ])
    def test_list_breweries_by_city(self, open_brewery_api, city):
        list_breweries_by_city = open_brewery_api.get_list_breweries(city=city)
        assert_that(list_breweries_by_city, is_not(empty()), 'Не получен ответ от сервера')
        assert_that(list_breweries_by_city[0].get('city'), equal_to(city), 'Город не соответствует требуемому значению')

    @pytest.mark.parametrize('latitude, longitude',
                             [
                                 ('37.47157834', '126.6222289'),
                                 ('39.9782443', '-105.1319826')
                             ])
    def test_list_breweries_by_dist(self, open_brewery_api, latitude, longitude):
        dist = f'{latitude},{longitude}'
        list_breweries_by_dist = open_brewery_api.get_list_breweries(dist=dist)
        assert_that(list_breweries_by_dist, is_not(empty()), 'Не получен ответ от сервера')
        assert_that(list_breweries_by_dist[0], has_entries({'latitude': latitude, 'longitude': longitude}),
                    'Полученные в ответе координаты не соответствует требуемому значению')

    @pytest.mark.parametrize('ids',
                             [
                                 '701239cb-5319-4d2e-92c1-129ab0b3b440,add42f7c-059e-4ecc-81dd-2f7d3eabb800',
                                 'ef970757-fe42-416f-931d-722451f1f59c,5fdcc498-f9df-4fa5-b35d-487a59f0fecc,3b0b5b9b-f6d8-49e3-8ebd-0bcef6939bcd'
                             ])
    def test_list_breweries_by_ids(self, open_brewery_api, ids):
        list_breweries_by_ids = open_brewery_api.get_list_breweries(ids=ids, per_page=None)
        list_ids = ids.split(",")
        assert_that(list_breweries_by_ids, is_not(empty()), 'Не получен ответ от сервера')
        for data in list_breweries_by_ids:
            assert_that(list_ids, has_item(data.get('id')),
                        'Значение идентификаторов в ответе не соответствует требуемому значению')

    @pytest.mark.parametrize('name',
                             [
                                 'Brew',
                                 'Brewing Company',
                                 '4th Tap Brewing Cooperative'
                             ])
    def test_list_breweries_by_name(self, open_brewery_api, name):
        list_breweries_by_name = open_brewery_api.get_list_breweries(name=name)
        assert_that(list_breweries_by_name, is_not(empty()), 'Не получен ответ от сервера')
        assert_that(list_breweries_by_name[0].get('name'), contains_string(name), 'Название не соответствует требуемому'
                                                                                  'значению')

    @pytest.mark.parametrize('state',
                             [
                                 'Incheon',
                                 'New York',
                                 'Bouche du Rhône'
                             ])
    def test_list_breweries_by_state(self, open_brewery_api, state):
        list_breweries_by_state = open_brewery_api.get_list_breweries(state=state)
        assert_that(list_breweries_by_state, is_not(empty()), 'Не получен ответ от сервера')
        assert_that(list_breweries_by_state[0].get('state'), equal_to(state), 'Название штата не соответствует '
                                                                              'требуемому значению')

    @pytest.mark.parametrize('postal',
                             [
                                 '44107',
                                 '44107-4840'
                             ])
    def test_list_breweries_by_postal(self, open_brewery_api, postal):
        list_breweries_by_postal = open_brewery_api.get_list_breweries(postal=postal)
        assert_that(list_breweries_by_postal, is_not(empty()), 'Не получен ответ от сервера')
        assert_that(list_breweries_by_postal[0].get('postal_code'), contains_string(postal), 'Почтовый индекс не '
                                                                                             'соответствует '
                                                                                             'требуемому значению')
    
    @pytest.mark.parametrize('_type',
                             [
                                 'micro',
                                 'nano',
                                 'regional',
                                 'brewpub',
                                 'large',
                                 'planning',
                                 'bar',
                                 'contract',
                                 'proprietor',
                                 'closed'
                             ])
    def test_list_breweries_by_type(self, open_brewery_api, _type):
        list_breweries_by_type = open_brewery_api.get_list_breweries(type=_type)
        assert_that(list_breweries_by_type, is_not(empty()), 'Не получен ответ от сервера')
        assert_that(list_breweries_by_type[0].get('brewery_type'), contains_string(_type), 'Тип пивоварни не '
                                                                                           'соответствует требуемому '
                                                                                           'значению')
