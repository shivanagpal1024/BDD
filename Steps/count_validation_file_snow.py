import os
import pandas as pd
from behave import given
from behave import then
from Config._test_config import browser
from Utilities.excel_utilities import work_with_excel

excel_data = work_with_excel()

root_dir = os.path.dirname(os.path.abspath(__file__))
# root_dir = WORKING_DIRECTORY
par_dir = os.path.dirname(root_dir)
input_path = par_dir + "\\Input"
output_path = par_dir + "\\Output"
source_path = par_dir + "\\Testdata"
out_file = output_path + "\\count_validation_file_snow_output.xlsx"


@given('the source response from file {file_name}')
def snowflake_read_source(context, file_name):
    context.source_file = file_name

    in_file = input_path + "\\" + file_name
    if os.path.exists(in_file):
        try:
            df_source = pd.read_csv(in_file, sep='|')
            context.source_response = len(df_source)
        except Exception:
            raise Exception(
                "Please check the query. Source and Target responses are having different column names or their count "
                "mismatch")

    else:
        raise Exception("Input data file does not exists")

@then('validate the record count for {tc_id}')
def response_validation(context, tc_id):
    try:
        context.source_count = str(context.source_response)
        context.target_count = (context.target_response[context.target_response.columns.values[0]]).to_string(
            index=False)
        data = [[tc_id, context.source_file, context.source_count, context.target_query, context.target_count]]
        df = pd.DataFrame(data, columns=['tc_id', 'source_file', 'source_response', 'target_query',
                                                 'target_response'])
        if not os.path.exists(out_file):
            df.to_csv(out_file, index=False)
        else:
            df.to_csv(out_file, mode='a', header=False, index=False)

        if context.source_count == "0" and context.target_count == "0":
            browser.update_step("Response validation",
                                "The source and Target response count should are equal and 0",
                                "Source and Target count = 0", True)
        elif context.source_count == context.target_count:
            browser.update_step("Response validation",
                                "The source and target response should be equal",
                                "Source count: " + context.source_count + " target count: " + context.target_count + " :: Counts are equal",
                                True)
        else:
            browser.update_step("Response validation",
                                "The source and target response should be equal",
                                "source count: " + context.source_count + " target count: " + context.target_count + " :: counts are not equal",
                                False)
    except Exception as e:
        browser.update_step("Response validation", "The source and target response should be equal",
                            str(e), False)