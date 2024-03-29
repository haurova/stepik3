import pytest

from pages import BasketPage, ProductPage, LoginPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(page.generate_email(), 'q123w456e789')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_cart_button(browser)
        page.check_that_product_is_added()
        page.check_that_price_is_correct()


@pytest.mark.parametrize('url', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, url):
    new_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{url}"
    page = ProductPage(browser, new_link)
    page.open()
    page.click_add_to_cart_button(browser)
    page.check_that_product_is_added()
    page.check_that_price_is_correct()


@pytest.mark.xfail(reason="expected behaviour")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button(browser)
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="expected behaviour")
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    new_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, new_link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()






