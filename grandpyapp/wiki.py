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
        
        if type(self.keywords) is list:
            str_keywords = ' '.join(self.keywords)
        
        else:
            str_keywords = self.keywords
        
        try:
            resp = {'wiki_response': wikipedia.summary(str_keywords, sentences=1)}
            print(resp)
        
        except wikipedia.exceptions.PageError as e:
            resp = {'error': f'{e}'}
            print(resp)
        
        return resp


# wiki = Wiki('fr', ['tour', 'eifel'])
# wiki.find_data_about_place()
