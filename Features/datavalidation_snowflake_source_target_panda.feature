@datavalidation_snowflake_source_target_panda
Feature: Validation of source to target table mapping using pandas lib

Scenario Outline: Validate the source to target table mapping for <tc_id>
    Given the source response from snowflake using <source_query>
    Then get the target response from snowflake using <target_query>
    Then validate that the source and target response is valid
    Then sort the response using given key <source_key>
    Then sort the target response using given target_key <target_key>
    Then compare the source and target response and get the differences for <tc_id>
    Examples:
      | tc_id | source_query | source_key | target_query | target_key |