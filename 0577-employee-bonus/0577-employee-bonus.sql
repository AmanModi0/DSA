SELECT name,
       bonus
FROM Employee e 
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE bonus is Null or bonus < 1000; 