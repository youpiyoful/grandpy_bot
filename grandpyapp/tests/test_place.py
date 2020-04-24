"""This file test the file class place than use the google place api"""
from grandpyapp import place
# from config import GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE
import requests
import json

DEFAULT_CONFIG = {"google_api_key": "apikey", "base_url_google_place": "https://fakeurl"}
PLACE = place.QueryPlace(["openclassrooms"], DEFAULT_CONFIG['google_api_key'], DEFAULT_CONFIG['base_url_google_place'])


class MockResponse:

    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

def test_find_place(monkeypatch):
    """this test verify than method return a correct json"""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


    resp = PLACE.find_place()
    print('response = ', resp)
    assert resp["mock_key"] == "mock_response"


def test_build_url_for_api_place():
    """this method take Place's attribut and build an endpoint"""
    assert PLACE.build_url_for_api_place() == \
    f"{DEFAULT_CONFIG['base_url_google_place']}?input=openclassrooms&inputtype" \
    f"=textquery&fields=formatted_address,name&key={DEFAULT_CONFIG['google_api_key']}"
