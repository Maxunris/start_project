import allure
import requests
from jsonschema import validate
from start_project.shemas.trailer_shemas import trailer


@allure.title("Checking trailer data")
def test_trailer_api(base_api_url):
    endpoint = "/web/watch/vyzov"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "locale": "ru",
              "content_lang": "ru"
              }

    response = requests.get(base_api_url + endpoint, params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('title = Вызов'):
        assert response.json()["title"] == "Вызов"
    with allure.step('description correct'):
        assert response.json()[
                   "description"] == "Член экипажа МКС получает травму в открытом космосе. Помочь ему может только срочная операция, но провести ее в невесомости — дело из области фантастики. Сложнейшую задачу предстоит выполнить торакальному хирургу Жене. И у нее всего месяц на подготовку, но помешать героине могут не только перегрузки и отсутствие притяжения…Чем же закончится уникальная миссия?"
    with allure.step('Schema is validate'):
        validate(response.json(), trailer)

