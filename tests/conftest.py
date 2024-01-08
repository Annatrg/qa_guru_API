import pytest


@pytest.fixture
def api_url():
    return 'https://api.rivegauche.ru'


@pytest.fixture
def headers():
    headers = \
        {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
    return headers
