"""This file control and build the response of grandpybot"""
from grandpyapp.place import QueryPlace
from grandpyapp.wiki import Wiki
from grandpyapp.parser import Parser


class GrandpyappResponse:
    """this class control and build a correct response of grandpy bot"""
    def __init__(self, stop_words, answer, apikey, base_url_google_place):
        self.stop_words = stop_words
        self.apikey = apikey
        self.answer = answer
        self.base_url = base_url_google_place

    def build_response_of_grandpy(self):
        """this method build the response of grandpybot"""
        parser_obj = Parser(self.answer, self.stop_words)
        keywords = parser_obj.find_keyword()

        if keywords[0] == "any keyword find":
            status_code = 404
            data = {"error": "aucun mot clef valide"}

        else:
            # instanciate Place class
            status_code = 200
            place_obj = QueryPlace(keywords, self.apikey, self.base_url)
            data_google = place_obj.find_place()  # call method of PLACE object
            wiki_obj = Wiki("fr", keywords)  # instanciate wiki class
            # call method of WIKI object
            data_wiki = wiki_obj.find_data_about_place()

            if "error" in data_wiki or data_google == False:
                data = {"error": "aucune donnée trouvée"}
                status_code = 404

            else:
                # concatenate data_google and data_wiki in a big json object
                data = {"data_google": data_google.json(), "data_wiki": data_wiki}
                print(data)


        response = {
            "response": data,
            "status": status_code,
        }
        return response