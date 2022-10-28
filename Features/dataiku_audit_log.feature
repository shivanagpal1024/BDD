@audit_log
Feature: Compare Scenario Execution logs with Snowflake Database in DataIKU
    Scenario Outline: Verify Scenario Execution Time with Snowflake Database - <TC_ID>
      Given User Launch the Browser and Navigates to DataIKU Application URL
      When User Enters the Valid Credentials and Login
      Then User Should be able to Navigates to the Home Page and search for "<project_name>"
      When User Navigates to Scenarios Page with "<menu>" and "<sub_menu>" then Search for Scenarios
      Then User go to the scenario details page using "<scenario_name>" and capture execution time then compare with Snowflake Database "<snow_query>"
      Then User Should be able to compare and validate the scenario execution time with Database


      Examples:
      | TC_ID  |  project_name |  menu | sub_menu  | scenario_name | snow_query |

