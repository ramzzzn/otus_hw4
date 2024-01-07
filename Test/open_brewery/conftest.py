import pytest
from Tools.open_brewery_api import OpenBreweryAPI


@pytest.fixture(scope='function')
def open_brewery_api():
    return OpenBreweryAPI()
