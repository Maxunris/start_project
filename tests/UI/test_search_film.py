import allure
from start_project.pages.search_film_page import Search_film


@allure.title("Seatch film")
def test_search_film():
    search_film = Search_film()
    search_film.open()
    search_film.enter_text()
    search_film.checking_text()
