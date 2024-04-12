from selene import browser, have, be
import allure


class Filter_page():
    @allure.title("The filter reset button is working")
    def open(self):
        with allure.step('Open site'):
            browser.open('series/family')

    def switching_the_filter(self):
        with allure.step('Switching the filter'):
            browser.element('[data-testid="reset_filter_button"]').click()

    def Checking_text(self):
        with allure.step('Checking the first series'):
            browser.element('#first-item').should(be.visible).wait_until(have.text('Престиж'))
