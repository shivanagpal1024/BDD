@null_check_snowflake
Feature: Validation of null check in Snowflake database

Scenario Outline:  Verify the null check for <tc_id>
    Given the Snowflake response with valid <snow_query>
    Then validate that the response has any records for <tc_id>
    Examples:
      | tc_id | snow_query |