@metadata_check_snowflake
Feature: Table's metadata validation in snowflake by comparing input excel

Scenario:  Verify the metadata information
    Given the metadata information for source
    When read the input excel and merge all the source information
    When get the metadata information from database
    Then validate the snowflake response with input excel information