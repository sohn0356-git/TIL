#Relational
DROP TABLE IF EXISTS cart;

SELECT * FROM items;
DESCRIBE items;
SELECT * FROM users;
DESCRIBE users;

CREATE TABLE IF NOT EXISTS cart
(
	id INT(10) AUTO_INCREMENT PRIMARY KEY,
	userid CHAR(4),
	itemid INT(10),
	regdate DATE,
	qt INT(10)
);


ALTER TABLE cart ADD CONSTRAINT user_fk FOREIGN KEY (userid) REFERENCES users(id);
ALTER TABLE cart ADD CONSTRAINT item_fk FOREIGN KEY (itemid) REFERENCES items(id);

INSERT INTO cart VALUES (id,'id01',1004,CURRENT_DATE,4);
SELECT * FROM cart;
SELECT c.id, c.regdate, u.id, u.name, i.name, i.price FROM cart AS c
JOIN users AS u ON c.userid = u.id
JOIN items AS i ON c.itemid = i.id;



