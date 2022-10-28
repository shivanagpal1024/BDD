@count_validation_snowflake
Feature: Validation of records count in snowflake to snowflake

Scenario Outline: Validate the count of records for <tc_id>
    Given the source response from snowflake using <source_query>
    Then get the target response from snowflake using <target_query>
    Then validate the records count for <tc_id>
    Examples:
      | tc_id | source_query | target_query |