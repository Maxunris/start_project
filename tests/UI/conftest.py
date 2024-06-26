import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from start_project.utils import attach
from selene import browser
from selenium import webdriver

DEFAULT_BROWSER_VERSION = "120.0"
DEFAULT_BROWSER_NAME = "chrome"


def pytest_addoption(parser):
    parser.addoption("--browser_version", default="120.0")
    parser.addoption("--browser_name", default="chrome")


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    browser_name = request.config.getoption('--browser_name')
    browser_name = browser_name if browser_name != "" else DEFAULT_BROWSER_NAME

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                              options=options)
    browser.config.base_url = "https://start.ru/"
    browser.config.driver = driver
    browser.config.driver_options = options
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope="function")
def browser_manage():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://start.ru/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.quit()
