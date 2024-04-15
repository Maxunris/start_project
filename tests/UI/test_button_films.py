import allure
from start_project.pages.button_films_page import films_page


@allure.title("The films button clickable")
def test_button_films():
    films_page.open()

    films_page.click_films_button()

    films_page.check_films_text()
