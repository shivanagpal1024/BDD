# Created by PURITSA1 at 6/16/2022
Feature: DataIKU Recipes Validation
  Scenario Outline: Validating SQL Recipes in DataIKU
    Given User Launch browser with application url and login with valid credentials
      When User Search for given project "<TestCaseName>" and "<ProjectName>"
      Then Validates the "<ProjectName>" SQL recipes and save screenshots to output file

      Examples:
        | TestCaseName | ProjectName |
#        | TC04 | MATCH_DATA_PROFILE_PIPELINE |
        | TC06 | MATCH_CONCERTO_DATA_PIPELINE |