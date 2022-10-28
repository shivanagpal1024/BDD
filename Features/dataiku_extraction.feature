Feature: Extract Prameters data from dataIKU

    Scenario Outline: Extract connection parameters from dataIKU
      Given User Launch browser with application url and login with valid credentials
      When User Search for given project "<TestCaseName>" and "<ProjectName>"
      Then Read the "<ProjectName>" config data and write to outputfile

      Examples:
        |TestCaseName|ProjectName|
         |TC06   |MATCH_COSENTYX_EMAIL_CONTENT|