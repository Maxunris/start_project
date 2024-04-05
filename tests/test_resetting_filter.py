import time

from selene import browser, have

def test_resetting_filter():
    browser.open('https://start.ru/series/family')
    browser.element('[data-testid="reset_filter_button"]').click()
    time.sleep(10)
    browser.element('#first-item').should(have.text('Престиж'))

