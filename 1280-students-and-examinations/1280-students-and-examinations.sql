SELECT a.student_id,
       a.student_name,
       a.subject_name,
       COALESCE(e.attended_exams, 0) as attended_exams

FROM (SELECT * FROM Students CROSS JOIN Subjects) a 
LEFT JOIN (SELECT student_id,
                  subject_name,
                  count(*) as attended_exams
                  FROM Examinations
                  GROUP BY student_id, subject_name
                  ) e
ON a.student_id = e.student_id AND a.subject_name = e.subject_name
ORDER BY a.student_id, a.subject_name