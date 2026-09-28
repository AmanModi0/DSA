    SELECT
    product_name , unit
    FROM Products p , ( SELECT product_id, order_date, SUM(unit) AS unit FROM Orders GROUP BY product_id, MONTH(order_date), YEAR(order_date)) AS o
    WHERE p.product_id = o.product_id AND MONTH(o.order_date) = 2 AND YEAR(o.order_date) = 2020 AND unit >= 100