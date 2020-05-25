from flask import Flask, render_template, url_for, json, make_response, request, jsonify
from flask_cors import CORS
from grandpyapp.place import QueryPlace
from grandpyapp.wiki import Wiki
from grandpyapp.parser import Parser

app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/grandpybot/*": {"origins": "*"}})
# Config options - Make sure you created a 'config.py' file.
# app.config.from_object('config.DevelopmentConfig')
app.config.from_object('config.ProductionConfig')
GOOGLE_API_KEY = app.config.get('GOOGLE_API_KEY')
# GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
# WIKI_API_KEY = app.config.get('WIKI_API_KEY')
BASE_URL_GOOGLE_PLACE = app.config.get('BASE_URL_GOOGLE_PLACE')
# BASE_URL_WIKI = app.config.get('BASE_URL_WIKI')


@app.route('/', methods=['GET'])
@app.route('/grandpy_bot/', methods=['GET'])
def index():
    # username = request.cookies.get('username')
    render = make_response(render_template('index.html',
                             api_key=GOOGLE_API_KEY,
                             key_word_place="openclassrooms",
                             logo=url_for('static', filename='img/dither_it_logo.jpg'), # logo is dither and take 80% space in less (low tech mag)
                             reset_css=url_for('static', filename='css/reset.css'),
                             grandpy_app_css=url_for('static', filename='css/grandpy_app.css')), 200)
    # render.set_cookie('same-site-cookie', 'foo', samesite='Lax')
    # render.set_cookie('username', 'the username', samesite='Strict', secure=True)

    print(render)
    return render


@app.route('/send_answer', methods=['POST', 'GET'])
def get_data():
    """This function take an answer and return a json with api google place and api wiki response"""
    # import request
    answer = request.args.get('answer')
    print("answer from get_data() : ", answer)
    status_code = 200 # if no error is raised the status code remains equal to 200
    stop_words = app.config.get('STOP_WORDS')  # use list of stop word stock in config.py
    print('ANSWER from view.get_data() : ', answer)
    parser_obj = Parser(answer, stop_words)  # instanciate Parser class
    keywords = parser_obj.find_keyword()  # call method of PARSER object
    print("KEYWORD : ", keywords)
    
    if keywords[0] == "any keyword find":
        status_code = 404
        data = {"error": "aucun mot clef valide"}
    
    else:
        place_obj = QueryPlace(keywords, GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE)  # instanciate Place class
        data_google = place_obj.find_place()  # call method of PLACE object
        wiki_obj = Wiki('fr', keywords)  # instanciate wiki class
        data_wiki = wiki_obj.find_data_about_place()  # call method of WIKI object
        if [i for i in data_wiki][0] == 'error':
            data = None
            status_code = 404
        else:
            data = {"data_google": data_google.json(), "data_wiki": data_wiki} # concatenate data_google and data_wiki in a big json object
            print(data)

    response = app.response_class(
        response=json.dumps(data, ensure_ascii=False),
        status=status_code,
        mimetype='application/json'
    )
    # response.set_cookie('username', 'the username', samesite='Strict', secure=True)
    return response


# mieux vaut avoir un gros appell que plusieurs petit

# TODO gérer les envoies vides directement depuis js !
# TODO : ne pas oublier de trouver la solution pour gérer les cookies
