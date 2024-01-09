import pytest
from Tools.dog_api import DogAPI


@pytest.fixture(scope='function')
def dog_api():
    return DogAPI()
