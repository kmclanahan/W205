SELECT h.name, SUM(e.score) AS cumulative_score, 
AVG(e.score) as avg_score,
VARIANCE(e.score) as variance,
AVG(s.hcahps_base_score)
FROM effective_care_data e
JOIN hospital_data h
ON e.provider_id = h.provider_id
JOIN survey_response_data s 
ON s.provider_id = h.provider_id
GROUP BY h.name
ORDER BY avg_score DESC
LIMIT 50;
