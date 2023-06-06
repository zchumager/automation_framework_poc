from selenium.webdriver.common.by import By
from pageobjects.CommonPage import CommonPage


class PersonalCheckingPage(CommonPage):
    def __init__(self, driver, timeout=10):
        super(PersonalCheckingPage, self).__init__(driver, timeout)

        self.CHECKING_BOXES_SELECTOR = (By.CSS_SELECTOR, '.bgGradient')
        self.SIMPLY_RIGHT_CHECKING_OPEN_ACCOUNT_SELECTOR = (
            By.CSS_SELECTOR,
            '.btn-primary[href="/personal/checking/simply-right-checking"]+a>p'
        )

    def get_checking_boxes(self):
        checking_boxes = self.wait_until_elements_is_found(self.CHECKING_BOXES_SELECTOR)

        return checking_boxes

    def click_simply_right_checking_open_account_link(self):
        link = self.wait_until_element_is_found(self.SIMPLY_RIGHT_CHECKING_OPEN_ACCOUNT_SELECTOR)
        self.retry_click(link)
