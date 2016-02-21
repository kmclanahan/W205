SELECT h.name, s.hcahps_base_score
FROM survey_response_data s 
JOIN hospital_data h
ON s.provider_id = h.provider_id
WHERE s.hcahps_base_score NOT LIKE "%Not Available%"
ORDER BY s.hcahps_base_score DESC
LIMIT 20;
