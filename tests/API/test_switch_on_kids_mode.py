import allure
import requests
from jsonschema import validate
from start_project.shemas.post import post


@allure.title("Checking switch on kids mode")
def test_trailer_api(base_api_url):
    endpoint = "/profile/select"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5"}
    payload = {
        "profile_id": "66eb0a9d-3afa-4607-acf0-b608597fd6a4"
    }

    headers = {
        'content-type': 'application/json',
        'Cookie': 'auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                  '.eyJ1aWQiOiI2NjE0NGEzY2JiOTliZDNlZjNkMjYwZjUiLCJwaWQiOiI1OTM4Njc2My1hN2FiLTQ4YzUtOWIzYy03YjhmOTI3MjA2NTAiLCJkaWQiOiIwZjcyMGVhNC03NDQwLTQxOGMtOTg2Mi1hYWY0MDIzNTY4YWUiLCJhbm9ueW1vdXMiOmZhbHNlLCJmb3Jfa2lkcyI6ZmFsc2UsImFjY291bnRfdHlwZSI6InJlZ2lzdGVyZWQiLCJhY2xfZXhwaXJlIjpudWxsLCJ1cGRhdGVkX2F0IjoxNzEyOTk1MTcwLCJ2IjozfQ.sIZfIJhvyQmVRvpT_xTievBH9VUIBJT5RY6ezVGr6uU'
    }
    response = requests.post(base_api_url + endpoint, params=params, json=payload, headers=headers)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Schema is validate'):
        validate(response.json(), post)
    with allure.step('True headers'):
        assert response.json()['profile_id'] == '59386763-a7ab-48c5-9b3c-7b8f92720650'
