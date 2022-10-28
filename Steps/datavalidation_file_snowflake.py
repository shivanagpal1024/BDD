import os
import pandas as pd
from behave import given
from behave import then
from Utilities.excel_utilities import work_with_excel

excel_data = work_with_excel()

root_dir = os.path.dirname(os.path.abspath(__file__))
# root_dir = WORKING_DIRECTORY
par_dir = os.path.dirname(root_dir)
input_path = par_dir + "\\Input"
output_path = par_dir + "\\Output"
source_path = par_dir + "\\Testdata"
out_file = output_path + "\\datavalidation_file_snowflake_output.xlsx"


@given(u'Given the source response in file {file_name} and {file_column} and {keys}')
def snowflake_read_source(context, file_name, file_column, keys):
    context.source_file = file_name
    context.file_column = file_column
    context.keys = keys.split(",")

    if file_column == '*':
        use_cols = None
    else:
        use_cols = file_column.split(",")

    context.use_cols = use_cols
    in_file = input_path + "\\" + file_name
    if os.path.exists(in_file):
        try:
            df_source = pd.read_csv(in_file, sep='|', usecols=use_cols)
            context.source_response = df_source
        except Exception:
            raise Exception(
                "Please check the query. Source and Target responses are having different column names or their count "
                "mismatch")

    else:
        raise Exception("Input data file does not exists")


@then('user can compare the data in the database table against file {tc_id}')
def response_validation(context, tc_id):

    if len(context.target_response) >= len(context.source_response):
        compare_volume = len(context.target_response)
    else:
        compare_volume = len(context.source_response)

    context.target_response = context.target_response.astype(str)
    context.source_response = context.source_response.astype(str)

    result = excel_data.compare_data(context.source_response, context.target_response, 'Source ', 'Target',
                                     context.keys)
    excel_data.prepare_report(result, out_file, tc_id, compare_volume)
