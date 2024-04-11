import allure
from selene import browser, have



class Series_action():
    @allure.title("Checking the desired category")
    def open(self):
        with allure.step('Open site'):
            browser.open("")
    def open_category(self):
        with allure.step('Open the desired category'):
            browser.element('[data-testid="series_button"]').click()
            browser.element('[href="/series/action"]').click()
    def checking_text(self):
        with allure.step('Checking the first series'):
            browser.element('.Catalog_catalog__Gjv4a').should(have.text('Сериалы: боевики - смотреть онлайн'))
