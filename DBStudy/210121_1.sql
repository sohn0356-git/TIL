USE company;

SELECT * FROM emp;

#1
SELECT IFNULL(e1.empno,'없음'), IFNULL(e1.titleno,'없음'), IFNULL(e1.deptno,'없음'), IFNULL(e1.name,'없음'), IFNULL(e2.name,'없음'), IFNULL(e1.salary,'없음'), IFNULL(e1.hdate,'없음') FROM EMP AS E1 LEFT OUTER JOIN EMP AS E2 ON E1.MANAGER = E2.EMPNO;

#2
SELECT IFNULL(e1.empno,'없음') AS empno, IFNULL(t.titlename,'없음') AS title, IFNULL(d.deptname,'없음') AS dept, IFNULL(e1.name,'없음') AS name, IFNULL(e2.name,'없음') AS manager, IFNULL(e1.salary,'없음') AS salary, IFNULL(e1.hdate,'없음') AS hdate FROM emp AS e1 LEFT OUTER JOIN emp AS e2 ON e1.manager = e2.empno
JOIN dept AS d ON e1.deptno = d.deptno
JOIN title AS t ON e1.titleno = t.titleno;