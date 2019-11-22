import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('url', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, url):
    new_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{url}"

    page = ProductPage(browser, new_link)

    page.open()
    page.click_add_to_cart_button(browser)
    page.check_that_product_is_added()
    page.check_that_price_is_correct()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)

    page.open()
    page.click_add_to_cart_button(browser)
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)

    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)

    page.open()
    page.click_add_to_cart_button(browser)
    page.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    new_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, new_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    new_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, new_link)
    page.open()
    page.go_to_login_page()

