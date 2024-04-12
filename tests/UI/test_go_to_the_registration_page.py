import allure
from start_project.pages.registration_page import RegistrationPage


@allure.title("Registration page")
def test_button_for_free():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.click_for_free_button()
    registration_page.check_registration_page()
