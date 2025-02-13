-- Write your PostgreSQL query statement below
WITH temp AS(SELECT 
    product_id,  
    CASE 
        WHEN change_date <= '2019-08-16'::DATE
            THEN change_date
        ELSE '1000-01-01'::DATE
    END AS change_date,
    CASE 
        WHEN change_date <= '2019-08-16'::DATE
            THEN new_price
        ELSE 10
    END AS price,
    ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY 
                        CASE 
                            WHEN change_date <= '2019-08-16'::DATE
                                THEN change_date
                            ELSE '1000-01-01'::DATE
                        END
    DESC) AS row_num
FROM products
)

SELECT product_id, price
FROM temp t
WHERE row_num = 1