"""File who test method of parser class"""
from grandpyapp.parser import Parser

# class TestParser:
#     """this class test method of Parser class"""
#     def __init__(self):
#         self.parser = Parser("test", ["test"])

PARSER = Parser("ceci est ma phrase", ["ceci", "est", "ma"])

# def test_string_parse():
#     """this method test than string_parse return a string"""
#     assert PARSER.string_parse() == "ceci est ma phrase"

def test_find_keyword():
    """test the method who find the keyword in a phrase"""
    assert PARSER.find_keyword() == ["phrase"]