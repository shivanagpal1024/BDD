from behave import given, then, when
from Utilities.excel import Excel_Read
from Utilities.excel_utility.read_excel_data import read_excel
from pages.ui_pages.pg_anzo_datalayers import datalayers_metadata
from pages.ui_pages.pg_anzo_login import anzo_login
from pages.ui_pages.pg_anzo_home import anzo_home
from pages.ui_pages.pg_graphmarts import graphmarts
from Config._app_config import AppConfig
import os
import time

obj_login = anzo_login()
obj_login_anzo=anzo_login()
obj_excel = read_excel()
excel_data = Excel_Read()
obj_home = anzo_home()
obj_graphmarts = graphmarts()
obj_anzo_datalayers = datalayers_metadata()


@given('User Launch the browser and navigates to application url')
def launch_app_url(context):
    url = obj_excel.get_app_url()
    obj_login.launch_anzo_url(url)


@when('User enter valid credentials and logged into application')
def enter_credentials(context):
    obj_login.enter_user_name(AppConfig.ANZO_UNAME)
    obj_login.enter_password(AppConfig.ANZO_PASSWORD)
    obj_login.click_login()

@when('User enters emailid and navigates to homepage')
def enter_emaiid(context):
    obj_login_anzo.enter_emailid()

@then('User navigates to graphmarts and perform search')
def search_graphmart(context):
    obj_home.select_menu("Blend")
    obj_home.select_menu("Graphmarts")
    obj_graphmarts.click_graphmarts("NGE_KG_Graphmart")

@then('"{testcase_name}" initiation using the "{sheet_name}" and create the dashboard by selecting network navigator')
def create_dashboard(context, testcase_name, sheet_name):
    data = excel_data.read_test_data_by_test_case_name("TestData", testcase_name, sheet_name)
    title = data.get("DashBoardName")
    obj_graphmarts.create_dashboard()
    obj_graphmarts.click_navigator()
    obj_graphmarts.enter_title(title)
    obj_graphmarts.click_finish()

@then('click on Find Data and search for HCP class')
def compare_class_properties(context):
    obj_graphmarts.click_find_data()
    obj_graphmarts.search_hcp("https://www.nvs.com/HCP/4623028")
    obj_graphmarts.select_anzo()
    obj_graphmarts.select_class_bubble()
    obj_graphmarts.get_properties_data()
    obj_graphmarts.read_anzo_data()
    obj_graphmarts.compare_and_generate_excel_properties()

@then('User navigates to Datalayers and perform calls')
def data_layers(context):
    obj_anzo_datalayers.datalayers()

@then('validate Metadata between STTM "{file_name}" "{sheet_name}" using the "{column_name}" and configuration data in ANZO')
def transformation_data(context, file_name, sheet_name, column_name):
    data = excel_data.read_test_data_by_sheet_name_and_column_name(file_name, sheet_name, column_name)
    obj_anzo_datalayers.transformation_data(data)
