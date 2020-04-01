"""This file maped an object than used google place api""" 

class Place:
    """this class used google api for find a place"""
    def __init__(self, keywords, api_key, base_url):
        self.keywords = keywords
        self.api_key = api_key
        self.base_url = base_url

    @staticmethod
    def construct_url_for_api_place():
        pass

    def find_place(self):
        """this method call google place api for find place with a keyword"""
        pass
    
