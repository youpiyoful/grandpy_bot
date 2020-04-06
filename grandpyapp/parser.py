"""This file is a class parser use like an helper for parse answer of user"""


class Parser:
    """class than use stop word and regex for parse string"""
    def __init__(self, answer, stop_words):
        self.answer = answer
        self.stop_words = stop_words

    @staticmethod
    def another_public_method():
        """an other public method"""
        return "an other public method"

    def find_keyword(self):
        """this fuction take a string and return a list of keyword"""
        list_of_words = self.answer.split(" ")

        for stop_word in self.stop_words:

            # use list comprehension
            [list_of_words.remove(word) for word in list_of_words if word == stop_word]

        return list_of_words

# parser = Parser("ceci est ma phrase", ["ceci", "est", "ma"])
# print(parser.find_keyword())