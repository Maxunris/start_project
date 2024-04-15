import allure
from start_project.pages.resetting_filter_page import filter_page


@allure.title("Checking the filter reset button")
def test_resetting_filter():
    filter_page.open()

    filter_page.switching_the_filter()

    filter_page.Checking_text()
