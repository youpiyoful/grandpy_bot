"""This file maped an object than used google place api""" 
import requests


class Place:
    """this class used google api for find a place"""
    def __init__(self, keywords, api_key, base_url):
        self.keywords = keywords
        self.api_key = api_key
        self.base_url = base_url

    def build_url_for_api_place(self):
        """This method build a correct url for call google place api with Place attribute"""
        str_keywords = ' '.join(self.keywords)
        print(str_keywords)
        url = f'{self.base_url}?input={str_keywords}&inputtype=textquery&fields=formatted_address,name&key={self.api_key}'
        print(url)
        return url

    def find_place(self):
        """this method call google place api for find place with a keyword"""
        r = requests.get(self.build_url_for_api_place())
        # r = requests.get(f'{self.base_url}?input={" ".join(self.keywords)}&inputtype=textquery&fields=formatted_address,name&key={self.api_key}')
        data = r.json
        # data_status = r.status_code
        print(data)
        # return data_status
        return data
        # return {'ok_google': f'la question était : {self.keywords}'}

# place = Place(["ou", "se", "situe", "openclassrooms"], "apikey", "http:/testofgoogle/json")
# place.build_url_for_api_place()