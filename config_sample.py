# this file is an example file, you have to create your own file called 'config.py'
# and replace the values in the tag by the real values

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])

SECRET_KEY = 'here put the generate secret key'

GOOGLE_API_KEY = 'here put the API key'

WIKI_API_KEY = 'here put the API key'

BASE_URL_GOOGLE_PLACE = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

BASE_URL_WIKI = ""

STOP_WORDS = ["add a list of stop words"]