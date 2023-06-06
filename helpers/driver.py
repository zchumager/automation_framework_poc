import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_browser(browser):
    if browser == 'chrome':
        return webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'headlesschrome':
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    elif browser == 'firefox':
        return webdriver.firefox(executable_path=GeckoDriverManager().install())


@pytest.fixture
def driver(browser):
    instance = get_browser(browser)
    yield instance
    instance.quit()
