DROP DATABASE IF EXISTS webcf;

CREATE DATABASE IF NOT EXISTS webcf;

CREATE TABLE IF NOT EXISTS cf(
	coffee_name NVARCHAR(30) PRIMARY KEY,
	code_coffee INT(5),
	coffee_price INT(10),
	coffee_reverse INT(5),
	coffee_image_path NVARCHAR(50)
)

CREATE TABLE IF NOT EXISTS cfcode(
	code_coffee INT(5) PRIMARY KEY AUTO_INCREMENT,
	code_cfname NVARCHAR(30)
)

CREATE TABLE IF NOT EXISTS buydetail(
	buy_id NVARCHAR(30),
	coffee_name NVARCHAR(30),
	detail_quantity INT(5)
)

CREATE TABLE IF NOT EXISTS users(
	users_id INT(10) PRIMARY KEY AUTO_INCREMENT,
	users_name NVARCHAR(20),
	users_phone NVARCHAR(20),
	users_email NVARCHAR(20)
)

CREATE TABLE IF NOT EXISTS buy(
	buy_id NVARCHAR(30),
	users_id INT(10),
	buy_addr NVARCHAR(30),
	buy_method NVARCHAR(10)
)	