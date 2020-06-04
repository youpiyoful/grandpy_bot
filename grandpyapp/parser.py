"""This file is a class parser use like an helper for parse answer of user"""
import re

class Parser:
    """class than use stop word and regex for parse string"""
    def __init__(self, answer, stop_words):
        self.answer = answer
        self.stop_words = stop_words

    def find_keyword(self):
        """this fuction take a string and return a list of keyword"""
        if self.answer:
            print("ANSWER : ", self.answer)
            r = re.compile(r"[^A-zêéëèîôïùç0-9-']")
            list_of_words = [r.sub("", word) for word in self.answer.lower().split(" ")] # transform the answer in a list and use list comprehension for test with regex all words in the list
            print("LIST_OF_WORDS : ", list_of_words)
            
            for stop_word in self.stop_words:

                # use list comprehension
                [list_of_words.remove(word) for word in list_of_words if word == stop_word]
                
        if list_of_words:
            return list_of_words
        
        return ["any keyword find"]
