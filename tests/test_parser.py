"""File who test method of parser class"""
from grandpyapp.parser import Parser

# PARSER = Parser("ceci est ma phrase", ["ceci", "est", "ma"])


def test_find_keyword():
    """test the method who find the keyword in a phrase"""
    parser = Parser("ceci est ma phrase", ["ceci", "est", "ma"])
    assert parser.find_keyword() == ["phrase"]


def test_find_any_keyword():
    """
    test the method who find the keyword in a phrase
    return if any keyword is find in the phrase
    """
    parser = Parser("ceci est ma phrase", ["ceci", "est", "ma", "phrase"])
    assert parser.find_keyword() == ["any keyword find"]
