DROP TABLE hospitals;
CREATE EXTERNAL TABLE hospitals
(provider_id string,
name string,
address string,
city string,
state string,
zip_code string,
county string,
phone string,
type string,
owner string,
emergency string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar" = ",",
"quoteChar" = '"',
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/hospitals';

DROP TABLE effective_care;
CREATE EXTERNAL TABLE effective_care
(provider_id string,
name string,
address string,
city string,
state string,
zip_code string,
county string,
phone string,
condition string,
measure_id string,
measure_name string,
score string,
sample string,
footnote string,
measure_start_date string,
measure_end_date string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar" = ",",
"quoteChar" = '"',
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/effective_care';

DROP TABLE readmissions;
CREATE EXTERNAL TABLE readmissions
(provider_id string,
name string,
address string,
city string,
state string,
zip_code string,
county string,
phone string,
condition string,
measure_name string,
measure_id string,
comp_to_national string,
denominator string,
score string,
low_estimate string,
high_estimate string,
footnote string,
measure_start_date string,
measure_end_date string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar" = ",",
"quoteChar" = '"',
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/readmissions';

DROP TABLE measures;
CREATE EXTERNAL TABLE measures
(name string,
id string,
start_quarter string,
start_date string,
end_quarter string,
end_date string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar" = ",",
"quoteChar" = '"',
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/measures';

DROP TABLE survey_responses;
CREATE EXTERNAL TABLE survey_responses
(provider_id string,
name string,
address string,
city string,
state string,
zip_code string,
county string,
com_nurses_ach_pts string,
com_nurses_imp_pts string,
com_nurses_dim_score string,
com_doc_ach_pts string,
com_doc_imp_pts string,
com_doc_dim_score string,
resp_staff_ach_pts string,
resp_staff_imp_pts string,
resp_staff_dim_score string,
pain_mgmt_ach_pts string,
pain_mgmt_imp_pts string,
pain_mgmt_dim_score string,
com_medicine_ach_pts string,
com_medicine_imp_pts string,
com_medicine_dim_score string,
clean_quiet_ach_pts string,
clean_quiet_imp_pts string,
clean_quiet_dim_score string,
discharge_ach_pts string,
discharge_imp_pts string,
discharge_dim_score string,
overall_ach_pts string,
overall_imp_pts string,
overall_dim_score string,
hcahps_base_score string,
hcahps_cons_score string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar" = ",",
"quoteChar" = '"',
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/survey_responses';
