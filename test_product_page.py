import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('url', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, url):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{url}"

    page = ProductPage(browser, link)

    page.open()
    page.click_add_to_cart_button(browser)
    page.check_that_product_is_added()
    page.check_that_price_is_correct()
