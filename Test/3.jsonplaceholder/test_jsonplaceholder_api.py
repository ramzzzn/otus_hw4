import pytest
from hamcrest import *


class TestJsonPlaceholderAPI:
    @pytest.mark.parametrize('resource_id',
                             [
                                 None, 1
                             ], ids=['all_resources', 'one_resource'])
    @pytest.mark.parametrize('route',
                             [
                                 'posts',
                                 'comments',
                                 'albums',
                                 'photos',
                                 'todos',
                                 'users'
                             ])
    def test_get_resource(self, jsonplaceholder_api, route, resource_id):
        response = jsonplaceholder_api.get_resource(route, resource_id)
        # проверяем успешность полученного ответа
        assert_that(response, is_not(empty()), 'Не получен ответ от сервера')
        if resource_id:
            assert_that(response.get('id'), equal_to(resource_id),
                        'Полученный идентификатор в ответе не соответствует запрашиваемому')

    @pytest.mark.parametrize('route, title, body, user_id',
                             [
                                 ('posts', 'test_title', 'test_body', 1)
                             ])
    def test_create_resource(self, jsonplaceholder_api, route, title, body, user_id):
        response = jsonplaceholder_api.create_resource(route, title, body, user_id)
        # проверяем успешность полученного ответа
        assert_that(response.status_code, equal_to(201), 'Статус ответа не соответствует требуемому значению')
        assert_that(response.ok, equal_to(True), 'Ошибка при создании ресурса')
        # проверяем соответствие значений параметров у созданного ресурса с переданными в запросе значениями
        assert_that(response.json().get('title'), equal_to(title), 'Заголовок не соответствует требуемому значению')
        assert_that(response.json().get('body'), equal_to(body), 'Тело сообщения не соответствует требуемому значению')
        assert_that(response.json().get('userId'), equal_to(user_id),
                    'Идентификатор пользователя не соответствует требуемому значению')

    @pytest.mark.parametrize('route, resource_id, title, body, user_id',
                             [
                                 ('comment', 1, 'test_title', 'test_body', 1)
                             ])
    def test_update_resource(self, jsonplaceholder_api, route, resource_id, title, body, user_id):
        response = jsonplaceholder_api.update_comment(route, resource_id, title, body, user_id)
        # проверяем успешность полученного ответа
        assert_that(response.status_code, equal_to(200), 'Статус ответа не соответствует требуемому значению')
        assert_that(response.ok, equal_to(True), 'Ошибка при создании ресурса')
        # проверяем соответствие значений параметров у обновленного ресурса с переданными в запросе значениями
        assert_that(response.json().get('id'), equal_to(resource_id),
                    'Идентификатор ресурса не соответствует требуемому значению')
        assert_that(response.json().get('title'), equal_to(title), 'Заголовок не соответствует требуемому значению')
        assert_that(response.json().get('body'), equal_to(body), 'Тело сообщения не соответствует требуемому значению')

    @pytest.mark.parametrize('route, resource_id, title, body',
                             [
                                 ('posts', 1, 'test_title', 'test_body')
                             ])
    def test_patch_resource(self, jsonplaceholder_api, route, resource_id, title, body):
        response = jsonplaceholder_api.patch_resource(route, resource_id, title, body)
        # проверяем успешность полученного ответа
        assert_that(response.status_code, equal_to(200), 'Статус ответа не соответствует требуемому значению')
        assert_that(response.ok, equal_to(True), 'Ошибка при создании ресурса')
        # проверяем соответствие значений параметров у исправленного ресурса с переданными в запросе значениями
        assert_that(response.json().get('id'), equal_to(resource_id),
                    'Идентификатор ресурса не соответствует требуемому значению')
        assert_that(response.json().get('title'), equal_to(title), 'Заголовок не соответствует требуемому значению')
        assert_that(response.json().get('body'), equal_to(body), 'Тело сообщения не соответствует требуемому значению')

    @pytest.mark.parametrize('route, resource_id',
                             [
                                 ('posts', 1)
                             ])
    def test_delete_resource(self, jsonplaceholder_api, route, resource_id):
        response = jsonplaceholder_api.delete_resource(route, resource_id)
        # проверяем успешность полученного ответа
        assert_that(response.status_code, equal_to(200), 'Статус ответа не соответствует требуемому значению')
        assert_that(response.ok, equal_to(True), 'Ошибка при создании ресурса')

    @pytest.mark.parametrize('route, filter_name, filter_id',
                             [
                                 ('posts', 'userId', 1),
                             ])
    def test_filter_resource(self, jsonplaceholder_api, route, resource_id):
        response = jsonplaceholder_api.get_resource(route, resource_id)
        # проверяем успешность полученного ответа
        assert_that(response, is_not(empty()), 'Не получен ответ от сервера')
        if resource_id:
            assert_that(response.get('id'), equal_to(resource_id),
                        'Полученный идентификатор в ответе не соответствует запрашиваемому')

    @pytest.mark.parametrize('route, resource_id, nested_route',
                             [
                                 ('posts', 1, 'comments'),
                                 ('albums', 1, 'photos'),
                                 ('users', 1, 'albums'),
                                 ('users', 1, 'todos'),
                                 ('users', 1, 'posts')
                             ])
    def test_get_nested_resource(self, jsonplaceholder_api, route, resource_id, nested_route):
        response = jsonplaceholder_api.get_nested_resource(route, resource_id, nested_route)
        # проверяем успешность полученного ответа
        assert_that(response, is_not(empty()), 'Не получен ответ от сервера')
        # проверяем соответствие значений параметров у полученного ресурса с переданными в запросе значениями
        for resource in response:
            assert_that(resource.get(f'{route[:-1]}Id'), equal_to(resource_id),
                        'Идентификатор ресурса не соответствует требуемому значению')
