import time

import allure
from pages.where_to_watch_page import Where_to_watch

@allure.title("Where to watch button clicable")
def test_where_to_watch():
    where_to_watch = Where_to_watch()
    where_to_watch.open()
    where_to_watch.check_films_text()


