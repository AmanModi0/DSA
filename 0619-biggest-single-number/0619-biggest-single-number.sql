SELECT MAX(num) AS num
FROM (SELECT num,
       COUNT(*) AS freq
      FROM MyNumbers
      GROUP BY num 
      HAVING freq = 1) AS m;

