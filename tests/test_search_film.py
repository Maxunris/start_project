
from selene import browser, have

def test_search_film():
    browser.open('https://start.ru/')
    browser.element('.HeaderSearch_header-search__loupe__1SJbV').click()
    (browser.element('.HeaderSearch_header-search__input-text__F3SjJ').
     type("Папины дочки").press_enter())
    browser.element('.VideoUnit_title__J_lZy').should(have.text('Папины дочки'))

