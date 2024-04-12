import requests
from jsonschema import validate
from start_project.shemas.trailer_shemas import trailer

def test_movie_api():
    BASE_URL = 'https://api.start.ru'
    endpoint = "/web/watch/vyzov"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "locale": "ru",
              "content_lang": "ru"
              }

    response = requests.get(BASE_URL + endpoint, params=params)

    assert response.status_code == 200
    assert response.json()["title"] == "Вызов"
    assert response.json()[
               "description"] == "Член экипажа МКС получает травму в открытом космосе. Помочь ему может только срочная операция, но провести ее в невесомости — дело из области фантастики. Сложнейшую задачу предстоит выполнить торакальному хирургу Жене. И у нее всего месяц на подготовку, но помешать героине могут не только перегрузки и отсутствие притяжения…Чем же закончится уникальная миссия?"



def shema_validation():
    url = "https://api.start.ru"
    endpoint = "/web/watch/vyzov"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "locale": "ru",
              "content_lang": "ru"
              }

    response = requests.get(url + endpoint, params=params)
    validate(response.json(), trailer)
