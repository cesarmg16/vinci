CREATE DATABASE IF NOT EXISTS `f1_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `f1_data`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: f1_data
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `circuits`
--

DROP TABLE IF EXISTS `circuits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `circuits` (
  `circuitId` int NOT NULL AUTO_INCREMENT,
  `circuitRef` text,
  `name` text,
  `location` text,
  `country` text,
  `lat` double DEFAULT NULL,
  `lng` double DEFAULT NULL,
  `alt` int DEFAULT NULL,
  `url` text,
  PRIMARY KEY (`circuitId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `circuits`
--

LOCK TABLES `circuits` WRITE;
/*!40000 ALTER TABLE `circuits` DISABLE KEYS */;
/*!40000 ALTER TABLE `circuits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constructor_results`
--

DROP TABLE IF EXISTS `constructor_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constructor_results` (
  `constructorResultsId` int NOT NULL AUTO_INCREMENT,
  `raceId` int NOT NULL,
  `constructorId` int NOT NULL,
  `points` int DEFAULT NULL,
  `status` text,
  PRIMARY KEY (`constructorResultsId`),
  KEY `fk_constructor_result_raceId_idx` (`raceId`),
  KEY `fk_constructor_result_constructorId_idx` (`constructorId`),
  CONSTRAINT `fk_constructor_result_constructorId` FOREIGN KEY (`constructorId`) REFERENCES `constructors` (`constructorId`),
  CONSTRAINT `fk_constructor_result_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constructor_results`
--

LOCK TABLES `constructor_results` WRITE;
/*!40000 ALTER TABLE `constructor_results` DISABLE KEYS */;
/*!40000 ALTER TABLE `constructor_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constructor_standings`
--

DROP TABLE IF EXISTS `constructor_standings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constructor_standings` (
  `constructorStandingsId` int NOT NULL AUTO_INCREMENT,
  `raceId` int NOT NULL,
  `constructorId` int NOT NULL,
  `points` int DEFAULT NULL,
  `position` int DEFAULT NULL,
  `positionText` text,
  `wins` int DEFAULT NULL,
  PRIMARY KEY (`constructorStandingsId`),
  KEY `fk_constructor_standings_raceId_idx` (`raceId`),
  KEY `fk_constructor_standings_constructorId_idx` (`constructorId`),
  CONSTRAINT `fk_constructor_standings_constructorId` FOREIGN KEY (`constructorId`) REFERENCES `constructors` (`constructorId`),
  CONSTRAINT `fk_constructor_standings_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constructor_standings`
--

LOCK TABLES `constructor_standings` WRITE;
/*!40000 ALTER TABLE `constructor_standings` DISABLE KEYS */;
/*!40000 ALTER TABLE `constructor_standings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constructors`
--

DROP TABLE IF EXISTS `constructors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constructors` (
  `constructorId` int NOT NULL AUTO_INCREMENT,
  `constructorRef` text,
  `name` text,
  `nationality` text,
  `url` text,
  PRIMARY KEY (`constructorId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constructors`
--

LOCK TABLES `constructors` WRITE;
/*!40000 ALTER TABLE `constructors` DISABLE KEYS */;
/*!40000 ALTER TABLE `constructors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `driver_standings`
--

DROP TABLE IF EXISTS `driver_standings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `driver_standings` (
  `driverStandingsId` int NOT NULL AUTO_INCREMENT,
  `raceId` int NOT NULL,
  `driverId` int NOT NULL,
  `points` int DEFAULT NULL,
  `position` int DEFAULT NULL,
  `positionText` text,
  `wins` int DEFAULT NULL,
  PRIMARY KEY (`driverStandingsId`),
  KEY `fk_driver_standings_raceId_idx` (`raceId`),
  KEY `fk_driver_standings_driverId_idx` (`driverId`),
  CONSTRAINT `fk_driver_standings_driverId` FOREIGN KEY (`driverId`) REFERENCES `drivers` (`driverId`),
  CONSTRAINT `fk_driver_standings_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver_standings`
--

LOCK TABLES `driver_standings` WRITE;
/*!40000 ALTER TABLE `driver_standings` DISABLE KEYS */;
/*!40000 ALTER TABLE `driver_standings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drivers`
--

DROP TABLE IF EXISTS `drivers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drivers` (
  `driverId` int NOT NULL AUTO_INCREMENT,
  `driverRef` text,
  `number` text,
  `code` text,
  `forename` text,
  `surname` text,
  `dob` text,
  `nationality` text,
  `url` text,
  PRIMARY KEY (`driverId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drivers`
--

LOCK TABLES `drivers` WRITE;
/*!40000 ALTER TABLE `drivers` DISABLE KEYS */;
/*!40000 ALTER TABLE `drivers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lap_times`
--

DROP TABLE IF EXISTS `lap_times`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lap_times` (
  `raceId` int NOT NULL,
  `driverId` int NOT NULL,
  `lap` int NOT NULL,
  `position` int DEFAULT NULL,
  `time` text,
  `milliseconds` int DEFAULT NULL,
  PRIMARY KEY (`raceId`,`driverId`,`lap`),
  KEY `fk_lap_times_driverId_idx` (`driverId`),
  CONSTRAINT `fk_lap_times_driverId` FOREIGN KEY (`driverId`) REFERENCES `drivers` (`driverId`),
  CONSTRAINT `fk_lap_times_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lap_times`
--

LOCK TABLES `lap_times` WRITE;
/*!40000 ALTER TABLE `lap_times` DISABLE KEYS */;
/*!40000 ALTER TABLE `lap_times` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pit_stops`
--

DROP TABLE IF EXISTS `pit_stops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pit_stops` (
  `raceId` int NOT NULL,
  `driverId` int NOT NULL,
  `stop` int NOT NULL,
  `lap` int DEFAULT NULL,
  `time` text,
  `duration` double DEFAULT NULL,
  `milliseconds` int DEFAULT NULL,
  PRIMARY KEY (`raceId`,`driverId`,`stop`),
  KEY `fk_pit_stops_driverId_idx` (`driverId`),
  CONSTRAINT `fk_pit_stops_driverId` FOREIGN KEY (`driverId`) REFERENCES `drivers` (`driverId`),
  CONSTRAINT `fk_pit_stops_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pit_stops`
--

LOCK TABLES `pit_stops` WRITE;
/*!40000 ALTER TABLE `pit_stops` DISABLE KEYS */;
/*!40000 ALTER TABLE `pit_stops` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qualifying`
--

DROP TABLE IF EXISTS `qualifying`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qualifying` (
  `qualifyId` int NOT NULL AUTO_INCREMENT,
  `raceId` int DEFAULT NULL,
  `driverId` int DEFAULT NULL,
  `constructorId` int DEFAULT NULL,
  `number` int DEFAULT NULL,
  `position` int DEFAULT NULL,
  `q1` text,
  `q2` text,
  `q3` text,
  PRIMARY KEY (`qualifyId`),
  KEY `fk_qualifying_raceId_idx` (`raceId`),
  KEY `fk_qualifying_driverId_idx` (`driverId`),
  KEY `fk_qualifying_constructorId_idx` (`constructorId`),
  CONSTRAINT `fk_qualifying_constructorId` FOREIGN KEY (`constructorId`) REFERENCES `constructors` (`constructorId`),
  CONSTRAINT `fk_qualifying_driverId` FOREIGN KEY (`driverId`) REFERENCES `drivers` (`driverId`),
  CONSTRAINT `fk_qualifying_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qualifying`
--

LOCK TABLES `qualifying` WRITE;
/*!40000 ALTER TABLE `qualifying` DISABLE KEYS */;
/*!40000 ALTER TABLE `qualifying` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `races`
--

DROP TABLE IF EXISTS `races`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `races` (
  `raceId` int NOT NULL AUTO_INCREMENT,
  `year` int DEFAULT NULL,
  `round` int DEFAULT NULL,
  `circuitId` int NOT NULL,
  `name` text,
  `date` text,
  `time` text,
  `url` text,
  `fp1_date` text,
  `fp1_time` text,
  `fp2_date` text,
  `fp2_time` text,
  `fp3_date` text,
  `fp3_time` text,
  `quali_date` text,
  `quali_time` text,
  `sprint_date` text,
  `sprint_time` text,
  PRIMARY KEY (`raceId`),
  KEY `fk_races_circuitId_idx` (`circuitId`),
  CONSTRAINT `fk_races_circuitId` FOREIGN KEY (`circuitId`) REFERENCES `circuits` (`circuitId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `races`
--

LOCK TABLES `races` WRITE;
/*!40000 ALTER TABLE `races` DISABLE KEYS */;
/*!40000 ALTER TABLE `races` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `resultId` int NOT NULL AUTO_INCREMENT,
  `raceId` int NOT NULL,
  `driverId` int NOT NULL,
  `constructorId` int NOT NULL,
  `number` int DEFAULT NULL,
  `grid` int DEFAULT NULL,
  `position` int DEFAULT NULL,
  `positionText` text,
  `positionOrder` int DEFAULT NULL,
  `points` int DEFAULT NULL,
  `laps` int DEFAULT NULL,
  `time` text,
  `milliseconds` int DEFAULT NULL,
  `fastestLap` int DEFAULT NULL,
  `rank` int DEFAULT NULL,
  `fastestLapTime` text,
  `fastestLapSpeed` double DEFAULT NULL,
  `statusId` int NOT NULL,
  PRIMARY KEY (`resultId`),
  KEY `fk_results_raceId_idx` (`raceId`),
  KEY `fk_results_driverId_idx` (`driverId`),
  KEY `fk_results_constructorId_idx` (`constructorId`),
  KEY `fk_results_statusId_idx` (`statusId`),
  CONSTRAINT `fk_results_constructorId` FOREIGN KEY (`constructorId`) REFERENCES `constructors` (`constructorId`),
  CONSTRAINT `fk_results_driverId` FOREIGN KEY (`driverId`) REFERENCES `drivers` (`driverId`),
  CONSTRAINT `fk_results_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`),
  CONSTRAINT `fk_results_statusId` FOREIGN KEY (`statusId`) REFERENCES `status` (`statusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seasons`
--

DROP TABLE IF EXISTS `seasons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seasons` (
  `year` int NOT NULL,
  `url` text,
  PRIMARY KEY (`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seasons`
--

LOCK TABLES `seasons` WRITE;
/*!40000 ALTER TABLE `seasons` DISABLE KEYS */;
/*!40000 ALTER TABLE `seasons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sprint_results`
--

DROP TABLE IF EXISTS `sprint_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sprint_results` (
  `sprintResultId` int NOT NULL AUTO_INCREMENT,
  `raceId` int NOT NULL,
  `driverId` int NOT NULL,
  `constructorId` int NOT NULL,
  `number` int DEFAULT NULL,
  `grid` int DEFAULT NULL,
  `position` int DEFAULT NULL,
  `positionText` text,
  `positionOrder` int DEFAULT NULL,
  `points` int DEFAULT NULL,
  `laps` int DEFAULT NULL,
  `time` text,
  `milliseconds` int DEFAULT NULL,
  `fastestLap` int DEFAULT NULL,
  `fastestLapTime` text,
  `statusId` int NOT NULL,
  PRIMARY KEY (`sprintResultId`),
  KEY `fk_sprint_results_raceId_idx` (`raceId`),
  KEY `fk_sprint_results_driverId_idx` (`driverId`),
  KEY `fk_sprint_results_constructorId_idx` (`constructorId`),
  KEY `fk_sprint_results_statusId_idx` (`statusId`),
  CONSTRAINT `fk_sprint_results_constructorId` FOREIGN KEY (`constructorId`) REFERENCES `constructors` (`constructorId`),
  CONSTRAINT `fk_sprint_results_driverId` FOREIGN KEY (`driverId`) REFERENCES `drivers` (`driverId`),
  CONSTRAINT `fk_sprint_results_raceId` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`),
  CONSTRAINT `fk_sprint_results_statusId` FOREIGN KEY (`statusId`) REFERENCES `status` (`statusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sprint_results`
--

LOCK TABLES `sprint_results` WRITE;
/*!40000 ALTER TABLE `sprint_results` DISABLE KEYS */;
/*!40000 ALTER TABLE `sprint_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `statusId` int NOT NULL AUTO_INCREMENT,
  `status` text,
  PRIMARY KEY (`statusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
