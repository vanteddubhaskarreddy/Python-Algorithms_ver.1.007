-- Write your PostgreSQL query statement below
SELECT contest_id, ROUND((COUNT(*)*100.0/(SELECT COUNT(*) FROM users)), 2) AS percentage
FROM register r
GROUP BY 1
ORDER BY 2 DESC, 1 ASC