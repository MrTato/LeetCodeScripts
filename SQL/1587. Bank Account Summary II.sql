SELECT
    Users.name,
    SUM(amount) AS balance
FROM Transactions JOIN Users
ON Transactions.account = Users.account
GROUP BY Users.name, Users.account
HAVING SUM(amount) > 10000