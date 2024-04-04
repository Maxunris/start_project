
from selene import browser, have

def test_kids_mod():
    browser.open('https://start.ru/')
    browser.element('.HeaderMenu_header-menu__wrapper___TgEa').click()
    browser.element('[data-testid="profile_kids"]').click()
    browser.element('.VideoUnit_vline__header__title__link__title__Nuqlc').should(have.text('Новинки для детей'))

