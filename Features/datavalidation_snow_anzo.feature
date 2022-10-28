@datavalidation_snow_anzo
Feature: Data validation between Snowflake and Anzo

  Scenario Outline: Data validation between Snowflake and Anzo for <tc_id>
    Given the source response from snowflake using <source_query>
    Then get the response from anzo using <class_name> <usr_id> <usr_table_cols> and <predicate_cols>
    Then validate the anzo and snow response using and <query> for <tc_id>
    Examples:
      | tc_id | class_name | usr_id | source_query | usr_table_cols | predicate_cols | query |