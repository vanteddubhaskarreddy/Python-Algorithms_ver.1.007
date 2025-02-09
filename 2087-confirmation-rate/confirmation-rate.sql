-- Write your PostgreSQL query statement below
SELECT s.user_id, 
    ROUND((SUM(CASE 
        WHEN action = 'confirmed'
        THEN 1
        ELSE 0
    END )/
    COUNT(1) :: NUMERIC), 2)
    AS confirmation_rate
FROM signups s
LEFT JOIN confirmations c
ON(s.user_id = c.user_id)
GROUP BY s.user_id