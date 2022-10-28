Feature: ANZO UI TestCases
  Background: common steps
    Given User Launch the browser and navigates to application url
    When User enter valid credentials and logged into application
    Then User navigates to graphmarts and perform search

  Scenario Outline: Create Dashboard and Verify properties
    Then "<TestCaseName>" initiation using the "<TestSheetName>" and create the dashboard by selecting network navigator
    Then click on Find Data and search for HCP class
    Examples:
      | TestCaseName   | TestSheetName  |
      | TC01 | UITestData |


  Scenario Outline: Metadata Validation between STTM and configuration in Anzo
    Then User navigates to Datalayers and perform calls
    Then validate Metadata between STTM "<FileName>" "<SheetName>" using the "<ColumnName>" and configuration data in ANZO
    Examples:
     | FileName | SheetName | ColumnName |
     | ANZO_Testdata | NGE_KG_CALLS | Predicate |

