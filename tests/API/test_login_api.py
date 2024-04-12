import time

import requests
from selene import browser


API_URL = "https://api.start.ru/auth/refresh?apikey=a20b12b279f744f2b3c7b5c5400c4eb5"
apikey = "a20b12b279f744f2b3c7b5c5400c4eb5"

import requests

url = "https://api.start.ru/web/watch/vyzov?apikey=a20b12b279f744f2b3c7b5c5400c4eb5&locale=ru&content_lang=ru"

response = requests.request("GET", url)

print(response.text)