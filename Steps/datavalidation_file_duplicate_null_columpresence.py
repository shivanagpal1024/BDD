import os
import pandas as pd
from behave import given
from behave import then
from Utilities.db_utilities import database_connect
from Utilities.excel_utilities import work_with_excel
from Config._test_config import browser

# use_step_matcher("re")

dbc = database_connect()
excel_data = work_with_excel()

root_dir = os.path.dirname(os.path.abspath(__file__))
print(root_dir)
par_dir = os.path.dirname(root_dir)
print("-------------------------")
print(par_dir)
input_path = par_dir + "\\Input"
output_path = par_dir + "\\Output"
source_path = par_dir + "\\Testdata"
out_file = output_path + "\\datavalidation_file_duplicate_null_columpresence.xlsx"


@given(u'The source data in file {file_name} with  {key} and {tc_id}')
def read_data_from_source_file(context, file_name, key, tc_id):
    context.file_name = file_name
    context.key = key
    context.tc_id = tc_id


@then("validate that certain columns present in the given order {column_presence}")
def verify_column_presence_order(context, column_presence):
    context.column_presence = column_presence.strip()
    column_presence_list = context.column_presence.split(",")
    in_file = input_path + "\\" + context.file_name
    try:
        df_source = pd.read_csv(in_file, usecols=column_presence_list)
        browser.update_step("Verify column presence", "All columns should  present" + str(column_presence_list),
                            "All columns are present " + str(column_presence_list), True)

        col_list_from_df = df_source.columns.to_list()
        if column_presence_list == col_list_from_df:
            browser.update_step("Verify column presence and order",
                                "Expected column order  = " + str(column_presence_list),
                                "Actual column order  = " + str(col_list_from_df), True)

        else:
            browser.update_step("Verify column presence and order",
                                "Expected column order  = " + str(column_presence_list),
                                "Actual column order  = " + str(col_list_from_df), False)
    except ValueError as e:
        ex = str(e)
        ex_messages = ex.split(",")
        browser.update_step("Columns presence check",
                            "All columns should be present in the file ",
                            "columns  did not present in the file " + str(ex_messages[1]), False)


@then("validate that certain  columns does not have duplicate values {duplicate_columns}")
def verify_duplicate_check(context, duplicate_columns):
    dflist = []
    context.duplicate_columns = duplicate_columns
    duplicate_columns_list = context.duplicate_columns.split(",")
    in_file = input_path + "\\" + context.file_name
    try:
        df_source = pd.read_csv(in_file, usecols=duplicate_columns_list)

        for col in duplicate_columns_list:
            df_tmp = df_source.groupby(col).size().reset_index(name='counts')
            df_tmp = df_tmp[df_tmp.counts > 1]
            df_tmp.reset_index(drop=True, inplace=True)
            dflist.append(df_tmp)

        dfcombine = pd.concat(dflist, axis=1)

        if os.path.exists(out_file):
            writer = pd.ExcelWriter(out_file, mode='a', engine='openpyxl', if_sheet_exists='new')
        else:
            writer = pd.ExcelWriter(out_file, mode='w')

        if len(dfcombine) > 0:
            dfcombine.to_excel(writer, sheet_name=context.tc_id + "-" + "DuplicateCheck", index=False)
            writer.save()
            browser.update_step("Find duplicates for the columns  = " + str(duplicate_columns_list),
                                "Data should not have duplicate values",
                                "Duplicate content found, please check " + out_file + " file for more details", False)
        else:
            browser.update_step("Find duplicates for the columns  = " + str(duplicate_columns_list),
                                "Data should not have duplicate values",
                                "Duplicate content not found", True)

    except ValueError as e:
        ex = str(e)
        ex_messages = ex.split(",")
        browser.update_step("Columns presence check",
                            "All columns should be present in the file ",
                            "columns  did not present in the file " + str(ex_messages[1]), False)


@then("validate that certain columns does not have null values {null_columns}")
def verify_null_check(context, null_columns):
    nul_found_col_list = []
    context.null_columns = null_columns
    null_columns_list = context.null_columns.split(",")
    in_file = input_path + "\\" + context.file_name
    try:
        df_source = pd.read_csv(in_file, usecols=null_columns_list)
        for col in null_columns_list:
            dfnulls = df_source[(df_source[col].isnull()) | (df_source[col] == '') | (df_source[col] == 'NaN')]
            if len(dfnulls) > 0:
                nul_found_col_list.append(col)

        if len(nul_found_col_list) > 0:
            browser.update_step("Find Null values for the columns  = " + str(null_columns_list),
                                "Data should not have Null values",
                                "Null values found in " + str(nul_found_col_list), False)

        else:
            browser.update_step("Find Null values for the columns  = " + str(null_columns_list),
                                "Data should not have Null values",
                                "Null values not found inn " + str(null_columns_list), True)
    except ValueError as e:
        ex = str(e)
        ex_messages = ex.split(",")
        browser.update_step("Unable to read the data from CSV due to" + str(ex_messages[1]),
                            "Data should be populated in dataframe", "Data did not populated in dataframe", False)
