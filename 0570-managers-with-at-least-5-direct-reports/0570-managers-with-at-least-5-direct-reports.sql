SELECT name
FROM Employee e, (SELECT managerId,
                         count(managerId) AS Report
                FROM Employee
                GROUP BY managerId
                ) m
WHERE e.id = m.managerId and Report >= 5 ;


