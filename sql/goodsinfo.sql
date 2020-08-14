-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: HAL
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `goods_goodsinfo`
--

DROP TABLE IF EXISTS `goods_goodsinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_goodsinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(100) NOT NULL,
  `goods_price` decimal(8,2) NOT NULL,
  `goods_inventory` varchar(20) NOT NULL,
  `goods_desc` longtext NOT NULL,
  `goods_img` varchar(100) NOT NULL,
  `goods_cag_id` int(11) NOT NULL,
  `gclick` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goodsinfo_goods_cag_id_a7b17a2d_fk_goods_goodscategory_id` (`goods_cag_id`),
  CONSTRAINT `goods_goodsinfo_goods_cag_id_a7b17a2d_fk_goods_goodscategory_id` FOREIGN KEY (`goods_cag_id`) REFERENCES `goods_goodscategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_goodsinfo`
--

LOCK TABLES `goods_goodsinfo` WRITE;
/*!40000 ALTER TABLE `goods_goodsinfo` DISABLE KEYS */;
INSERT INTO `goods_goodsinfo` VALUES (1,'女剑士',35.00,'200','剑士格挡无敌，一剑开天','goods/237.jpg',1,0),(2,'女拳师',25.00,'300','一拳超人，所向无敌','goods/238.jpg',1,0),(3,'npc',100.00,'10','冒充npc，调戏玩家，世界里的妹子','goods/239.jpg',1,0),(4,'男拳',15.00,'400','无敌铁拳，遭最毒的打，默默保护队友','goods/240.jpg',1,0),(5,'男剑士',45.00,'120','游戏里最帅的男人','goods/241.jpg',1,0),(6,'灵剑士',24.00,'200','身材矮小，但是力量很大，视野很低，蹲草丛我最行','goods/242.jpg',1,0),(7,'美丽的小姐姐',26.00,'26','谁都不能欺负我的小姐姐','goods/243.jpg',1,0),(8,'大姐姐',80.00,'20','御姐不是一般人能降服的','goods/245.jpg',1,0),(9,'秦义绝01',100.00,'100','绝美的秦义绝，冷酷的大姐头','goods/321.jpg',4,0),(10,'秦义绝02',120.00,'120','绝美的秦义绝，冷酷的大姐头','goods/322.jpg',4,0),(11,'秦义绝03',123.00,'123','绝美的秦义绝，冷酷的大姐头','goods/323.jpg',4,0),(12,'火炮兰',80.00,'200','很多小伙伴都来挑战火炮兰，就能了得她马尾辫','goods/324.jpg',4,0),(13,'熔岩美女',45.00,'234','火红是世界的唯一颜色','goods/325.jpg',4,0),(14,'幽蘭01',61.00,'61','刺客美女','goods/326.jpg',4,0),(15,'小可爱',50.00,'50','可爱的灵族','goods/327.jpg',4,0),(16,'秦义绝04',350.00,'14','魔鬼的身材，天使的面孔','goods/328.jpg',4,0),(17,'灵族小姐姐',80.00,'100','灵族小姐姐','goods/329.jpg',4,0),(18,'灵族小哥哥',75.00,'75','灵族小哥哥','goods/33o.jpg',4,0),(19,'泰云宝玉神物',2.50,'200','泰云宝玉神物','goods/1.jpg',3,0),(20,'泰云武魂神物',12.50,'144','泰云武魂神物','goods/2.jpg',3,0),(21,'黑夜猫',88.88,'88','五彩斑斓的黑夜猫','goods/3.jpg',3,0),(22,'鹤立鸡群礼包箱',2.00,'200','鹤立鸡群','goods/4.jpg',3,0),(23,'璀璨钥匙',5.00,'500','鹤立鸡群','goods/5.jpg',3,0),(24,'真红幻影拳套',144.00,'144','真红幻影拳套（拳师）','goods/6.jpg',3,0),(25,'真红幻影剑',144.00,'144','真红幻影剑（剑士）','goods/7.jpg',3,0),(26,'泰云魂神物',2.50,'200','泰云魂神物','goods/8.jpg',3,0),(27,'白帝',188.00,'188','梦中的白马王子','goods/9.jpg',3,0),(28,'门派名变更使用券',200.00,'200','门派名变更使用券','goods/10.jpg',3,0),(29,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(30,'定制T恤',50.00,'50','定制T恤','goods/11_ZP15ZBw.jpg',2,0),(31,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(32,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(33,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(34,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(35,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(36,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(37,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(38,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',2,0),(39,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(40,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(41,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(42,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(43,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(44,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(45,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(46,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(47,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(48,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',5,0),(49,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(50,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(51,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(52,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(53,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(54,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(55,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(56,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(57,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0),(58,'定制T恤',50.00,'100','定制T恤','goods/11.jpg',6,0);
/*!40000 ALTER TABLE `goods_goodsinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-14 19:46:12
