import allure
from selene import browser, have, command


class Sorting():


    @allure.title("Checking sorting button")
    def open(self):
        with allure.step('Open site'):
            browser.open("")
    def open_category(self):
        with allure.step('Open the desired category'):
            browser.element('[data-testid="animation_button"]').click()
            browser.element('[href="/animation/nurseryrhymes"]').click()
    def open_desired_sorting(self):
        with allure.step('Open the desired sorting'):
            browser.element('[alt="sort"]').click()
            browser.all('.CatalogSelect_select__item__Ea2Dr').element_by(have.exact_text('По рейтингу')).click()
    def checking_text(self):
        with allure.step('Checking the first series'):
            browser.driver.refresh()
            browser.element('#first-item').perform(command.js.scroll_into_view).should(have.text('Маша и Медведь'))
