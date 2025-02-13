-- Write your PostgreSQL query statement below
SELECT x,y,z,
    CASE 
        WHEN x+y <= GREATEST(x,y,z)
            THEN 'No'
        WHEN x+z <= GREATEST(x,y,z)
            THEN 'No'
        WHEN z+y <= GREATEST(x,y,z)
            THEN 'No'
        ELSE 'Yes'
    END AS triangle
FROM triangle