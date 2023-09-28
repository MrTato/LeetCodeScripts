SELECT s.name FROM SalesPerson s
WHERE s.sales_id NOT IN (SELECT o.sales_id FROM Orders o, Company c
WHERE c.com_id = o.com_id AND c.name = 'RED')