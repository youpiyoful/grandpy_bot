from flask import Flask, render_template, url_for


app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
GOOGLE_API_KEY = app.config.get('GOOGLE_API_KEY')


@app.route('/', methods=['GET'])
@app.route('/grandpy_bot/', methods=['GET'])
def index():
    render = render_template('index.html',
                             api_key=GOOGLE_API_KEY,
                             key_word_place="openclassrooms",
                             logo=url_for('static', filename='img/grandpy_bot2.png'),
                             # logo2=url_for('static', filename='img/mustache.png'),
                             reset_css=url_for('static', filename='css/reset.css'),
                             grandpy_app_css=url_for('static', filename='css/grandpy_app.css'),
                             submited=False)
    print(render)
    return render


@app.route('/send_question/<answer>', methods=['GET'])
def get_answer(answer):
    submited = False
    if answer:
        submited = True

    return render_template('index.html',
                           submited,
                           answer)
