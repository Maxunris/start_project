import time
import allure

from selene import browser, have


@allure.title("Checking sorting button")
def test_sorting():
    with allure.step('Open site'):
        browser.open('https://start.ru/')
    with allure.step('Open the desired category'):
        browser.element('[data-testid="animation_button"]').click()
        browser.element('[href="/animation/nurseryrhymes"]').click()
    with allure.step('Open the desired sorting'):
        browser.element('[alt="sort"]').click()
        browser.all('.CatalogSelect_select__item__Ea2Dr').element_by(have.exact_text('По рейтингу')).click()
    with allure.step('Checking the first series'):
        time.sleep(5)
        browser.element('#first-item').should(have.text('Малышарики'))
