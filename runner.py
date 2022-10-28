import subprocess


# dparam=datetime.now().strftime("%d%m%Y_%H%M%S")

### to run all the feature file
# command1= "behave -D source_env=qa -D environment=qa Features"

### to run particular feature file ## mention the feature file name at end
command1= "behave -D source_env=qa -D environment=qa ./Features/count_validation_file_snow.feature"

### to run multiple feature file ## mention the feature files names at end with space
# command1= "behave -D source_env=qa -D environment=qa ./Features/metadata_validation_snow.feature ./Features/count_validation_snowflake.feature"

# command2= "python Utilities/report_html.py --input_json_file Reports/"+dparam+"_json_report.json --output_html_file Reports/"+dparam+"_html_report.html"

process=subprocess.run(command1, shell=True)
# process=subprocess.run(command2, shell=True)
