
from selene import browser, have

def test_sorting():
    browser.open('https://start.ru/')
    browser.element('[data-testid="movies_button"]').click()
    browser.element('.Catalog_catalog__Gjv4a').should(have.text('Фильмы - смотреть онлайн'))

