import pytest
from Tools.jsonplaceholder_api import JsonPlaceholderAPI


@pytest.fixture(scope='function')
def jsonplaceholder_api():
    return JsonPlaceholderAPI()
