SELECT h.state, SUM(e.score) AS cumulative_score, 
AVG(e.score) as avg_score,
VARIANCE(e.score) as variance
FROM effective_care_data e
JOIN hospital_data h
ON e.provider_id = h.provider_id
GROUP BY h.state
ORDER BY avg_score DESC
LIMIT 10;
