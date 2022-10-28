from behave import then
from Utilities.db_utilities import database_connect
from Utilities.excel_utility.compare_find_diff import CompareAndFindDifferences
from Utilities.common_utilities.common_utility import CommonUtilities
from Config._test_config import browser

dbc = database_connect()
cad = CompareAndFindDifferences()
cui = CommonUtilities()

out_file = "data_validation_snowflake_panda_diff.xlsx"


@then('validate that the source and target response is valid')
def validate_source_target_response(context):
    try:
        if context.source_response.empty and context.target_response.empty:
            browser.update_step("Validate the source and target response",
                                "source and target response are valid",
                                "The both source and target response has empty result set", False)
            raise Exception("The both source and target response has empty result set")
        elif context.source_response.empty:
            browser.update_step("Validate the source response",
                                "Source response is valid",
                                "The source response has empty result set", False)
            raise Exception("The source response has empty result set")
        elif context.target_response.empty:
            browser.update_step("Validate the target response",
                                "Target response is valid",
                                "The target response has empty result set", False)
            raise Exception("Please check the query. The target response has empty result set")
        elif context.source_response.shape[1] != context.target_response.shape[1]:
            browser.update_step("Validate the source and target response",
                                "Source and Target response has same number of columns",
                                "Source and Target responses are having different number of columns", False)
            raise Exception("Source and Target responses are having different number of columns")
        else:
            s_list = context.source_response.columns.tolist()
            t_list = context.target_response.columns.tolist()
            s_list.sort()
            t_list.sort()
            if s_list != t_list:
                browser.update_step("Validate the source and target response",
                                    "Source and Target response has same column names",
                                    "Source and Target responses are having different column names", False)
                raise Exception("Source and Target responses are having different column names")

    except Exception as e:
        browser.update_step("Validate the source and target response",
                            "Source and Target response should be valid",
                            str(e), False)
        raise Exception("Source and Target response not valid")


@then('sort the response using given key {source_key}')
def sort_source_response(context, source_key):
    try:
        context.source_key = str(source_key).lower().replace(' ', '')
        context.source_response = cui.sort_snowflake_response(context.source_response, context.source_key)
        src_key_list = context.source_key.split(",")
        context.source_key_list = list(src_key_list)
        browser.update_step("Sort the source response", "Sorted the source response",
                            "Sorted the source response", True)
    except Exception as e:
        browser.update_step("Sort the source response", "Sorted the source response",
                            str(e), False)
        raise Exception("Not able to sort the source response")


@then('sort the target response using given target_key {target_key}')
def sort_target_response(context, target_key):
    try:
        context.target_response = cui.sort_snowflake_response(context.target_response, target_key)
        browser.update_step("Sort the target response", "Sorted the target response",
                            "Sorted the target response", True)
    except Exception as e:
        browser.update_step("Sort the target response", "Sorted the target response",
                            str(e), False)
        raise Exception("Not able to sort the target response")


@then('compare the source and target response and get the differences for {tc_id}')
def validate_response(context, tc_id):
    try:
        if context.source_response.equals(context.target_response):
            browser.update_step("Response validation", "Source and Target responses are matched",
                                "Source and Target responses are matched", True)
        else:
            if context.source_key != 'no':
                cad.find_diff(context.source_response, context.target_response, context.source_key_list, tc_id, out_file)
                browser.update_step("Response validation", "Source and Target responses are matched",
                                    "Source and Target responses are not matched", False)
            elif context.source_key == 'no':
                cad.find_diff_concat(context.source_response, context.target_response, tc_id, out_file)
                browser.update_step("Response validation", "Source and Target responses are matched",
                                    "Source and Target responses are not matched", False)

    except Exception as e:
        browser.update_step("SResponse validation", "Source and Target responses are matched",
                            str(e), False)