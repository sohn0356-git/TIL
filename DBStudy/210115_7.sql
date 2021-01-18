DROP DATABASE IF EXISTS coffeeshop;

CREATE DATABASE coffeeshop;
USE coffeeshop;

DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS order_detail;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS board;

CREATE TABLE IF NOT EXISTS board
(
	mem_id NVARCHAR(30),
	board_detail NVARCHAR(200),
	PRIMARY KEY(mem_id)
);

CREATE TABLE IF NOT EXISTS review
(
	mem_id NVARCHAR(30),
	p_id NVARCHAR(10),
	review_detail NVARCHAR(200),
	review_rating INT(5),
	PRIMARY KEY(mem_id, p_id)
);

CREATE TABLE IF NOT EXISTS cart
(
	cart_id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	cart_userid NVARCHAR(30),
	cart_itemid NVARCHAR(10),
	cart_amount INT(10)
);

CREATE TABLE IF NOT EXISTS product
(
	p_id NVARCHAR(10) NOT NULL PRIMARY KEY,
	p_category_id INT(5) NOT NULL,
	p_stock INT(10),
	p_name NVARCHAR(30),
	p_price INT(10),
	p_detail NVARCHAR(500),
	p_image_path NVARCHAR(100),
	p_date DATE,
	p_salescount INT(10)
);

CREATE TABLE IF NOT EXISTS member
(
	mem_id NVARCHAR(30) NOT NULL PRIMARY KEY,
	mem_pwd NVARCHAR(30) NOT NULL,
	mem_name NVARCHAR(10) NOT NULL,
	mem_addr NVARCHAR(50),
	mem_phone NVARCHAR(20),
	mem_email NVARCHAR(20),
	mem_joindate DATE,
	mem_status INT(1)
);

CREATE TABLE IF NOT EXISTS orders
(
	order_id NVARCHAR(20) NOT NULL PRIMARY KEY,
	order_mem_id NVARCHAR(30) NOT NULL,
	order_recv_name NVARCHAR(10) NOT NULL,
	order_recv_addr NVARCHAR(50) NOT NULL,
	order_total_price INT(10) NOT NULL,
	order_date DATE,
	order_status INT(1),
	order_msg NVARCHAR(100)
);

CREATE TABLE IF NOT EXISTS order_detail
(
	detail_id NVARCHAR(10) NOT NULL PRIMARY KEY,
	detail_p_id NVARCHAR(10),
	detail_order_id NVARCHAR(20),
	detail_amount INT(5)
);


ALTER TABLE board ADD CONSTRAINT board_id_fk_member FOREIGN KEY (mem_id) REFERENCES member(mem_id);
ALTER TABLE review ADD CONSTRAINT id_fk_product FOREIGN KEY (p_id) REFERENCES product(p_id);
ALTER TABLE review ADD CONSTRAINT id_fk_member FOREIGN KEY (mem_id) REFERENCES member(mem_id);
ALTER TABLE order_detail ADD CONSTRAINT item_fk_detail FOREIGN KEY (detail_p_id) REFERENCES product(p_id);
ALTER TABLE order_detail ADD CONSTRAINT order_fk_detail FOREIGN KEY (detail_order_id) REFERENCES orders(order_id);
ALTER TABLE cart ADD CONSTRAINT user_fk_cart FOREIGN KEY (cart_userid) REFERENCES member(mem_id);
ALTER TABLE cart ADD CONSTRAINT item_fk_cart FOREIGN KEY (cart_itemid) REFERENCES product(p_id);
ALTER TABLE orders ADD CONSTRAINT user_fk_order FOREIGN KEY (order_mem_id) REFERENCES member(mem_id);

#	p_id p_category_id p_stock p_name p_price p_detail
#	p_image_path p_date DATE p_salescount
INSERT INTO product VALUES('p01',0,100,'T-shirt',10000,'100% 면','C:\Users\sohn0\Desktop\blog\id01',CURRENT_DATE,0);
INSERT INTO product VALUES('p02',0,100,'skirt',15000,'100% 캐시미어','C:\Users\sohn0\Desktop\blog\id02',CURRENT_DATE,0);
INSERT INTO product VALUES('p03',0,100,'sweater',5000,'100% 털','C:\Users\sohn0\Desktop\blog\id03',CURRENT_DATE,0);

INSERT INTO member VALUES('user01','1234','name01','addr1','010-0000-0001','user01@gmail.com',CURRENT_DATE,0);
INSERT INTO member VALUES('user02','1234','name02','addr2','010-0000-0002','user02@gmail.com',CURRENT_DATE,0);
INSERT INTO member VALUES('user03','1234','name03','addr3','010-0000-0003','user03@gmail.com',CURRENT_DATE,0);

SELECT * FROM product;
SELECT * FROM member;

INSERT INTO cart VALUES(NULL, 'user01','p02',5);
INSERT INTO cart VALUES(NULL, 'user02','p01',5);

SELECT * FROM cart;

INSERT INTO review VALUES('user01', 'p01', 'Good',5);
INSERT INTO review VALUES('user02', 'p01', 'Bad',1);

SELECT * FROM review;

# INSERT INTO review VALUES('user01', 'p01', 'Good',1);

INSERT INTO orders VALUES('order01','user01','name01','add1',10000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order02','user01','name01','add1',15000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order03','user02','name01','add1',40000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order04','user03','name01','add1',12000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order05','user02','name01','add1',1000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order06','user01','name01','add1',12000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order07','user02','name01','add1',20000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order08','user02','name01','add1',30000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order09','user03','name01','add1',11000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order10','user01','name01','add1',20000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order11','user02','name01','add1',14000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order12','user03','name01','add1',15000,CURRENT_DATE,NULL,NULL);
INSERT INTO orders VALUES('order13','user02','name01','add1',13000,CURRENT_DATE,NULL,NULL);
SELECT * FROM orders;

INSERT INTO order_detail VALUES('detail01','p01','order01',10);
SELECT * FROM order_detail;

SELECT * FROM orders;
SELECT order_mem_id AS mem_id, SUM(order_total_price) FROM orders GROUP BY order_mem_id ORDER BY SUM(order_total_price);

SELECT * FROM orders AS order_list JOIN
(SELECT order_mem_id AS mem_id, SUM(order_total_price) FROM orders GROUP BY order_mem_id ORDER BY SUM(order_total_price) DESC LIMIT 1) AS sum_of_pay
ON order_list.order_mem_id = sum_of_pay.mem_id;
