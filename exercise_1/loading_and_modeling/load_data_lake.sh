rm -rf /home/w205/hospital
mkdir /home/w205/hospital

tail -n +2 /home/w205/'Hospital General Information.csv' > /home/w205/hospital/hospitals.csv
tail -n +2 /home/w205/'Timely and Effective Care - Hospital.csv' > /home/w205/hospital/effective_care.csv
tail -n +2 /home/w205/'Timely and Effective Care - State.csv' > /home/w205/hospital/effective_care_state.csv
tail -n +2 /home/w205/'Readmissions and Deaths - Hospital.csv' > /home/w205/hospital/readmissions.csv
tail -n +2 /home/w205/'Readmissions and Deaths - State.csv' > /home/w205/hospital/readmissions_state.csv
tail -n +2 /home/w205/hvbp_hcahps_05_28_2015.csv > /home/w205/hospital/survey_responses.csv

hdfs dfs -rm -r /user/w205/hospital_compare
hdfs dfs -mkdir /user/w205/hospital_compare
hdfs dfs -mkdir /user/w205/hospital_compare/hospitals
hdfs dfs -mkdir /user/w205/hospital_compare/effective_care
hdfs dfs -mkdir /user/w205/hospital_compare/effective_care_state
hdfs dfs -mkdir /user/w205/hospital_compare/readmissions
hdfs dfs -mkdir /user/w205/hospital_compare/readmissions_state
hdfs dfs -mkdir /user/w205/hospital_compare/survey_responses

hdfs dfs -put /home/w205/hospital/hospitals.csv /user/w205/hospital_compare/hospitals
hdfs dfs -put /home/w205/hospital/effective_care.csv /user/w205/hospital_compare/effective_care
hdfs dfs -put /home/w205/hospital/effective_care_state.csv /user/w205/hospital_compare/effective_care_state
hdfs dfs -put /home/w205/hospital/readmissions.csv /user/w205/hospital_compare/readmissions
hdfs dfs -put /home/w205/hospital/readmissions_state.csv /user/w205/hospital_compare/readmissions_state
hdfs dfs -put /home/w205/hospital/survey_responses.csv /user/w205/hospital_compare/survey_responses
