import allure
import requests
from jsonschema import validate
from start_project.shemas.trailer_shemas import trailer


@allure.title("Checking movie data")
def test_trailer_api():
    endpoint = "/v2/search"
    headers = {
        'Cookie': 'FOR_KIDS=False; AUTHORIZED_USER=True; IS_PAID=False; auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI2NjE0NGEzY2JiOTliZDNlZjNkMjYwZjUiLCJwaWQiOiI1OTM4Njc2My1hN2FiLTQ4YzUtOWIzYy03YjhmOTI3MjA2NTAiLCJkaWQiOiIwZjcyMGVhNC03NDQwLTQxOGMtOTg2Mi1hYWY0MDIzNTY4YWUiLCJhbm9ueW1vdXMiOmZhbHNlLCJmb3Jfa2lkcyI6ZmFsc2UsImFjY291bnRfdHlwZSI6InJlZ2lzdGVyZWQiLCJhY2xfZXhwaXJlIjpudWxsLCJ1cGRhdGVkX2F0IjoxNzEyOTk3MTU3LCJ2IjozfQ.RVxgflQd5vbCnU3H_GEMQQscnIjxuz5FPEkFc5Y088o'
    }
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "q": "%D0%BC%D0%B0%D1%88%D0%B0%20%D0%B8%20%D0%BC%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%8C",
              "locale": "ru",
              "limit": "40",
              "offset": 0

              }
    url = "https://api.start.ru/v2/search?apikey=a20b12b279f744f2b3c7b5c5400c4eb5&q=%D0%BC%D0%B0%D1%88%D0%B0%20%D0%B8%20%D0%BC%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%8C&locale=ru&limit=40&offset=0"

    response = requests.get(url, headers=headers)
    print(response.text)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('alias = masha-i-medved'):
        pass
