from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobjects.CommonPage import CommonPage


class LocationsPage(CommonPage):
    def __init__(self, driver, timeout=10):
        super(LocationsPage, self).__init__(driver, timeout)

        self.LOCATION_SEARCH_BOX_SELECTOR = (By.CSS_SELECTOR, '[type="text"][name="locator-search-value"]')
        self.BRANCH_BOXES_SELECTOR = (By.CSS_SELECTOR, '.map-list-info')

    def fill_location_search_box_and_hit_enter(self, text):
        textbox = self.wait_until_element_is_found(self.LOCATION_SEARCH_BOX_SELECTOR)
        textbox.send_keys(text)
        textbox.send_keys(Keys.ENTER)

    def get_branch_boxes(self):
        branch_boxes = self.wait_until_elements_is_found(self.BRANCH_BOXES_SELECTOR)

        return branch_boxes
