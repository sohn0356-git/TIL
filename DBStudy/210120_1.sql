DROP DATABASE IF EXISTS company;
CREATE DATABASE IF NOT EXISTS company;
USE company;

DROP TABLE IF EXISTS emp;

CREATE TABLE IF NOT EXISTS title(
	titleno CHAR(2) PRIMARY KEY,
	titlename NVARCHAR(20)
);

CREATE TABLE IF NOT EXISTS dept(
	deptno CHAR(2) PRIMARY KEY,
	deptname NVARCHAR(20),
	deptloc NVARCHAR(20)
);

CREATE TABLE IF NOT EXISTS emp(
	empno CHAR(4) PRIMARY KEY,
	titleno CHAR(2),
	deptno CHAR(2),
	name NVARCHAR(10),
	manager CHAR(4),
	salary INT(10),
	hdate DATE
);

ALTER TABLE emp ADD CONSTRAINT fk_title FOREIGN KEY (titleno) REFERENCES title (titleno);
ALTER TABLE emp ADD CONSTRAINT fk_dept FOREIGN KEY (deptno) REFERENCES dept (deptno);

INSERT INTO title VALUES('10','사원');
INSERT INTO title VALUES('20','대리');
INSERT INTO title VALUES('30','과장');
INSERT INTO title VALUES('40','사장');
INSERT INTO title VALUES('50','인턴');

INSERT INTO dept VALUES('10','본사','서울');
INSERT INTO dept VALUES('20','영업부','경기');
INSERT INTO dept VALUES('30','생산부','부산');
INSERT INTO dept VALUES('40','연구소','대전');

INSERT INTO emp VALUES('1001','40','10','킹',NULL, 5000, '1997-01-01');
INSERT INTO emp VALUES('1002','30','20','이영업','1001', 3000, '1998-01-01');
INSERT INTO emp VALUES('1003','30','30','김생산','1001', 3500, '1998-02-01');
INSERT INTO emp VALUES('1004','30','40','홍연구','1001', 2800, '1997-12-01');

INSERT INTO emp VALUES('1005','20','20','영대리','1002', 1500, '1999-05-01');
INSERT INTO emp VALUES('1006','10','20','영사원','1002', 500, '2000-01-01');

INSERT INTO emp VALUES('1007','20','30','생대리','1003', 1300, '1999-06-01');
INSERT INTO emp VALUES('1008','10','30','생사원','1003', 500, '2000-03-01');

INSERT INTO emp VALUES('1009','20','40','연대리','1004', 1700, '1999-04-01');
INSERT INTO emp VALUES('1010','10','40','연대리','1004', 600, '2000-02-01');