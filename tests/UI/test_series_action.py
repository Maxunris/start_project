import allure
from start_project.pages.series_action_page import series_action


@allure.title("Checking the desired category")
def test_series_action():
    series_action.open()
    series_action.open_category()
    series_action.checking_text()
