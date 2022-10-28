@count_validation_file_snow
Feature: Validation of records count in file to snowflake

Scenario Outline: Validate the count of records for <tc_id>
    Given the source response from file <file_name>
    Then get the target response from snowflake using <target_query>
    Then validate the record count for <tc_id>
    Examples:
      | tc_id  | target_query | file_name |
