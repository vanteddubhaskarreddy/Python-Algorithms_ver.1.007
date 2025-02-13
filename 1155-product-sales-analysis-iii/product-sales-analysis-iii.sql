-- Write your PostgreSQL query statement below
WITH temp AS (SELECT
    product_id,
    MIN(year)
FROM sales
GROUP BY 1)

SELECT product_id, year AS first_year, quantity, price
FROM sales
WHERE (product_id, year) IN (SELECT
    product_id,
    MIN(year)
FROM sales
GROUP BY 1)