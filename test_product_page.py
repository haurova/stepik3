import time

from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)

    page.open()
    page.click_add_to_cart_button(browser)
    page.check_that_product_is_added()
    page.check_that_price_is_correct()

