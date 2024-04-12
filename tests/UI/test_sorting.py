import allure
from start_project.pages.sorting_page import sorting


@allure.title("Checking sorting button")
def test_sorting():
    sorting.open()
    sorting.open_category()
    sorting.open_desired_sorting()
    sorting.checking_text()
