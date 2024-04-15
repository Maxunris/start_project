import requests
from start_project.utils.attach import response_logging, response_attaching


def api_request(base_api_url, endpoint, method, json=None, params=None, headers=None):
    url = f"{base_api_url}{endpoint}"
    response = requests.request(method, url, json=json, params=params, headers=headers)
    response_logging(response)
    response_attaching(response)
    return response
