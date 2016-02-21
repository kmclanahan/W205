DROP TABLE survey_response_data;
CREATE TABLE survey_response_data AS SELECT provider_id, hcahps_base_score, hcahps_cons_score FROM survey_responses;
DROP TABLE survey_responses;
