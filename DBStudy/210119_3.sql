SELECT id, name, price, CAST(rate AS SIGNED INTEGER), regdate FROM items;

ALTER TABLE items ADD category NVARCHAR(10);
DESCRIBE items;

SELECT * FROM items;
SELECT category, ROUND(AVG(price),2) FROM items
GROUP BY category;

SELECT CONCAT(id,name), price, regdate FROM items;

SELECT CONCAT(id,' ',name), price, DATE_FORMAT(regdate,'%Y%m%d') FROM items;

INSERT INTO items VALUES(NULL,'pants11',NULL,3.2,CURRENT_TIMESTAMP(),'c3');
SELECT category, AVG(IFNULL(price,1))FROM items GROUP BY category;