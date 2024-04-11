from selene import browser, have
import allure

class RegistrationPage:
    def open(self):
        with allure.step('Open site'):
            browser.open("")
    def click_for_free_button(self):
        with allure.step('Button try it for free'):
            browser.element('[data-testid="try_free_button_text"]').click()
    def check_registration_page(self):
        with allure.step('Checking text'):
            browser.element('.Sign_sign__form-title__USFwT').should(have.text('Зарегистрируйтесь и смотрите START 7 дней бесплатно'))
