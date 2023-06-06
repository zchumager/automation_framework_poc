import time

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.wait import WebDriverWait
from helpers import environments
from helpers.driver import driver
from pageobjects.HomePage import HomePage
from pageobjects.PersonalCheckingPage import PersonalCheckingPage
from pageobjects.LocationsPage import LocationsPage


@pytest.mark.parametrize("browser", ["chrome"])
@scenario('../sanity.feature', 'Checking Accounts')
def test_checking_accounts(driver):
    expected_url = 'https://secureopen.santanderbank.com' \
                   '/apps/servlet/SmartForm.html?formCode=sbnadao&product=SimplyRightChecking'

    # Switching to new tab opened
    driver.switch_to.window(driver.window_handles[1])

    assert expected_url in driver.current_url


@pytest.mark.parametrize("browser", ["chrome"])
@scenario('../sanity.feature', 'Find Branch')
def test_find_branch(driver):
    pass


@pytest.mark.parametrize("browser", ["chrome"])
@scenario('../sanity.feature', 'Invalid Zip Code')
def test_invalid_zipcode(driver):
    error_message_locator = (By.CLASS_NAME, "no-results-apps")
    error_message_div = WebDriverWait(driver, 10).until(
        condition.visibility_of_element_located(error_message_locator)
    )

    assert error_message_div is not None
    assert error_message_div.tag_name == "div"


@given(parsers.parse('Navigate to {env} home page'))
def navigate_to_home_page(driver, env):
    url = environments.e2e_envs.get(env)
    driver.get(url)


@when('Click checking accounts button')
def click_checking_account_button(driver):
    HomePage(driver).click_checking_accounts_btn()


@when('Click find a branch button')
def click_find_a_branch(driver):
    HomePage(driver).click_find_a_branch_btn()


@when('Click simply right checking open account link')
def click_simply_right_checking_open_account_link(driver):
    PersonalCheckingPage(driver).click_simply_right_checking_open_account_link()


@when(parsers.parse("Fill location search box with zip code {zipcode} and hit enter"))
def fill_location_search_box_and_hit_enter(driver, zipcode):
    LocationsPage(driver).fill_location_search_box_and_hit_enter(zipcode)


@when('Get checking boxes')
def get_checking_boxes(driver):
    expected_labels = ["Santander Select®", "Simply Right® Checking", "Student Value"]
    checking_boxes = PersonalCheckingPage(driver).get_checking_boxes()

    assert len(expected_labels) == len(checking_boxes)

    for label, box in zip(expected_labels, checking_boxes):
        assert label in box.text


@then(parsers.parse("Validate quantity of boxes is {boxes_number}"))
def validate_quatity_of_boxes(driver, boxes_number):
    checking_boxes = LocationsPage(driver).get_branch_boxes()

    assert len(checking_boxes) == int(boxes_number)


@then(parsers.parse("Validate boxes belong to location {location}"))
def validate_boxes_belong_to_location(driver, location, boxes_number=1):
    checking_boxes = LocationsPage(driver).get_branch_boxes()

    time.sleep(1)
    location_boxes = list(filter(lambda box: location in box.text, checking_boxes))

    assert len(location_boxes) >= boxes_number

