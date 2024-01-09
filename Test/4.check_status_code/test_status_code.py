import requests
from hamcrest import *


def test_check_status_code(url, status_code):
    response = requests.get(url)
    assert_that(response.status_code, equal_to(status_code), "Статус ответа не соответствует требуемому значению")
