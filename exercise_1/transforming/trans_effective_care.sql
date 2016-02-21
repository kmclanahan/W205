DROP TABLE effective_care_data;
CREATE TABLE effective_care_data AS SELECT provider_id, measure_id, measure_name, score FROM effective_care;
DROP TABLE effective_care;

