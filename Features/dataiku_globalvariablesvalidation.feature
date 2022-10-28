Feature: Validate Table Data in dataIKU

Scenario Outline: Validate all the variables in Global variables are declared in parameters the Data in dataIKU
      Given User Launch browser with application url and login into valid credentials
      When User Search for project "<TestFile>" "<TestCaseName>" and "<TestSheetName>"
      Then Read project and Dataset from "<TestFile>" "<TestSheetName>" and validate connection parameters with global variables
      Examples:
        | TestFile |TestCaseName|TestSheetName|
        |EmailContent_Mapping_Document_Ver3_GV|TC11|MATCH_COSENTYX_EMAIL_CONTENT|