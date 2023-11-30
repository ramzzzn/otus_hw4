import pytest
from Tools.dog_api import DogAPI
from hamcrest import *


class TestDogApi:
    """

    """
    @pytest.fixture(scope='function')
    def dog_api(self):
        return DogAPI()

    def test_get_all_bread(self, dog_api):
        result = dog_api.get_list_all_breeds()
        assert_that(result['status'], equal_to('success'), "Список пород не получен")
