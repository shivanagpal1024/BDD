from behave import given
from behave import then
from behave import when
from Utilities.db_utilities import database_connect
from Utilities import db_utilities
import pandas as pd
from datetime import datetime
from datetime import date

@then('validate the date information')
def validate_the_date(context):
    cdate=str(date.today())
    print (f"the currect date {cdate}")
    if (len(context.snow_response==1)):
        print (f"the snowflake response is {context.snow_response}")
        dt=str(context.snow_response.loc[:,"adt_odh_updt_tmstmp"])
        # print (dt)
        assert dt.__contains__(cdate), 'The dates are not matched'

    else:
        raise Exception ("The response has more than one row")