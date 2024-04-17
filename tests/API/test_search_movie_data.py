import allure
from jsonschema import validate
from start_project.shemas.search_shema import search
from start_project.utils.api_helper import api_request



@allure.title("Checking movie data")
def test_trailer_api(base_api_url):
    endpoint = "/v2/search"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "q": "маша и медведь",
              "locale": "ru",
              "limit": "40",
              "offset": 0

              }

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('alias = masha-i-medved'):
        assert response.json()["items"][0]["alias"] == "masha-i-medved"
    with allure.step('Schema is validate'):
        validate(response.json(), search)

