from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        assert 'login' in self.browser.current_url, 'It is not login page'

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)