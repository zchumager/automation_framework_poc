from selenium.webdriver.common.by import By
from pageobjects.CommonPage import CommonPage


class HomePage(CommonPage):
    def __init__(self, driver, timeout=10):
        super(HomePage, self).__init__(driver, timeout)

        self.CHECKING_ACCOUNTS_SELECTOR = (
            By.CSS_SELECTOR, '[id="better-btn-02"][href="/personal/checking"]'
        )

        self.FIND_A_BRANCH_SELECTOR = (
            By.CSS_SELECTOR, '[href="https://locations.santanderbank.com/search.html"]'
        )

    def click_checking_accounts_btn(self):
        button = self.wait_until_element_is_found(self.CHECKING_ACCOUNTS_SELECTOR)
        self.retry_click(button)

    def click_find_a_branch_btn(self):
        button = self.wait_until_element_is_found(self.FIND_A_BRANCH_SELECTOR)
        self.retry_click(button)
