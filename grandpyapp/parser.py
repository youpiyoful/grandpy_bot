"""This file is a class parser use like an helper for parse answer of user"""

class Parser:
    """class than use stop word and regex for parse string"""
    def __init__(self, answer, stop_words):
        self.answer = answer
        self.stop_words = stop_words

    # @staticmethod
    # def string_parse(string):
    #     return string.split(" ")

    def find_keyword(self):
        """this fuction take a string and return a list of keyword"""
        list_of_words = self.answer.split(" ")

        for stop_word in self.stop_words:
            
            for word in list_of_words:

                if word == stop_word:
                    print('print : ', stop_word, ' -> ', word)
                    list_of_words.remove(word)
                    
        return list_of_words