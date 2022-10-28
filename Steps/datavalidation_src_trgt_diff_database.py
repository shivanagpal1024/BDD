from behave import given
from behave import then
from Utilities.db_utilities import database_connect
from Config._test_config import browser
import sys

dbc = database_connect()


@given('snowflake response using query {source_query} database {source_database} role {src_db_role}')
def snowflake_source_response_db(context, source_query, source_database, src_db_role):
    try:
        if len(sys.argv) > 1:
            context.source_env = context.config.userdata['source_env']
            context.target_env = context.config.userdata['environment']
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")
        context.source_query = source_query
        context.source_database = source_database
        context.src_db_role = src_db_role
        dbc.db_env_with_data(context.source_env, context.source_database, context.src_db_role)
        context.source_response = dbc.snowflake_query_execution(context.source_query)
        browser.update_step("Get the source response from snowflake",
                            "Get the valid snowflake response",
                            "The response returned from snowflake", True)
    except Exception as e:
        browser.update_step("Get the source response from snowflake",
                            "Get the valid snowflake response",
                            str(e), False)
        raise Exception("Not able get the source response")


@then('get the snowflake response using query {target_query} database {target_database} role {tgt_db_role}')
def snowflake_target_response_db(context, target_query, target_database, tgt_db_role):
    try:
        context.target_query = target_query
        context.target_database = target_database
        context.tgt_db_role = tgt_db_role
        dbc.db_env_with_data(context.target_env, context.target_database, context.tgt_db_role)
        context.target_response = dbc.snowflake_query_execution(context.target_query)
        browser.update_step("Get the target response from snowflake",
                            "Get the valid snowflake response",
                            "The response returned from snowflake", True)
    except Exception as e:
        browser.update_step("Get the target response from snowflake",
                            "Get the valid snowflake response",
                            str(e), False)
        raise Exception("Not able get the target response")
