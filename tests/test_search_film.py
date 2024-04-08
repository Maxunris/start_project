from selene import browser, have
import allure


@allure.title("Seatch film")
def test_search_film():
    with allure.step('Open site'):
        browser.open("")

    with allure.step('Enter the text in the search bar'):
        browser.element('.HeaderSearch_header-search__loupe__1SJbV').click()
        browser.element('.HeaderSearch_header-search__input-text__F3SjJ').type("Папины дочки").press_enter()
    with allure.step('Checking the first film'):
        browser.element('.VideoUnit_title__J_lZy').should(have.text('Папины дочки'))
