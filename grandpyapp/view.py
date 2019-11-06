from flask import Flask, render_template

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
GOOGLE_API_KEY = app.config.get('GOOGLE_API_KEY')


@app.route('/', methods=['GET'])
@app.route('/grandpy_bot/', methods=['GET'])
def index():
    render = render_template('index.html')
    print(render)
    return render
