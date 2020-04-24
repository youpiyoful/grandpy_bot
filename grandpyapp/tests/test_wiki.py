"""This file test the class wiki who call the wikipedia api"""
from grandpyapp.wiki import Wiki
import wikipedia

wiki = Wiki('fr', 'openclassrooms')

def test_find_data_about_place(monkeypatch):
    """
    This function test the method who call the api wikipedia and 
    return a json with a key corresponding to the self.keywords attribute
    """

    def mock_wikipedia_summary(*args, **kwargs):
        return "Openclassrooms est un site web d'apprentissage."

    monkeypatch.setattr(wikipedia, 'summary', mock_wikipedia_summary)

    resp = wiki.find_data_about_place()
    assert resp == {"openclassrooms": "Openclassrooms est un site web d'apprentissage."}
    assert resp.get('openclassrooms') == "Openclassrooms est un site web d'apprentissage."
