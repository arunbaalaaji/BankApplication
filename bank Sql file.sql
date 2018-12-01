-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 12, 2018 at 02:38 PM
-- Server version: 5.5.24-log
-- PHP Version: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE IF NOT EXISTS `account` (
  `userid` int(11) DEFAULT NULL,
  `accno` int(11) NOT NULL AUTO_INCREMENT,
  `balance` float DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`accno`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`userid`, `accno`, `balance`, `type`) VALUES
(1, 1, 9900, 'saving'),
(2, 2, 5600, 'Saving'),
(3, 3, 7001, 'saving'),
(5, 5, 100000, 'current'),
(6, 6, 10000, 'current'),
(7, 7, 2000, 'saving');

-- --------------------------------------------------------

--
-- Table structure for table `closed`
--

CREATE TABLE IF NOT EXISTS `closed` (
  `userid` int(11) DEFAULT NULL,
  `accno` int(11) DEFAULT NULL,
  `closedate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `closed`
--

INSERT INTO `closed` (`userid`, `accno`, `closedate`) VALUES
(4, 4, '2017-12-04');

-- --------------------------------------------------------

--
-- Table structure for table `fixed`
--

CREATE TABLE IF NOT EXISTS `fixed` (
  `userid` int(11) DEFAULT NULL,
  `fdid` int(11) NOT NULL AUTO_INCREMENT,
  `duration` int(2) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `start` date DEFAULT NULL,
  PRIMARY KEY (`fdid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `fixed`
--

INSERT INTO `fixed` (`userid`, `fdid`, `duration`, `amount`, `start`) VALUES
(1, 1, 13, 2000, '2017-12-05'),
(6, 2, 12, 2000, '2017-12-05');

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE IF NOT EXISTS `loan` (
  `userid` int(11) DEFAULT NULL,
  `loanid` int(11) NOT NULL AUTO_INCREMENT,
  `lamount` float DEFAULT NULL,
  `repayterm` int(11) DEFAULT NULL,
  `start` date DEFAULT NULL,
  PRIMARY KEY (`loanid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`userid`, `loanid`, `lamount`, `repayterm`, `start`) VALUES
(2, 1, 2000, 1, '2017-12-05');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `userid` int(11) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`userid`, `password`) VALUES
(1, 'pass'),
(2, 'p123'),
(3, 'vanibass'),
(5, 'arun'),
(6, 'mepco'),
(7, 'raj');

-- --------------------------------------------------------

--
-- Table structure for table `trans`
--

CREATE TABLE IF NOT EXISTS `trans` (
  `userid` int(11) DEFAULT NULL,
  `accno` int(11) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `tdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `trans`
--

INSERT INTO `trans` (`userid`, `accno`, `type`, `amount`, `tdate`) VALUES
(1, 1, 'deposit', 5000, '2017-12-04'),
(2, 2, 'deposit', 1000, '2017-12-04'),
(3, 3, 'deposit', 2000, '2017-12-04'),
(1, 1, 'deposit', 500, '2017-12-04'),
(5, 5, 'deposit', 100000, '2017-12-05'),
(2, 2, 'Loancredit', 2000, '2017-12-05'),
(6, 6, 'deposit', 1000, '2017-12-05'),
(6, 6, 'deposit', 8000, '2017-12-05'),
(6, 6, 'withdraw', 1000, '2017-12-05');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE IF NOT EXISTS `transaction` (
  `userid` int(11) DEFAULT NULL,
  `fromacc` int(11) DEFAULT NULL,
  `toacc` int(11) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `transdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`userid`, `fromacc`, `toacc`, `amount`, `transdate`) VALUES
(1, 1, 2, 500, '2017-12-04'),
(5, 5, 3, 5001, '2017-12-05'),
(6, 6, 1, 4000, '2017-12-05'),
(1, 1, 2, 100, '2018-03-17');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(10) DEFAULT NULL,
  `lname` varchar(10) DEFAULT NULL,
  `phone` bigint(10) DEFAULT NULL,
  `addressline1` varchar(20) DEFAULT NULL,
  `addressline2` varchar(15) DEFAULT NULL,
  `city` varchar(10) DEFAULT NULL,
  `state` varchar(10) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userid`, `fname`, `lname`, `phone`, `addressline1`, `addressline2`, `city`, `state`, `pin`) VALUES
(1, 'Arun', 'Balaji', 9636543211, 'Ramstreet', 'rr nagar', 'Madurai', 'Tamilnadu', 625009),
(2, 'Surya', 'Reo', 7845555962, 'Eng street', 'kk nagar', 'madurai', 'tamil nadu', 625009),
(3, 'hari', 'krish', 8667253688, 'Ragu st', 'Kalavasal', 'Madurai', 'Tamil nadu', 625005),
(5, 'arunbal', 'sps', 9445982779, 'colony', 'svks', 'sivakasi', 'tamilnadu', 626123),
(6, 'ram', 'kumar', 9876543210, '2nd street', 'kk nagar', 'chennai', 'tamil nadu', 600030),
(7, 'Raju', 'M', 8907654321, 'annanagar', 'r colony', 'Erode', 'Tamil nadu', 623007);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
