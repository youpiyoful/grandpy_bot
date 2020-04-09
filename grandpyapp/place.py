"""This file maped an object than used google place api""" 
import requests
import json


class QueryPlace: # query place
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
        # print(r.json())
        # if r.json()['status'] == "ZERO_RESULTS":
            
        #     for keyword in self.keywords:
        #         r = requests.get(f'{self.base_url}?input={keyword}&inputtype=textquery&fields=formatted_address,name&key={self.api_key}')
                
        #         if r.json()['status'] != "ZERO_RESULTS":
        #             break
        return r

# PLACE = Place(["openclassrooms"], 'AIzaSyDhEhf5rfvxofPXL85o1Z8M6XrKEhAGBgc', 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json')
# place.build_url_for_api_place()
# PLACE.find_place()