from behave import given, then
from pyspark.sql import SparkSession
from Config._test_config import browser


@given('the Spark initialization')
def initiate_spark_session(context):
    try:
        context.spark = None
        context.spark = SparkSession.builder.master("local").appName("demo").getOrCreate()
        browser.update_step("The Spark initialization", "The Spark initialization is successful",
                            "The Spark initialization is successful", True)
    except Exception as e:
        browser.update_step("The Spark initialization", "The Spark initialization is successful",
                            str(e), False)
        raise Exception("Not able to initialize the spark")


@then('stop the spark session')
def stop_spar(context):
    try:
        context.spark.stop()
        browser.update_step("Stop the Spark session", "Stopped the spark session",
                            "Stopped the spark session", True)
    except Exception as e:
        browser.update_step("Stop the Spark session", "Stopped the spark session",
                            str(e), False)
        raise Exception("Not able to stop the spark")
