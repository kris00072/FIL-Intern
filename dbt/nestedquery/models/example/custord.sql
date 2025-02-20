{{ config(materialized='view') }}

SELECT  
    c.customerName,  
    c.phone,  
    CONCAT(c.addressLine1, ' ', COALESCE(c.addressLine2, '')) AS address,  
    o.orderDate,  
    o.status  
FROM  
    {{ source('models', 'customers') }} AS c  
JOIN  
    {{ source('models', 'orders') }} AS o  
ON  
    c.customerNumber = o.customerNumber

    