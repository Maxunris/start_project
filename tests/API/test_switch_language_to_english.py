import allure
from start_project.utils.api_helper import api_request

@allure.title("Checking switch Language in English")
def test_trailer_api(base_api_url):
    endpoint = "/document/terms_of_use/en"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5"}

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200

    with allure.step('True headers'):
        assert response.headers['Content-Type'] == 'text/html; charset=UTF-8'
    with allure.step('True language'):
        assert 'START user agreement' in response.text
