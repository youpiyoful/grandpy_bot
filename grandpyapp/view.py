"""This page contains all the endpoints of our application"""
from flask import Flask, render_template, url_for, json, make_response, request
from flask_cors import CORS

from grandpyapp.place import QueryPlace
from grandpyapp.wiki import Wiki
from grandpyapp.parser import Parser

APP = Flask(__name__)
CORS(APP)
# Config options - Make sure you created a 'config.py' file.
APP.config.from_object("config.DevelopmentConfig")
# APP.config.from_object('config.ProductionConfig')
GOOGLE_API_KEY = APP.config.get("GOOGLE_API_KEY")
BASE_URL_GOOGLE_PLACE = APP.config.get("BASE_URL_GOOGLE_PLACE")


@APP.route("/", methods=["GET"])
@APP.route("/grandpy_bot/", methods=["GET"])
def index():
    """This function returns the single page of the app"""
    render = make_response(
        render_template(
            "index.html",
            api_key=GOOGLE_API_KEY,
            # logo is dither it take 80% space in less (low tech mag)
            logo=url_for("static", filename="img/dither_it_logo.jpg"),
            reset_css=url_for("static", filename="css/reset.css"),
            grandpy_app_css=url_for("static", filename="css/grandpy_app.css"),
        ),
        200,
    )
    # render.set_cookie('same-site-cookie', 'foo', samesite='Lax')

    print(render)
    return render


@APP.route("/send_answer", methods=["POST", "GET"])
def get_data():
    """
    This function take an answer and return a json
    with api google place and api wiki response
    """
    print("APIKEY : ", GOOGLE_API_KEY)
    answer = request.args.get("answer")
    print("answer from get_data() : ", answer)
    # if no error is raised the status code remains equal to 200
    status_code = 200
    # use list of stop word stock in config.py
    stop_words = APP.config.get("STOP_WORDS")
    print("ANSWER from view.get_data() : ", answer)
    parser_obj = Parser(answer, stop_words)  # instanciate Parser class
    keywords = parser_obj.find_keyword()  # call method of PARSER object
    print("KEYWORD : ", keywords)

    if keywords[0] == "any keyword find":
        status_code = 404
        data = {"error": "aucun mot clef valide"}

    else:
        # instanciate Place class
        place_obj = QueryPlace(keywords, GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE)
        data_google = place_obj.find_place()  # call method of PLACE object
        wiki_obj = Wiki("fr", keywords)  # instanciate wiki class
        # call method of WIKI object
        data_wiki = wiki_obj.find_data_about_place()

        if "error" in data_wiki:
            data = None
            status_code = 404

        else:
            # concatenate data_google and data_wiki in a big json object
            data = {"data_google": data_google.json(), "data_wiki": data_wiki}
            print(data)

    response = APP.response_class(
        response=json.dumps(data, ensure_ascii=False),
        status=status_code,
        mimetype="application/json",
    )
    # response.set_cookie(
    #     "username", "the username", samesite="Strict", secure=True
    # )
    return response
