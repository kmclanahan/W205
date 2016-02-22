SELECT h.name, AVG(s.hcahps_base_score) AS avg_score,
COUNT(s.hcahps_base_score) AS num_surveys
FROM survey_response_data s 
JOIN hospital_data h
ON s.provider_id = h.provider_id
GROUP BY h.name
ORDER BY avg_score DESC
LIMIT 20;

