import time

import requests
from selene import browser


API_URL = "https://api.start.ru/auth/refresh?apikey=a20b12b279f744f2b3c7b5c5400c4eb5"
apikey = "a20b12b279f744f2b3c7b5c5400c4eb5"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
    "content-length": "0",
    "cookie": "IS_PAID=False; AUTHORIZED_USER=True; _ga_TFM2K2079M=GS1.1.1712604705.6.1.1712605772.42.0.0; startCookieAgreement=true; mindboxDeviceUUID=72fb6e01-d153-4a65-bbed-8e0398a39cb6; directCrm-session=%7B%22deviceGuid%22%3A%2272fb6e01-d153-4a65-bbed-8e0398a39cb6%22%7D; FOR_KIDS=False; startOrigin=start.ru; startSliderHeight=staticHeight; auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI2NjE0NGEzY2JiOTliZDNlZjNkMjYwZjUiLCJwaWQiOiI1OTM4Njc2My1hN2FiLTQ4YzUtOWIzYy03YjhmOTI3MjA2NTAiLCJkaWQiOiIwZjcyMGVhNC03NDQwLTQxOGMtOTg2Mi1hYWY0MDIzNTY4YWUiLCJhbm9ueW1vdXMiOmZhbHNlLCJmb3Jfa2lkcyI6ZmFsc2UsImFjY291bnRfdHlwZSI6InJlZ2lzdGVyZWQiLCJhY2xfZXhwaXJlIjpudWxsLCJ1cGRhdGVkX2F0IjoxNzEyODYyNjE4LCJ2IjozfQ.u5A2LrtaLh-2X3fPB-vNhnNAGhdATGM5WQ5GjKXDbLk; session_id={\"profileId\":\"59386763-a7ab-48c5-9b3c-7b8f92720650\",\"sessionId\":\"937fda9f-2db9-4a22-8616-063613ecb758\"}; sequenceNumber=1; device_type=web",
    "origin": "https://payment.start.ru",
    "referer": "https://payment.start.ru/",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Postman-Token": "3eeda94d-91bf-45a1-bf40-ddfcbd80809a",
    "Host": "api.start.ru",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
data = {"apikey" : "a20b12b279f744f2b3c7b5c5400c4eb5"}
def test_login_api():

    response = requests.post(url=API_URL, data=data, headers=headers)
    print(response.cookies)
    print(response.status_code)
    print(response.cookies.get("auth"))
    cookies = response.cookies.get("auth")
    cookies2 = response.cookies.get("AUTHORIZED_USER")

    browser.open("https://start.ru")
    browser.driver.add_cookie({"name" : "auth", "value" : cookies})
    browser.driver.add_cookie({"name": "AUTHORIZED_USER", "value": cookies2})
    time.sleep(10)