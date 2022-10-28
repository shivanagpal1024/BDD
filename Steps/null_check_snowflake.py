from behave import then
from Utilities.db_utilities import database_connect
from Utilities.excel_utility.write_excel_df import WriteExcel
from Config._test_config import browser

dbc = database_connect()
exc = WriteExcel()


@then('validate that the response has any records for {tc_id}')
def validate_the_nulls(context, tc_id):
    try:
        if len(context.snow_response) == 0:
            browser.update_step("Response validation",
                                "The data base response should have empty result set",
                                "Records not found with null values", True)
        else:
            exc.write_excel("Output", "snowflake_null_check_output.xlsx", tc_id, context.snow_response)
            browser.update_step("Response validation",
                                "The data base response should have empty result set",
                                "No of records returned : " + str(
                                    len(context.snow_response)) + ". sample records written in "
                                                                  "output folder", False)
    except Exception as e:
        browser.update_step("Response validation", "The data base response should have empty result set",
                            str(e), False)
