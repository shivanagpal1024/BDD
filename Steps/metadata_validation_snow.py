from behave import given
from behave import then
from behave import when
from Utilities.db_utilities import database_connect
import pandas as pd
import openpyxl
from Utilities.config._config import WORKING_DIRECTORY
from Utilities.excel_utility.compare_find_diff import CompareAndFindDifferences
from Utilities.excel_utility.write_excel_df import WriteExcel
from Config._test_config import browser
import sys

dbc = database_connect()
cad = CompareAndFindDifferences()
exc = WriteExcel()

root_dir = WORKING_DIRECTORY


@given('the metadata information for source')
def get_excel_path(context):
    try:
        input_path = root_dir + "\\Testdata"
        context.input_file = input_path + "\\metadata_validation_snowflake.xlsx"
        context.source_file = "metadata_validation_source.xlsx"
        context.db_file = "metadata_validation_database.xlsx"
        context.diff_file = "metadata_validation_differences.xlsx"
        browser.update_step("Read the file path", "Files are present",
                            "Files are present", True)
    except Exception as e:
        browser.update_step("Read the file path", "Files are present",
                            str(e), False)
        raise Exception("Files are Not present")


@when('read the input excel and merge all the source information')
def merge_source_information(context):
    try:
        inp_excel = pd.ExcelFile(context.input_file)
        context.inp_df = pd.DataFrame()
        for sheet_name in inp_excel.sheet_names:
            df = pd.read_excel(inp_excel, sheet_name=sheet_name, usecols="C,D,E")
            context.inp_df = pd.concat([context.inp_df, df], axis=0, ignore_index=True)
            context.inp_df = context.inp_df.sort_values(['Target_Table', 'name']).reset_index(drop=True)
        browser.update_step("Read the input excel and merge all the source information", "Successfully read the input "
                                                                                         "information",
                            "Successfully read the input information", True)
    except Exception as e:
        browser.update_step("Read the input excel and merge all the source information",
                            "Not able to read the input information",
                            str(e), False)
        raise Exception("Not able to read the input information")


@when('get the metadata information from database')
def get_database_information(context):
    try:
        if len(sys.argv) > 1:
            target_env = context.config.userdata['environment']
        else:
            browser.update_step("Validate the environment variable", "Valid environment variable",
                                "environment variable is not in qa/dev/prod", False)
            raise Exception("Please mention the correct environment variable - qa/dev/prod")
        wb = openpyxl.load_workbook(context.input_file)
        sheets = wb.sheetnames
        context.db_df = pd.DataFrame()
        for sheet_name in sheets:
            sheet = wb[sheet_name]
            target_database = sheet["A2"].value
            target_schema = sheet["B2"].value
            target_table = sheet["C2"].value
            query = 'DESC TABLE "' + target_database + '"."' + target_schema + '"."' + target_table + '"'
            dbc.db_env(target_env)
            df1 = dbc.snowflake_query_execution(query)
            if df1.empty:
                browser.update_step("Get the metadata information from database",
                                    "Got the metadata information from database",
                                    "The response has empty result set", False)
                raise Exception("Check the query, the response has empty result set")
            else:
                df1 = df1.filter(["name", "type"])
                df1 = df1.assign(Target_Table=target_table)
                df1 = df1[['Target_Table', 'name', 'type']]
                context.db_df = pd.concat([context.db_df, df1], axis=0, ignore_index=True)
                context.db_df = context.db_df.sort_values(['Target_Table', 'name']).reset_index(drop=True)

        browser.update_step("Get the metadata information from database", "Got the metadata information from database",
                            "Got the metadata information from database", True)
    except Exception as e:
        browser.update_step("Get the metadata information from database",
                            "Not able to get the metadata information from database",
                            str(e), False)
        raise Exception("Not able to get the metadata information from database")


@then('validate the snowflake response with input excel information')
def validate_response(context):
    try:
        exc.write_excel("Output", context.source_file, "meta_data", context.inp_df)
        exc.write_excel("Output", context.db_file, "meta_data", context.db_df)
        if len(context.inp_df) != len(context.db_df):
            browser.update_step("Response Validation",
                                "Source and Target has same number of columns",
                                "The number of records/columns are mismatched between source and target", False)
        elif context.inp_df.equals(context.db_df):
            browser.update_step("Response Validation",
                                "Source and Target Metadata information matched",
                                "Meta data information matched", True)
        else:
            source_key_list = ['Target_Table', 'name']
            cad.find_diff(context.inp_df, context.db_df, source_key_list, "meta_data", context.diff_file)
            browser.update_step("Response Validation",
                                "Source and Target Metadata information matched",
                                "Meta data information not matched,check the Output folder for mismatches.", False)

    except Exception as e:
        browser.update_step("Response validation", "Source and Target Metadata information matched",
                            str(e), False)
