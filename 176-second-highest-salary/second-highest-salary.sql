-- Write your PostgreSQL query statement below
WITH temp1 AS (
SELECT
    salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS ranker
FROM employee
)
,temp2 AS (
SELECT 
    CASE 
        WHEN salary IS NOT NULL
            THEN salary
        ELSE NULL
    END AS SecondHighestSalary
FROM temp1
WHERE ranker = 2
UNION ALL
SELECT 
    NULL AS SecondHighestSalary
)
SELECT * FROM temp2 LIMIT 1