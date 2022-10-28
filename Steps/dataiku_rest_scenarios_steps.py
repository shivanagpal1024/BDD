from behave import given, when, step, then
from pages.api_pages.dataiku_rest_scenarios import dataiku_rest_scenario


scenarios = dataiku_rest_scenario()


@given('user send a request to the URL to get Scenarios Last Run "{project_name}"')
def verify_scenario_last_run(context, project_name):
    """
    :type context: behave.runner.Context
    :type project_name: str
    """
    scenarios.export_scenarios(project_name)


@when("user get the last run status for the scenarios")
def verify_scenario_details(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("the user should be able to see the last run status")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
