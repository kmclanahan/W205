SELECT h.name, SUM(e.score) AS cumulative_score, 
AVG(e.score) as avg_score,
VARIANCE(e.score) as variance
FROM effective_care_data e
JOIN hospital_data h
ON e.provider_id = h.provider_id
GROUP BY h.name
ORDER BY cumulative_score DESC
LIMIT 10;
