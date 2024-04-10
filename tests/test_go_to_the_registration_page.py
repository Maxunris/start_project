from selene import browser, have
import allure


@allure.title("Registration page")
def test_button_films():
    with allure.step('Open site'):
        browser.open("")
    with allure.step('Button try it for free'):
        browser.element('[data-testid="try_free_button_text"]').click()
    with allure.step('Checking text'):
        browser.element('.Sign_sign__form-title__USFwT').should(have.text('Зарегистрируйтесь и смотрите START 7 дней бесплатно'))
