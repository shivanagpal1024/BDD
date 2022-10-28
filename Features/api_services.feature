Feature: Get Users List

  Scenario Outline: Verify Users List
    Given user send a request to the URL to get user details using "<sheet_name>"
    Then the response will return status 200
    Examples:
      |sheet_name|
      |users     |
      |register  |

