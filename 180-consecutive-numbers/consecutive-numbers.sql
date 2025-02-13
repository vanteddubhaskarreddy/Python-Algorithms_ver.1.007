-- Write your PostgreSQL query statement below
WITH temp AS (
SELECT id, num, 
    LEAD(num, 1) OVER(ORDER BY id) AS next_1,
    LEAD(num, 2) OVER(ORDER BY id) AS next_2
FROM logs)

SELECT DISTINCT(num) AS ConsecutiveNums
FROM temp
WHERE num = next_1 AND num = next_2