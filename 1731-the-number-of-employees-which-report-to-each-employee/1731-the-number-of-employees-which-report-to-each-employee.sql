SELECT e.employee_id,
       e.name,
       COUNT(*) AS reports_count,
       ROUND(AVG(s.age),0) AS average_age
FROM Employees e, Employees s
WHERE e.employee_id = s.reports_to
GROUP BY employee_id
ORDER By employee_id