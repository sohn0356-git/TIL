SELECT * FROM items;

SELECT ROW_NUMBER() OVER (ORDER BY price DESC, name ASC) AS 'RK', name, price FROM items LIMIT 10;

SELECT RANK() OVER (ORDER BY price desc) AS 'RK', name, price FROM items;


SELECT * FROM items;
SELECT category, ROUND(AVG(price),2), RANK() OVER (ORDER BY AVG(price)) AS 'RK' FROM items GROUP BY category;

USE shop1;

DESCRIBE cart;