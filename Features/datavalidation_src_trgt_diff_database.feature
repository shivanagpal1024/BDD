@datavalidation_src_trgt_diff_database
Feature: Validation of source to target table mapping using pandas lib

Scenario Outline: Validate the source and target table for <tc_id>
    Given snowflake response using query <source_query> database <source_database> role <src_db_role>
    Then get the snowflake response using query <target_query> database <target_database> role <tgt_db_role>
    Then validate that the source and target response is valid
    Then sort the response using given key <source_key>
    Then sort the target response using given target_key <target_key>
    Then compare the source and target response and get the differences for <tc_id>
    Examples:
        | tc_id | source_query | source_database | src_db_role | target_query | target_database | tgt_db_role | source_key | target_key |