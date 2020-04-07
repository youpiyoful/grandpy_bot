"""This file test the file class place than use the google place api"""
from grandpyapp import place
from config import GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE
import requests
import json


# PLACE = place.Place(["openclassrooms"], "anApiKey", "http://ça_marche_fort_bien.com")
PLACE = place.Place(["openclassrooms"], GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE)

def test_find_place(monkeypatch):
    """this test verify than method return a correct json"""
    google_resp = requests.models.Response()
    google_resp.code = "200"
    google_resp.json = """{
        "candidates": [
            {
                "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                "name": "OpenClassrooms"
            }
        ],
        "status": "OK"
    }"""

    def mock_req(request):
        return google_resp


    monkeypatch.setattr(requests.Response, 'json', mock_req)

    resp = PLACE.find_place()
    print('google_resp = ', json.loads(google_resp.json))
    print('response = ', json.loads(resp))
    assert json.loads(resp) == json.loads(google_resp.json)
# 

def test_build_url_for_api_place():
    """this method take Place's attribut and build an endpoint"""
    assert PLACE.build_url_for_api_place() == f"{BASE_URL_GOOGLE_PLACE}?input=openclassrooms&inputtype=textquery&fields=formatted_address,name&key={GOOGLE_API_KEY}"
