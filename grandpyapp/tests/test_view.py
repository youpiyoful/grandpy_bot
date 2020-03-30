from grandpyapp import view
import json


class TestView:
    def __init__(self):
        pass

    def test_index(self, monkeypatch):
        index_html = "<html><body></body></html>"

        def mock_template_render(request):
            return index_html

        monkeypatch.setattr(view, "render_template", mock_template_render)

        render = view.index()

        assert render == index_html

    def test_response(self, monkeypatch):
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

        monkeypatch.setattr(view, 'find_keyword', mock_find_keyword)
        monkeypatch.setattr(view, 'find_place', mock_google_place)

        response_result = [
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
        ]

        assert response_result == view.get_answer(answer)

    def test_response_wiki(self, monkeypatch):
        """test than response wiki return correctly the wiki data when she receive a answer"""

        def mock_find_keyword(request):
            keyword_from_answer = "openclassrooms"
            return keyword_from_answer

        def mock_wiki(request):
            wiki_resp = {
                "je ne connais pas la reponse": "mais je sais qu'elle est en json"
            }
            return wiki_resp

        monkeypatch.setattr(view, 'find_keyword', mock_find_keyword)
        monkeypatch.setattr(view, 'wiki_annotation', mock_wiki)

        result_resp = {
            "je ne connais pas la reponse": "mais je sais qu'elle est en json"
        }

        assert result_resp == view.get_answer_to_wiki()
