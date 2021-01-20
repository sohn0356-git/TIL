DROP DATABASE IF EXISTS webcf;

CREATE DATABASE IF NOT EXISTS webcf;
USE webcf;

CREATE TABLE IF NOT EXISTS cfcode(
	code_coffee INT(5) PRIMARY KEY AUTO_INCREMENT,
	code_cfname NVARCHAR(30)
);


CREATE TABLE IF NOT EXISTS users(
	users_id INT(10) PRIMARY KEY AUTO_INCREMENT,
	users_name NVARCHAR(20),
	users_phone NVARCHAR(20),
	users_email NVARCHAR(20)
);


CREATE TABLE IF NOT EXISTS cf(
	coffee_name NVARCHAR(30),
	code_coffee INT(5),
	coffee_price INT(10),
	coffee_reverse INT(5),
	coffee_image_path NVARCHAR(50),
	PRIMARY KEY(coffee_name, code_coffee)
);

CREATE TABLE IF NOT EXISTS buy(
	buy_id INT(10) PRIMARY KEY AUTO_INCREMENT,
	users_id INT(10) ,
	buy_addr NVARCHAR(30),
	buy_method NVARCHAR(10)
	
);

CREATE TABLE IF NOT EXISTS buydetail(
	buy_id INT(10),
	coffee_name NVARCHAR(30),
	detail_quantity INT(5),
	PRIMARY KEY(buy_id, coffee_name)
);

CREATE TABLE IF NOT EXISTS boardcode(
	code_board_id INT(5) PRIMARY KEY AUTO_INCREMENT,
	code_boardname NVARCHAR(20)
);

CREATE TABLE IF NOT EXISTS boardcate(
	cate_board_id INT(5) PRIMARY KEY AUTO_INCREMENT,
	cate_boardname NVARCHAR(20)
);

CREATE TABLE IF NOT EXISTS board(
	board_id INT(5) AUTO_INCREMENT,
	code_board_id INT(5),
	cate_board_id INT(5),
	users_id INT(10),
	board_title NVARCHAR(20),
	board_reg DATE,
	board_views INT(5),
	board_detail NVARCHAR(200),
	board_show TINYINT,
	PRIMARY KEY(board_id, cate_board_id, code_board_id)	
);

ALTER TABLE cfcode AUTO_INCREMENT = 1;
ALTER TABLE users AUTO_INCREMENT = 1;
ALTER TABLE boardcode AUTO_INCREMENT = 1;
ALTER TABLE boardcate AUTO_INCREMENT = 1;
ALTER TABLE board AUTO_INCREMENT = 1;
ALTER TABLE board ADD CONSTRAINT fk_boardcode FOREIGN KEY (code_board_id)
REFERENCES boardcode (code_board_id);
ALTER TABLE board ADD CONSTRAINT fk_boardcate FOREIGN KEY (cate_board_id)
REFERENCES boardcate (cate_board_id);
ALTER TABLE board ADD CONSTRAINT fk_boardusers FOREIGN KEY (users_id)
REFERENCES users (users_id);
ALTER TABLE cf ADD CONSTRAINT fk_cfcode FOREIGN KEY (code_coffee)
REFERENCES cfcode (code_coffee);
ALTER TABLE buy ADD CONSTRAINT fk_userid FOREIGN KEY (users_id)
REFERENCES users (users_id);
ALTER TABLE buydetail ADD CONSTRAINT fk_cfname FOREIGN KEY (coffee_name)
REFERENCES cf (coffee_name);
ALTER TABLE buydetail ADD CONSTRAINT fk_buyid FOREIGN KEY (buy_id)
REFERENCES buy (buy_id);

INSERT INTO cfcode VALUES(NULL,'SINGLE ORIGINS');
INSERT INTO cfcode VALUES(NULL,'BLEND');
INSERT INTO cfcode VALUES(NULL,'EASY COFFEE');

INSERT INTO cf VALUES('코체레 하마 G1, 에티오피아',1,16000,800,'md_images/코체레_하마');
INSERT INTO cf VALUES('시다마 디카페인, 에티오피아',1,16000,800,'md_images/시다마_디카페인');
INSERT INTO cf VALUES('정글에스프레소(JUNGLE ESPRESSO)',2,16000,800,'md_images/정글에스프레소');
INSERT INTO cf VALUES('메리제인(MARY JANE)',2,18000,900,'md_images/메리제인');
INSERT INTO cf VALUES('메리제인 드립백(6개입)',3,11500,500,'md_images/메리제인_드립백');
INSERT INTO cf VALUES('메리제인 콜드브루(500ml 원액)',3,14000,700,'md_images/메리제인_콜드브루');
INSERT INTO cf VALUES('ACR 월넛 우드 트레이 & 미니',3,18000,900,'md_images/우드_트레이');

