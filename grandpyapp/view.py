from flask import Flask

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
GOOGLE_API_KEY = app.config.get('GOOGLE_API_KEY')


@app.route('/', methods=['GET'])
def index():
    return 'Hello world'
