import allure
from pages.series_action_page import Series_action


@allure.title("Checking the desired category")
def test_series_action():
    series_action = Series_action()
    series_action.open()
    series_action.open_category()
    series_action.checking_text()

