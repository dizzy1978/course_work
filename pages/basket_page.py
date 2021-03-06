from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_empty_basket_main(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert basket_empty.text == "Your basket is empty. Continue shopping", "Basket is not empty!"

    def check_empty_basket(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert basket_empty.text == "Your basket is empty. Continue shopping", "Basket is not empty!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be!"


