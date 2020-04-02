"""this file test all function's view"""
from grandpyapp import view


def test_index(monkeypatch):
    """test than index function return correctly html and mock render_template function"""
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

    def mock_template_render(request, *args, **kwargs):
        variable_to_html_elt = ""
        for key in kwargs:
            # print(kwargs[key])
            variable_to_html_elt += f"""
                        <div>{kwargs[key]}</div>"""
            
        return f"""
                <html>
                    <body>
                    {variable_to_html_elt}
                    </body>
                </html>
                """

    def mock_url_for(request, *args, **kwargs):
        return "path/to/css"

    monkeypatch.setattr(view, "render_template", mock_template_render)
    monkeypatch.setattr(view, 'url_for', mock_url_for)

    render = view.index()
    assert render == index_html


def test_response(monkeypatch):
    """test than response wiki return correctly the wiki data when she receive an answer"""
    answer = "Ou se situe openclassrooms"

    def mock_find_keyword(request):
        keyword_from_answer = "openclassrooms"
        return keyword_from_answer

    def mock_google_place(request):
        google_resp = {
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
        return google_resp

    def mock_wiki(request):
        wiki_resp = {
            "je ne connais pas la reponse": "mais je sais qu'elle est en json"
        }
        return wiki_resp

    monkeypatch.setattr(view, 'find_keyword', mock_find_keyword)
    monkeypatch.setattr(view, 'find_place', mock_google_place)
    monkeypatch.setattr(view, 'wiki_annotation', mock_wiki)

    response_result = {
        "resp_google":
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
        },
        "resp_wiki":
        {
            "je ne connais pas la reponse": "mais je sais qu'elle est en json"
        }
    }

    assert response_result == view.get_data(answer)
