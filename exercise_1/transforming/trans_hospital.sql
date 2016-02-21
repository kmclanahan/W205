DROP TABLE hospital_data;
CREATE TABLE hospital_data AS SELECT provider_id, name, state FROM hospitals;
DROP TABLE hospitals;
