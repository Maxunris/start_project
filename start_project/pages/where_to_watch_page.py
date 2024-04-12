from selene import browser, have, command
import allure


class Where_to_watch:
    def open(self):
        with allure.step('Open site'):
            browser.open("ways-to-watch")

    def check_films_text(self):
        with allure.step('Checking text'):
            browser.all('.WaysToWatch_ways-to-watch__device-title__HdDMl').should(
                have.texts('Телевизоры', 'Приставки', 'Мобильные устройства'))


where_to_watch = Where_to_watch()
