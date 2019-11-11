import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
    
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    if browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    elif browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
        raise pytest.UsageError("--language should be described")

    yield browser
    print("\nquit browser..")
    browser.quit()

	