@datavalidation_file_snowflake
Feature: Validation of data in db against data in the file

Scenario Outline:compare  the data present in db table against the file  <tc_id>
   Given  Given the source response in file <file_name> and <file_column> and <keys>
   Then get the target response from snowflake using <target_query>
   Then validate that the source and target response is valid
   Then user can compare the data in the database table against file <tc_id>
   Examples:
      | tc_id  | target_query | file_name | file_column | keys |

