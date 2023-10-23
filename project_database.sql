-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: project_database
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `product_info_table`
--
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_info_table` (
  `product_id` varchar(255) NOT NULL,
  `urls` varchar(255) NOT NULL,
  `class_type` varchar(255) NOT NULL,
  `class_name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_info_table`
--

LOCK TABLES `product_info_table` WRITE;
/*!40000 ALTER TABLE `product_info_table` DISABLE KEYS */;
INSERT INTO `product_info_table` VALUES ('boatairdropes1','https://www.snapdeal.com/product/boat-airdopes-121v2-on-ear/683350354126#bcrumbSearch:boat%20airdopes%20431','span','payBlkBig','2023-10-15 06:50:21','2023-10-15 06:50:21'),('boatairdropes2','https://www.ohlocal.in/product?detail=product_details&product_id=EA131889BO','div','col-6 text-start value1 onlineP','2023-10-15 06:53:14','2023-10-16 18:22:16'),('laptop1','https://myitworld.com/products/victus-gaming-laptop-15-fb0147ax?_pos=2&_sid=3726e1da7&_ss=r','span','product-price-minimum money','2023-10-15 14:59:23','2023-10-15 14:59:23'),('laptop2','https://www.smartprix.com/laptops/hp-victus-15-fb0147ax-gaming-laptop-amd-ryzen-ppd1naisspur','div','price','2023-10-15 16:47:22','2023-10-15 16:47:22'),('watch1','https://rameshwatch.com/products/titan-1639sm01','span','product__price on-sale','2023-10-15 05:09:01','2023-10-15 05:09:01'),('watch2','https://www.price-hunt.com/watches/titan-karishma-analog-multi-colour-dial-mens-watch-1639-sm-01.php','span','min_price','2023-10-15 05:35:44','2023-10-15 05:35:44');
/*!40000 ALTER TABLE `product_info_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-17 14:02:38
