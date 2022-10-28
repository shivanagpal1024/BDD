Feature: Get Scenario Last Run Status

  Scenario Outline: Verify Scenarios Last Run Status
    Given user send a request to the URL to get Scenarios Last Run "<project_name>"
    When user get the last run status for the scenarios
    Then the user should be able to see the last run status
    Examples:
      |project_name|
      |PRJ_MATCH_AKTANA_DATA_PIPELINE    |
      |MATCH_DATA_ENRICH_PIPELINE|
      |MATCH_CONCERTO_DATA_PIPELINE|
      |MATCH_IRMA_DATA_PIPELINE    |
      |MATCH_N2_DATA_PIPELINE|
      |MATCH_ISR_DATA_PIPELINE|
      |MATCH_DATA_PROFILE_PIPELINE|
      |MATCH_FEED0_VALIDATION|
      |DE_MATCH_CAMPAIGN_DATA_MANAGEMENT|
      |DE_MATCH_CAL_CAM_DATA_MGMT|
      |DE_MATCH_CAMPAIGN_DATA_MANAGEMENT_INBOUND|
      |DE_MATCH_CON_CAMPAIGN_DATA_MANAGEMENT|
      |PROD_ENTRESTOPS|
      |DS_AI_INNOV_MATCH_X|
      |DS_AI_MATCH_COSENTYX_DERM|
      |MATCH_COSENTYX_EMAIL_CONTENT    |
