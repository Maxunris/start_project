import allure
from start_project.pages.where_to_watch_page import where_to_watch


@allure.title("Checking 'Where to watch' button")
def test_where_to_watch():
    where_to_watch.open()

    where_to_watch.check_films_text()
