@datavalidation_snowflake_minus
Feature: Data validation in Snowflake database using minus query

Scenario Outline:  Validate that the columns are straight move from source table for <tc_id>
    Given the Snowflake response with valid <snow_query>
    Then validate that the response has no differences for <tc_id>
    Examples:
      | tc_id | snow_query |