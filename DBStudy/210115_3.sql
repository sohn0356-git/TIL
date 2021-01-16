DROP TABLE IF EXISTS product;

CREATE TABLE IF NOT EXISTS product
(
	pcoid CHAR(3),
	pserial CHAR(4),
	pname NVARCHAR(10) NOT NULL,
	pprice INT(10) NOT NULL,
	qt INT(10) NOT NULL
);

ALTER TABLE product ADD CONSTRAINT mypk PRIMARY KEY (pcoid, pserial);
ALTER TABLE product ALTER pprice SET DEFAULT 10000;
ALTER TABLE product ADD CONSTRAINT mycheck CHECK (qt>10);
ALTER TABLE product ADD CONSTRAINT myunique UNIQUE (pname);

ALTER TABLE product DROP CONSTRAINT mycheck;

INSERT INTO product VALUES('112','1111','p1', DEFAULT,5);
SELECT * FROM product;