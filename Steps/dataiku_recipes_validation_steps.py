from behave import *

from pages.ui_pages.pg_dataiku_recipes import recipes
from Config._test_config import browser
from Utilities.excel import Excel_Read
from Utilities.excel_utility.read_excel_data import read_excel
import time
import pandas as pd

obj_recipes = recipes()
excel_obj = Excel_Read()
excel_data = read_excel()

@then('Validates the "{ProjectName}" SQL recipes and save screenshots to output file')
def get_recipes(context,ProjectName):
    obj_recipes.select_menu()
    obj_recipes. get_recipes(ProjectName)
    browser.tear_down()