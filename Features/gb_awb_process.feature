Feature: Glassbox AWB Process
    Scenario: Verify The Knowledge Article functionality for AWB
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to to process tab and select AWB
      When User select knowledge article with valid url for AWB
      When User update the knowledge article with empty value for AWB
      When User update the knowledge article with invalid url for AWB
      Then User user should be able to save the AWB article successfully

    Scenario: Verify Process Owner for AWB
        Given User Launch the browser and navigates to glassbox url then login with valid credentials
        When User go to to process tab and select AWB
        When User verify the Process Owner Name
        Then User user should be able to see the Process Owner Name


    Scenario: Verify Process name and Description for AWB
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to to process tab and select AWB
      When User verify the AWB Process Name and Description with DataIKU Instance
      Then The AWB Process Name and Description should match with DataIKU Instance


    Scenario: Verify Process and Operational Lineage for AWB
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to to process tab and select AWB
      When User select AWB Process Lineage and verify the DataIKU instance with Flow
      When User select AWB Operational Lineage and verify the DataIKU instance with Scenarios
      Then The User should be able to validate the AWB process and operational lineage

