-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 13, 2022 at 07:41 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pc`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_pay`
--

CREATE TABLE `emp_pay` (
  `em_id` int(11) NOT NULL,
  `name` int(11) NOT NULL,
  `scale` int(11) NOT NULL,
  `pay` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp_pay`
--

INSERT INTO `emp_pay` (`em_id`, `name`, `scale`, `pay`) VALUES
(1, 1, 1, 150),
(2, 2, 2, 200),
(1, 1, 1, 150),
(2, 2, 2, 200);

-- --------------------------------------------------------

--
-- Table structure for table `staff_info`
--

CREATE TABLE `staff_info` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `lastname` text NOT NULL,
  `lvl` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff_info`
--

INSERT INTO `staff_info` (`id`, `name`, `lastname`, `lvl`) VALUES
(1, 'cca', 'bxa', 1),
(2, 'bba', 'MBBs', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_pay`
--
ALTER TABLE `emp_pay`
  ADD KEY `emp_id_fk` (`em_id`);

--
-- Indexes for table `staff_info`
--
ALTER TABLE `staff_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `staff_info`
--
ALTER TABLE `staff_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `emp_pay`
--
ALTER TABLE `emp_pay`
  ADD CONSTRAINT `emp_pay_ibfk_1` FOREIGN KEY (`em_id`) REFERENCES `staff_info` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
