@duplicate_check_snowflake
Feature: Validation of duplicate check in Snowflake database

Scenario Outline:  Verify the duplicate check for <tc_id>
    Given the Snowflake response with valid <snow_query>
    Then validate that the response has duplicates or not for <tc_id>
    Examples:
      | tc_id | snow_query |