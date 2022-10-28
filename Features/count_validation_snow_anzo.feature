@count_validation_snow_anzo
Feature: Validation of records count against Snowflake and Anzo

  Scenario Outline: Compare the count of records for <tc_id>
    Given the source response from snowflake using <source_query>
    Then query the Anzo database with valid <anzo_query>
    Then compare the record counts are matching or not for <tc_id>
    Examples:
      | tc_id | source_query | anzo_query |