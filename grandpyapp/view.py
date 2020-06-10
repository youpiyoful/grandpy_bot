"""This page contains all the endpoints of our application"""
from flask import Flask, render_template, url_for, json, make_response, request
from flask_cors import CORS

from grandpyapp.place import QueryPlace
from grandpyapp.wiki import Wiki
from grandpyapp.parser import Parser
from grandpyapp.grandpy_response import GrandpyappResponse

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
    answer = request.args.get("answer")
    # if no error is raised the status code remains equal to 200
    status_code = 200
    # use list of stop word stock in config.py
    stop_words = APP.config.get("STOP_WORDS")
    grandpy_resp = GrandpyappResponse(
        stop_words, answer, GOOGLE_API_KEY, BASE_URL_GOOGLE_PLACE
    )
    build_reponse = grandpy_resp.build_response_of_grandpy()
    data = build_reponse.get("response")
    status_code = build_reponse.get("status")
    response = APP.response_class(
        response=json.dumps(data, ensure_ascii=False),
        status=status_code,
        mimetype="application/json",
    )
    # response.set_cookie(
    #     "username", "the username", samesite="Strict", secure=True
    # )
    return response
