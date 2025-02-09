-- Write your PostgreSQL query statement below
SELECT e2.name
FROM employee e1
JOIN employee e2
ON (e1.managerId = e2.id)
GROUP BY e2.id,e2.name
HAVING COUNT(1) > 4