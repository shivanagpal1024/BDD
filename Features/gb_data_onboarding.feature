Feature: Data Onboard for csv on Glassbox
    Scenario: Verify Onboard Objects for csv in Glassbox
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to the Data Onboard
      When User Onboard the Data Objects
      Then User Should be able to Onboard the Objects

    Scenario: Verify Onboard Objects for json in Glassbox
      Given User Launch the browser and navigates to glassbox url then login with valid credentials
      When User go to the Data Onboard for json
      When User Onboard the Data Objects for json
      Then User Should be able to Onboard the Objects for json