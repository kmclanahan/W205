rm -rf ./hospital
mkdir ./hospital

tail -n +2 ./'Hospital General Information.csv' > ./hospital/hospitals.csv
tail -n +2 ./'Timely and Effective Care - Hospital.csv' > ./hospital/effective_care.csv
tail -n +2 ./'Readmissions and Deaths - Hospital.csv' > ./hospital/readmissions.csv
tail -n +2 ./'Measure Dates.csv' > ./hospital/measures.csv
tail -n +2 ./hvbp_hcahps_05_28_2015.csv > ./hospital/survey_responses.csv

hdfs dfs -rm /user/w205/hospital_compare/*
hdfs dfs -rmdir /user/w205/hospital_compare
hdfs dfs -mkdir /user/w205/hospital_compare

hdfs dfs -put ./hospital/hospitals.csv /user/w205/hospital_compare
hdfs dfs -put ./hospital/effective_care.csv /user/w205/hospital_compare
hdfs dfs -put ./hospital/readmissions.csv /user/w205/hospital_compare
hdfs dfs -put ./hospital/measures.csv /user/w205/hospital_compare
hdfs dfs -put ./hospital/survey_responses.csv /user/w205/hospital_compare
