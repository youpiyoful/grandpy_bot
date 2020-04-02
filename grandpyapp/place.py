"""This file maped an object than used google place api""" 
import requests

class Place:
    """this class used google api for find a place"""
    def __init__(self, keywords, api_key, base_url):
        self.keywords = keywords
        self.api_key = api_key
        self.base_url = base_url

    def build_url_for_api_place(self):
        url = f'{self.base_url}?input={self.keywords}&key={self.api_key}'
        print(url)
        return url

    def find_place(self):
        """this method call google place api for find place with a keyword"""
        r = requests.get(self.build_url_for_api_place())
        
        data = r.json
        print(data)
        return {'ok_google': 'yes c\'est moi'}

place = Place("openclassrooms", "apikey", "http:/testofgoogle/json")
place.build_url_for_api_place()