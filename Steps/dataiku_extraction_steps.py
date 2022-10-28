from behave import *
from pages.ui_pages.pg_datasets_validation import datasets
from pages.ui_pages.pg_dataiku_login import login
from pages.ui_pages.pg_dataiku_home import home
from Config._test_config import browser
from Utilities.excel import Excel_Read
from Utilities.excel_utility.read_excel_data import read_excel
import time
import pandas as pd

obj_login = login()
obj_home = home()
obj_dataset=datasets()
excel_obj = Excel_Read()
excel_data = read_excel()

@when(u'User Search for given project "{testcase_name}" and "{sheet_name}"')
def search_project(context, testcase_name, sheet_name):
    obj_home.search_project("TestData", testcase_name, "DataIKUDEV", "")
    obj_home.click_project()
    obj_home.click_got_it()



@then('Read the "{ProjectName}" Config data and write to outputfile')
def get_datasets(context, ProjectName):
    obj_dataset.select_menu()
    obj_dataset. get_connection_params(ProjectName)
    browser.tear_down()