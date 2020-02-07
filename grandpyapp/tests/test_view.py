from grandpyapp import view


class MockResponse:
    @staticmethod
    def json():
        return {
            results: [
                {
                    formatted_address: "7 Cité Paradis, 75010 Paris, France",
                    geometry: {
                        location: {
                            lat: 48.8748465,
                            lng: 2.3504873
                        }
                    }
                }
            ],
            status: "OK"
        }


class TestView:
    def test_index(self, monkeypatch):
        """test than index return correctly the html render by the template"""
        index_html = "<html><body></body></html>"

        def mock_render_template(*args, **kwargs):
            return index_html

        monkeypatch.setattr(view, "render_template", mock_render_template)

        assert view.index() == index_html

    def test_get_question(self, monkeypatch):
        """test than get_question function return the answser of google api than we past in argument"""
        question = 'this is a question'
        answer_google = 'this is a google response'
        answer_wiki = 'this is a wiki response'

        def mock_google_api(request):
            return

        assert view.get_question(question) == question

    def test_parse_question(self, monkeypatch):
        pass

    def test_call_api_google(self, monkeypatch):
        """test than call api google return a json response"""

        mock_
