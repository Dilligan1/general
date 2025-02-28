import pytest
import requests

URL = 'https://wexler.io'
URL_STAR ='https://swapi.dev'

@pytest.fixture
def login():
    url = f'{URL}/user/login'
    res = requests.post(url,data = {
        'login': 'string',
        'password': 'string'
    })
    data = res.json()
    return data['token']


def test_request_people():
    url = f'{URL_STAR}/api/people'
    res = requests.get(url)
    data = res.json()
    assert res.status_code == 200
    for person in data['results']:
        if person ['name'] =='Luke Skywalker':
            assert person['eye_color'] =='blue'
            return
    assert False




def test_swapi():
    url = "https://swapi.dev/api/planets/3/"
    res = requests.get(url)
    assert res.status_code == 200
    data = res.json()
    if data ['name'] == 'Yavin IV':
        assert data ['rotation_period'] == str
        assert data ['orbital_period'] == str
