SELECT user_id, MAX(time_stamp) AS last_stamp
FROM 
    (SELECT * FROM Logins 
    WHERE YEAR(time_stamp) = '2020') as m 
GROUP BY user_id;