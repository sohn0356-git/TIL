DROP DATABASE IF EXISTS shop;
CREATE DATABASE IF NOT EXISTS shop;
USE shop;

CREATE TABLE IF NOT EXISTS usertb(
	id NVARCHAR(10) PRIMARY KEY,
	pwd NVARCHAR(10),
	name NVARCHAR(20)
);

CREATE TABLE IF NOT EXISTS itemtb(
	id INT(10) AUTO_INCREMENT PRIMARY KEY,
	name NVARCHAR(20),
	price INT(10),
	regdate DATE,
	imgname NVARCHAR(30)
);

INSERT INTO usertb VALUES('id01','pwd01','james1');
INSERT INTO usertb VALUES('id02','pwd02','james2');
INSERT INTO usertb VALUES('id03','pwd03','james3');
SELECT * FROM usertb;

INSERT INTO itemtb VALUES(NULL, 'pants1', 10000, CURRENT_DATE(), 'abc.jpg');
INSERT INTO itemtb VALUES(NULL, 'pants2', 10000, CURRENT_DATE(), 'def.jpg');
INSERT INTO itemtb VALUES(NULL, 'pants3', 10000, CURRENT_DATE(), 'ghi.jpg');
SELECT * FROM itemtb;