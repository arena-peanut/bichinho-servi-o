import json
import pytest
from app.hello import app


@pytest.fixture
def client():
    test_client = app.test_client()
    return test_client


def json_of_response(response):
    return json.loads(response.data.decode('utf8'))


def test_get_hello_world_when_requesting_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert json_of_response(response) == {"hello": "hello world"}


def test_get_name_when_requesting_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert json_of_response(response) == {'nome': 'bichinho service'}
