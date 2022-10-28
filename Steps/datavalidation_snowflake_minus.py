from behave import given
from behave import then
from Utilities.db_utilities import database_connect
from Utilities.excel_utility.write_excel_df import WriteExcel
from Config._test_config import browser
import sys

dbc = database_connect()
exc = WriteExcel()


@given('the Snowflake response with valid {snow_query}')
def snowflake_source_response(context, snow_query):
    try:
        if len(sys.argv) > 1:
            target_env = context.config.userdata['environment']
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")
        context.snow_query = snow_query
        dbc.db_env(target_env)
        context.snow_response = dbc.snowflake_query_execution(context.snow_query)
        browser.update_step("Get the snowflake response for given query",
                            "Get the valid snowflake response",
                            "The response returned from snowflake", True)
    except Exception as e:
        browser.update_step("Get the snowflake response for given query",
                            "Get the valid snowflake response",
                            "Not able to get the response from snowflake " + str(e), False)
        raise Exception("Not able to get the response")


@then('validate that the response has no differences for {tc_id}')
def validate_response_no_difference(context, tc_id):
    try:
        if len(context.snow_response) == 0:
            browser.update_step("Response validation",
                                "The data base response should have empty result set",
                                "Records not found with differences", True)
        else:
            exc.write_excel("Output", "datavalidation_snowflake_minus_output.xlsx", tc_id, context.snow_response)
            browser.update_step("Response validation",
                                "The data base response should have empty result set",
                                "No of records returned : " + str(
                                    len(context.snow_response)) + ". sample records written in "
                                                                  "output folder", False)

    except Exception as e:
        browser.update_step("Response validation", "The data base response should have empty result set",
                            str(e), False)
