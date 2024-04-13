import allure
import requests
from jsonschema import validate
from start_project.shemas.search_shema import search


@allure.title("Checking movie data")

def test_trailer_api(base_api_url):
    endpoint = "/v2/search"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "q": "маша и медведь",
              "locale": "ru",
              "limit": "40",
              "offset": 0

              }
    url = "https://api.start.ru/v2/search?apikey=a20b12b279f744f2b3c7b5c5400c4eb5&q=%D0%BC%D0%B0%D1%88%D0%B0%20%D0%B8%20%D0%BC%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%8C&locale=ru&limit=40&offset=0"

    response = requests.get(base_api_url + endpoint, params=params)
    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('alias = masha-i-medved'):
        assert response.json()["items"][0]["alias"] == "masha-i-medved"
    with allure.step('Shema is validate'):
        validate(response.json(), search)
