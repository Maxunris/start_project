import allure
from start_project.pages.search_film_page import search_film


@allure.title("Checking search film")
def test_search_film():
    search_film.open()

    search_film.enter_text()

    search_film.checking_text()
