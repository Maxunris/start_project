from selene import browser, have
import allure

class Tv_page:
    def open(self):
        with allure.step('Open site'):
            browser.open("")

    def click_tv_button(self):
        with allure.step('TV button clickable'):
            browser.element('[data-testid="tv_button"]').click()

    def check_tv_text(self):
        with allure.step('Checking text'):
            browser.element('.TvSchedule_container__VQpHm').should(have.text('ТВ Каналы Онлайн и Программа Передач'))
