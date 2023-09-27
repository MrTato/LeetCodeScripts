SELECT
    name,
    bonus
FROM Employee LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE
    bonus is null OR
    bonus < 1000