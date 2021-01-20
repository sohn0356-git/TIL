SELECT id, name, price, CAST(rate AS SIGNED INTEGER), regdate FROM items;

ALTER TABLE items ADD category NVARCHAR(10);
DESCRIBE items;

SELECT * FROM items;
SELECT category, ROUND(AVG(price),2) FROM items
GROUP BY category;

SELECT CONCAT(id,name), price, regdate FROM items;

SELECT CONCAT(id,' ',name), price, DATE_FORMAT(regdate,'%Y%m%d') FROM items;

INSERT INTO items VALUES(NULL,'pants11',NULL,3.2,CURRENT_TIMESTAMP(),'c3');
SELECT category, AVG(IFNULL(price,0)) FROM items GROUP BY category;
SELECT category, AVG(price) FROM items GROUP BY category;

SELECT *,
	CASE 
		WHEN price<=10000 THEN 'low'
		WHEN price<=20000 THEN 'middle'
		WHEN price>20000 THEN 'high'
		ELSE 'none'
		END
FROM items;

SELECT *, AVG(IFNULL(price,-100000)) AS avg_price,
	CASE 
		WHEN AVG(IFNULL(price,-100000))<=10000 THEN 'low'
		WHEN AVG(IFNULL(price,-100000))<=20000 THEN 'middle'
		WHEN AVG(IFNULL(price,-100000))>20000 THEN 'high'
		ELSE 'none'
		END
FROM items
GROUP BY category;

SELECT id, name, price ,rate, regdate,
	CASE category
		WHEN  'c1' THEN '반바지'
		WHEN  'c2' THEN '여름바지'
		WHEN  'c3' THEN '겨울바지'
		END
	AS 상품명
FROM items
