import allure
from selene import browser, have


@allure.title("Checking the desired category")
def test_series_action():
    with allure.step('Open site'):
        browser.open("")
    with allure.step('Open the desired category'):
        browser.element('[data-testid="series_button"]').click()
        browser.element('[href="/series/action"]').click()
    with allure.step('Checking the first series'):
        browser.element('.Catalog_catalog__Gjv4a').should(have.text('Сериалы: боевики - смотреть онлайн'))
