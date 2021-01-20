SELECT LEFT(UPPER(first_name),3), LPAD(last_name,10,'#') FROM employees

SELECT SUBSTR(last_name,2,3) FROM employees;

SELECT emp_no, hire_date, ADDDATE(hire_date, INTERVAL 10 DAY), FROM employees;

SELECT TIMESTAMPDIFF(YEAR, hire_date, NOW()) FROM employees;

SELECT PERIOD_DIFF(DATE_FORMAT(NOW(),'%Y%m'),DATE_FORMAT(hire_date,'%Y%m'))
FROM employees;

SELECT YEAR(hire_date) AS 입사년, AVG(ROUND((TIMESTAMPDIFF(DAY,hire_date, NOW())),2)) AS 근무일수평균 FROM employees GROUP BY 입사년 ORDER BY 입사년;