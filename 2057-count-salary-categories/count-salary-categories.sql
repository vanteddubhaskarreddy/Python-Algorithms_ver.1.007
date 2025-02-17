-- Write your PostgreSQL query statement below
WITH temp AS(
SELECT 
    COUNT(
        CASE 
            WHEN income < 20000
                THEN 1
        END) AS low,
    COUNT(
        CASE 
            WHEN income BETWEEN 20000 AND 50000
                THEN 1
        END) AS average,
    COUNT(
        CASE 
            WHEN income > 50000
                THEN 1
        END) AS high
FROM accounts
)

SELECT 'High Salary' AS category, high AS accounts_count
FROM temp
UNION ALL
SELECT 'Average Salary' AS category, average AS accounts_count
FROM temp
UNION ALL
SELECT 'Low Salary' AS category, low AS accounts_count
FROM temp
-- CROSS JOIN (UNNEST(ARRAY[ROW("low salary", "average salary", "high salary")]))
