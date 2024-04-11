import allure
from pages.button_films_page import MainPage

@allure.title("The films button clickable")
def test_button_films():
    main_page = MainPage()
    main_page.open()
    main_page.click_films_button()
    main_page.check_films_text()