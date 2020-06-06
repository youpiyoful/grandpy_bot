"""This file maped an object than used google place api"""
import requests
import json


class QueryPlace:  # query place
    """this class used google api for find a place"""

    def __init__(self, keywords, api_key, base_url):
        self.keywords = keywords
        self.api_key = api_key
        self.base_url = base_url

    def build_url_for_api_place(self):
        """This method build a correct url for call google place api with Place attribute"""
        if isinstance(self.keywords, list):
            str_keywords = ' '.join(self.keywords)
            print(str_keywords)

        else:
            str_keywords = self.keywords

        url = f"{self.base_url}?input={str_keywords}\
            &inputtype=textquery&fields=formatted_address,name,geometry&key={self.api_key}"
        print(url)
        return url

    def find_place(self):
        """this method call google place api for find place with a keyword"""
        r = requests.get(self.build_url_for_api_place())
        return r
