CREATE DATABASE IF NOT EXISTS test2;

CREATE TABLE IF NOT EXISTS items(
	id INT(10) AUTO_INCREMENT PRIMARY KEY,
	name NVARCHAR(20),
	price INT(10),
	rate FLOAT(10.2),
	regdate DATE
);

ALTER TABLE items MODIFY regdate DATETIME;

INSERT INTO items VALUES(NULL, 'pants9',10000,3.2,CURRENT_TIMESTAMP());
INSERT INTO items VALUES(NULL, 'pants10',10000,3.5,CURRENT_DATE());
INSERT INTO items VALUES(NULL, 'pants11',10000,3.5,CURRENT_DATE()),
(NULL, 'pants12',10000,3.5,CURRENT_DATE()),
(NULL, 'pants13',10000,3.5,CURRENT_DATE()),
(NULL, 'pants14',10000,3.5,CURRENT_DATE());

UPDATE items SET price = price + 5000 WHERE NAME='pants9';

SELECT * FROM items;

SELECT id, CAST(regdate AS TIME) AS DATE FROM items;
