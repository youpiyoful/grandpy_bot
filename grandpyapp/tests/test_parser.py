"""File who test method of parser class"""
from grandpyapp.parser import Parser

# class TestParser:
#     """this class test method of Parser class"""
#     def __init__(self):
#         self.parser = Parser("test", ["test"])

PARSER = Parser("test", ["test"])

def test_string_parse():
    """this method test than string_parse return a string"""
    assert PARSER.string_parse() == "test"