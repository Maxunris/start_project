from selene import browser, have
import allure


@allure.title("The films button clickable")
def test_button_films():
    with allure.step('Open site'):
        browser.open("")
    with allure.step('Films button clickable'):
        browser.element('[data-testid="movies_button"]').click()
    with allure.step('Checking text'):
        browser.element('.Catalog_catalog__Gjv4a').should(have.text('Фильмы - смотреть онлайн'))
