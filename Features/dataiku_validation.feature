Feature: Validate Prameters data in dataIKU

    Scenario Outline: Validate connection parameters in dataIKU
      Given User Launch browser with application url and login with valid credentials
      When User Search for project "<TestFile>" "<TestCaseName>" and "<TestSheetName>"
      Then select Dataset for given "<TestCaseName>" "<TestFile>"and "<TestSheetName>" validate
      Then select Global Variables for given "<TestCaseName>" "<TestFile>"and "<TestSheetName>" validate
      Examples:
        | TestFile |TestCaseName|TestSheetName|
#         |SFMC_CALENDARIZATION_AWB_COREPLUS_MAPPING_Table_Ver_Part1|TC13 |DE_MATCH_CAL_CAM_DATA_MGMT |
#          |SFMC_CALENDARIZATION_AWB_COREPLUS_MAPPING_Table_Ver_Part2|TC13 |DE_MATCH_CAL_CAM_DATA_MGMT |
#           |Derm_Mapping_Document_Ver2_part4|TC10|DS_AI_MATCH_COSENTYX_DERM |
#            |RheumMappingDocumentVer4_part2_two|TC12|DS_AI_MATCH_COSENTYX_RHEUM |
#             |EntrestoMappingDocumentVer_part1|TC15|Prod_Entresto_PS |
#            |AWB_COREPLUS_MAPPING_Ver_updated_final|TC09|match_data_enrich_pipeline |
#            |DE_MATCH_CAMPAIGN_DATA_MANAGEMENT_INBOUND_AWB_COREPLUS_MAPPING_part2|TC16|DE_MATCH_CAMP_DATA_MGMT_INBOUND|
#           |AWB_COREPLUS_MAPPING_Ver_updated_final|TC06 |MATCH_CONCERTO_DATA_PIPELINE |
#                 |SFMC_CALENDARIZATION_AWB_COREPLUS_MAPPING_Table_Ver_Part1|TC13 |DE_MATCH_CAL_CAM_DATA_MGMT |
#      |SFMC_CALENDARIZATION_AWB_COREPLUS_MAPPING_Table_Ver_Part1|TC14   |DE_MATCH_CAMPAIGN_DATA_MANAGEMENT |
      |DE_MATCH_CON_CAMPAIGN_DATA_MGMT_Global Variables_dryrun|TC17|DE_MATCH_CON_CAMPAIGN_DATA_MGMT |