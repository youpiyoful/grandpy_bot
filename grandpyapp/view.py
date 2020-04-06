from flask import Flask, render_template, url_for, json
from grandpyapp.place import Place
from grandpyapp.wiki import Wiki
from grandpyapp.parser import Parser


app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
GOOGLE_API_KEY = app.config.get('GOOGLE_API_KEY')
WIKI_API_KEY = app.config.get('WIKI_API_KEY')
BASE_URL_GOOGLE_PLACE = app.config.get('BASE_URL_GOOGLE_PLACE')
BASE_URL_WIKI = app.config.get('BASE_URL_WIKI')


@app.route('/', methods=['GET'])
@app.route('/grandpy_bot/', methods=['GET'])
def index():
    render = render_template('index.html',
                             api_key=GOOGLE_API_KEY,
                             key_word_place="openclassrooms",
                             logo=url_for('static', filename='img/grandpy_bot2.png'),
                             # logo2=url_for('static', filename='img/mustache.png'),
                             reset_css=url_for('static', filename='css/reset.css'),
                             grandpy_app_css=url_for('static', filename='css/grandpy_app.css'),)
                            #  submited=False)
    print(render)
    return render


@app.route('/send_answer/<answer>', methods=['GET'])
def get_data(answer):
    """This function take an answer and return a json with api google place and api wiki response"""
    
    stop_words = app.config.get('STOP_WORDS')  # use list of stop word stock in config.py
    parser_obj = Parser(answer, stop_words)  # instanciate Parser class
    keyword = parser_obj.find_keyword()  # call method of PARSER object
    place_obj = Place(keyword, GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE)  # instanciate Place class
    data_google = place_obj.find_place()  # call method of PLACE object
    wiki_obj = Wiki()  # instanciate wiki class
    data_wiki = wiki_obj.find_data_about_place()  # call method of WIKI object
    data = {'data_google': data_google, 'data_wiki': data_wiki}  # concatenate data_google and data_wiki in a big json object
    print(data)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


# mieux vaut avoir un gros appell que plusieurs petit