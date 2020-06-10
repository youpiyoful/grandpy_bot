"""This file test the grandpy_response class"""
import pytest
from grandpyapp import parser, place, wiki, grandpy_response

RESP = grandpy_response.GrandpyappResponse(
    "fake_stop_words", "fake_answer", "fake_apikey", "fake_base_url"
)


class MockRequestsGet:
    def __init__(self, url, params=None):
        self.status_code = 200

    def json(self):
        return {
            "candidates": [
                {"formatted_address": "7 Cité Paradis, 75010 Paris, France"}
            ]
        }


# region fixture
@pytest.fixture
def mock_response_find_keyword_is_ok(monkeypatch):
    """mock the method find_keyword"""

    def mock_find_keyword(*args, **kwargs):
        keyword_from_answer = "openclassrooms"
        return keyword_from_answer

    monkeypatch.setattr(parser.Parser, "find_keyword", mock_find_keyword)


@pytest.fixture
def mock_response_find_place_is_ok(monkeypatch):
    """mock the method find_place()"""

    def mock_find_place(*args, **kwargs):
        return MockRequestsGet("https://fakeUrl.com")

    monkeypatch.setattr(place.QueryPlace, "find_place", mock_find_place)


@pytest.fixture
def mock_response_find_data_about_place_is_ok(monkeypatch):
    """mock the method find_data_about_place"""

    def mock_wiki(*args, **kwargs):
        return {"i don't know the response": "but i know it's in json"}

    monkeypatch.setattr(wiki.Wiki, "find_data_about_place", mock_wiki)


# endregion

# region test for get_data
def test_build_response_of_grandpy_is_ok(
    mock_response_find_keyword_is_ok,
    mock_response_find_place_is_ok,
    mock_response_find_data_about_place_is_ok,
):
    """
    test than response wiki return correctly
    the wiki data when she receive an answer
    """
    # answer = "Ou se situe openclassrooms"
    response_result = {
        "data_google": {
            "candidates": [
                {"formatted_address": "7 Cité Paradis, 75010 Paris, France"}
            ]
        },
        "data_wiki": {"i don't know the response": "but i know it's in json"},
    }

    response = RESP.build_response_of_grandpy()
    # response = rv.request.args.get(args)
    assert response.get("response") == response_result


def test_build_response_of_grandpy_if_any_keyword(
    mock_response_find_place_is_ok,
    mock_response_find_data_about_place_is_ok,
    monkeypatch,
):
    """
    test the behavior of get_data() if parser.find_keyword return any keyword
    """

    def mock_find_any_keyword(*args, **kwargs):
        return ["any keyword find"]

    monkeypatch.setattr(parser.Parser, "find_keyword", mock_find_any_keyword)

    response = RESP.build_response_of_grandpy()

    assert response.get("response") == {"error": "aucun mot clef valide"}
    assert response.get("status") == 404


def test_build_response_of_grandpy_if_google_place_is_wrong(
    mock_response_find_keyword_is_ok,
    mock_response_find_data_about_place_is_ok,
    monkeypatch,
):
    """test the behavior of get_data() if google_place encounter a problem"""

    def mock_find_place_is_wrong(*args, **kwargs):
        return False

    monkeypatch.setattr(
        place.QueryPlace, "find_place", mock_find_place_is_wrong
    )

    resp = RESP.build_response_of_grandpy()
    assert resp.get("status") == 404
    assert resp.get("response") == {"error": "aucune donnée trouvée"}


def test_build_response_of_grandpy_if_wikipedia_is_wrong(
    mock_response_find_place_is_ok,
    mock_response_find_keyword_is_ok,
    monkeypatch,
):
    """
    test the behavior of get_data()
    if find_data_about_place() encounter a problem
    """

    def mock_find_any_data_about_place(*args, **kwargs):
        return {"error": "data not found"}

    monkeypatch.setattr(
        wiki.Wiki, "find_data_about_place", mock_find_any_data_about_place
    )

    resp = RESP.build_response_of_grandpy()
    assert resp.get("status") == 404
    assert resp.get("response") == {"error": "aucune donnée trouvée"}


# endregion
