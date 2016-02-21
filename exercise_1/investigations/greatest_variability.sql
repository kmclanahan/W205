SELECT measure_name,
VARIANCE(score) as variance
FROM effective_care_data
GROUP BY measure_name
ORDER BY variance DESC
LIMIT 10;
