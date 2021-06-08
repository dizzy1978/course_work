import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button1 = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button1.click()
        self.solve_quiz_and_get_code()

    def control_added_label(self):
        actual_label = self.browser.find_element(*ProductPageLocators.ACTUAL_LABEL).text
        label_in_cart = self.browser.find_element(*ProductPageLocators.LABEL_IN_CART).text
        assert label_in_cart == actual_label, "Product label does not match with label in cart!"

    def control_added_price(self):
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE).text
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert price_in_cart == actual_price, "Product price does not match with price in cart!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be!"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not desappeared!"


