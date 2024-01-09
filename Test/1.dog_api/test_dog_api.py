import pytest
from hamcrest import *


class TestDogApi:
    def test_list_all_breeds(self, dog_api):
        """
        Проверка эндпоинта "List all breeds" - получение списка всех имеющихся пород
        """
        result = dog_api.get_list_all_breeds()
        assert_that(result['status'], equal_to('success'), "Ошибка при получении ответа от сервера")
        assert_that(len(result['message']), greater_than(0), 'Список пород не получен')
        assert_that(result['message'], has_entries(
            {'affenpinscher': [], 'bulldog': ['boston', 'english', 'french'],
             'wolfhound': ['irish']}), "Список пород получен не полностью")

    @pytest.mark.parametrize('number_of_images',
                             [
                                 None, 1, 20, 50
                             ], ids=['null', 'min', 'normal', 'max'])
    def test_random_image(self, dog_api, number_of_images):
        """
        Проверка эндпоинта "Random image" - получение случайного изображения случайной породы
        """
        result = dog_api.get_random_image(number_of_images)
        assert_that(result['status'], equal_to('success'), "Ошибка при получении ответа от сервера")
        assert_that(len(result['message']), greater_than(0), 'Список изображений не получен')
        if number_of_images:
            assert_that(len(result['message']), equal_to(number_of_images), 'Число полученных изображений меньше '
                                                                            'запрашиваемого')

    @pytest.mark.parametrize('breed_name',
                             [
                                 'hound', 'akita', 'corgi'
                             ])
    @pytest.mark.parametrize('number_of_images',
                             [
                                 None, 1, 10
                             ])
    def test_by_breed(self, dog_api, breed_name, number_of_images):
        """
        Проверка эндпоинта "By breed" - получение изображений по указанной породе
        """
        # Получаем все изображения по породе
        list_all_images = dog_api.get_all_images_by_breed(breed_name)
        assert_that(list_all_images['status'], equal_to('success'), "Ошибка при получении ответа от сервера")
        assert_that(len(list_all_images['message']), greater_than(0),
                    f'Список изображений породы {breed_name} не получен')

        # Получаем несколько рандомных изображений
        list_random_images = dog_api.get_images_by_breed(breed_name, number_of_images)
        assert_that(list_random_images['status'], equal_to('success'), "Ошибка при получении ответа от сервера")
        assert_that(len(list_random_images['message']), greater_than(0), 'Список изображений не получен')
        if number_of_images:
            assert_that(len(list_random_images['message']),
                        less_than_or_equal_to(number_of_images), 'Число полученных изображений больше запрашиваемого')

    @pytest.mark.parametrize('breed_name, number_of_images',
                             [
                                 ('australian', None),
                                 ('hound', 1),
                                 ('mastiff', 5)
                             ])
    def test_by_sub_breed(self, dog_api, breed_name, number_of_images):
        """
        Проверка эндпоинта "By sub-breed" - получение списка подпород по указанной породе и их изображений
        """
        # Получаем список всех подпород
        list_sub_breeds = dog_api.list_all_sub_breeds(breed_name)
        assert_that(list_sub_breeds['status'], equal_to('success'), "Ошибка при получении ответа от сервера")
        assert_that(len(list_sub_breeds['message']), greater_than(0), 'Список под-пород не получен')

        for sub_breed in list_sub_breeds['message']:
            # Получаем все изображения по подпороде
            list_all_sub_breed_images = dog_api.list_all_sub_breeds_images(breed_name, sub_breed)
            assert_that(list_all_sub_breed_images['status'], equal_to('success'), "Ошибка при получении ответа от "
                                                                                  "сервера")
            assert_that(len(list_all_sub_breed_images['message']), greater_than(0), 'Список с изображениями под-пород '
                                                                                    'не получен')

            # Получаем несколько изображений по подпороде
            list_random_images = dog_api.list_random_image_by_sub_breed(breed_name, sub_breed, number_of_images)
            assert_that(list_random_images['status'], equal_to('success'), "Ошибка при получении ответа от сервера")
            assert_that(len(list_random_images['message']), greater_than(0), 'Список с изображениями под-пород не '
                                                                             'получен')
            if number_of_images:
                assert_that(len(list_random_images['message']),
                            less_than_or_equal_to(number_of_images),
                            'Число полученных изображений больше запрашиваемого')

    @pytest.mark.parametrize('breed_name',
                             [
                                 'test', '1234'
                             ]
                             )
    def test_get_all_images_by_incorrect_breed(self, dog_api, breed_name):
        """
        Проверка получения ошибки при запросе списка всех изображений с некорректной породой
        """
        err_response = dog_api.get_all_images_by_breed(breed_name, expected_error=True)
        assert_that(err_response['status'], equal_to('error'), "Неверный ответ от сервера")
        assert_that(err_response['message'], equal_to('Breed not found (master breed does not exist)'),
                    'Ожидаемая ошибка '
                    'не получена')

    @pytest.mark.parametrize('breed_name', ['hound'])
    @pytest.mark.parametrize('sub_breed',
                             [
                                 'test', '1234'
                             ]
                             )
    def test_get_all_images_by_incorrect_sub_breed(self, dog_api, breed_name, sub_breed):
        """
        Проверка получения ошибки при запросе списка всех изображений с некорректной подпородой
        """
        err_response = dog_api.list_all_sub_breeds_images(breed_name, sub_breed, expected_error=True)
        assert_that(err_response['status'], equal_to('error'), "Неверный ответ от сервера")
        assert_that(err_response['message'], equal_to('Breed not found (sub breed does not exist)'), 'Ожидаемая ошибка '
                                                                                                     'не получена')
