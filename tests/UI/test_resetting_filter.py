import allure
from pages.resetting_filter_page import Filter_page

@allure.title("The filter reset button is working")
def test_resetting_filter():
    filter_page = Filter_page()
    filter_page.open()
    filter_page.switching_the_filter()
    filter_page.Checking_text()
