from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_cart_button(self, browser):
        alert = BasePage(browser, browser.current_url)

        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "No add to cart button found"
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()
        alert.solve_quiz_and_get_code()

    def check_that_product_is_added(self):
        actual_text = self.browser.find_element(*ProductPageLocators.SUCCESS_TEXT).text
        expected_text = ProductPageLocators.EXPECTED_SUCCESS_TEXT
        assert actual_text == expected_text, "Text is wrong. Should be '" + expected_text + "', but it's '" + actual_text + "'"

    def check_that_price_is_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert cart_price == product_price, "Price is wrong. Should be '" + product_price + "', but it's '" + cart_price + "'"

