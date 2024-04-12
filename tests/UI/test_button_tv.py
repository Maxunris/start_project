import allure
from start_project.pages.button_tv_page import tv_page

@allure.title("The tv button clickable")
def test_button_films():
    tv_page.open()
    tv_page.click_tv_button()
    tv_page.check_tv_text()