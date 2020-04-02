"""This file test the file class place than use the google place api"""
from grandpyapp import place
import requests

PLACE = place.Place("openclassrooms", "anApiKey", "http://ça_marche_fort_bien.com")


def test_find_place(monkeypatch):
    """this test verify than method return a correct json"""
    google_resp = \
    {
        "candidates": [
            {
                "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                "geometry": {
                    "lat": 48.8748465,
                    "long": 2.3504873
                }
            }
        ]
    }

    def mock_google_api_request(request):
        return google_resp

    monkeypatch.setattr(place, 'une fonction de request', mock_google_api_request)

    resp = PLACE.find_place()
    print('response = ', resp)
    print('google_resp = ', google_resp["candidates"][0]["formatted_address"])
    # assert google_resp["candidates"][0]["formatted_address"] == response["candidates"][0]["formatted_address"]


def test_build_url_for_api_place():
    """this method take Place's attribut and build an endpoint"""
    PLACE