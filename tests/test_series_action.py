
from selene import browser, have

def test_series_action():
    browser.open('https://start.ru/')
    browser.element('[data-testid="series_button"]').click()
    browser.element('[href="/series/action"]').click()
    browser.element('.Catalog_catalog__Gjv4a').should(have.text('Сериалы: боевики - смотреть онлайн'))

