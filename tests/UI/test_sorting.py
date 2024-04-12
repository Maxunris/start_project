import allure
from pages.sorting_page import Sorting


@allure.title("Checking sorting button")
def test_sorting():
    sorting = Sorting()
    sorting.open()
    sorting.open_category()
    sorting.open_desired_sorting()
    sorting.checking_text()
