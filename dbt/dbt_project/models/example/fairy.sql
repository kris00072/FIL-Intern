{{ config(materialized='table') }}

SELECT  
    transaction_id,  
    quantity,  
    price,  
    2 AS product_id  
FROM  
    fil.sales_2  
WHERE  
    quantity > 1