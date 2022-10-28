from behave import *
from pages.ui_pages.pg_datasets_validation import datasets
from pages.ui_pages.pg_dataiku_login import login
from pages.ui_pages.pg_dataiku_home import home
from Config._app_config import AppConfig
from Utilities.excel import Excel_Read
from Utilities.excel_utility.read_excel_data import read_excel
import time
import pandas as pd

obj_login = login()
obj_home = home()
obj_dataset=datasets()
excel_obj = Excel_Read()
excel_data = read_excel()


@given('User Launch browser with application url and login with valid credentials')
def launch_app_url(context):
    url = excel_data.get_app_url()
    obj_login.launch_url(url)
    obj_login.enter_user_name(AppConfig.DATAIKU_UNAME)


@when(u'User Search for project "{testfile}" "{testcase_name}" and "{sheet_name}"')
def search_project(context, testfile, testcase_name, sheet_name):
    obj_home.search_project("TestData", testcase_name, "DataIKUQA", "")
    obj_home.click_project()
    obj_home.click_got_it()


@then(u'select Dataset for given "{testcase_name}" "{file_name}"and "{sheet_name}" validate')
def verify_connection_data(context, testcase_name, file_name, sheet_name):
    obj_dataset.select_menu()
    obj_dataset.read_datasets(file_name,sheet_name)

@then(u'select Global Variables for given "{testcase_name}" "{file_name}"and "{sheet_name}" validate')
def verify_global_var_data(context, testcase_name, file_name, sheet_name):
    obj_dataset.select_variables_menu()
    global_variables = obj_dataset.read_global_variables()
    obj_dataset.compare_global_variables_with_mappingsheet(file_name, sheet_name)

@Then('Read project and Dataset from "{excel_file_name}" "{sheetName}" and validate connection parameters with global variables')
def step_impl(self, excel_file_name, sheetName):
    obj_dataset.select_variables_menu()
    global_variables = obj_dataset.read_global_variables()
    obj_dataset.select_menu()
    time.sleep(2)
    obj_dataset.compare_global_variables_with_datasetparameters(global_variables,excel_file_name, sheetName)

