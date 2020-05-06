# import requests
# import json
# # import pytest
#
# from io import BytesIO
#
# # region #! simple test
# def hello(name):
#     return 'Hello ' + name
#
#
# def test_hello():
#     print('ok')  # use -s parameter in cli pytest for debug test
#     assert hello('Celine') == 'Hello Celine'
# # endregion
#
#
# def getOpenApi():
#     response = requests.get('https://fr.openfoodfacts.org/categorie/pizzas.json')
#     print(response)
#     json_resp = json.loads(response.read().decode("utf8"))
#     return json_resp
#
#
# def get_json(url):
#     response = requests.get(url)
#     json_resp = response.json()
#     return json_resp
#
#
# # region #! setup and teardown
# def setup_function(function):
#     """ setup any state tied to the execution of the given function.
#     Invoked for every test function in the module.
#     """
#     print("before: ", function)
#
#
# def teardown_function(function):
#     """ teardown any state that was previously setup with a setup_function
#     call.
#     """
#     print("after:", function)
# # endregion
#
#
# # region #! test 1
# def test_get_open_api(monkeypatch):
#     results = {
#             'properties': [{'coucou': 'test'}]
#         }
#
#     def mockreturn(request):
#         return BytesIO(json.dumps(results).encode())
#
#     monkeypatch.setattr(requests, "get", mockreturn)
#
#     x = getOpenApi()
#     assert x == results
# # endregion
#
#
# # region #! test2
# class MockResponse:
#     @staticmethod
#     def json():
#         return {'mock_key': 'mock_response'}
#
#
# def test_get_json(monkeypatch):
#
#     def mock_get(*args, **kwargs):
#         return MockResponse()
#
#     monkeypatch.setattr(requests, "get", mock_get)
#
#     result = get_json('https://url_bidon.com')
#     assert result['mock_key'] == 'mock_response'
# # endregion
#
#
# # region #! test3
# class TestJson:
#     @staticmethod
#     def json():
#         return {'mock_key': 'mock_response'}
#
#     def test_get_json(self, monkeypatch):
#
#         def mock_get(*args, **kwargs):
#             return TestJson()
#
#         monkeypatch.setattr(requests, "get", mock_get)
#
#         result = get_json('https://url_bidon.com')
#         assert result.get('mock_key') == 'mock_response'
#
# # endregion