INSERT INTO users VALUES(NULL,'son','010-1234-5678','sohn@gmail.com');
INSERT INTO users VALUES(NULL,'kim','010-2345-5678','kim@gmail.com');
INSERT INTO users VALUES(NULL,'park','010-5678-5678','park@gmail.com');
INSERT INTO users VALUES(NULL,'admin','010-9999-9876','admin@gmail.com');

INSERT INTO buy VALUES(NULL, 1, 'Seoul', '카드');
INSERT INTO buy VALUES(NULL, 2, 'Busan', '카드');
INSERT INTO buy VALUES(NULL, 3, 'Daegu', '카드');
INSERT INTO buy VALUES(NULL, 1, 'Incheon', '현금');

INSERT INTO buydetail VALUES(1,'정글에스프레소(JUNGLE ESPRESSO)',1);
INSERT INTO buydetail VALUES(1,'메리제인(MARY JANE)',1);
INSERT INTO buydetail VALUES(2,'메리제인 드립백(6개입)',5);
INSERT INTO buydetail VALUES(3,'시다마 디카페인, 에티오피아',1);
INSERT INTO buydetail VALUES(2,'ACR 월넛 우드 트레이 & 미니',1);
INSERT INTO buydetail VALUES(4,'메리제인(MARY JANE)',10);

INSERT INTO boardcode VALUES(NULL, 'FAQ');
INSERT INTO boardcode VALUES(NULL, '도매 납품 상담');
INSERT INTO boardcode VALUES(NULL, 'Q & A');

INSERT INTO boardcate VALUES(NULL, '주문/결제');
INSERT INTO boardcate VALUES(NULL, '배송');
INSERT INTO boardcate VALUES(NULL, '제품문의');
INSERT INTO boardcate VALUES(NULL, '납품신청');
INSERT INTO boardcate VALUES(NULL, '회원신청');
INSERT INTO boardcate VALUES(NULL, '제품불량');
INSERT INTO boardcate VALUES(NULL, '기타');

INSERT INTO board VALUES(NULL, 1,3,4,'제품 관련 문의','2020-06-29',166,'[제품문의] 로스팅 후 언제 가장 맛있나요? (에스프레소 블렌드) 생산일로부터 4~7일 후에 사용을 시작, 1개월 안에 사용하시는 것을 권장합니다.',1);
INSERT INTO board VALUES(NULL, 1,1,4,'교환 및 반품','2020-06-29',57,'[주문/결제] 교환 및 반품 규정 : 생산 직후부터 변화하는 커피의 특성 때문에 단순변심, 주문실수 등에 의한 교환/반품은 어렵습니다.',1);
INSERT INTO board VALUES(NULL, 2,5,1,'도매 회원 신청합니다.','2020-04-08',3,'1. 업체명 : Star 2. 성함 : son, 3. 주소 : 서울, 4. 연락처 : 010-1234-5678',0);
INSERT INTO board VALUES(NULL, 3,6,2,'500g 주문했는데요','2020-06-29',166,'200g 원두만 왔어요',0);

CREATE VIEW vboard AS
SELECT b.board_id,bcate.cate_boardname,b.board_title,u.users_name,b.board_reg,b.board_views FROM board AS b
JOIN boardcode AS bcode ON b.code_board_id = bcode.code_board_id
JOIN boardcate AS bcate ON b.cate_board_id = bcate.cate_board_id
JOIN users AS u ON b.users_id = u.users_id;

CREATE VIEW vfaq AS
SELECT ROW_NUMBER() OVER (ORDER BY b.board_reg) AS 번호,bcate.cate_boardname,b.board_title,u.users_name,b.board_reg,b.board_views FROM board AS b
JOIN boardcode AS bcode ON b.code_board_id = bcode.code_board_id
JOIN boardcate AS bcate ON b.cate_board_id = bcate.cate_board_id
JOIN users AS u ON b.users_id = u.users_id
WHERE bcode.code_boardname = 'FAQ';

CREATE VIEW vwholesale AS
SELECT ROW_NUMBER() OVER (ORDER BY b.board_reg) AS 번호,bcate.cate_boardname,b.board_title,u.users_name,b.board_reg,b.board_views FROM board AS b
JOIN boardcode AS bcode ON b.code_board_id = bcode.code_board_id
JOIN boardcate AS bcate ON b.cate_board_id = bcate.cate_board_id
JOIN users AS u ON b.users_id = u.users_id
WHERE bcode.code_boardname = '도매 납품 상담';

CREATE VIEW vqna AS
SELECT ROW_NUMBER() OVER (ORDER BY b.board_reg) AS 번호,bcate.cate_boardname,b.board_title,u.users_name,b.board_reg,b.board_views FROM board AS b
JOIN boardcode AS bcode ON b.code_board_id = bcode.code_board_id
JOIN boardcate AS bcate ON b.cate_board_id = bcate.cate_board_id
JOIN users AS u ON b.users_id = u.users_id
WHERE bcode.code_boardname = 'Q & A';

SELECT * FROM vboard;
SELECT * FROM vfaq;
SELECT * FROM vwholesale;
SELECT * FROM vqna;