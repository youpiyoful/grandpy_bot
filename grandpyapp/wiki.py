"""This file maped an object than used wiki api"""
import wikipedia


class Wiki:
    """this class use wiki api for find data about place"""

    def __init__(self, language, keywords):
        self.language = language
        self.keywords = keywords

    def find_data_about_place(self):
        """this method call wiki api for find data about place and return a dict response"""
        wikipedia.set_lang(self.language)

        if isinstance(self.keywords, list):
            str_keywords = ' '.join(self.keywords)

        else:
            str_keywords = self.keywords

        try:
            resp = {'wiki_response': wikipedia.summary(
                str_keywords, sentences=1)}
            print(resp)

        except wikipedia.exceptions.PageError as error:
            resp = {'error': f'{error}'}
            print(resp)

        return resp
