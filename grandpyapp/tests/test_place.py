"""This file test the file class place than use the google place api"""
from grandpyapp.place import Place

PLACE = Place("openclassrooms", "an api key", "http://ça_marche_fort_bien.com")

def test_find_place():
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
    response = PLACE.find_place()
    assert google_resp["candidates"][0]["formatted_address"] == response["candidates"][0]["formatted_address"]