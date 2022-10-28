from behave import given
from behave import then
from Utilities.db_utilities import database_connect
import pandas as pd
import os
from Utilities.config._config import WORKING_DIRECTORY
from Config._test_config import browser
import sys

dbc = database_connect()

root_dir = WORKING_DIRECTORY
out_file = os.path.join(root_dir, "Output", "count_validation_snowflake.csv")


@given('the source response from snowflake using {source_query}')
def snowflake_source_response(context, source_query):
    try:
        if len(sys.argv) > 1:
            context.source_env = context.config.userdata['source_env']
            context.target_env = context.config.userdata['environment']
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")
        context.source_query = source_query
        dbc.db_env(context.source_env)
        context.source_response = dbc.snowflake_query_execution(context.source_query)
        browser.update_step("Get the source response from snowflake",
                            "Get the valid snowflake response",
                            "The response returned from snowflake", True)
    except Exception as e:
        browser.update_step("Get the source response from snowflake",
                            "Get the valid snowflake response",
                            str(e), False)
        raise Exception("The source response not returned")


@then('get the target response from snowflake using {target_query}')
def snowflake_target_response(context, target_query):
    try:
        if len(sys.argv) > 1:
            context.target_env = context.config.userdata['environment']
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")
        context.target_query = target_query
        dbc.db_env(context.target_env)
        context.target_response = dbc.snowflake_query_execution(context.target_query)
        browser.update_step("Get the target response from snowflake",
                            "Get the valid snowflake response",
                            "The response returned from snowflake", True)
    except Exception as e:
        browser.update_step("Get the target response from snowflake",
                            "Get the valid snowflake response",
                            str(e), False)
        raise Exception("The target response not returned")


@then('validate the records count for {tc_id}')
def response_validation(context, tc_id):
    try:
        if context.source_response.empty and context.target_response.empty:
            browser.update_step("Response validation",
                                "Source and Target response should not be empty",
                                "Source and Target response has no records", False)
        elif context.source_response.empty:
            browser.update_step("Response validation",
                                "Source and Target response should not be empty",
                                "Source response has no records", False)
        elif context.target_response.empty:
            browser.update_step("Response validation",
                                "Source and Target response should not be empty"
                                "Target response has no records", False)
        else:
            if context.source_response.shape[1] and context.target_response.shape[1] == 1:
                context.source_count = (context.source_response[context.source_response.columns.values[0]]).to_string(index=False)
                context.target_count = (context.target_response[context.target_response.columns.values[0]]).to_string(index=False)
                data = [[tc_id, context.source_query, context.source_count, context.target_query, context.target_count]]
                df = pd.DataFrame(data, columns=['tc_id', 'source_query', 'source_response', 'target_query', 'target_response'])
                if not os.path.exists(out_file):
                    df.to_csv(out_file, index=False)
                else:
                    df.to_csv(out_file, mode='a', header=False, index=False)
            else:
                browser.update_step("Response validation",
                                    "The response should have only one column as count",
                                    "The response has more than one columns", False)

            if context.source_count == "0" and context.target_count == "0":
                browser.update_step("Response validation",
                                    "The source and Target response count should are equal and 0",
                                    "Source and Target count = 0", True)
            elif context.source_response.equals(context.target_response):
                browser.update_step("Response validation",
                                    "The source and target response should be equal",
                                    "Source count: "+context.source_count+" target count: "+context.target_count+" :: Counts are equal", True)
            else:
                browser.update_step("Response validation",
                                    "The source and target response should be equal",
                                    "source count: "+context.source_count+" target count: "+context.target_count+" :: counts are not equal", False)

    except Exception as e:
        browser.update_step("Response validation", "The source and target response should be equal",
                            str(e), False)
