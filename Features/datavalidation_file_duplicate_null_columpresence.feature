@db_duplicate_null_col_validation
Feature: Validation of duplicates, null and columns in db

Scenario Outline:validate  the data present in db table for duplicates, null values and column presence <tc_id>
   Given The source data in file <file_name> with  <key> and <tc_id>
   Then validate that certain  columns does not have duplicate values <duplicate_columns>
   Then validate that certain columns does not have null values <null_columns>
   Then validate that certain columns present in the given order  <column_presence>
   Examples:
      | tc_id  | duplicate_columns | null_columns | column_presence | file_name| key |