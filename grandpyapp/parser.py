"""This file is a class parser use like an helper for parse answer of user"""
import re

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
        if self.answer:
            print("ANSWER : ", self.answer)
            r = re.compile(r"[^A-zêéëèîôïù0-9-']")
            list_of_words = [r.sub("", word) for word in self.answer.lower().split(" ")] # transform the answer in a list and use list comprehension for test with regex all words in the list
            print("LIST_OF_WORDS : ", list_of_words)
            
            for stop_word in self.stop_words:

                # use list comprehension
                [list_of_words.remove(word) for word in list_of_words if word == stop_word] #  + rapide que != stop_word mais plus verbeux car nécessite deux ligne
                
        if list_of_words:
            return list_of_words
        
        return ["any keyword find"]

# parser = Parser("ceci est ma phrase", ["ceci", "est", "ma"])
# print(parser.find_keyword())
# Salut grandpy ! Comment s'est passé ta soirée avec Grandma hier soir ? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît ?
# Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.