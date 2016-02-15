DROP TABLE readmission_data;
CREATE TABLE readmission_data AS SELECT provider_id, measure_name, measure_id, comp_to_national, score FROM readmissions;
