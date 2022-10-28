from behave import given, when, then
from pages.ui_pages.glassbox.pg_data_catalog import data_catalog

obj_data_catalog = data_catalog()


@when("User go to to process tab and select Core")
def select_core_process(context):
    obj_data_catalog.click_data_catalog("Data Catalog & Lineage")
    obj_data_catalog.verify_title("Data Catalog & Lineage")
    obj_data_catalog.select_menu("Process")
    obj_data_catalog.select_menu("Core ++")


@when("User select knowledge article with valid url for Core")
def update_core_valid_article(context):
    obj_data_catalog.click_core_knowledge_article("https://www.novartis.com/", "PSS_INCLISIRAN")


@when("User update the knowledge article with empty value for Core")
def update_core_empty_article(context):
    obj_data_catalog.verify_empty_core_article(article="", awb_process="SNTL_CV")


@when("User update the knowledge article with invalid url for Core")
def update_awb_invalid_article(context):
    obj_data_catalog.verify_core_invalid_article("https://www.novartis", "Invalid URL format.",
                                                 awb_process="SNTL_COSENTYX")


@then("User user should be able to save the Core article successfully")
def step_impl(context):
    pass


@when("User verify the Core Process Name and Description with DataIKU Instance")
def verify_core_name_desc(context):
    obj_data_catalog.verify_core_process_desc("COREPL_DATA_LOAD")


@then("The Core Process Name and Description should match with DataIKU Instance")
def step_impl(context):
    pass


@when("User select Core Process Lineage and verify the DataIKU instance with Flow")
def verify_core_process_lineage(context):
    obj_data_catalog.click_core_process_lineage("PSS_INCLISIRAN")


@when("User select Core Operational Lineage and verify the DataIKU instance with Scenarios")
def verify_core_operational_lineage(context):
    obj_data_catalog.click_core_operational_lineage("PSS_INCLISIRAN")


@then("The User should be able to validate the Core process and operational lineage")
def step_impl(context):
    pass
