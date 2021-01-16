CREATE TABLE item
(	
	id INT NOT NULL,
	name NVARCHAR(10) NOT NULL,
	code CHAR(5),
	price INT AUTO_INCREMENT UNIQUE,
	rate FLOAT,
	regdate DATE
);
ALTER TABLE item ADD CONSTRAINT PRIMARY KEY(id)

ALTER TABLE item AUTO_INCREMENT = 1000;
INSERT INTO item VALUES(130,'item02','1111',NULL,5.2,CURRENT_DATE);
INSERT INTO item VALUES(135,'item02','1111',NULL,5.2,CURRENT_DATE);
SELECT * FROM item;item

DROP TABLE IF EXISTS item