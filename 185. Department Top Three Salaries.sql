/* Write your T-SQL query statement below */
WITH empMod AS (
  SELECT
    DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) rank,
    name,
    salary,
    departmentId
  FROM Employee
)

SELECT
  d.name AS Department,
  empMod.name AS Employee,
  empMod.salary AS Salary
FROM Department d JOIN empMod ON d.id = empMod.departmentId AND rank <= 3
