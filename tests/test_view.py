"""this file test all function's view"""
from grandpyapp import view, parser, place, wiki
import pytest
import json

#region test for index_render_template
def test_index_render_template_correctly(monkeypatch):
    """test index function return correctly html"""
    index_html = """
                <html>
                    <body>
                        <div>AIzaSyBkuQqSZkEBSmlSbeBOw_yr9G_GTayiwks</div>
                        <div>openclassrooms</div>
                        <div>path/to/css</div>
                        <div>path/to/css</div>
                        <div>path/to/css</div>
                    </body>
                </html>
                """

    def mock_template_render(*args, **kwargs):
        variable_to_html_elt = ""
        for key in kwargs:
            # print(kwargs[key])

            if key == 'api_key':
                variable_to_html_elt += f"""    <div>AIzaSyBkuQqSZkEBSmlSbeBOw_yr9G_GTayiwks</div>"""
                
            else:
                variable_to_html_elt += f"""
                        <div>{kwargs[key]}</div>"""
            
        return f"""
                <html>
                    <body>
                    {variable_to_html_elt}
                    </body>
                </html>
                """

    def mock_url_for(*args, **kwargs):
        return "path/to/css"

    monkeypatch.setattr(view, "render_template", mock_template_render)
    monkeypatch.setattr(view, 'url_for', mock_url_for)

    render = view.index()
    assert index_html == render
#endregion

#region test for get_data

#region mocks
class MockRequestsGet:
    def __init__(self, url, params=None):
        self.status_code = 200

    def json(self):
        return {"candidates": [{"formatted_address": "7 Cité Paradis, 75010 Paris, France"}]}


@pytest.fixture
def mock_response_find_keyword_is_ok(monkeypatch):
    """mock the method find_keyword"""

    def mock_find_keyword(*args, **kwargs):
        keyword_from_answer = "openclassrooms"
        return keyword_from_answer

    monkeypatch.setattr(parser.Parser, 'find_keyword', mock_find_keyword)


@pytest.fixture
def mock_response_find_place_is_ok(monkeypatch):
    """mock the method find_place()"""
    def mock_google_place(*args, **kwargs):
        return MockRequestsGet('https://fakeUrl.com')

    monkeypatch.setattr(place.QueryPlace, 'find_place', mock_google_place)


@pytest.fixture
def mock_response_find_data_about_place_is_ok(monkeypatch):
    """mock the method find_data_about_place"""

    def mock_wiki(*args, **kwargs):
        return {"je ne connais pas la reponse": "mais je sais qu'elle est en json"}

    monkeypatch.setattr(wiki.Wiki, 'find_data_about_place', mock_wiki)

#endregion

def test_get_data_is_ok(mock_response_find_keyword_is_ok, 
                        mock_response_find_place_is_ok,
                        mock_response_find_data_about_place_is_ok):
    """test than response wiki return correctly the wiki data when she receive an answer"""
    answer = "Ou se situe openclassrooms"

    response_result = {
        "data_google":
        {
            "candidates": [
                {
                    "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                }
            ]
        },
        "data_wiki":
        {
            "je ne connais pas la reponse": "mais je sais qu'elle est en json"
        }
    }

    response = view.get_data(answer)
    assert response.json == response_result


def test_get_data_if_any_keyword(mock_response_find_place_is_ok, 
                                 mock_response_find_data_about_place_is_ok,
                                 monkeypatch):
    """test the behavior of get_data() if parser.find_keyword return any keyword"""
    def mock_find_any_keyword(*args, **kwargs):
        return ["any keyword find"]
    
    monkeypatch.setattr(parser.Parser, 'find_keyword', mock_find_any_keyword)

    response = view.get_data("")

    assert response.json == {"error": "aucun mot clef valide"}
    assert response.status_code == 404


def test_get_data_if_google_place_is_wrong():
    """test the behavior of get_data() if google_place encounter a problem"""
    pass

def test_get_data_if_wikipedia_is_wrong(mock_response_find_place_is_ok,
                                        mock_response_find_keyword_is_ok,
                                        monkeypatch):
    """test the behavior of get_data() if find_data_about_place() encounter a problem"""

    def mock_find_any_data_about_place(*args, **kwargs):
        return {'error': 'data not found'}
    
    monkeypatch.setattr(wiki.Wiki, 'find_data_about_place', mock_find_any_data_about_place)

    resp = view.get_data('tour eifel')
    assert resp.status_code == 404
    assert resp.json == {'error': 'aucune donnée trouvée'}

#endregion