-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2017-12-14 21:14:58
-- 服务器版本： 5.5.56-log
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `focus`
--

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `userid` varchar(16) NOT NULL COMMENT 'student id',
  `name` varchar(32) DEFAULT NULL COMMENT 'real name',
  `school` varchar(128) DEFAULT NULL COMMENT 'school name',
  `gender` varchar(8) DEFAULT NULL COMMENT 'in Chinese',
  `percentage` float DEFAULT '0' COMMENT 'percentage %0.4f',
  `avatar` int(3) NOT NULL,
  `total_time` int(11) DEFAULT '0',
  `total_study` int(11) DEFAULT '0',
  `this_class_start` int(11) DEFAULT '-1',
  `this_class_end` int(11) DEFAULT '0',
  `this_start` int(11) DEFAULT '-1',
  `this_study` int(11) DEFAULT '0',
  `last_name` varchar(64) DEFAULT NULL,
  `last_total` int(11) DEFAULT '0',
  `last_study` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`userid`, `name`, `school`, `gender`, `percentage`, `avatar`, `total_time`, `total_study`, `this_class_start`, `this_class_end`, `this_start`, `this_study`, `last_name`, `last_total`, `last_study`) VALUES
('6108117001', '万伟强', '信息工程学院', '男', 0, 8, 0, 0, -1, 0, -1, 0, NULL, 0, 0),
('6109117204', '易晟', '信息工程学院', '男', 0.318416, 3, 54300, 17290, 35100, 43800, -1, 0, NULL, 0, 0),
('6109117208', '彭瀚林', '信息工程学院', '男', 0.546185, 8, 60009, 32776, -1, 0, -1, 0, NULL, 0, 0),
('8207667209', 'test', '信息工程学院', '男', 0, 2, 0, 0, -1, 0, -1, 0, NULL, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `users_username_uindex` (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
