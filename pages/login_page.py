from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        gotlink = self.browser.current_url
        assert "login" in gotlink, "Login URL has no contains 'login' string"

    def should_be_login_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is NOT FOUND!"


    def should_be_register_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is NOT FOUND!"




