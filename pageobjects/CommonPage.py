import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException


class CommonPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, timeout)

    def retry_click(self, web_element, timeout=10, sleep_time=1):
        retry = True
        ref_time = time.time()

        while retry and (time.time() - ref_time <= timeout):
            try:
                web_element.click()
                retry = False
            except ElementClickInterceptedException:
                time.sleep(sleep_time)
                retry = True
            except ElementNotInteractableException:
                time.sleep(sleep_time)
                retry = True
            except StaleElementReferenceException:
                time.sleep(sleep_time)
                retry = True

    def scroll_into_view(self, web_element):
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)

    def wait_until_element_is_found(self, locator, timeout=10, sleep_time=1):
        web_element = None
        ref_time = time.time()

        while web_element is None and (time.time() - ref_time <= timeout):
            try:
                web_element = self.driver.find_element(*locator)
                self.scroll_into_view(web_element)
            except NoSuchElementException:
                time.sleep(sleep_time)
            except StaleElementReferenceException:
                time.sleep(sleep_time)

        if web_element is not None:
            return web_element
        else:
            raise ValueError(f'Element with locator: {locator} was not found by the Web Driver')

    def wait_until_elements_is_found(self, locator, timeout=10, sleep_time=1):
        web_elements = []
        ref_time = time.time()

        while len(web_elements) <= 0 and (time.time() - ref_time <= timeout):
            try:
                web_elements = self.driver.find_elements(*locator)
            except NoSuchElementException:
                time.sleep(sleep_time)
            except StaleElementReferenceException:
                time.sleep(sleep_time)

        if len(web_elements) > 0:
            return web_elements
        else:
            raise ValueError(f'Elements with locator: {locator} was not found by the Web Driver')
