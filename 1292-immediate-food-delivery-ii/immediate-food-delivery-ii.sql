-- Write your PostgreSQL query statement below
WITH temp AS(
SELECT customer_id AS temp_customer_id, MIN(order_date) AS min_order_date
FROM delivery
GROUP BY 1)

SELECT 
    ROUND(SUM(
    CASE
        WHEN order_date = customer_pref_delivery_date
            THEN 1
        ELSE 0
    END)*100.00/COUNT(*), 2) AS immediate_percentage
FROM delivery d
JOIN temp t
    ON (d.customer_id = t.temp_customer_id AND d.order_date = t.min_order_date)