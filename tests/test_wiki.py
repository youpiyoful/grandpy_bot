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
    assert resp == {"wiki_response": "Openclassrooms est un site web d'apprentissage."}
    assert resp.get('wiki_response') == "Openclassrooms est un site web d'apprentissage."


def test_find_any_data_about_place(monkeypatch):
    """
    test the behavior of the find_data_about_place method when the keywords
    in parameters cannot be found
    """
    from wikipedia import exceptions
    page_error_response = {'error': 'Page id "tour eifel grandes" does not match any pages. Try another id!'}

    def mock_wikipedia_page_error(*args, **kwargs):
        raise wikipedia.exceptions.PageError('tour eifel grandes')
    
    monkeypatch.setattr(wikipedia, 'summary', mock_wikipedia_page_error)

    resp_wrong = wiki.find_data_about_place()
    assert resp_wrong == page_error_response