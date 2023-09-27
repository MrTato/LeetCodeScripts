/* Write your T-SQL query statement below */
SELECT name
FROM employee
WHERE id IN (SELECT managerID
FROM employee
GROUP BY managerID
HAVING COUNT(managerID)>=5)