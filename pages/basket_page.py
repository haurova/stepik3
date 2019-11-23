from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), "There is no empty basket message"

    def should_not_be_displayed_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), "The empty basket message is displayed"

