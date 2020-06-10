"""This file test the file class place than use the google place api"""
import pytest
import requests
from grandpyapp.place import QueryPlace

DEFAULT_CONFIG = {
    "google_api_key": "apikey",
    "base_url_google_place": "https://fakeurl",
}
PLACE = QueryPlace(
    ["openclassrooms"],
    DEFAULT_CONFIG["google_api_key"],
    DEFAULT_CONFIG["base_url_google_place"],
)


# region object mock response
class MockResponse:
    """Mock response for requests response"""

    def __init__(self, status_code):
        self.status_code = status_code

    def json(self):
        """method return json response"""

        if self.status_code == 200:
            return {"mock_key": "mock_response"}
        return {"mock_key": "error data not found"}


# endregion

# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """
    Requests.get() mocked to return
    {'mock_key': 'mock_response} and status_code == 200
    """

    def mock_requests_get(request):
        """mock requests response with object MockResponse"""
        return MockResponse(200)

    monkeypatch.setattr(requests, "get", mock_requests_get)


@pytest.fixture
def mock_response_wrong(monkeypatch):
    """mock when data is not found"""

    def mock_requests_get_when_data_is_not_found(request):
        """mock requests response with object MockResponse"""
        return MockResponse(404)

    monkeypatch.setattr(
        requests, "get", mock_requests_get_when_data_is_not_found
    )


def test_find_place(mock_response):
    """this test verify than method return a correct json"""
    resp = PLACE.find_place()
    print("response = ", resp)
    assert resp.json().get("mock_key") == "mock_response"


def test_find_place_is_wrong(mock_response_wrong):
    """test behavior if place is not find"""
    resp = PLACE.find_place()
    assert resp == False


def test_build_url_for_api_place():
    """this method take Place's attribut and build an endpoint"""
    assert (
        PLACE.build_url_for_api_place()
        == f"{DEFAULT_CONFIG['base_url_google_place']}"
        "?input=openclassrooms&inputtype"
        "=textquery&fields=formatted_address,name,"
        f"geometry&key={DEFAULT_CONFIG['google_api_key']}"
    )


def test_build_url_for_api_place_with_many_keywords():
    """this method take Place's attribut and build an endpoint"""
    PLACE = QueryPlace(
        ["citadelle", "besançon"],
        DEFAULT_CONFIG["google_api_key"],
        DEFAULT_CONFIG["base_url_google_place"],
    )
    assert (
        PLACE.build_url_for_api_place()
        == f"{DEFAULT_CONFIG['base_url_google_place']}"
        "?input=citadelle besançon&inputtype"
        "=textquery&fields=formatted_address,name,geometry&"
        f"key={DEFAULT_CONFIG['google_api_key']}"
    )
