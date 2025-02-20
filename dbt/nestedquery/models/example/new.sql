SELECT 
    status 
FROM 
    {{ref('nested')}} AS n 
WHERE
    status='Shipped'