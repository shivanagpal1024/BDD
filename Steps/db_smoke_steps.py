from behave import given, then
from pages.db_pages.pg_db_smoke import db_smoke

smoke = db_smoke()


@given('User Connected to Snowflake Data Base and execute the query using')
def verify_db_connection(context):
    db_dict = smoke.execute_query("SMOKE")
    smoke.verify_db_results(db_dict)


@then("User Should be able to execute the Data Base Query and export the results")
def verify_db_results(context):
    pass