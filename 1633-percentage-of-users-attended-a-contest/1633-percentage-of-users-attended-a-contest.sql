SELECT contest_id,
       ROUND((COUNT(contest_id)/total_users)*100,2) AS percentage
FROM Register, (SELECT COUNT(*) AS total_users FROM Users) m
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC