UPDATE emp SET deptno = NULL WHERE empno=1001;
SELECT e.*, d.deptname, d.deptloc FROM emp e JOIN dept d ON e.deptno = d.deptno;

SELECT e.*, d.deptname, d.deptloc FROM emp e
LEFT OUTER JOIN dept d
ON e.deptno = d.deptno;

SELECT e.*, d.deptname, d.deptloc FROM emp e
RIGHT OUTER JOIN dept d
ON e.deptno = d.deptno;

SELECT e.*, d.deptname, d.deptloc FROM emp e
LEFT OUTER JOIN dept d
ON e.deptno = d.deptno
UNION
SELECT e.*, d.deptname, d.deptloc FROM emp e
RIGHT OUTER JOIN dept d
ON e.deptno = d.deptno;

#1
SELECT e.empno, e.name, t.titlename, d.deptname, d.deptloc FROM emp AS e LEFT OUTER JOIN dept AS d ON e.deptno = d.deptno
JOIN title AS t ON e.titleno = t.titleno WHERE YEAR(e.hdate)>='2000';

#2
SELECT d.deptname, salary_avg FROM dept AS d JOIN (SELECT deptno, ROUND(AVG(salary),2) AS salary_avg FROM emp GROUP BY deptno) AS e ON d.deptno=e.deptno
WHERE salary_avg>=3000;

#3
SELECT d.deptloc, ROUND(AVG(salary),2) FROM emp AS e JOIN dept AS d ON e.deptno = d.deptno GROUP BY d.deptloc HAVING d.deptloc = '경기';

#3
SELECT d.deptloc, ROUND(AVG(salary),2) FROM emp AS e JOIN dept AS d ON e.deptno = d.deptno WHERE d.deptloc = '경기' GROUP BY d.deptloc;

#4
SELECT * FROM emp;
SELECT A.empno, PERIOD_DIFF(DATE_FORMAT(CURRENT_DATE,'%Y%m'), DATE_FORMAT(A.hdate,'%Y%m')) AS 근무월수 FROM emp AS A JOIN (SELECT * FROM emp WHERE name = '홍영자') AS B
ON A.deptno=B.deptno;

#5
SELECT RANK() OVER(ORDER BY e.hdate) AS 순위, e.name, d.deptname, t.titlename, YEAR(NOW())-YEAR(e.hdate) AS 년수  FROM emp AS e LEFT OUTER JOIN dept AS d ON e.deptno = d.deptno JOIN title AS t ON t.titleno = e.titleno;