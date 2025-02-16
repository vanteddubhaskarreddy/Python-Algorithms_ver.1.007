-- Write your PostgreSQL query statement below
WITH temp AS(SELECT turn, person_id, person_name, weight, 
    SUM(weight) OVER(ORDER BY turn) AS total_weight
FROM queue
)

SELECT person_name
FROM temp
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1