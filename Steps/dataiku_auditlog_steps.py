from behave import given, when, step, then
from pages.ui_pages.pg_dataiku_login import login
from pages.ui_pages.pg_dataiku_home import home
from pages.ui_pages.pg_audit_validation import audit_log
from Config._app_config import AppConfig
from Config._test_config import browser
import sys

obj_login = login()
obj_home = home()
obj_audit = audit_log()


@given('User Launch the Browser and Navigates to DataIKU Application URL')
def launch_app_url(context):
    if len(sys.argv) > 1:
        env = context.config.userdata['environment']
        obj_login.launch_url("QA")
    else:
        obj_login.launch_url("QA")


@when("User Enters the Valid Credentials and Login")
def enter_credentials(context):
    obj_login.enter_user_name(AppConfig.DATAIKU_UNAME)


@then('User Should be able to Navigates to the Home Page and search for "{project_name}"')
def search_project(context, project_name):
    obj_audit.enter_project_name(project_name)
    obj_audit.click_project(project_name)
    obj_home.click_got_it()


@when('User Navigates to Scenarios Page with "{menu}" and "{sub_menu}" then Search for Scenarios')
def select_menu(context, menu, sub_menu):
    obj_audit.select_menu(menu, sub_menu)


@then('User go to the scenario details page using "{scenario_name}" and capture execution time then compare with '
      'Snowflake Database "{snow_query}"')
def compare_scenario_logs(context, scenario_name, snow_query):
    context.scenario_name = scenario_name
    print("SCENARIO_DATA", context.scenario_name)
    context.snow_query = snow_query
    if len(sys.argv) > 1:
        env = context.config.userdata['environment']
    else:
        env = "QA"
    obj_audit.get_scenario_date(env, context.scenario_name, context.snow_query)


@then("User Should be able to compare and validate the scenario execution time with Database")
def close_browser(context):
    browser.driver.close()
