import json
import pytest
from app.hello import app

@pytest.fixture
def client(request):
    test_client = app.test_client()
    return test_client

def json_of_response(response):
    return json.loads(response.data.decode('utf8'))

def testGetHelloWorldWhenRequestingHello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert json_of_response(response) == {"hello": "hello world"}
