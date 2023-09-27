SELECT *
FROM Users
WHERE mail LIKE '[a-zA-Z]@leetcode.com'
   OR (mail LIKE '[a-zA-Z]%@leetcode.com'
       AND mail NOT LIKE '%[^a-zA-Z0-9_.-]%@leetcode.com');
