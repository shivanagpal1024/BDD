@audit_check_snowflake
Feature: Validation of Audit table in Snowflake database

Scenario Outline:  Verify the details in audit table for <TC_ID>
    Given the Snowflake response with valid <snow_query>
    Then validate the date information
    Examples:
      | TC_ID | snow_query |