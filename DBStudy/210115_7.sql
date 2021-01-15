#CREATE DATABASE coffeeshop;
#USE coffeeshop;

DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS order_detail;
DROP TABLE IF EXISTS orders;

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


# ALTER TABLE order_detail ADD CONSTRAINT item_fk_detail FOREIGN KEY (detail_p_id) REFERENCES product(p_id);
# ALTER TABLE order_detail ADD CONSTRAINT order_fk_detail FOREIGN KEY (detail_order_id) REFERENCES orders(order_id);
# ALTER TABLE cart ADD CONSTRAINT user_fk_cart FOREIGN KEY (cart_userid) REFERENCES member(mem_id);
# ALTER TABLE cart ADD CONSTRAINT item_fk_cart FOREIGN KEY (cart_itemid) REFERENCES product(p_id);
# ALTER TABLE orders ADD CONSTRAINT user_fk_order FOREIGN KEY (order_mem_id) REFERENCES member(mem_id);