-- Write your PostgreSQL query statement below
SELECT query_name, ROUND(AVG(rating::NUMERIC/position), 2) AS quality
    ,ROUND(SUM(
        CASE WHEN rating < 3
        THEN 1
        ELSE 0
        END)*100/(COUNT(*)::NUMERIC), 2) AS poor_query_percentage
FROM queries
GROUP BY 1