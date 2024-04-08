from selene import browser, have
import allure


@allure.title("Switching to kids mode")
def test_kids_mod():
    with allure.step('Open site'):
        browser.open("")
    with allure.step('Switching to child mode'):
        browser.element('.HeaderMenu_header-menu__wrapper___TgEa').click()
        browser.element('[data-testid="profile_kids"]').click()
    with allure.step('Checking text'):
        browser.element('.VideoUnit_vline__header__title__link__title__Nuqlc').should(have.text('Новинки для детей'))
