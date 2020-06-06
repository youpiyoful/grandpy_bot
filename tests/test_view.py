"""this file test all function's view"""
import pytest
import json
import flask
from grandpyapp import view, parser, place, wiki


app = flask.Flask(__name__)

with app.test_request_context('send_answer?answer=openclassrooms'):
    assert flask.request.path == '/send_answer'
    assert flask.request.args['answers'] == 'openclassrooms'

#region test for index_render_template
def test_index_render_template_correctly(monkeypatch):
    """test index function return correctly html"""
    index_html = """
                <html>
                    <body>
                        <div>AIzaSyBkuQqSZkEBSmlSbeBOw_yr9G_GTayiwks</div>
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

    with app.test_request_context('/'):
        

    # render = view.index()
    # print(index_html)
    # print(render)
    # assert index_html == render
#endregion

#region test for get_data

#region mocks
class MockRequestsGet:
    def __init__(self, url, params=None):
        self.status_code = 200

    def json(self):
        return {"candidates": [{"formatted_address": "7 Cité Paradis, 75010 Paris, France"}]}


class MockRequest:
    def __init__(self, *args):
        last = []
        for arg in args:
            last += [(x, y) for x, y in arg.items()]

        self.args = dict((x, y) for x, y in last)

            
    # def get(self, key_arg):

    #     for arg in self.args:
    #         dict_arg = [(key, value) for key, value in arg.items()][0]
        
    #         if key_arg == dict_arg[0]:
    #             return dict_arg[1]

    #     return None


# r = MockRequest({"test": "test"}, {"test2": "test2"})
# print(r.args)
# print(r.args.get("test"))
# print(r.get("test"))

# print("}, {".split(str(r.args)))
        


@pytest.fixture
def mock_request_args_is_ok(monkeypatch):
    """mock the request.args"""

    def mock_request_args():
        return MockRequest(dict(answer="ou se trouve la tour eifel ?"))

    monkeypatch.setattr(view.get_data, 'request.args.get', mock_request_args)


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
    def mock_find_place(*args, **kwargs):
        return MockRequestsGet('https://fakeUrl.com')

    monkeypatch.setattr(place.QueryPlace, 'find_place', mock_find_place)


@pytest.fixture
def mock_response_find_data_about_place_is_ok(monkeypatch):
    """mock the method find_data_about_place"""

    def mock_wiki(*args, **kwargs):
        return {"i don't know the response": "but i know it's in json"}

    monkeypatch.setattr(wiki.Wiki, 'find_data_about_place', mock_wiki)

#endregion

def test_get_data_is_ok(mock_response_find_keyword_is_ok, 
                        mock_response_find_place_is_ok,
                        mock_response_find_data_about_place_is_ok):
                        # mock_request_args_is_ok):
    """test than response wiki return correctly the wiki data when she receive an answer"""
    # answer = "Ou se situe openclassrooms"

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
            "i don't know the response": "but i know it's in json"
        }
    }

    response = view.get_data()
    assert response.json == response_result


def test_get_data_if_any_keyword(mock_response_find_place_is_ok, 
                                 mock_response_find_data_about_place_is_ok,
                                 mock_request_args_is_ok,
                                 monkeypatch):
    """test the behavior of get_data() if parser.find_keyword return any keyword"""
    def mock_find_any_keyword(*args, **kwargs):
        return ["any keyword find"]
    
    monkeypatch.setattr(parser.Parser, 'find_keyword', mock_find_any_keyword)

    response = view.get_data()

    assert response.json == {"error": "aucun mot clef valide"}
    assert response.status_code == 404


def test_get_data_if_google_place_is_wrong(
    mock_response_find_keyword_is_ok, 
    mock_response_find_data_about_place_is_ok,
    monkeypatch):
    """test the behavior of get_data() if google_place encounter a problem"""
    
    def mock_find_place_is_wrong():
        pass

    pass

def test_get_data_if_wikipedia_is_wrong(mock_response_find_place_is_ok,
                                        mock_response_find_keyword_is_ok,
                                        mock_request_args_is_ok,
                                        monkeypatch):
    """test the behavior of get_data() if find_data_about_place() encounter a problem"""

    def mock_find_any_data_about_place(*args, **kwargs):
        return {'error': 'data not found'}
    
    monkeypatch.setattr(wiki.Wiki, 'find_data_about_place', mock_find_any_data_about_place)

    resp = view.get_data()
    assert resp.status_code == 404
    assert resp.json == {'error': 'aucune donnée trouvée'}

#endregion