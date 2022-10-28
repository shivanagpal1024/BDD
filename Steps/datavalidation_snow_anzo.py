from behave import then
from Utilities.db_utilities import database_connect
from Utilities.anzo_utility.snow_anzo_result_mapping import AnzoTransformMapping
from Utilities.excel_utility.write_excel_df import WriteExcel
import os
import sys
from Config._test_config import browser

dbc = database_connect()
snm = AnzoTransformMapping()
wex = WriteExcel()

snow_file = "datavalidation_snow_anzo_snowResp.xlsx"
anzo_file = "datavalidation_snow_anzo_anzoResp.xlsx"
out_file = "datavalidation_snow_anzo_query_output.xlsx"

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


@then('get the response from anzo using {class_name} {usr_id} {usr_table_cols} and {predicate_cols}')
def response_from_anzo(context, class_name, usr_id, usr_table_cols, predicate_cols):
    try:
        if len(sys.argv) > 1:
            target_env = context.config.userdata['environment']
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")
        context.class_name = class_name

        user_list = str(usr_id).split(",")
        usr_id_list = list(user_list)

        table_cols = str(usr_table_cols).split(",")
        usr_table_cols_list = list(table_cols)

        pred_cols = str(predicate_cols).split(",")
        predicate_cols_list = list(pred_cols)

        context.anzo_response = snm.anzo_snow_mapping(class_name, usr_id_list, usr_table_cols_list, predicate_cols_list, target_env)

        browser.update_step("Get the anzo response", "Anzo response returned",
                            "Anzo response returned", True)

    except Exception as e:
        browser.update_step("Get the anzo response", "Anzo response returned",
                            str(e), False)
        raise Exception("Not able to get the Anzo the response")


@then('validate the anzo and snow response using and {query} for {tc_id}')
def validate_response(context, query, tc_id):
    try:
        if context.source_response.empty:
            browser.update_step("Response Validation",
                                "Snowflake response is valid",
                                "The Snowflake response has empty result set", False)
        elif context.anzo_response.empty:
            browser.update_step("Response Validation",
                                "Anzo response is valid",
                                "The ANZO response has empty result set", False)
        elif context.source_response.empty and context.anzo_response.empty:
            browser.update_step("Response Validation",
                                "Snowflake and Anzo response are valid",
                                "The Snowflake and ANZO response has empty result set", False)
        else:
            wex.write_excel("Output", snow_file, tc_id, context.source_response)
            wex.write_excel("Output", anzo_file, tc_id, context.anzo_response)
            anzo_schema = snm.pandas_to_spark(context.anzo_response)
            anzo_df = context.spark.createDataFrame(context.anzo_response, anzo_schema)
            anzo_df.createOrReplaceTempView("anzo_data")
            snow_schema = snm.pandas_to_spark(context.source_response)
            snow_df = context.spark.createDataFrame(context.source_response, snow_schema)
            snow_df.createOrReplaceTempView("snow_data")
            final_df = context.spark.sql(query)
            final_df.show()
            if final_df.count() == 0:
                browser.update_step("Response Validation",
                                    "Spark query should return empty result",
                                    "Spark query returned empty result", True)
            else:
                f_df = final_df.toPandas()
                wex.write_excel("Output", out_file, tc_id, f_df)
                browser.update_step("Response Validation",
                                    "Spark query should return empty result",
                                    "Spark query returned some records,check output folder for response", False)

    except Exception as e:
        browser.update_step("Response validation", "Spark query should return empty result",
                            str(e), False)
