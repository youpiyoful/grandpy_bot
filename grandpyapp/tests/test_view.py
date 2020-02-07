from grandpyapp import view


class TestView:
    def test_index(self, monkeypatch):
        """test than index return correctly the html render by the template"""
        index_html = "<html><body></body></html>"

        def mock_render_template(*args, **kwargs):
            return index_html

        monkeypatch.setattr(view, "render_template", mock_render_template)

        assert view.index() == index_html

    # def test_get_question(self, monkeypatch):
    #     """test than get_question function return the question than we past in argument"""
    #     question = 'this is a question'
    #
    #     def mock_args(request):
    #         return question
    #
    #     monkeypatch.setattr(view, '')