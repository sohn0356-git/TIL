#GROUP BY

SELECT emp_no, SUM(salary) FROM salaries
GROUP BY emp_no
HAVING SUM(salary) > 1000000;

SELECT emp_no, salary FROM salaries
WHERE salary > 70000
AND emp_no = 10001;

SELECT emp_no, ROUND(AVG(salary / 12),2) AS 월급 FROM salaries
GROUP BY emp_no HAVING 월급 > 5000;

SELECT emp_no, MAX(salary), MIN(salary), MAX(salary) - MIN(salary) AS 연봉차  FROM salaries GROUP BY emp_no ORDER BY 연봉차, emp_no;

SELECT emp_no, COUNT(*) FROM salaries GROUP BY emp_no;