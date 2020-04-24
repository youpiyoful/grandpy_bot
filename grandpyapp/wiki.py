"""This file maped an object than used wiki api"""
import wikipedia
import json


class Wiki:
    """this class use wiki api for find data about place"""

    def __init__(self, language, keywords):
        self.language = language
        self.keywords = keywords

    def find_data_about_place(self):
        """this method call wiki api for find data about place and return a dict response"""
        wikipedia.set_lang(self.language)
        resp = {' '.join(self.keywords): wikipedia.summary(self.keywords, sentences=1)}
            
        print(resp)
        print(type(resp))
        return resp

# wiki = Wiki('fr', 'tour eifel')
# wiki.find_data_about_place()
