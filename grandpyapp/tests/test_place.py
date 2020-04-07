"""This file test the file class place than use the google place api"""
from grandpyapp import place
from config import GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE
import requests
import json


# PLACE = place.Place(["openclassrooms"], "anApiKey", "http://ça_marche_fort_bien.com")
PLACE = place.Place(["openclassrooms"], GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE)

def test_find_place(monkeypatch):
    """this test verify than method return a correct json"""
    google_resp = {
        "candidates": [
            {
                "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                "geometry": {
                    "lat": 48.8748465,
                    "long": 2.3504873
                }
            }
        ]}

    def mock_requests():
        return json.dumps(google_resp)

    monkeypatch.setattr(place, 'requests', mock_requests)

    resp = PLACE.find_place()
    print('response = ', resp)
    # print('google_resp = ', google_resp["candidates"][0]["formatted_address"])
    assert resp == requests.get(f"{BASE_URL_GOOGLE_PLACE}?input=openclassrooms&inputtype=textquery&fields=formatted_address,name&key={GOOGLE_API_KEY}")


def test_build_url_for_api_place():
    """this method take Place's attribut and build an endpoint"""
    assert PLACE.build_url_for_api_place() == f"{BASE_URL_GOOGLE_PLACE}?input=openclassrooms&inputtype=textquery&fields=formatted_address,name&key={GOOGLE_API_KEY}"