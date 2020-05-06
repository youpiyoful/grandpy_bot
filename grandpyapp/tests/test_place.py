"""This file test the file class place than use the google place api"""
from grandpyapp.place import QueryPlace
import pytest
# from config import GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE
import requests
import json

DEFAULT_CONFIG = {"google_api_key": "apikey", "base_url_google_place": "https://fakeurl"}
PLACE = QueryPlace(["openclassrooms"], DEFAULT_CONFIG['google_api_key'], DEFAULT_CONFIG['base_url_google_place'])


class MockResponse:
    def __init__(self):
        self.status_code = 200
    
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key': 'mock_response} and status_code == 200"""
    def mock_requests_get(*args, **kwargs): 
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_requests_get)

def test_find_place(mock_response):
    """this test verify than method return a correct json"""
    resp = PLACE.find_place()
    print('response = ', resp)
    assert resp.json().get("mock_key") == "mock_response"


def test_build_url_for_api_place():
    """this method take Place's attribut and build an endpoint"""
    assert PLACE.build_url_for_api_place() == \
    f"{DEFAULT_CONFIG['base_url_google_place']}?input=openclassrooms&inputtype" \
    f"=textquery&fields=formatted_address,name&key={DEFAULT_CONFIG['google_api_key']}"
