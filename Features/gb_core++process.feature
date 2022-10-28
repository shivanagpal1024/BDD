Feature: Glassbox Core ++ Process
    Scenario: Verify The Knowledge Article functionality for Core ++
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to to process tab and select Core
      When User select knowledge article with valid url for Core
      When User update the knowledge article with empty value for Core
      When User update the knowledge article with invalid url for Core
      Then User user should be able to save the Core article successfully


    Scenario: Verify Process name and Description for Core ++
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to to process tab and select Core
      When User verify the Core Process Name and Description with DataIKU Instance
      Then The Core Process Name and Description should match with DataIKU Instance


    Scenario: Verify Process and Operational Lineage for Core ++
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to to process tab and select Core
      When User select Core Process Lineage and verify the DataIKU instance with Flow
      When User select Core Operational Lineage and verify the DataIKU instance with Scenarios
      Then The User should be able to validate the Core process and operational lineage

