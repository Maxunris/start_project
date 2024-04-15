from selene import browser, have, command
import allure


class Search_film():
    @allure.title("Seatch film")
    def open(self):
        with allure.step('Open site'):
            browser.open("")

    def enter_text(self):
        with allure.step('Enter the text in the search bar'):
            browser.element('.HeaderSearch_header-search__loupe__1SJbV').perform(command.js.click)
            browser.element('.HeaderSearch_header-search__input-text__F3SjJ').type("Папины дочки").press_enter()

    def checking_text(self):
        with allure.step('Checking the first film'):
            browser.element('.VideoUnit_title__J_lZy').should(have.text('Папины дочки'))


search_film = Search_film()
