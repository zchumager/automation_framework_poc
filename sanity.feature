Feature: Sanity
  Test Suite for Sanity

  Scenario Outline: Checking Accounts
    Examples:
      | environment |
      | prod |

    Given Navigate to <environment> home page
    When Click checking accounts button
    When Get checking boxes
    When Click simply right checking open account link

  Scenario Outline: Find Branch
    Examples:
      | environment | zipcode |  location | boxes_number |
      | prod        |  07733  |   Hazlet  |       4      |

    Given Navigate to <environment> home page
    When Click find a branch button
    When Fill location search box with zip code <zipcode> and hit enter
    Then Validate quantity of boxes is <boxes_number>
    Then Validate boxes belong to location <location>



  Scenario Outline: Invalid Zip Code
    Examples:
      | environment | zipcode |
      | prod        | 0000    |

    Given Navigate to <environment> home page
    When Click find a branch button
    When Fill location search box with zip code <zipcode> and hit enter

