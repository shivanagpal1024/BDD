@common_steps
  Feature: To define the common steps

    Scenario: Initialize the spark session
      Given the Spark initialization
      Then stop the spark session