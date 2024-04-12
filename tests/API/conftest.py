import requests
import pytest
def get_id(url, headers, payload):
    result = requests.post(url=url, headers=headers, json=payload)
    return result.json()['session_id']