"""File who test method of parser class"""
from grandpyapp.parser import Parser

PARSER = Parser("ceci est ma phrase", ["ceci", "est", "ma"])


def test_find_keyword():
    """test the method who find the keyword in a phrase"""
    assert PARSER.find_keyword() == ["phrase"]
