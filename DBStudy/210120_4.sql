CREATE VIEW vemp
AS
SELECT e.empno, e.name, d.deptname, t.titlename
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno;

SELECT * FROM vemp;