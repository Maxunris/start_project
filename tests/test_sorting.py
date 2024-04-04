import time

from selene import browser, have

def test_sorting():
    browser.open('https://start.ru/')
    browser.element('[data-testid="animation_button"]').click()
    browser.element('[href="/animation/nurseryrhymes"]').click()
    browser.element('[alt="sort"]').click()
    browser.all('.CatalogSelect_select__item__Ea2Dr').element_by(have.exact_text('По рейтингу')).click()
    time.sleep(5)
    browser.element('#first-item').should(have.text('Малышарики'))

