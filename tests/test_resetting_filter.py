import time

from selene import browser, have, be
import allure


@allure.title("The filter reset button is working")
def test_resetting_filter():
    with allure.step('Open site'):
        browser.open('series/family')

    with allure.step('Switching the filter'):
        browser.element('[data-testid="reset_filter_button"]').click()

    with allure.step('Checking the first series'):
        browser.element('#first-item').should(have.text('Престиж'))
