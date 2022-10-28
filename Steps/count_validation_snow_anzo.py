from behave import then
from Utilities.db_utilities import database_connect
from Config._test_config import browser
from Utilities.config._config import WORKING_DIRECTORY
import os
import pandas as pd
import sys

dbc = database_connect()

root_dir = WORKING_DIRECTORY
out_file = os.path.join(root_dir, "Output", "count_validation_snow_anzo.csv")


@then('query the Anzo database with valid {anzo_query}')
def execute_anzo_query(context, anzo_query):
    try:
        if len(sys.argv) > 1:
            target_env = context.config.userdata['environment']
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")
        context.anzo_query = anzo_query
        if target_env == 'qa':
            context.anzo_response = dbc.anzo_query_execution_qa(context.anzo_query)
        elif target_env == 'dev':
            context.anzo_response = dbc.anzo_query_execution_dev(context.anzo_query)
        elif target_env == 'prod':
            context.anzo_response = dbc.anzo_query_execution_prod(context.anzo_query)
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "Environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")

        browser.update_step("Get the Anzo response", "Anzo response returned",
                            "Anzo response returned", True)
    except Exception as e:
        browser.update_step("Get the Anzo response", "Anzo response returned",
                            str(e), False)
        raise Exception("Not able to get the anzo response")


@then('compare the record counts are matching or not for {tc_id}')
def validate_response(context, tc_id):
    try:
        if context.source_response.empty and context.anzo_response.empty:
            browser.update_step("Response validation", "snowflake and Anzo response should eb valid",
                                "The snowflake and Anzo response has empty result set", False)
        elif context.source_response.empty:
            browser.update_step("Response validation", "snowflake response should eb valid",
                                "The snowflake response has empty result set", False)
        elif context.anzo_response.empty:
            browser.update_step("Response validation", "Anzo response should eb valid",
                                "The Anzo response has empty result set", False)
        else:
            if context.source_response.shape[1] and context.anzo_response.shape[1] == 1:
                context.snow_count = (context.source_response[context.source_response.columns.values[0]]).to_string(index=False)
                context.anzo_count = (context.anzo_response[context.anzo_response.columns.values[0]]).to_string(index=False)
                data = [[tc_id, context.source_query, context.snow_count, context.anzo_query, context.anzo_count]]
                df = pd.DataFrame(data,
                                  columns=['tc_id', 'source_query', 'source_response', 'target_query', 'target_response'])
                if not os.path.exists(out_file):
                    df.to_csv(out_file, index=False)
                else:
                    df.to_csv(out_file, mode='a', header=False, index=False)
            else:
                browser.update_step("Response validation",
                                    "The response should have only one column as count",
                                    "The response has more than one columns", False)

            if context.source_response.equals(context.anzo_response):
                browser.update_step("Response validation",
                                    "The source and target response should be equal",
                                    "Source count: " + context.snow_count + " target count: " + context.anzo_count + ":: Counts are equal",
                                    True)
            else:
                browser.update_step("Response validation",
                                    "The source and target response should be equal",
                                    "source count: " + context.snow_count + " target count: " + context.anzo_count + ":: counts are not equal",
                                    False)

    except Exception as e:
        browser.update_step("Response validation", "The source and target response should be equal",
                            str(e), False)
