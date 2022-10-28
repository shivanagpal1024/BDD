from behave import  given, then
from pages.api_pages.pg_services import rest_services
api_services = rest_services()


@given(u'user send a request to the URL to get user details using "{sheet_name}"')
def get_users_list(context, sheet_name):
    api_services.get_api_service_response(sheet_name)


@then(u'the response will return status 200')
def step_impl(context):
    pass