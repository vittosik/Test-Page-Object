from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        assert 'login' in self.browser.current_url, 'It is not login page'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)