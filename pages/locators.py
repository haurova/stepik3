from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-default[href='/en-gb/basket/']")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/en-gb/password-reset/']")
    LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_TEXT = (By.CSS_SELECTOR, "#messages > *:first-child div")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    EXPECTED_SUCCESS_TEXT = " has been added to your basket."
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    CART_PRICE = (By.CSS_SELECTOR, "#messages > *:last-child > div > p > strong")
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")
