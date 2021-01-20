SELECT *, salary*0.1 AS 세금 FROM emp;

SELECT * FROM emp WHERE YEAR(hdate)<'2001' AND salary <4000;

SELECT * FROM emp WHERE name like '%생%'

SELECT *, CASE 
	WHEN salary < 2000 THEN '하'
	WHEN salary < 4000 THEN '중'
	ELSE '고'
	END
FROM emp;

#5
SELECT deptno, ROUND(AVG(salary),2) FROM emp GROUP BY deptno;

#6
SELECT deptno, ROUND(AVG(IF(titleno='20',salary,0)),2) AS 대리평균, ROUND(AVG(IF(titleno='10',salary,0)),2) AS 사원평균 FROM emp GROUP BY deptno;

#7
SELECT AVG(salary) FROM emp WHERE YEAR(hdate) BETWEEN '2000' AND '2002';

#8
SELECT total.deptno, total_salary, RANK() OVER(ORDER BY total.total_salary) FROM(
	SELECT deptno, SUM(salary) AS total_salary FROM emp GROUP BY deptno
) AS total;

#9
SELECT * FROM emp WHERE deptno = 10;

#10
SELECT * FROM emp AS A JOIN (SELECT * FROM emp WHERE name = '이영자') AS B
ON A.deptno=B.deptno;

#11
SELECT * FROM emp;
SELECT * FROM emp AS A JOIN (SELECT * FROM emp WHERE name = '김강국') AS B
ON A.titleno=B.titleno;