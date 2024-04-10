import allure
from selene import browser, have, command


@allure.title("Checking sorting button")
def test_sorting():
    with allure.step('Open site'):
        browser.open("")
    with allure.step('Open the desired category'):
        browser.element('[data-testid="animation_button"]').click()
        browser.element('[href="/animation/nurseryrhymes"]').click()
    with allure.step('Open the desired sorting'):
        browser.element('[alt="sort"]').click()
        browser.all('.CatalogSelect_select__item__Ea2Dr').element_by(have.exact_text('По рейтингу')).click()
    with allure.step('Checking the first series'):
        browser.driver.refresh()
        browser.element('#first-item').perform(command.js.scroll_into_view).should(have.text('Маша и Медведь'))
