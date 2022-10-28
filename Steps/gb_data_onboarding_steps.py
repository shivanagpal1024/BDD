from behave import given, when, then
from pages.ui_pages.glassbox.pg_data_onboarding import data_onboard
from Config._app_config import AppConfig

obj_data_onboard = data_onboard()


@when("User go to the Data Onboard")
def add_data_feed(context):
    obj_data_onboard.click_data_onboarding()
    obj_data_onboard.click_add_source()
    obj_data_onboard.click_data_source()
    obj_data_onboard.select_data_provider("AMGEN")
    obj_data_onboard.select_dataset("AMGEN CALLS")
    obj_data_onboard.enter_business_name("UAT_TESTING")
    obj_data_onboard.click_source_type()
    obj_data_onboard.click_next()


@when("User Onboard the Data Objects")
def add_layer_config(context):
    obj_data_onboard.select_inbound_type("S3")
    obj_data_onboard.select_inbound_layer("NVS GLASSBOX S3 INBOUND")
    obj_data_onboard.select_inbound_path()
    obj_data_onboard.enter_inbound_path("proj/glassbox/roster/amgen/inbound/uat_test/[cd|%Y-%m-%d]")
    obj_data_onboard.select_landing_layer("NVS GLASSBOX S3")
    obj_data_onboard.select_landing_path()
    obj_data_onboard.enter_landing_path("udata/PH/COM/raw/USA/glassbox/inbound/uat_test")
    obj_data_onboard.select_staging_layer("STAGING INTERACTION")
    obj_data_onboard.select_archive_layer("NVS GLASSBOX S3 ARCHIVE")
    obj_data_onboard.select_archive_path()
    obj_data_onboard.enter_archive_path("udata/PH/COM/raw/USA/glassbox/archive/uat_test")
    obj_data_onboard.select_frequency("Adhoc")
    # obj_data_onboard.enter_arrival_time("12:30")
    obj_data_onboard.enter_file_pattern("SALES_UAT_TESTING_DAILY_[0-9].csv")
    obj_data_onboard.click_next()


@then("User Should be able to Onboard the Objects")
def verify_onboarding_objects(context):
    path = str(AppConfig.WORKING_DIRECTORY) + "\\Testdata\\td_ui\\UAT_TESTING_ACTIVITY_DAILY_[0-9].csv"
    obj_data_onboard.upload_file(path)
    obj_data_onboard.click_next()
    obj_data_onboard.select_target_table("UAT_TESTING_TABLE")
    obj_data_onboard.click_submit()


@when("User go to the Data Onboard for json")
def json_data_feed(context):
    obj_data_onboard.click_data_onboarding()
    obj_data_onboard.click_add_source()
    obj_data_onboard.click_data_source()
    obj_data_onboard.select_data_provider("AMGEN")
    obj_data_onboard.select_dataset("AMGEN CALLS")
    obj_data_onboard.enter_business_name("UAT_TESTING")
    obj_data_onboard.click_source_type()
    obj_data_onboard.click_next()


@when("User Onboard the Data Objects for json")
def json_layer_config(context):
    obj_data_onboard.select_inbound_type("S3")
    obj_data_onboard.select_inbound_layer("NVS GLASSBOX S3 INBOUND")
    obj_data_onboard.select_inbound_path()
    obj_data_onboard.enter_inbound_path("proj/glassbox/roster/amgen/inbound/uat_test/nested_json/")
    obj_data_onboard.select_landing_layer("NVS GLASSBOX S3")
    obj_data_onboard.select_landing_path()
    obj_data_onboard.enter_landing_path("proj/glassbox/roster/amgen/landing/uat_test/")
    obj_data_onboard.select_staging_layer("STAGING INTERACTION")
    obj_data_onboard.select_archive_layer("NVS GLASSBOX S3 ARCHIVE")
    obj_data_onboard.select_archive_path()
    obj_data_onboard.enter_archive_path("proj/glassbox/roster/amgen/archive/uat_test/")
    obj_data_onboard.select_frequency("Adhoc")
    # obj_data_onboard.enter_arrival_time("12:30")
    obj_data_onboard.enter_file_pattern("simple_json.json")
    obj_data_onboard.click_next()


@then("User Should be able to Onboard the Objects for json")
def verify_json_onboarding(context):
    obj_data_onboard.select_file_format("Simple Json File")
    path = str(AppConfig.WORKING_DIRECTORY) + "\\Testdata\\td_ui\\Simple_Json.json"
    obj_data_onboard.upload_file(path)
    obj_data_onboard.click_next()
    obj_data_onboard.select_target_table("UAT_TESTING_TABLE")
    obj_data_onboard.click_submit()
