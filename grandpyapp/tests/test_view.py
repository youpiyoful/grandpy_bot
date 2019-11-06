from grandpyapp import view


class TestView:
    def test_index(self, monkeypatch):
        index_html = "<html><body></body></html>"

        def mock_template_render(request):
            return index_html

        monkeypatch.setattr(view, "render_template", mock_template_render)

        render = view.index()

        assert render == index_html
