WITH temp AS(
SELECT player_id as temp_pid, event_date AS temp_edate,
    LEAD(event_date, 1) OVER(PARTITION BY player_id ORDER BY event_date) AS next_played,
    ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS row_num
FROM activity
GROUP BY 1,2)

SELECT -- next_played-1, *
    ROUND(SUM(CASE WHEN event_date = next_played - 1 THEN 1 ELSE 0 END)*1.00/COUNT(*) , 2) AS fraction
FROM activity a
JOIN temp t
ON(a.player_id = t.temp_pid AND a.event_date = t.temp_edate AND row_num = 1)