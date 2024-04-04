import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_manage():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://start.ru/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.quit()
# import os
#
# import pytest
# from selene import browser
# from selenium import webdriver
# import allure
# from selenium.webdriver.chrome.options import Options
# from dotenv import load_dotenv
# from utils import attach
#
# DEFAULT_BROWSER_VERSION = '100.0'
#
#
#
# @allure.step('Select browser version')
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='100.0'
#     )
#
# @allure.step('Load env')
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope="function", autouse=True)
# def driver_configuration(request):
#     with allure.step('Driver configuration strategy'):
#         browser_version = request.config.getoption('--browser_version')
#         browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
#         driver_options = webdriver.ChromeOptions()
#         driver_options.page_load_strategy = 'eager'
#         browser.config.driver_options = driver_options
#         browser.config.window_width = 1920
#         browser.config.window_height = 1080
#         browser.config.base_url = "https://start.ru/"
#         options = Options()
#         selenoid_capabilities = {
#             "browserName": 'chrome',
#             "browserVersion": browser_version,
#             "selenoid:options": {
#                 "enableVNC": True,
#                 "enableVideo": True
#             }
#         }
#
#         options.capabilities.update(selenoid_capabilities)
#         login = os.getenv('LOGIN')
#         password = os.getenv('PASSWORD')
#         driver = webdriver.Remote(
#             command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
#             options=options)
#
#         browser.config.driver = driver
#
#     yield
#
#     with allure.step('Add screenshot'):
#         attach.add_screenshot(browser)
#
#     with allure.step('Add logs'):
#         attach.add_logs(browser)
#
#     with allure.step('Add html'):
#         attach.add_html(browser)
#
#     with allure.step('Add video'):
#         attach.add_video(browser)
#
#     with allure.step('Close driver'):
#         browser.quit()