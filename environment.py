from Utilities.report_utility.reportCss import *
from Utilities.file_handles.fileobjects import *
import Utilities.config._config as config
from Config._app_config import AppConfig
import Utilities.ui_utility.ui as Ui
from Utilities.report_utility.TestReports import ReportsFinal
import pandas as pd
import os

_report = Report()
reports_final = ReportsFinal()

root_dir = os.path.dirname(os.path.abspath(__file__))
testdata_path = root_dir + "\Testdata"
output_path = root_dir + "\Output"


def before_all(context):
    for file in os.listdir(output_path):
        os.remove(os.path.join(output_path, file))


def before_feature(context, feature):
    if 'count_validation_snow_anzo' in feature.tags:
        path_to_file = testdata_path + "\count_validation_snow_anzo.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if sc.name == 'Compare the count of records for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'datavalidation_snow_anzo' in feature.tags:
        path_to_file = testdata_path + "\datavalidation_snow_anzo.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(sc.examples[0] for sc in feature.scenarios if
                       sc.name == 'Data validation between Snowflake and Anzo for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

        context.execute_steps('''
                    Given the Spark initialization
                ''')

    elif 'count_validation_snowflake' in feature.tags:

        path_to_file = testdata_path + "\count_validation_snowflake.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if sc.name == 'Validate the count of records for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'count_validation_file_snow' in feature.tags:

        path_to_file = testdata_path + "\\count_validation_file_snow.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if sc.name == 'Validate the count of records for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'duplicate_check_snowflake' in feature.tags:

        path_to_file = testdata_path + "\duplicate_check_snowflake.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if sc.name == 'Verify the duplicate check for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)


    elif 'null_check_snowflake' in feature.tags:

        path_to_file = testdata_path + "\snowflake_null_check.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(sc.examples[0] for sc in feature.scenarios if sc.name == 'Verify the null check for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'datavalidation_snowflake_minus' in feature.tags:

        path_to_file = testdata_path + "\datavalidation_snowflake_minus.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(sc.examples[0] for sc in feature.scenarios if
                       sc.name == 'Validate that the columns are straight move from source table for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'audit_check_snowflake' in feature.tags:

        path_to_file = testdata_path + "\Audit_table_validation_snow.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if sc.name == 'Verify the details in audit table for <TC_ID>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)


    elif 'datavalidation_snowflake_source_target_panda' in feature.tags:

        path_to_file = testdata_path + "\\datavalidation_snowflake_source_target_panda.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(sc.examples[0] for sc in feature.scenarios if
                       sc.name == 'Validate the source to target table mapping for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'datavalidation_file_snowflake' in feature.tags:

        path_to_file = testdata_path + "\datavalidation_file_snow_panda.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if sc.name == 'compare  the data present in db table against the file  <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'datavalidation_src_trgt_diff_database' in feature.tags:

        path_to_file = testdata_path + "\datavalidation_src_trgt_diff_database.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if sc.name == 'Validate the source and target table for <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'audit_log' in feature.tags:
        path = str(AppConfig.WORKING_DIRECTORY) + "//Testdata//td_ui//audit_log_validation.xlsx"
        df = pd.read_excel(path)
        example = next(
            sc.examples[0] for sc in feature.scenarios if
            sc.name == 'Verify Scenario Execution Time with Snowflake Database - <TC_ID>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)

    elif 'db_duplicate_null_col_validation' in feature.tags:
        print("in env file...............................")
        path_to_file = testdata_path + "\\DB_validation.xlsx"
        df = pd.read_excel(path_to_file)
        example = next(
            sc.examples[0] for sc in feature.scenarios if
            sc.name == 'validate  the data present in db table for duplicates, null values and column presence <tc_id>')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)



def add_testcase_result(current_tc_info, tc_time_info):
    print("tc_time_info" + "*" * 50)
    print(tc_time_info)
    testcase_info = [current_tc_info, tc_time_info]
    _report.genrate_report(testcase_info, Ui.listVal)
    Ui.listVal.clear()


def before_scenario(context, scenario):
    start_time = reports_final.start()
    mod_start_time = reports_final.module_start()
    return start_time, mod_start_time


def after_scenario(context, scenario):
    close_time = reports_final.close_time()
    name = context.feature.filename
    name = name.split('.', 1)[0]
    name = name.split("/")[1]
    tc_time_info = {'Date': get_current_time_zone_timestamp('Asia/Kolkata'),
                    'Execution_Time': close_time,
                    'Executed_On': config.BROWSER_TYPE}

    current_tc_info = {'module_name': str(scenario.name),
                       'VSTS_ID': "Testing_ID",
                       'TestCase_Name': str(name)}
    add_testcase_result(current_tc_info, tc_time_info)
    # mod_close_time = reports_final.module_close(scenario.name)


def after_feature(context, feature):
    name = context.feature.filename
    name = name.split('.', 1)[0]
    name = name.split("/")[1]
    scenario_name = feature.scenarios
    mod_close_time = reports_final.module_close(feature.name)

    if 'datavalidation_snow_anzo' in feature.tags:
        context.execute_steps('''
                    Then stop the spark session
                ''')
