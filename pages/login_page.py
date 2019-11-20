from pages.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        curl = self.browser.current_url
        assert self.browser.current_url == LoginPageLocators.LOGIN_URL, "Login page url is wrong, it's " + curl + ", should be " + LoginPageLocators.LOGIN_URL

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login form: email field is missing"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form: password field is missing"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOT_PASSWORD_LINK), "Login form: no 'Forgot password' link"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BTN), "Login form: 'Login' button is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration form: email field is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration form: password field is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "Registration form: 'repeat password' field is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), "Registration form: 'Submit' button is missing"
