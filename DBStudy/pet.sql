-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.3.11-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- tutorial 데이터베이스 구조 내보내기
DROP DATABASE IF EXISTS `tutorial`;
CREATE DATABASE IF NOT EXISTS `tutorial` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `tutorial`;

-- 테이블 tutorial.pet 구조 내보내기
DROP TABLE IF EXISTS `pet`;
CREATE TABLE IF NOT EXISTS `pet` (
  `name` varchar(20) DEFAULT NULL,
  `owner` varchar(20) DEFAULT NULL,
  `species` varchar(20) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  `death` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 tutorial.pet:~8 rows (대략적) 내보내기
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
INSERT INTO `pet` (`name`, `owner`, `species`, `sex`, `birth`, `death`) VALUES
	('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', '0000-00-00'),
	('Claws', 'Gwen', 'cat', 'm', '1994-03-17', '0000-00-00'),
	('Buffy', 'Harold', 'dog', 'f', '1989-05-13', '0000-00-00'),
	('Fang', 'Benny', 'dog', 'm', '1990-08-27', '0000-00-00'),
	('Bowser', 'Diane', 'dog', 'm', '1989-08-31', '1995-07-29'),
	('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', '0000-00-00'),
	('Whistler', 'Gwen', 'bird', '', '1997-12-09', '0000-00-00'),
	('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', NULL);
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
