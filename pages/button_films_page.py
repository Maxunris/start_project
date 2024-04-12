from selene import browser, have
import allure

class Films_page:
    def open(self):
        with allure.step('Open site'):
            browser.open("")

    def click_films_button(self):
        with allure.step('Films button clickable'):
            browser.element('[data-testid="movies_button"]').click()

    def check_films_text(self):
        with allure.step('Checking text'):
            browser.element('.Catalog_catalog__Gjv4a').should(have.text('Фильмы - смотреть онлайн'))
