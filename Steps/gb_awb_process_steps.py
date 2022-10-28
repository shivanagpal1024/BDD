from behave import given, when, then
from Config._app_config import AppConfig
from Config._test_config import browser
from pages.ui_pages.glassbox.pg_data_catalog import data_catalog

obj_data_catalog = data_catalog()


@given("User Launch the browser and navigates to glassbox url then login with valid credentials")
def launch_glassbox_app(context):
    obj_data_catalog.launch_gb_url(AppConfig.BROWSER_TYPE, "https://glassbox-uat.novartis.net/portal/landing/")


@when("User go to to process tab and select AWB")
def select_awb_process(context):
    obj_data_catalog.click_data_catalog("Data Catalog & Lineage")
    obj_data_catalog.verify_title("Data Catalog & Lineage")
    obj_data_catalog.select_menu("Process")
    obj_data_catalog.select_menu("Analytical Work Bench")


@when("User select knowledge article with valid url for AWB")
def update_awb_valid_article(context):
    obj_data_catalog.click_awb_knowledge_article("https://www.novartis.com/", awb_process="BRAND_HIERARCHY")


@when("User update the knowledge article with empty value for AWB")
def update_awb_empty_article(context):
    obj_data_catalog.verify_empty_awb_article("", awb_process="ANALYTICAL_DM")


@when("User update the knowledge article with invalid url for AWB")
def update_awb_invalid_article(context):
    obj_data_catalog.verify_awb_invalid_article("https://www.novartis", "Invalid URL format.",
                                                awb_process="BRAND_HIERARCHY")


@then("User user should be able to save the AWB article successfully")
def step_impl(context):
    browser.driver.close()


@when("User verify the AWB Process Name and Description with DataIKU Instance")
def verify_awb_name_desc(context):
    obj_data_catalog.verify_awb_process_desc("ANALYTICAL_DATA_MODEL")


@then("The AWB Process Name and Description should match with DataIKU Instance")
def step_impl(context):
    browser.driver.close()


@when("User select AWB Process Lineage and verify the DataIKU instance with Flow")
def verify_awb_process_lineage(context):
    obj_data_catalog.click_awb_process_lineage("ANALYTICAL_DATA_MODEL")


@when("User select AWB Operational Lineage and verify the DataIKU instance with Scenarios")
def verify_awb_operational_lineage(context):
    obj_data_catalog.click_awb_operational_lineage("ANALYTICAL_DATA_MODEL")


@then("The User should be able to validate the AWB process and operational lineage")
def step_impl(context):
    browser.driver.close()


@when("User verify the Process Owner Name")
def verify_awb_process_owner_name(context):
    obj_data_catalog.awb_process_owner("VA_TEST")


@then("User user should be able to see the Process Owner Name")
def step_impl(context):
    browser.driver.close()
