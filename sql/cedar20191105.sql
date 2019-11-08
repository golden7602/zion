-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.63-MariaDB - mariadb.org binary distribution
-- 服务器操作系统:                      Win32
-- HeidiSQL 版本:                  9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 cedar 的数据库结构
DROP DATABASE IF EXISTS `cedar`;
CREATE DATABASE IF NOT EXISTS `cedar` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `cedar`;

-- 导出  表 cedar.sysconfig 结构
DROP TABLE IF EXISTS `sysconfig`;
CREATE TABLE IF NOT EXISTS `sysconfig` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fName` varchar(50) DEFAULT NULL,
  `fValueInt` int(11) DEFAULT NULL,
  `fValueStr` text,
  `fValueBool` bit(1) DEFAULT NULL,
  `fValueDate` date DEFAULT NULL,
  `fValueDateTime` datetime DEFAULT NULL,
  `TS` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fValue` longtext,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.sysconfig 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `sysconfig` DISABLE KEYS */;
INSERT INTO `sysconfig` (`fID`, `fName`, `fValueInt`, `fValueStr`, `fValueBool`, `fValueDate`, `fValueDateTime`, `TS`, `fValue`) VALUES
	(3, 'configValue', NULL, NULL, NULL, NULL, NULL, '2019-09-17 16:33:31', 'gAN9cQAoWBIAAABOb3RlX1ByaW50aW5nT3JkZXJxAVjhAAAATm90ZToKRXN0YSBvcmRlbSBzZXJhIGVudHJlZ3VlIGVtIDEwIGRpYXMgZGUgdHJhYmFsaG8sIHNlIGVzdGEgZm9yIHVyZ2VudGUsZSBuZWNlc3NhcmlvIHBhZ2FyIG1haXMgMjQwJS4gUGFyYSBxdWUgbmFvIGFmZWN0ZSBvcyB0cnJhYmFsaG9zIGRpYXJpb3MgZGEgdm9zc2EgZW1wcmVzYSxwb3IgZmF2b3IsIGVuY29tZW5kZW0gYSB2b3NzYSBvcmRlbSAgbyBtYWlzIHJhcGlkbyBwb3NzaXZlbC4KcQJYDAAAAEJhbmtfQWNjb3VudHEDWHkAAABDb250YSBCYW5jYXJpYTogIE1PWkEgQkFOQ08KTm9tZSBkYSBDb250YTogQ09MT1BSTyBTSU5HUyAmIFBSSU5USU5HCk5vIGRhIENvbnRhOiAxNTQ2NjMxODEwMDAxCk5JQjogMDAzNDAwMDAxNTQ2NjMxODEwMTU5cQRYFQAAAE51bGxfcHJvbXB0X2JhY19jb2xvcnEFY1B5UXQ1LnNpcApfdW5waWNrbGVfdHlwZQpxBlgLAAAAUHlRdDUuUXRHdWlxB1gGAAAAUUNvbG9ycQgoS/9LAEsAS/90cQmHcQpScQtYDwAAAEF1dG9TaHJpbmtGb250c3EMiFgMAAAAQXV0b0VsbGlwc2lzcQ2JWB0AAABQcmludEhpZ2hsaWdodEJhY2tncm91bmRDb2xvcnEOaAZoB1gGAAAAUUNvbG9ycQ8oS8JLwkvCS/90cRCHcRFScRJYDwAAAEJpbGxDb3B5c19PcmRlcnETWCoAAABhdGVuZGltZW50bzsxO3Byb2R1Y2FvOzA7Y2xpZW50ZTsxO2NhaXhhOzFxFFgXAAAAQmlsbENvcHlzX1ByaW50aW5nT3JkZXJxFVgqAAAAYXRlbmRpbWVudG87MTtwcm9kdWNhbzswO2NsaWVudGU7MTtjYWl4YTsxcRZYFwAAAEJpbGxDb3B5c19PdXRib3VuZE9yZGVycRdYKgAAAGF0ZW5kaW1lbnRvOzE7cHJvZHVjYW87MDtjbGllbnRlOzE7Y2FpeGE7MXEYWBsAAABCaWxsQ29weXNfV2FyZWhvdXNlUnJlY2VpcHRxGVgqAAAAYXRlbmRpbWVudG87MTtwcm9kdWNhbzswO2NsaWVudGU7MTtjYWl4YTsxcRpYGQAAAEF1dG9SZWZyZXNoV2hlbkRhdGFDaGFuZ2VxG4hYGAAAAEJ1YmJsZVRpcHNXaGVuRGF0YUNoYW5nZXEciFgYAAAAQmlsbENvcHlzX1F1b3RhdGlvbk9yZGVycR1YDQAAAGF0ZW5kaW1lbnRvOzFxHlggAAAAQmlsbENvcHlzX1F1b3RhdGlvblByaW50aW5nT3JkZXJxH1gYAAAAYXRlbmRpbWVudG87MTtwcm9kdWNhbzswcSBYDQAAAFRheFJlZ0NlclBhdGhxIVgMAAAARTovWmlvbi96aW9ucSJ1Lg==');
/*!40000 ALTER TABLE `sysconfig` ENABLE KEYS */;

-- 导出  表 cedar.sysnavigationmenus 结构
DROP TABLE IF EXISTS `sysnavigationmenus`;
CREATE TABLE IF NOT EXISTS `sysnavigationmenus` (
  `fNMID` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `fDispIndex` int(11) DEFAULT NULL COMMENT '显示顺序',
  `fParentId` int(11) DEFAULT NULL COMMENT '上级编号',
  `fEnabled` bit(1) NOT NULL DEFAULT b'1' COMMENT '可用',
  `fMenuText` char(60) DEFAULT NULL COMMENT '文本',
  `fCommand` tinyint(4) NOT NULL DEFAULT '0' COMMENT '命令',
  `fObjectName` char(50) DEFAULT NULL COMMENT '对象名',
  `fFormMode` tinyint(2) DEFAULT NULL COMMENT '模式',
  `fArg` char(255) DEFAULT NULL COMMENT '参数',
  `fIcon` char(50) DEFAULT NULL COMMENT '图标',
  `fDefault` bit(1) NOT NULL DEFAULT b'0' COMMENT '默认',
  `fNodeBackvolor` int(11) DEFAULT NULL COMMENT '背景色',
  `fNodeForeColor` int(11) DEFAULT NULL COMMENT '前景色',
  `fNodeFontBold` tinyint(1) NOT NULL DEFAULT '0' COMMENT '加粗',
  `fExpanded` tinyint(1) NOT NULL DEFAULT '1' COMMENT '展开',
  `fDescription` char(255) DEFAULT NULL COMMENT '说明',
  `fLevel` bit(1) NOT NULL DEFAULT b'0' COMMENT '级别',
  `fIsCommandButton` bit(1) DEFAULT b'0' COMMENT '是否按钮',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fNMID`),
  KEY `ParentID` (`fParentId`)
) ENGINE=InnoDB AUTO_INCREMENT=186 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.sysnavigationmenus 的数据：~105 rows (大约)
/*!40000 ALTER TABLE `sysnavigationmenus` DISABLE KEYS */;
INSERT INTO `sysnavigationmenus` (`fNMID`, `fDispIndex`, `fParentId`, `fEnabled`, `fMenuText`, `fCommand`, `fObjectName`, `fFormMode`, `fArg`, `fIcon`, `fDefault`, `fNodeBackvolor`, `fNodeForeColor`, `fNodeFontBold`, `fExpanded`, `fDescription`, `fLevel`, `fIsCommandButton`, `TS`) VALUES
	(1, 110, 0, b'1', 'Function', 0, '', 0, '', 'home', b'1', NULL, NULL, 0, 1, '', b'0', b'0', '2019-04-20 13:45:28'),
	(2, 40, 71, b'1', 'Order', 2, 'f_Order', -1, '', 'application_form.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 14:14:36'),
	(6, 190, 1, b'0', 'Design', 0, '', 0, '', '', b'0', NULL, NULL, 0, 1, '', b'0', b'0', '2019-05-17 13:52:42'),
	(9, 200, 1, b'1', 'Payment', 2, 'f_PaymentOrder', -1, '', 'payment.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 14:02:56'),
	(10, 450, 11, b'1', 'Enumeration', 2, 'SysfrmEnumeration', -1, '', 'enum.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 14:03:01'),
	(11, 440, 1, b'1', 'Setup', 0, '', 0, '', 'setup.png', b'0', NULL, NULL, 0, 1, '', b'0', b'0', '2019-07-18 11:38:11'),
	(12, 999999990, 1, b'1', 'Exit', 3, 'Application_Quit', 0, '', 'exit.png', b'1', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 13:53:18'),
	(13, 120, 11, b'1', 'User', 2, 'SysfrmUsers', -1, '', 'user.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 13:53:30'),
	(14, 480, 11, b'1', 'Config', 2, 'SysfrmConfig', -1, '', 'config.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 13:58:46'),
	(15, 300, 1, b'1', 'Complete', 2, 'f_Complete', -1, '', 'delivery.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 13:51:54'),
	(17, 510, 11, b'1', 'Help', 2, 'f_Help', -1, '', 'help.png', b'1', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 13:51:30'),
	(18, 350, 1, b'1', 'Adjustment', 2, 'f_Adjustment', -1, '', 'edit.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 13:58:10'),
	(19, 500, 11, b'1', 'Language', 2, 'SysfrmLanguage', -1, '', 'translate.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-20 12:26:58'),
	(20, 250, 1, b'1', 'Receivables', 2, 'f_Receivables', -1, '', 'Receivables.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-07-18 11:33:38'),
	(21, 410, 1, b'1', 'Report', 0, '', 0, '', 'reports.png', b'0', NULL, NULL, 0, 1, '', b'0', b'0', '2019-05-17 14:14:29'),
	(22, 420, 21, b'1', 'RecYearReport', 2, 'f_report_day', -1, '', 'month.png', b'0', NULL, NULL, 0, 0, '', b'0', b'0', '2019-05-17 13:59:06'),
	(54, 520, 1, b'1', 'Quotation', 0, '', 0, NULL, 'folder.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-05-17 13:50:09'),
	(55, 530, 54, b'1', 'PrintingOrderQuotation', 2, 'f_Quotation_Prt', -1, NULL, 'folder.png', b'0', NULL, NULL, 0, 0, NULL, b'0', b'0', '2019-05-17 14:21:00'),
	(56, 540, 54, b'1', 'OrderQuotation', 2, 'f_Quotation_O', -1, NULL, 'OrderQuotation.png', b'0', NULL, NULL, 0, 0, NULL, b'0', b'0', '2019-07-18 11:35:56'),
	(71, 10, 1, b'1', 'Order', 0, '', 0, NULL, 'folder.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-05-17 13:50:09'),
	(72, 50, 71, b'1', 'PrintOrder', 2, 'f_PrintingOrder', -1, NULL, 'folder.png', b'0', NULL, NULL, 0, 0, NULL, b'0', b'0', '2019-05-17 14:21:11'),
	(73, 30, 1, b'1', 'Customer', 2, 'f_Customer', -1, NULL, 'customers.png', b'0', NULL, NULL, 0, 0, NULL, b'0', b'0', '2019-05-17 14:16:14'),
	(80, 800, 14, b'1', 'Ok', 0, 'CmdOk', NULL, NULL, 'Ok.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-07-15 18:38:01'),
	(81, 202, 2, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:22:17'),
	(82, 201, 2, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:22:19'),
	(83, 207, 2, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(84, 203, 2, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-29 16:08:16'),
	(85, 204, 2, b'1', 'Submit', 0, 'CmdSubmit', NULL, NULL, 'Submit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:22:26'),
	(86, 205, 2, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:22:28'),
	(87, 206, 2, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(88, 2001, 20, b'1', 'Recibido', 0, 'CmdRecibido', NULL, NULL, 'Recibido.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:21:47'),
	(89, 2005, 20, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(90, 2003, 20, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:21:53'),
	(91, 2004, 20, b'1', 'DailyRreport', 0, 'CmdDailyRreport', NULL, NULL, 'DailyRreport.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:21:56'),
	(92, 7302, 73, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:36:41'),
	(93, 7301, 73, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:36:36'),
	(94, 7304, 73, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:36:50'),
	(95, 950, 73, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(97, 970, 9, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-07-15 18:38:01'),
	(98, 980, 9, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-07-15 18:38:01'),
	(99, 990, 9, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(100, 1000, 9, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-07-15 18:38:01'),
	(101, 982, 9, b'1', 'Confirm', 0, 'CmdConfirm', NULL, NULL, 'tick.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-29 00:10:12'),
	(102, 1020, 9, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(103, 7202, 72, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:29:54'),
	(104, 7201, 72, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:29:50'),
	(105, 7207, 72, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(106, 7203, 72, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:30:15'),
	(107, 7204, 72, b'1', 'Submit', 0, 'CmdSubmit', NULL, NULL, 'Submit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:30:08'),
	(108, 7205, 72, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:30:23'),
	(109, 7206, 72, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(110, 1501, 15, b'1', 'Complete', 0, 'CmdComplete', NULL, NULL, 'delivery.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:16:05'),
	(111, 1506, 15, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(112, 1502, 15, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:32:16'),
	(113, 1503, 15, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:32:19'),
	(114, 1504, 15, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(115, 5502, 55, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:33:51'),
	(116, 5501, 55, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:33:45'),
	(117, 5507, 55, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(118, 5503, 55, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:33:55'),
	(119, 5504, 55, b'1', 'Order', 0, 'CmdOrder', NULL, NULL, 'Order.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:34:04'),
	(120, 5505, 55, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:34:09'),
	(121, 5506, 55, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(122, 1804, 18, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(123, 1800, 18, b'1', 'Adjustment', 0, 'CmdAdjustment', NULL, NULL, 'edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:15:28'),
	(124, 1803, 18, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:33:13'),
	(125, 1801, 18, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:32:48'),
	(126, 1805, 18, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(127, 1802, 18, b'1', 'Cancel', 0, 'CmdCancel', NULL, NULL, 'Cancel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:33:08'),
	(128, 5602, 56, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:34:51'),
	(129, 5601, 56, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:34:34'),
	(130, 5607, 56, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-24 10:06:14'),
	(131, 5603, 56, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:34:55'),
	(132, 5604, 56, b'1', 'Order', 0, 'CmdOrder', NULL, NULL, 'Order.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:35:00'),
	(133, 5605, 56, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:35:04'),
	(134, 5606, 56, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 18:14:15'),
	(135, 1350, 13, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-07-15 18:38:01'),
	(136, 1360, 13, b'1', 'Delete', 0, 'CmdDelete', NULL, NULL, 'Delete.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-07-15 18:38:01'),
	(137, 1370, 13, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-07-15 18:38:01'),
	(145, 7303, 73, b'1', 'Delete', 0, 'CmdDelete', NULL, NULL, 'Delete.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-22 19:36:46'),
	(147, 515, 11, b'1', 'BackupData', 2, 'SysfrmBackupData', -1, NULL, 'backup.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-05-17 14:20:51'),
	(148, 411, 1, b'1', 'CustomerArrears', 0, 'f_Customer_Arrears', -1, NULL, 'query.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-08-22 20:33:41'),
	(149, 2002, 20, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-23 12:21:35'),
	(150, 14801, 148, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-08-28 19:48:44'),
	(151, 191, 1, b'1', 'Inventory', 0, NULL, NULL, NULL, 'folder.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-10-10 10:39:48'),
	(152, 15101, 151, b'1', 'OutBoundOrder', 2, 'OutBoundOrder', -1, NULL, 'sales.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-10-14 17:05:55'),
	(153, 202, 152, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(154, 201, 152, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(155, 207, 152, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(156, 203, 152, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(157, 204, 152, b'1', 'Submit', 0, 'CmdSubmit', NULL, NULL, 'Submit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(158, 205, 152, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(159, 206, 152, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(160, 15102, 151, b'1', 'WarehouseReceipt', 0, 'WarehouseReceipt', NULL, NULL, 'buy.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-10-14 17:06:02'),
	(161, 202, 160, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(162, 201, 160, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(163, 207, 160, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(164, 203, 160, b'1', 'Browse', 0, 'CmdBrowse', NULL, NULL, 'Browse.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(165, 204, 160, b'1', 'Submit', 0, 'CmdSubmit', NULL, NULL, 'Submit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(166, 205, 160, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(167, 206, 160, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-10 11:00:53'),
	(168, 15103, 151, b'1', 'ProductInformation', 0, 'ProductInformation', NULL, NULL, 'stock.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-10-14 17:06:09'),
	(169, 7302, 168, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-14 16:46:43'),
	(170, 7301, 168, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-14 16:46:43'),
	(171, 7304, 168, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-14 16:46:43'),
	(173, 7303, 168, b'1', 'Delete', 0, 'CmdDelete', NULL, NULL, 'Delete.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-14 16:46:43'),
	(176, 31, 1, b'1', 'Supplier', 0, 'Supplier', NULL, NULL, 'suppliers.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-10-16 08:08:23'),
	(177, 7302, 176, b'1', 'Edit', 0, 'CmdEdit', NULL, NULL, 'Edit.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-15 17:44:40'),
	(178, 7301, 176, b'1', 'New', 0, 'CmdNew', NULL, NULL, 'New.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-15 17:44:40'),
	(179, 7304, 176, b'1', 'Refresh', 0, 'CmdRefresh', NULL, NULL, 'Refresh.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-15 17:44:40'),
	(180, 950, 176, b'1', 'Search', 0, 'CmdSearch', NULL, NULL, 'folder_explore.ico', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-15 17:44:40'),
	(181, 7303, 176, b'1', 'Delete', 0, 'CmdDelete', NULL, NULL, 'Delete.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-15 17:44:40'),
	(184, 16809, 168, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-18 09:37:16'),
	(185, 16810, 168, b'1', 'Print', 0, 'CmdPrint', NULL, NULL, 'print.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-18 09:39:54');
/*!40000 ALTER TABLE `sysnavigationmenus` ENABLE KEYS */;

-- 导出  表 cedar.systabelautokeyroles 结构
DROP TABLE IF EXISTS `systabelautokeyroles`;
CREATE TABLE IF NOT EXISTS `systabelautokeyroles` (
  `fRoleID` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `fRoleName` varchar(50) NOT NULL COMMENT '名称',
  `fTabelName` varchar(50) NOT NULL COMMENT '表名',
  `fFieldName` varchar(50) NOT NULL COMMENT '字段名',
  `fHasDateTime` bit(1) NOT NULL DEFAULT b'0' COMMENT '有时间',
  `fPreFix` varchar(50) NOT NULL COMMENT '前缀',
  `fCurrentValue` int(10) unsigned zerofill DEFAULT NULL COMMENT '当前值',
  `fLenght` tinyint(4) NOT NULL DEFAULT '6' COMMENT '长度',
  `fLastKey` varchar(255) DEFAULT NULL COMMENT '最后生成键值',
  `fDateFormat` varchar(50) DEFAULT NULL COMMENT '日期格式',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fRoleID`),
  UNIQUE KEY `PreFix` (`fPreFix`),
  KEY `LastKey` (`fLastKey`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.systabelautokeyroles 的数据：~7 rows (大约)
/*!40000 ALTER TABLE `systabelautokeyroles` DISABLE KEYS */;
INSERT INTO `systabelautokeyroles` (`fRoleID`, `fRoleName`, `fTabelName`, `fFieldName`, `fHasDateTime`, `fPreFix`, `fCurrentValue`, `fLenght`, `fLastKey`, `fDateFormat`, `TS`) VALUES
	(1, 'OrderID', 't_order', 'forderID', b'1', 'CP', 0000000000, 6, 'CP2019-1028000002', 'yyyy-mmdd', '2019-10-29 12:34:12'),
	(2, 'InkjetPrintingGuide_ID', 't_InkjetPrintingGuide', 'InkjetPrintingGuide_ID', b'1', 'PG', 0000000000, 6, '0', 'yyyy-mmdd', '2019-04-18 12:37:08'),
	(3, 'Attachment', 't_InkjetPrintingGuide_Map', 'MapName', b'1', 'ATT', 0000000000, 10, '', 'yyyymmdd', '2019-04-18 12:37:08'),
	(4, 'PrintingQuoteID', 't_quotation', 'fQuoteID', b'1', 'QP', 0000000000, 6, 'QP2019-1017000002', 'yyyy-mmdd', '2019-10-28 16:51:30'),
	(5, 'PrintingOderID', 't_order', 'fOrderID', b'1', 'TP', 0000000000, 6, 'TP2019-1026000020', 'yyyy-mmdd', '2019-10-28 16:51:30'),
	(6, 'OrderQuoteID', 't_Quotation', 'fQuoteID', b'1', 'QS', 0000000000, 6, 'QS2019-1011000006', 'yyyy-mmdd', '2019-10-28 16:51:30'),
	(7, 'OuttboundOrderID', 't_product_outbound_order', 'fOrderID', b'1', 'PO', 0000000000, 6, 'PO2019-1029000003', 'yyyy-mmdd', '2019-10-29 12:34:12');
/*!40000 ALTER TABLE `systabelautokeyroles` ENABLE KEYS */;

-- 导出  表 cedar.sysuserright 结构
DROP TABLE IF EXISTS `sysuserright`;
CREATE TABLE IF NOT EXISTS `sysuserright` (
  `fID` smallint(6) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `fRightID` smallint(6) NOT NULL COMMENT '权限编号',
  `fUserID` smallint(6) NOT NULL COMMENT '用户编号',
  `fHasRight` bit(1) DEFAULT b'0' COMMENT '有权限',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`),
  UNIQUE KEY `UserID` (`fUserID`,`fRightID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.sysuserright 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `sysuserright` DISABLE KEYS */;
/*!40000 ALTER TABLE `sysuserright` ENABLE KEYS */;

-- 导出  表 cedar.sysusers 结构
DROP TABLE IF EXISTS `sysusers`;
CREATE TABLE IF NOT EXISTS `sysusers` (
  `fUserID` int(11) NOT NULL AUTO_INCREMENT,
  `fOnline` bit(1) NOT NULL DEFAULT b'0',
  `fEnabled` bit(1) NOT NULL DEFAULT b'1',
  `fDepartment` varchar(20) DEFAULT NULL,
  `fUsername` varchar(20) NOT NULL,
  `fNickname` varchar(20) DEFAULT NULL,
  `fPassword` varchar(255) NOT NULL,
  `fRoleID` smallint(6) DEFAULT NULL,
  `fLastLoginComputer` char(50) DEFAULT NULL,
  `fLastLoginTime` datetime DEFAULT NULL,
  `fLoginID` varchar(255) DEFAULT NULL,
  `fNotes` varchar(255) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fUserID`),
  KEY `LoginID` (`fLoginID`),
  KEY `RoleID` (`fRoleID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.sysusers 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `sysusers` DISABLE KEYS */;
INSERT INTO `sysusers` (`fUserID`, `fOnline`, `fEnabled`, `fDepartment`, `fUsername`, `fNickname`, `fPassword`, `fRoleID`, `fLastLoginComputer`, `fLastLoginTime`, `fLoginID`, `fNotes`, `TS`) VALUES
	(1, b'0', b'0', NULL, 'admin', '管理员', '51e599aaf7f3bf4feba2a0f9166cd709', 1, NULL, '2015-09-28 19:02:10', '{AF962165-3D2D-483B-A71B-D7D3F97502A4}', NULL, '2019-09-09 13:35:45');
/*!40000 ALTER TABLE `sysusers` ENABLE KEYS */;

-- 导出  表 cedar.t_customer 结构
DROP TABLE IF EXISTS `t_customer`;
CREATE TABLE IF NOT EXISTS `t_customer` (
  `fCustomerID` int(11) NOT NULL AUTO_INCREMENT,
  `fCustomerName` varchar(50) NOT NULL COMMENT '客户名',
  `fNUIT` varchar(25) DEFAULT NULL COMMENT '税号',
  `fCity` varchar(30) DEFAULT NULL COMMENT '所在地 Mordo',
  `fContato` varchar(20) DEFAULT NULL COMMENT '联系人',
  `fAreaCode` varchar(15) DEFAULT NULL COMMENT '区号',
  `fCelular` varchar(15) DEFAULT NULL COMMENT '手机',
  `fTelefone` varchar(15) DEFAULT NULL COMMENT '电话',
  `fEndereco` varchar(50) DEFAULT NULL COMMENT '地址',
  `fEmail` varchar(50) DEFAULT NULL COMMENT '电子邮件',
  `fWeb` varchar(50) DEFAULT NULL COMMENT '主页',
  `fFax` varchar(15) DEFAULT NULL COMMENT '传真',
  `fNote` varchar(255) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fTaxRegCer` varchar(50) DEFAULT NULL COMMENT '税务登记证',
  PRIMARY KEY (`fCustomerID`),
  UNIQUE KEY `OnlyOne` (`fCustomerName`),
  UNIQUE KEY `fNUIT` (`fNUIT`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_customer 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_customer` ENABLE KEYS */;

-- 导出  表 cedar.t_enumeration 结构
DROP TABLE IF EXISTS `t_enumeration`;
CREATE TABLE IF NOT EXISTS `t_enumeration` (
  `fItemID` int(11) NOT NULL AUTO_INCREMENT COMMENT '选项编号',
  `fTypeID` int(11) NOT NULL,
  `fTitle` varchar(50) NOT NULL,
  `fSpare1` varchar(50) DEFAULT NULL COMMENT '备用1',
  `fSpare2` varchar(50) DEFAULT NULL COMMENT '备用2',
  `fNote` varchar(255) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_enumeration 的数据：~93 rows (大约)
/*!40000 ALTER TABLE `t_enumeration` DISABLE KEYS */;
INSERT INTO `t_enumeration` (`fItemID`, `fTypeID`, `fTitle`, `fSpare1`, `fSpare2`, `fNote`, `TS`) VALUES
	(3, 5, 'PVC001', '', '', NULL, '2019-04-05 08:22:05'),
	(4, 5, 'PVC002', '', '', NULL, '2019-04-05 08:22:05'),
	(5, 5, 'PVC003', '', '', NULL, '2019-04-05 08:22:05'),
	(6, 5, 'PVC004', '', '', NULL, '2019-04-05 08:22:05'),
	(7, 5, 'PVC005', '', '', NULL, '2019-04-05 08:22:05'),
	(8, 5, 'PVC006', '', '', NULL, '2019-04-05 08:22:05'),
	(9, 5, 'PVC007', '', '', NULL, '2019-04-05 08:22:05'),
	(10, 5, 'PVC008', '', '', NULL, '2019-04-05 08:22:05'),
	(11, 5, 'PVC009', '', '', NULL, '2019-04-05 08:22:05'),
	(12, 5, 'PVC010', '', '', NULL, '2019-04-05 08:22:05'),
	(13, 5, 'VY001', '', '', NULL, '2019-04-05 08:22:05'),
	(14, 5, 'VY002', '', '', NULL, '2019-04-05 08:22:05'),
	(15, 5, 'VY003', '', '', NULL, '2019-04-05 08:22:05'),
	(16, 5, 'VY004', '', '', NULL, '2019-04-05 08:22:05'),
	(17, 5, 'VY005', '', '', NULL, '2019-04-05 08:22:05'),
	(18, 5, 'VY006', '', '', NULL, '2019-04-05 08:22:05'),
	(19, 5, 'MESP001', '', '', NULL, '2019-04-05 08:22:05'),
	(20, 5, 'MESP002', '', '', NULL, '2019-04-05 08:22:05'),
	(21, 5, 'MESP003', '', '', NULL, '2019-04-05 08:22:05'),
	(22, 5, 'MESP004', '', '', NULL, '2019-04-05 08:22:05'),
	(23, 5, 'MESP005', '', '', NULL, '2019-04-05 08:22:05'),
	(24, 5, 'MESP006', '', '', NULL, '2019-04-05 08:22:05'),
	(25, 5, 'MESP007', '', '', NULL, '2019-04-05 08:22:05'),
	(26, 5, 'MESP008', '', '', NULL, '2019-04-05 08:22:05'),
	(27, 5, 'MESP009', '', '', NULL, '2019-04-05 08:22:05'),
	(28, 5, 'MESP010', '', '', NULL, '2019-04-05 08:22:05'),
	(29, 5, 'SHP001', '', '', NULL, '2019-04-05 08:22:05'),
	(30, 5, 'SHP002', '', '', NULL, '2019-04-05 08:22:05'),
	(31, 5, 'SHP003', '', '', NULL, '2019-04-05 08:22:05'),
	(32, 5, 'SHP004', '', '', NULL, '2019-04-05 08:22:05'),
	(33, 5, 'SHP005', '', '', NULL, '2019-04-05 08:22:05'),
	(34, 5, 'SHP006', '', '', NULL, '2019-04-05 08:22:05'),
	(35, 5, 'SHP007', '', '', NULL, '2019-04-05 08:22:05'),
	(36, 5, 'SHP008', '', '', NULL, '2019-04-05 08:22:05'),
	(37, 5, 'SHP009', '', '', NULL, '2019-04-05 08:22:05'),
	(38, 5, 'SHP010', '', '', NULL, '2019-04-05 08:22:05'),
	(39, 4, '喷绘 Impressao digifal', '', '', NULL, '2019-04-05 08:22:05'),
	(40, 4, '打印  Impressao', '', '', NULL, '2019-04-05 08:22:05'),
	(41, 4, '板材打印', '', '', NULL, '2019-04-05 08:22:05'),
	(42, 4, '复印Copiar', '', '', NULL, '2019-04-05 08:22:05'),
	(43, 4, '彩色印刷 Impressão a cor', '', '', NULL, '2019-04-05 08:22:05'),
	(44, 4, '易拉宝 ROLL UP', '', '', NULL, '2019-04-05 08:22:05'),
	(45, 4, '广告牌（发光字）painel lunin', '', '', NULL, '2019-04-05 08:22:05'),
	(46, 4, '购买 Compra', '', '', NULL, '2019-04-05 08:22:05'),
	(47, 4, '其他 Outro', '', '', NULL, '2019-04-05 08:22:05'),
	(48, 1, '马普托 MAPUTO', '', '', '', '2019-07-22 14:14:35'),
	(49, 1, '南普拉 NAMPULA', '', '', NULL, '2019-04-05 08:22:05'),
	(50, 1, '贝拉 BEIRA', '', '', '', '2019-07-22 14:23:43'),
	(51, 1, '太特 TETE', '', '', NULL, '2019-04-05 08:22:05'),
	(52, 1, '南卡拉 NACALA', '', '', NULL, '2019-04-05 08:22:05'),
	(53, 1, '其他 OUTRO', '', '', NULL, '2019-04-05 08:22:05'),
	(54, 6, '80MICM', '', '', NULL, '2019-04-05 08:22:05'),
	(55, 6, '光面白底冷裱膜 80MICM', '', '', NULL, '2019-04-05 08:22:05'),
	(56, 6, '十字纹冷裱膜 SZWM', '', '', NULL, '2019-04-05 08:22:05'),
	(57, 6, '210粗纹地板膜 210MICCWDM', '', '', NULL, '2019-04-05 08:22:05'),
	(59, 3, 'Cash', '', '', NULL, '2019-04-05 08:22:05'),
	(60, 3, 'Check', '', '', NULL, '2019-04-05 08:22:05'),
	(61, 3, 'Transf', '', '', NULL, '2019-04-05 08:22:05'),
	(62, 3, 'Pos', '', '', NULL, '2019-04-05 08:22:05'),
	(63, 3, 'OUTRO', '', '', NULL, '2019-04-15 13:19:41'),
	(64, 2, 'LIVROS DE VD', '1', NULL, NULL, '2019-04-05 08:22:05'),
	(65, 2, 'RECIBOS ', '1', NULL, NULL, '2019-04-05 08:22:05'),
	(66, 2, 'FACTURA', '1', NULL, NULL, '2019-04-05 08:22:05'),
	(67, 2, 'GUIA DE REMESSA', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(68, 2, 'GUIA DE TRANSPORTE', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(69, 2, 'AGENDAS', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(70, 2, 'SENHAS', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(71, 2, 'PAPEL DE EXAME', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(72, 2, 'ATESTADO MEDICO', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(73, 2, 'CARTAO DE ESTUDANTE', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(74, 2, 'PAPEL TIMBRADO', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(75, 2, 'FOLHA DE EXERCICIO', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(76, 2, 'IMPRESSO HOSPITALAR', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(77, 2, 'OUTRO', '0', NULL, NULL, '2019-04-05 08:22:05'),
	(78, 7, '1 AVISTA', '1', NULL, NULL, '2019-05-05 16:59:35'),
	(79, 7, '2 AVISTA', '2', NULL, NULL, '2019-05-05 16:59:37'),
	(80, 7, '4 AVISTA', '4', NULL, NULL, '2019-05-05 16:59:39'),
	(81, 7, '6 AVISTA', '6', NULL, NULL, '2019-05-05 16:59:42'),
	(82, 8, 'A3', NULL, NULL, NULL, '2019-04-05 08:28:22'),
	(83, 8, 'A4', NULL, NULL, NULL, '2019-04-05 08:28:22'),
	(84, 8, 'A5', NULL, NULL, NULL, '2019-04-05 08:28:22'),
	(85, 8, 'B5', NULL, NULL, NULL, '2019-04-05 08:28:22'),
	(86, 9, '1', '1', NULL, NULL, '2019-05-05 16:59:51'),
	(87, 9, '2', '2', NULL, NULL, '2019-05-05 16:59:53'),
	(88, 9, '3', '3', NULL, NULL, '2019-05-05 16:59:55'),
	(89, 8, 'OUTRO', NULL, NULL, NULL, '2019-04-15 13:19:13'),
	(90, 10, 'OUTRO', NULL, NULL, NULL, '2019-04-15 13:19:28'),
	(91, 7, 'OUTRO', '0', NULL, NULL, '2019-05-05 16:59:08'),
	(92, 5, 'OUTRO', NULL, NULL, NULL, '2019-04-15 13:20:04'),
	(93, 9, '4', '4', NULL, NULL, '2019-05-05 16:59:57'),
	(94, 9, '5', '5', NULL, NULL, '2019-05-05 16:59:59'),
	(95, 9, '6', '6', NULL, NULL, '2019-05-05 17:00:02'),
	(96, 9, 'Outro', '0', NULL, NULL, '2019-05-05 17:00:37');
/*!40000 ALTER TABLE `t_enumeration` ENABLE KEYS */;

-- 导出  表 cedar.t_enumeration_type 结构
DROP TABLE IF EXISTS `t_enumeration_type`;
CREATE TABLE IF NOT EXISTS `t_enumeration_type` (
  `fTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `fTypeName` varchar(20) NOT NULL,
  `fNote` varchar(50) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fTypeID`),
  UNIQUE KEY `fTypeName` (`fTypeName`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_enumeration_type 的数据：~10 rows (大约)
/*!40000 ALTER TABLE `t_enumeration_type` DISABLE KEYS */;
INSERT INTO `t_enumeration_type` (`fTypeID`, `fTypeName`, `fNote`, `TS`) VALUES
	(1, '城市City', NULL, '2019-04-05 08:29:16'),
	(2, '产品类型Especie', NULL, '2019-04-05 08:29:32'),
	(3, '付款方式PaymentMethod', NULL, '2019-04-05 08:29:41'),
	(4, '产品名称Descrição', NULL, '0000-00-00 00:00:00'),
	(5, '物料编号 Número do mater', NULL, '0000-00-00 00:00:00'),
	(6, '腹膜型号Nome peritoneal', NULL, '0000-00-00 00:00:00'),
	(7, '每页序号数Avista', NULL, '2019-04-05 08:29:57'),
	(8, '尺寸Tamanho', NULL, '2019-04-05 08:29:04'),
	(9, '联次Nr.Copy', NULL, '2019-04-05 23:37:28'),
	(10, '销售Vendedor', NULL, '2019-04-05 23:56:19');
/*!40000 ALTER TABLE `t_enumeration_type` ENABLE KEYS */;

-- 导出  表 cedar.t_order 结构
DROP TABLE IF EXISTS `t_order`;
CREATE TABLE IF NOT EXISTS `t_order` (
  `fOrderID` char(20) NOT NULL COMMENT '订单号',
  `fPrice` decimal(10,2) DEFAULT NULL COMMENT '单价_印刷',
  `fCustomerID` int(11) NOT NULL COMMENT '客户编号',
  `fOrderDate` date NOT NULL COMMENT '订单日期',
  `fEspecieID` int(11) DEFAULT NULL COMMENT '印刷分类',
  `fRequiredDeliveryDate` date DEFAULT NULL COMMENT '客户要求交货日期',
  `fCategoryID` int(11) DEFAULT NULL COMMENT '类别',
  `fBrandMateriaID` int(11) DEFAULT NULL COMMENT '品牌材料',
  `fAmount` decimal(11,2) DEFAULT NULL COMMENT '金额',
  `fTax` decimal(11,2) DEFAULT NULL COMMENT '税金',
  `fPayable` decimal(11,2) DEFAULT NULL COMMENT '应付金额',
  `fDesconto` decimal(11,2) DEFAULT NULL COMMENT '折扣',
  `fColorID` int(11) DEFAULT NULL COMMENT '颜色',
  `fEntryID` int(11) DEFAULT NULL COMMENT '录入人',
  `fSubmited` bit(1) NOT NULL DEFAULT b'0' COMMENT '提交',
  `fSubmitID` int(11) DEFAULT NULL COMMENT '提交人',
  `fReviewed` bit(1) NOT NULL DEFAULT b'0' COMMENT '已审核',
  `fReviewerID` int(11) DEFAULT NULL COMMENT '审核人',
  `fConfirmed` bit(1) NOT NULL DEFAULT b'0' COMMENT '已确认',
  `fConfirmID` int(11) DEFAULT NULL COMMENT '确认人',
  `fDelivered` bit(1) NOT NULL DEFAULT b'0' COMMENT '已交付',
  `fDelivererID` int(11) DEFAULT NULL COMMENT '交付人',
  `fCanceled` bit(1) NOT NULL DEFAULT b'0' COMMENT '已作废',
  `fCancelID` int(11) DEFAULT NULL COMMENT '作废人',
  `fDeliveryDate` date DEFAULT NULL COMMENT '交付日期',
  `fNumerBegin` int(11) DEFAULT NULL COMMENT '起始编号',
  `fQuant` int(11) DEFAULT NULL COMMENT '数量',
  `fPagePerVolumn` smallint(6) DEFAULT NULL COMMENT '每本号数',
  `fNumerEnd` int(11) DEFAULT NULL COMMENT '结束编号',
  `fAvistaID` int(11) DEFAULT NULL COMMENT '每页单据数',
  `fTamanhoID` int(11) DEFAULT NULL COMMENT '尺寸',
  `fSucursal` bit(1) DEFAULT NULL COMMENT 'Sucursal 分公司',
  `fLogo` bit(1) DEFAULT b'0' COMMENT '标志',
  `fVendedorID` int(11) DEFAULT NULL COMMENT '销售人员',
  `fNrCopyID` int(11) DEFAULT NULL COMMENT '联次',
  `fContato` varchar(20) DEFAULT NULL COMMENT '联系人',
  `fCelular` varchar(15) DEFAULT NULL COMMENT '手机',
  `fTelefone` varchar(15) DEFAULT NULL COMMENT '电话',
  `fNote` varchar(255) DEFAULT NULL COMMENT '备注',
  `fDeliverViewed` bit(1) DEFAULT b'0' COMMENT '已查阅',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fOrderID`),
  KEY `iDelivererID` (`fDelivererID`),
  KEY `iOrderDate` (`fOrderDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_order 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_order` ENABLE KEYS */;

-- 导出  表 cedar.t_order_detail 结构
DROP TABLE IF EXISTS `t_order_detail`;
CREATE TABLE IF NOT EXISTS `t_order_detail` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fOrderID` char(20) DEFAULT NULL,
  `fQuant` smallint(6) DEFAULT NULL,
  `fProductName` varchar(50) DEFAULT NULL,
  `fLength` decimal(10,3) DEFAULT NULL,
  `fWidth` decimal(10,3) DEFAULT NULL,
  `fPrice` decimal(11,2) DEFAULT NULL,
  `fAmount` decimal(11,2) NOT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=216 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_order_detail 的数据：~153 rows (大约)
/*!40000 ALTER TABLE `t_order_detail` DISABLE KEYS */;
INSERT INTO `t_order_detail` (`fID`, `fOrderID`, `fQuant`, `fProductName`, `fLength`, `fWidth`, `fPrice`, `fAmount`, `TS`) VALUES
	(2, 'CP2019-0909000001', 200, 'IMP Cartao de visita laminado F/V', 1.000, 1.000, 7.00, 1400.00, '2019-09-09 14:11:41'),
	(3, 'CP2019-0909000002', 1500, ' IMP DE VINNL', 1.300, 2.500, 400.00, 1950000.00, '2019-09-09 14:17:44'),
	(4, 'CP2019-0909000003', 1500, ' IMP DE VINNL', 1.300, 2.500, 400.00, 1950000.00, '2019-09-09 15:03:32'),
	(5, 'CP2019-0910000004', 3, 'IMP/ CORTE E LAMINACAO DE VINYL', 1.039, 1.059, 800.00, 2645.76, '2019-09-10 08:36:18'),
	(6, 'CP2019-0910000005', 1, 'IMP/ DE VINIL', 1.250, 0.450, 400.00, 225.00, '2019-09-10 10:17:14'),
	(7, 'CP2019-0910000005', 1, 'IMP/ DE VINIL', 0.760, 0.595, 400.00, 182.40, '2019-09-10 10:17:14'),
	(8, 'CP2019-0910000006', 1, 'IMP/ DE VINIL', 1.015, 3.204, 400.00, 1305.60, '2019-09-10 10:27:12'),
	(9, 'CP2019-0910000007', 100, ' PROD/ DE BLOCOS A4 DUPLIC./ PAPEL NCR', 1.000, 1.000, 350.00, 35000.00, '2019-09-10 11:36:57'),
	(10, 'CP2019-0910000008', 1, 'IMP/ E LAMINACAO DE VINIL', 0.866, 0.539, 750.00, 352.35, '2019-09-10 11:50:17'),
	(11, 'CP2019-0910000009', 1, 'IMP/ EM PANO DE BANDEIRAS 1.192*3.351', 1.000, 1.000, 2500.00, 2500.00, '2019-09-10 13:50:52'),
	(12, 'CP2019-0910000010', 1, 'COMPRA DE BASE DE ROLL UP 05', 1.000, 1.000, 3500.00, 3500.00, '2019-09-10 14:47:49'),
	(13, 'CP2019-0910000011', 1, 'IMP/ DE ROLL UP EXECUTIVO 06', 1.000, 1.000, 3500.00, 3500.00, '2019-09-10 16:09:59'),
	(14, 'CP2019-0910000012', 1, 'IMP/ DE VINYL', 2.050, 1.470, 400.00, 1205.40, '2019-09-10 16:13:51'),
	(15, 'CP2019-0910000013', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.000, 1.000, 400.00, 400.00, '2019-09-10 16:36:11'),
	(16, 'CP2019-0911000014', 30, 'IMP/ E CORTE DE PANO DE BANDEIRA 0.269* 0.14*', 1.000, 1.000, 75.00, 2250.00, '2019-09-11 11:09:47'),
	(17, 'CP2019-0911000015', 1, 'IMP/ DE VINYL', 1.800, 0.900, 400.00, 648.00, '2019-09-11 11:16:50'),
	(18, 'CP2019-0911000016', 1, 'IMP/ DE BANNER P/ BACKDROP SEM ESTRUTURA', 2.980, 2.250, 400.00, 2682.00, '2019-09-11 11:44:02'),
	(19, 'CP2019-0911000017', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.850, 1.000, 400.00, 740.00, '2019-09-11 13:13:59'),
	(20, 'CP2019-0911000018', 15, 'IMP/ DE BANDEIRAS C/ COSTURA 0.60* 0.40*', 1.000, 1.000, 190.00, 2850.00, '2019-09-11 13:26:34'),
	(21, 'CP2019-0911000019', 40, 'IMP/ DE PAPEL DE FOTO 0.30* 0.40*', 1.000, 1.000, 66.00, 2640.00, '2019-09-11 13:36:18'),
	(22, 'CP2019-0911000020', 5, 'IMP/ DE VINYL', 0.720, 0.250, 400.00, 360.00, '2019-09-11 13:41:19'),
	(23, 'CP2019-0911000021', 1, 'IMP/ DE VINIL', 0.500, 1.000, 400.00, 200.00, '2019-09-11 14:49:43'),
	(24, 'CP2019-0911000022', 650, ' IMP/ A4 F/V 115 GRMS', 1.000, 1.000, 0.00, 0.00, '2019-09-11 15:24:05'),
	(26, 'CP2019-0911000023', 100, 'IMP/ A3 150 GRMS 1 FACE', 1.000, 1.000, 0.00, 0.00, '2019-09-11 15:29:17'),
	(27, 'CP2019-0911000023', 25, 'IMP/ DE CONVITE A4 1 FACE', 1.000, 1.000, 0.00, 0.00, '2019-09-11 15:32:42'),
	(28, 'CP2019-0911000024', 1, 'IMP/ DE VINIL', 1.470, 2.050, 400.00, 1205.40, '2019-09-11 15:48:51'),
	(29, 'CP2019-0911000025', 1, 'IMP/ DE VINIL', 3.000, 0.580, 400.00, 696.00, '2019-09-11 15:59:45'),
	(30, 'CP2019-0911000025', 4, 'IMP/ DE VINIL', 0.650, 0.350, 400.00, 364.00, '2019-09-11 16:00:45'),
	(31, 'CP2019-0911000025', 1, 'PROD/ DE ROLL UP 05', 1.000, 1.000, 4500.00, 4500.00, '2019-09-11 16:01:36'),
	(32, 'CP2019-0911000026', 1, 'IMP/ DE VINYL', 0.297, 0.420, 400.00, 50.40, '2019-09-11 16:15:00'),
	(33, 'CP2019-0911000026', 1, 'IMP/ DE VINYL', 1.000, 0.200, 400.00, 80.00, '2019-09-11 16:17:59'),
	(34, 'CP2019-0911000026', 1, 'IMP/ DE VINYL', 0.970, 0.280, 400.00, 108.64, '2019-09-11 16:17:59'),
	(35, 'CP2019-0911000027', 2, 'IMP/ DE VINYL', 4.150, 1.240, 400.00, 4116.80, '2019-09-11 16:48:50'),
	(36, 'CP2019-0911000027', 2, 'IMP/ DE VINYL', 4.150, 0.470, 400.00, 1560.40, '2019-09-11 16:48:50'),
	(37, 'CP2019-0912000028', 1, 'IMP/ DE BANDEIRA C/ COSTURA 1.35*0.90', 1.000, 1.000, 1200.00, 1200.00, '2019-09-12 11:09:29'),
	(38, 'CP2019-0912000029', 12, 'IMP/ DE LIVROS NCR DUPLICADO', 1.000, 1.000, 200.00, 2400.00, '2019-09-12 11:24:15'),
	(39, 'CP2019-0912000030', 6, 'IMP/ DE FATURAS', 1.000, 1.000, 200.00, 1200.00, '2019-09-12 11:25:11'),
	(40, 'CP2019-0912000030', 6, 'IMP/ DE RECIBOS', 1.000, 1.000, 200.00, 1200.00, '2019-09-12 11:25:11'),
	(41, 'CP2019-0912000031', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 2.000, 1.000, 400.00, 800.00, '2019-09-12 11:32:03'),
	(42, 'CP2019-0912000031', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 2.000, 2.000, 400.00, 1600.00, '2019-09-12 11:32:03'),
	(43, 'CP2019-0912000032', 30, 'IMP/ DE VINYL', 0.210, 0.297, 400.00, 756.00, '2019-09-12 11:36:05'),
	(45, 'CP2019-0912000033', 2, 'IMP/ DE BANNER PRETO C/ 12 ILHOSES P/ CADA', 2.000, 1.000, 400.00, 1600.00, '2019-09-12 12:09:19'),
	(46, 'CP2019-0912000034', 2, 'IMP/ DE VINIL', 0.500, 0.500, 400.00, 200.00, '2019-09-12 12:30:27'),
	(47, 'CP2019-0912000035', 1, 'IMP/ DE BANNER PRETO', 3.000, 2.300, 350.00, 2415.00, '2019-09-12 13:16:32'),
	(48, 'CP2019-0912000035', 115, 'IMP/ DE CONVITES F/V C/ DOBRA NO CENT.', 1.000, 1.000, 10.00, 1150.00, '2019-09-12 13:16:32'),
	(49, 'CP2019-0912000036', 126, 'IMP/ DE STICKERS', 0.106, 0.071, 600.00, 582.12, '2019-09-12 13:39:31'),
	(50, 'CP2019-0912000037', 2, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES P/ CADA', 2.000, 0.800, 350.00, 1120.00, '2019-09-12 13:55:47'),
	(51, 'CP2019-0912000038', 100, 'IMP/ DE BANDEIRAS C/ MARGEM DE 10 CM 1.20*0.90', 1.000, 1.000, 650.00, 65000.00, '2019-09-12 14:23:53'),
	(52, 'CP2019-0912000039', 53, 'IMP/ DE STICKERS', 0.080, 0.080, 600.00, 203.52, '2019-09-12 14:49:24'),
	(53, 'CP2019-0912000040', 1, 'IMP/ DE VINIL E RECORTE', 1.000, 1.000, 600.00, 600.00, '2019-09-12 15:05:04'),
	(54, 'CP2019-0912000041', 2, 'PROD/ DE ROLL UP 06', 1.000, 1.000, 3500.00, 7000.00, '2019-09-12 15:08:27'),
	(55, 'CP2019-0912000042', 23, 'IMP/ DE BANDEIRAS C/ COSTURA', 1.500, 0.700, 650.00, 15697.50, '2019-09-12 15:29:27'),
	(56, 'CP2019-0912000043', 3500, 'IMP/ DE FLYER A4 F/V', 1.000, 1.000, 2.90, 10150.00, '2019-09-12 15:43:45'),
	(57, 'CP2019-0912000044', 2, 'PROD/ DE ROLL UP 06', 1.000, 1.000, 3500.00, 7000.00, '2019-09-12 15:56:31'),
	(58, 'CP2019-0913000045', 42, 'IMP/ DE STICKERS', 0.201, 0.040, 600.00, 201.60, '2019-09-13 09:29:11'),
	(59, 'CP2019-0913000045', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 2.500, 2.000, 400.00, 2000.00, '2019-09-13 09:30:08'),
	(60, 'CP2019-0913000046', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 3.500, 1.000, 400.00, 1400.00, '2019-09-13 09:55:40'),
	(61, 'CP2019-0913000047', 5, 'IMP/ DE VINYL ', 2.200, 2.700, 400.00, 11880.00, '2019-09-13 10:08:38'),
	(62, 'CP2019-0913000047', 2, 'IMP/ DE VINYL', 2.200, 2.000, 400.00, 3520.00, '2019-09-13 10:08:38'),
	(63, 'CP2019-0913000048', 200, 'IMP/ DE CARTOES DE VISITA LAM MATT F/V', 1.000, 1.000, 7.00, 1400.00, '2019-09-13 10:17:52'),
	(64, 'CP2019-0913000049', 20, 'IMP/ DE IDENT. DE MESAS A5 C/ L. MATT 300GRMS', 1.000, 1.000, 20.00, 400.00, '2019-09-13 11:07:16'),
	(65, 'CP2019-0913000050', 4, 'PROD/ DE ROLL UP COMPLETO', 1.000, 1.000, 2500.00, 10000.00, '2019-09-13 11:37:24'),
	(66, 'CP2019-0913000050', 4, 'PROD/ DE ROLL UP SEM IMPRESSAO', 1.000, 1.000, 1500.00, 6000.00, '2019-09-13 11:37:24'),
	(67, 'CP2019-0913000051', 600, 'IMP/ DE CARTOES DE VISITA 1 FACEC/ L. MATT', 1.000, 1.000, 7.00, 4200.00, '2019-09-13 12:20:32'),
	(68, 'CP2019-0913000051', 100, 'IMP/ DE CARTOES DE VISITA F/V C/ L. MATT', 1.000, 1.000, 7.00, 700.00, '2019-09-13 12:20:32'),
	(69, 'CP2019-0913000052', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.500, 1.000, 300.00, 450.00, '2019-09-13 13:16:12'),
	(70, 'CP2019-0913000053', 1, 'IMP/ DE BANNER PRETO C/ MARGM DE 5CM', 1.500, 1.500, 400.00, 900.00, '2019-09-13 13:29:26'),
	(71, 'CP2019-0913000054', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.000, 0.500, 400.00, 200.00, '2019-09-13 13:49:03'),
	(72, 'CP2019-0913000055', 6, 'IMP/ DE VINYL', 1.200, 0.600, 400.00, 1728.00, '2019-09-13 13:59:21'),
	(73, 'CP2019-0913000056', 150, 'IMP/ DE STIKERS', 0.065, 0.065, 600.00, 441.00, '2019-09-13 14:30:03'),
	(74, 'CP2019-0913000057', 400, 'IMP/ DE CARTOES DE VISITA F/V C/ L. MATT', 1.000, 1.000, 7.00, 2800.00, '2019-09-13 15:50:45'),
	(75, 'CP2019-0913000057', 1, 'IMP/ DE VINIL', 0.600, 0.205, 400.00, 50.40, '2019-09-13 15:50:45'),
	(76, 'CP2019-0913000057', 1, 'IMP/ DE VINIL', 0.595, 0.760, 400.00, 182.40, '2019-09-13 15:51:10'),
	(77, 'CP2019-0913000058', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.400, 1.300, 400.00, 728.00, '2019-09-13 15:52:52'),
	(78, 'CP2019-0913000057', 1, 'IMP/ DE VINIL', 0.450, 1.250, 400.00, 225.00, '2019-09-13 15:52:55'),
	(79, 'CP2019-0913000058', 1, 'IMP/ DE VINYL', 0.880, 0.290, 400.00, 102.08, '2019-09-13 15:53:36'),
	(80, 'CP2019-0913000059', 2, 'IMP/ DE BANDEIRAS C/ COSTURA 1.35*0.90', 1.000, 1.000, 1000.00, 2000.00, '2019-09-13 16:16:36'),
	(81, 'CP2019-0913000060', 300, 'IMP DE VINNL ', 0.300, 0.900, 250.00, 20250.00, '2019-09-13 17:58:16'),
	(82, 'CP2019-0914000061', 1, 'IMP/ DE ROLL UP 07', 1.000, 1.000, 1800.00, 1800.00, '2019-09-14 08:36:37'),
	(83, 'CP2019-0914000062', 7, 'IMP/ DE ROLL UP EXECUTIVO 06', 1.000, 1.000, 3500.00, 24500.00, '2019-09-14 08:47:39'),
	(84, 'CP2019-0914000063', 2, 'IMP/ DE ROLL UP NORMAL 07', 1.000, 1.000, 1800.00, 3600.00, '2019-09-14 09:15:00'),
	(85, 'CP2019-0914000064', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 3.500, 1.000, 400.00, 1400.00, '2019-09-14 09:55:23'),
	(86, 'CP2019-0914000064', 2, 'IMP/ DE ROLL UP EXECUTIVA 06', 1.000, 1.000, 3500.00, 7000.00, '2019-09-14 10:03:14'),
	(87, 'CP2019-0914000065', 50, 'IMP/ A4 ', 1.000, 1.000, 4.00, 200.00, '2019-09-14 10:49:12'),
	(88, 'CP2019-0914000066', 1, 'IMP/ DE VINYL ', 1.000, 1.000, 400.00, 400.00, '2019-09-14 11:42:53'),
	(89, 'CP2019-0916000067', 1, 'IMP/ DE VINIL', 1.500, 1.000, 400.00, 600.00, '2019-09-16 09:06:16'),
	(90, 'CP2019-0916000068', 1, 'COMPRA DE ROLO DE VINIL', 1.000, 1.000, 6000.00, 6000.00, '2019-09-16 09:38:53'),
	(91, 'CP2019-0916000069', 1, 'IMP/ DE BANNER PRETO ', 3.000, 3.000, 400.00, 3600.00, '2019-09-16 09:58:43'),
	(92, 'CP2019-0916000070', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.500, 0.500, 400.00, 300.00, '2019-09-16 10:03:40'),
	(93, 'CP2019-0916000071', 800, 'IMP/ DE MENU A3 F/V 80G PAPEL NORMAL', 1.000, 1.000, 14.00, 11200.00, '2019-09-16 10:20:49'),
	(94, 'CP2019-0916000071', 400, 'IMP/ DE MENU A3 F/V 80G PAPEL NORMAL', 1.000, 1.000, 14.00, 5600.00, '2019-09-16 10:20:49'),
	(95, 'CP2019-0916000071', 300, 'IMP/ DE MENU 0.21*0.21 200G C/ LAMIN', 1.000, 1.000, 45.00, 13500.00, '2019-09-16 10:20:49'),
	(96, 'CP2019-0916000072', 50, 'IMP/ DE VINYL', 0.297, 0.420, 400.00, 2520.00, '2019-09-16 10:23:17'),
	(97, 'CP2019-0916000073', 200, 'IMP/ DE CARTOES DE VISITA F/V LAM MATT', 1.000, 1.000, 7.00, 1400.00, '2019-09-16 11:27:04'),
	(98, 'CP2019-0916000074', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 3.000, 1.000, 400.00, 1200.00, '2019-09-16 14:02:11'),
	(99, 'CP2019-0916000075', 2, 'COMPRA DE BASE DE ROLL UP 07', 1.000, 1.000, 1500.00, 3000.00, '2019-09-16 14:44:59'),
	(100, 'CP2019-0916000076', 2, 'IMP/ DE PVC P/ ROLL UP 06', 1.000, 1.000, 1250.00, 2500.00, '2019-09-16 15:51:59'),
	(101, 'CP2019-0916000076', 1, 'IMP/ DE BANNER PRETO P/ BACKDROP 3.0*2.25', 1.000, 1.000, 3000.00, 3000.00, '2019-09-16 15:51:59'),
	(102, 'CP2019-0917000077', 1, 'IMP/ DE CONTRAVISION', 1.700, 2.200, 550.00, 2057.00, '2019-09-17 08:08:44'),
	(103, 'CP2019-0917000078', 1, 'IMP/ DE BANNER PRETO C/ MARGENS 5CM', 2.950, 1.500, 400.00, 1770.00, '2019-09-17 09:31:07'),
	(104, 'CP2019-0917000079', 1, 'IMP/ DE BANNER PRETO ', 1.000, 0.500, 400.00, 200.00, '2019-09-17 11:49:53'),
	(105, 'CP2019-0917000080', 100, 'IMP/ DE BANDEIRA PART. FRELIMO 1.20*0.80 C/ COSTUR', 1.000, 1.000, 300.00, 30000.00, '2019-09-17 12:11:08'),
	(106, 'CP2019-0917000080', 50, 'IMP/ DE BANDEIRA DE PRESIDENTE 1.20*0.80 C/ COSTUR', 1.000, 1.000, 300.00, 15000.00, '2019-09-17 12:11:08'),
	(107, 'CP2019-0917000081', 1, 'IMP/ DE BANNER PRETO C/ 6 ILHOSES', 2.100, 1.420, 400.00, 1192.80, '2019-09-17 11:59:31'),
	(108, 'CP2019-0917000082', 5000, 'IMP/ A3', 1.000, 1.000, 5.00, 25000.00, '2019-09-17 12:18:54'),
	(109, 'CP2019-0917000083', 7, 'COMPRA DE BASE DE ROLL UP 06', 1.000, 1.000, 2300.00, 16100.00, '2019-09-17 12:24:51'),
	(110, 'CP2019-0917000083', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 2.500, 1.500, 400.00, 1500.00, '2019-09-17 12:24:51'),
	(111, 'CP2019-0917000084', 1, 'PROD/ DE ROLL UP 06', 1.000, 1.000, 3500.00, 3500.00, '2019-09-17 16:06:42'),
	(112, 'CP2019-0917000084', 1, 'IMP/ DE BANNER PRETO', 2.400, 2.400, 400.00, 2304.00, '2019-09-17 16:06:42'),
	(113, 'CP2019-0917000085', 200, 'IMP/ DE CARTOES DE VISITA F/V', 1.000, 1.000, 7.00, 1400.00, '2019-09-17 16:07:20'),
	(114, 'CP2019-0917000086', 2, 'IMP/ DE VINIL', 6.350, 2.150, 400.00, 10922.00, '2019-09-17 16:59:37'),
	(115, 'CP2019-0917000086', 1, 'IMP/ DE VINIL', 2.000, 1.850, 400.00, 1480.00, '2019-09-17 17:01:23'),
	(116, 'CP2019-0918000087', 1, 'IMP/ DE ROLL UP NORMAL 07', 1.000, 1.000, 1800.00, 1800.00, '2019-09-18 08:28:20'),
	(117, 'CP2019-0918000088', 300, 'IMP/ DE FLYERS A5 1 FACE 150GRAMAS', 1.000, 1.000, 6.00, 1800.00, '2019-09-18 09:34:55'),
	(118, 'CP2019-0918000089', 1, 'IMP/ DE BANNER PRETO ', 2.400, 2.400, 400.00, 2304.00, '2019-09-18 10:39:43'),
	(119, 'CP2019-0918000090', 1, ' IMP/ DE TEARDROP 0,699* 2,798*', 1.000, 1.000, 1500.00, 1500.00, '2019-09-18 14:53:05'),
	(120, 'CP2019-0918000091', 360, 'IMP/ DE CARTOES DE VISITA F/V LAM MATT', 1.000, 1.000, 7.00, 2520.00, '2019-09-18 15:20:29'),
	(121, 'CP2019-0918000092', 100, 'IMP/ DE CARTOES DE VISITA F/V LAM MATT', 1.000, 1.000, 7.00, 700.00, '2019-09-18 15:45:13'),
	(122, 'CP2019-0918000092', 100, 'IMP/ DE CARTOES DE VISITA 1FACE MATT', 1.000, 1.000, 7.00, 700.00, '2019-09-18 15:45:13'),
	(123, 'CP2019-0918000093', 3, 'COMPRA DE BASE DE ROLL UP 06', 1.000, 1.000, 2300.00, 6900.00, '2019-09-18 16:09:11'),
	(124, 'CP2019-0919000094', 1, 'PROD/ DE ROLL UP 06', 1.000, 1.000, 3500.00, 3500.00, '2019-09-19 08:06:01'),
	(125, 'CP2019-0919000095', 1000, 'IMP/ DE FLYERS A4 F/V 150 GRMS C/ LAMIN', 1.000, 1.000, 0.00, 0.00, '2019-09-19 08:30:51'),
	(126, 'CP2019-0919000096', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 0.800, 1.200, 400.00, 384.00, '2019-09-19 10:49:28'),
	(127, 'CP2019-0919000097', 200, 'IMP/ DE CARTOES DE VISITA F/V C/ LAM. MATT', 1.000, 1.000, 7.00, 1400.00, '2019-09-19 11:30:10'),
	(128, 'CP2019-0919000098', 300, 'IMP/ DE CARTOES DE VISITA F/V C/ LAM. MATT', 1.000, 1.000, 7.00, 2100.00, '2019-09-19 12:14:10'),
	(129, 'CP2019-0919000099', 1, 'IMP/ DE VINYL ', 2.500, 2.500, 400.00, 2500.00, '2019-09-19 13:22:40'),
	(130, 'CP2019-0919000100', 50, 'IMP/ DE STIKERS', 0.200, 0.060, 600.00, 360.00, '2019-09-19 13:43:02'),
	(131, 'CP2019-0919000100', 40, 'IMP/ DE STIKERS', 0.100, 0.100, 600.00, 240.00, '2019-09-19 13:43:02'),
	(132, 'CP2019-0919000100', 30, 'IMP/ DE STIKERS', 0.050, 0.050, 600.00, 45.00, '2019-09-19 13:43:02'),
	(133, 'CP2019-0919000100', 25, 'IMP/ DE STIKERS', 0.270, 0.060, 600.00, 243.00, '2019-09-19 13:43:02'),
	(134, 'CP2019-0919000101', 1, 'IMP/ DE BANNER PRETO C/ 6 ILHOSES', 1.500, 2.000, 400.00, 1200.00, '2019-09-19 14:11:11'),
	(135, 'CP2019-0919000102', 1, 'IMP/ DE BANNER PRETO C/ 6 ILHOSES', 3.000, 2.000, 300.00, 1800.00, '2019-09-19 14:31:47'),
	(136, 'CP2019-0919000103', 125, 'IMP/ DE A3 300GRAMAS', 1.000, 1.000, 35.00, 4375.00, '2019-09-19 14:41:25'),
	(137, 'CP2019-0919000103', 13, 'IMP/ DE A3 F/V 300GRAMAS', 1.000, 1.000, 70.00, 910.00, '2019-09-19 14:41:25'),
	(138, 'CP2019-0919000104', 300, 'IMP/ DE CARTOES DE VISITA F/V MATT', 1.000, 1.000, 7.00, 2100.00, '2019-09-19 15:36:59'),
	(139, 'CP2019-0919000105', 176, 'IMP/ DE STIKERS', 0.080, 0.050, 600.00, 422.40, '2019-09-19 15:39:30'),
	(140, 'CP2019-0920000106', 2, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES CADA', 0.800, 0.600, 400.00, 384.00, '2019-09-20 11:18:54'),
	(141, 'CP2019-0920000107', 1, 'COMPRA DE ROLO DE VINYL 1.27', 1.000, 1.000, 3500.00, 3500.00, '2019-09-20 13:01:55'),
	(142, 'CP2019-0920000108', 200, 'IMP/ DE CARTOES DE VISITA F/V C/ LAM. MATT', 1.000, 1.000, 7.00, 1400.00, '2019-09-20 13:44:25'),
	(143, 'CP2019-0920000109', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 2.000, 1.330, 300.00, 798.00, '2019-09-20 14:53:44'),
	(144, 'CP2019-0920000110', 1, 'IMP/ DE BANNER PRETO C/ 6 ILHOSES', 0.800, 2.000, 400.00, 640.00, '2019-09-20 15:24:33'),
	(145, 'CP2019-0920000111', 1, 'IMP/ DE ROLL UP NORMAL 07', 1.000, 1.000, 1800.00, 1800.00, '2019-09-20 16:25:46'),
	(146, 'CP2019-0923000112', 2, 'COMPRA DE BASE DE ROLL UL 06', 1.000, 1.000, 2500.00, 5000.00, '2019-09-23 10:08:10'),
	(147, 'CP2019-0923000113', 1, 'CORTE DE VINIL 0.46*0.66', 1.000, 1.000, 200.00, 200.00, '2019-09-23 13:34:16'),
	(148, 'CP2019-0923000114', 2, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 0.594, 0.841, 400.00, 396.48, '2019-09-23 13:16:47'),
	(149, 'CP2019-0923000115', 200, 'IMP/ DE CARTOES DE VISITA F/V LAM MATT', 1.000, 1.000, 7.00, 1400.00, '2019-09-23 13:55:49'),
	(150, 'CP2019-0923000116', 300, 'IMP/ DE CARTOES DE VISITA F/V LAM MATT', 1.000, 1.000, 7.00, 2100.00, '2019-09-23 14:47:07'),
	(151, 'CP2019-0923000117', 500, 'IMP/ DE VINYL', 0.420, 0.594, 400.00, 49560.00, '2019-09-23 15:25:33'),
	(152, 'CP2019-0923000118', 3, 'COMPRA DE BASE DE ROLL UP 06', 1.000, 1.000, 2300.00, 6900.00, '2019-09-23 16:09:56'),
	(153, 'CP2019-0924000119', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 5.000, 1.000, 400.00, 2000.00, '2019-09-24 08:33:01'),
	(154, 'CP2019-0924000120', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES ', 1.000, 1.000, 400.00, 400.00, '2019-09-24 08:53:15'),
	(155, 'CP2019-0924000121', 1, 'IMP/ DE VINYL', 1.000, 1.400, 400.00, 560.00, '2019-09-24 09:27:08'),
	(156, 'CP2019-0924000122', 1, 'IMP/ DE VINYL', 1.000, 0.868, 400.00, 348.00, '2019-09-24 11:27:25'),
	(157, 'CP2019-0924000123', 2, 'IMP/ E PEODUCAO DE MOLDURA 0.594* 0.841*', 1.000, 1.000, 2200.00, 4400.00, '2019-09-24 12:05:39'),
	(158, 'CP2019-0924000124', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.600, 1.000, 300.00, 480.00, '2019-09-24 13:35:39'),
	(159, 'CP2019-0924000125', 1, 'IMP/ DE VINYL C/ MARGENS DE 5CM', 8.900, 1.450, 400.00, 5162.00, '2019-09-24 14:16:15'),
	(160, 'CP2019-0924000126', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.400, 0.600, 400.00, 336.00, '2019-09-24 14:41:04'),
	(161, 'CP2019-0924000127', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.000, 1.000, 400.00, 400.00, '2019-09-24 15:01:00'),
	(162, 'CP2019-0924000128', 1, 'IMP/ DE VINIL', 1.500, 1.000, 400.00, 600.00, '2019-09-24 16:12:09'),
	(163, 'CP2019-0924000129', 35, 'IMP/ DE ROLL UP NORMAL 07', 1.000, 1.000, 1500.00, 52500.00, '2019-09-24 16:15:35'),
	(164, 'CP2019-0924000130', 1, 'IMP/ DE CONTRAVISION', 1.100, 2.140, 550.00, 1294.70, '2019-09-24 16:32:25'),
	(165, 'CP2019-0924000130', 1, 'IMP/ DE CONTRAVISION', 1.145, 2.150, 550.00, 1359.88, '2019-09-24 16:32:25'),
	(166, 'CP2019-0924000130', 1, 'IMP/ DE CONTRAVISION', 1.100, 2.150, 550.00, 1300.75, '2019-09-24 16:35:18'),
	(167, 'CP2019-0924000130', 1, 'IMP/ DE CONTRAVISION', 1.120, 2.150, 550.00, 1324.40, '2019-09-24 16:35:18'),
	(168, 'CP2019-0924000130', 1, 'IMP/ DE CONTRAVISION', 1.150, 2.140, 550.00, 1353.55, '2019-09-24 16:35:18'),
	(169, 'CP2019-0924000130', 1, 'IMP/ DE CONTRAVISION', 0.802, 2.140, 550.00, 941.60, '2019-09-24 16:35:18'),
	(170, 'CP2019-0926000131', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.970, 1.080, 300.00, 638.28, '2019-09-26 09:36:29'),
	(171, 'CP2019-0926000132', 1, 'PROD/ DE BACKDROP 2.98*2.25', 1.000, 1.000, 13000.00, 13000.00, '2019-09-26 10:45:38'),
	(172, 'CP2019-0926000133', 1, 'IMP/ DE BANNER BRANCO C/ MARGEM DE 5CM', 5.800, 0.801, 600.00, 2784.00, '2019-09-26 11:07:30'),
	(173, 'CP2019-0926000134', 2, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES CADA', 1.000, 0.300, 400.00, 240.00, '2019-09-26 11:42:23'),
	(174, 'CP2019-0926000135', 2, 'IMP/ DE BANNER PRETO', 0.800, 2.000, 400.00, 1280.00, '2019-09-26 14:50:15'),
	(175, 'CP2019-0926000136', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 3.000, 1.000, 400.00, 1200.00, '2019-09-26 15:15:44'),
	(176, 'CP2019-0926000137', 200, 'IMP/ DE CARTOES DE VISITA F/V LAM MATT', 1.000, 1.000, 7.00, 1400.00, '2019-09-26 15:46:08'),
	(177, 'CP2019-0926000138', 2000, 'IMPRESSÃO DE BANDEIRA 1.30M*0.80M', 1.000, 1.000, 487.50, 975000.00, '2019-09-26 17:54:32'),
	(178, 'CP2019-0926000138', NULL, '', NULL, NULL, NULL, 0.00, '2019-09-26 17:54:32'),
	(180, 'CP2019-0927000139', 300, 'IMP/ DE CARTOES DE VISITA F/V LAM MATT', 1.000, 1.000, 7.00, 2100.00, '2019-09-27 09:05:11'),
	(181, 'CP2019-0927000140', 1, 'COMPRA DE ROLO DE VINIL 1.37', 1.000, 1.000, 6000.00, 6000.00, '2019-09-27 09:39:42'),
	(182, 'CP2019-0927000141', 1, 'IMP/ DE VINYL', 2.180, 2.180, 400.00, 1900.96, '2019-09-27 09:59:29'),
	(183, 'CP2019-0927000142', 1, 'IMP/ DE VINYL', 2.200, 2.700, 400.00, 2376.00, '2019-09-27 11:00:42'),
	(184, 'CP2019-0927000143', 1, 'IMP/ DE BANNER BRANCO C/ MARGEM 10CM', 1.200, 1.200, 450.00, 648.00, '2019-09-27 12:30:42'),
	(185, 'CP2019-0927000143', 1, 'IMP/ DE BANNER BRANCO C/ MARGEM 10CM', 1.200, 1.200, 450.00, 648.00, '2019-09-27 12:30:42'),
	(186, 'CP2019-0927000143', 1, 'IMP/ DE BANNER BRANCO C/ MARGEM 10CM', 4.400, 1.200, 450.00, 2376.00, '2019-09-27 12:30:42'),
	(187, 'CP2019-0927000144', 1, 'IMP/ DE VINIL', 1.060, 0.880, 400.00, 373.12, '2019-09-27 13:14:12'),
	(188, 'CP2019-0927000144', 1, 'IMP/ DE VINIL', 0.890, 0.660, 400.00, 234.96, '2019-09-27 13:14:12'),
	(189, 'CP2019-0927000144', 8, 'IMP/ DE VINIL', 1.060, 1.970, 400.00, 6682.24, '2019-09-27 13:14:12'),
	(190, 'CP2019-0927000144', 6, 'IMP/ DE VINIL', 1.060, 1.711, 400.00, 4350.24, '2019-09-27 13:14:12'),
	(191, 'CP2019-0927000145', 1, 'IMP/ DE CONTRAVISION', 1.330, 0.490, 550.00, 358.44, '2019-09-27 13:14:59'),
	(192, 'CP2019-0927000146', 1, 'IMP/ DE BANNER PRETO C/ 5 ILHOSES', 1.400, 1.300, 400.00, 728.00, '2019-09-27 13:31:53'),
	(193, 'CP2019-0927000146', 1, 'IMP/ DE VINYL', 1.000, 0.300, 400.00, 120.00, '2019-09-27 13:32:25'),
	(194, 'CP2019-0927000147', 1, 'IMP/ DE VINYL TRANSPARENTE', 1.000, 0.800, 800.00, 640.00, '2019-09-27 14:29:11'),
	(195, 'CP2019-0927000148', 25, 'IMP/ DE INDENTIFICARES DE MESA A4', 1.000, 1.000, 25.00, 625.00, '2019-09-27 15:09:18'),
	(196, 'CP2019-0927000149', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 0.800, 1.200, 400.00, 384.00, '2019-09-27 15:19:38'),
	(197, 'CP2019-0927000149', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.000, 1.000, 400.00, 400.00, '2019-09-27 15:19:38'),
	(198, 'CP2019-0927000150', 1, 'IMP/ DE VINYL', 2.200, 2.700, 400.00, 2376.00, '2019-09-27 15:35:28'),
	(199, 'CP2019-0927000151', 250, 'IMP/ DE FLYERS A5 F 150 GRMS', 1.000, 1.000, 6.00, 1500.00, '2019-09-27 16:25:13'),
	(200, 'CP2019-0927000152', 1, 'IMP/ DE BANNER BRANCO C/ COSTURA', 5.670, 1.970, 600.00, 6701.94, '2019-09-27 16:26:42'),
	(201, 'CP2019-0927000153', 1, 'IMP/ DE ROLL UP 06', 1.000, 1.000, 3500.00, 3500.00, '2019-09-27 16:57:09'),
	(202, 'CP2019-0927000154', 100, 'IMP/ DE FLYERS A6', 1.000, 1.000, 8.00, 800.00, '2019-09-27 16:58:30'),
	(203, 'CP2019-0928000155', 1, 'IMP/ DE VINYL', 1.316, 9.743, 400.00, 5142.72, '2019-09-28 08:18:39'),
	(204, 'CP2019-0928000156', 100, 'IMP/ DE STIKERS', 0.120, 0.037, 600.00, 288.00, '2019-09-28 08:42:07'),
	(205, 'CP2019-0928000157', 250, 'IMP/ DE FLYERS A5 1 FACE 150GRAMAS', 1.000, 1.000, 6.00, 1500.00, '2019-09-28 08:55:23'),
	(206, 'CP2019-0928000158', 25, 'IMP/ DE BANDEIRAS C/ COSTURA 1.2m*08m', 1.000, 1.000, 500.00, 12500.00, '2019-09-28 10:59:02'),
	(207, 'CP2019-0928000159', 1, 'IMP/ DE BANNER PRETO C/ 4 ILHOSES', 1.406, 0.606, 400.00, 344.04, '2019-09-28 11:02:59'),
	(214, 'CP2019-0930000160', 1, '1', 1.000, 1.000, 1.00, 1.00, '2019-09-30 12:22:03'),
	(215, 'CP2019-1024000164', 1, '2', 3.000, 4.000, 5.00, 60.00, '2019-10-24 11:21:26');
/*!40000 ALTER TABLE `t_order_detail` ENABLE KEYS */;

-- 导出  表 cedar.t_product_information 结构
DROP TABLE IF EXISTS `t_product_information`;
CREATE TABLE IF NOT EXISTS `t_product_information` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fProductName` varchar(250) NOT NULL,
  `fSpesc` varchar(50) DEFAULT NULL,
  `fWidth` varchar(20) DEFAULT NULL,
  `fLength` varchar(20) DEFAULT NULL,
  `fUint` varchar(10) DEFAULT NULL,
  `fNote` varchar(250) DEFAULT NULL,
  `fCurrentQuantity` int(11) NOT NULL DEFAULT '0',
  `fMinimumStock` int(11) NOT NULL DEFAULT '0',
  `fCancel` tinyint(4) NOT NULL DEFAULT '0',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fProductPic` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_product_information 的数据：~105 rows (大约)
/*!40000 ALTER TABLE `t_product_information` DISABLE KEYS */;
INSERT INTO `t_product_information` (`fID`, `fProductName`, `fSpesc`, `fWidth`, `fLength`, `fUint`, `fNote`, `fCurrentQuantity`, `fMinimumStock`, `fCancel`, `TS`, `fProductPic`) VALUES
	(1, 'CTP板 Chapa de CTP', '', '', '', '包', '', 80, 0, 0, '2019-10-28 17:38:03', NULL),
	(2, 'PS板 Chapa  positivas ( PS)', '', '', '', '包', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(3, 'PS显影液 Revelador', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(4, '洁板剂 Plate cleaner', '', '', '', '瓶', '印刷', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(5, '还原清洗剂 blanket rejuvenator (caucho)', '', '', '', '瓶', '1箱+6瓶', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(6, '印刷机油墨 白 Tinta branca officet ', '2.5 kg', '', '', '罐', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(7, '印刷机油墨 黑 Tinta preta officet', '2.5 kg', '', '', '罐', '1 montra', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(8, '印刷机油墨 蓝 Tinta azul ciao officet', '2.5 kg', '', '', '罐', '1 montra', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(9, '印刷机油墨 黄 Tinta amarela officet', '2.5 kg', '', '', '罐', '1 montra', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(10, '印刷机油墨 红 Tinta magenta officet', '2.5 kg', '', '', '罐', '1 montra', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(11, '普通喷绘机墨水 红 Tinta rolaund(magenta)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(12, '普通喷绘机墨水 蓝 Tinta rolaund (azul ciao)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(13, '普通喷绘机墨水 黄 Tinta rolaund (amarelo)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(14, '普通喷绘机墨水 黑 Tinta rolaud (preto)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(15, '旗帜机油墨 红 Tinta cartucho (magenta)', '', '', '', '罐', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(16, '旗帜机油墨 黑 Tinta cartucho (preto)', '', '', '', '罐', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(17, '旗帜机油墨 黄 Tinta cartucho (amarelo)', '', '', '', '罐', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(18, '旗帜机油墨 蓝 Tinta cartucho( azul ciao)', '', '', '', '罐', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(19, '铁门型架 Estrutura de backdrop', '', '', '', '套', '1 montra', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(20, '拉伸膜（过塑膜） Papel aderrente', '', '', '', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(21, '硫酸纸 ', '', '', '', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(22, '印衣服打印卷材 Rolo de estampar(pequena)', '', '', '', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(23, '转印膜 Rolo de estampar(grande)', '', '', '', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(24, 'BOPP预涂膜 光面腹膜 Laminacao', '', '', '', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(25, 'BOPP预涂膜 哑面腹膜 ', '', '', '', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(26, '大喷绘机墨水 黄 Tinta (amarelo)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(27, '大喷绘机墨水 黑 Tinta (preto)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(28, '大喷绘机墨水 蓝 Tinta (azul ciao)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(29, '大喷绘机墨水 红 Tinta (Magenta)', '', '', '', '瓶', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(30, '豪华单屏易拉宝（最常用）06 Roll up base 06 ', '', '', '', '套', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(31, '豪华单屏易拉宝（最好的 Roll up(Bom)', '', '', '', '套', '黑色袋子/4500mt', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(32, '标准易拉宝（黑袋）07 Roll up standard (pasta preta)', '', '', '', 'pcs', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(33, '标准易拉宝（黑袋）蓝色边 ', '', '', '', 'pcs', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(34, '豪华易拉宝（黄色袋子） Roll up standard (pasta laranja)', '', '', '', 'pcs', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(35, '铁拉网 Rede de puxar de ferro', '', '', '', '套', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(36, '不干胶 ', '', '', '', '箱', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(37, '毕业证书筒 Certificado de graduacao (canudo)', '', '', '', 'caixa', '每箱大概140个', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(38, '3.4米旗杆 Tripé (3 metros/40) 4头', '', '', '', 'pcs', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(39, '3.4米旗杆 Tripé (3 metros/40) 3头', '', '', '', 'pcs', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(40, '旗杆小 Tripé', '', '', '', 'pcs', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(41, '栏杆 Separador', '', '', '', 'pcs', '外加10条', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(42, '栏杆底座/铝 Base de bandeira', '', '', '', 'pcs', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(43, '绘图纸 Papel de desenho', '', '', '', 'caixa', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(44, '装订圈 Argolas para encadernacao de livros', '', '', '', 'caixa', '加4小盒', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(45, '热熔胶 Adesivos', '', '', '', 'Saco', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(46, '装订机 Maquina de encadernar', '', '', '', 'PCS', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(47, '斜纹地板膜 Filme de chao(20180225)', '', '1.27', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(48, '五米注水旗杆 Pau de subir bandeira(5 metros)', '', '', '', '件', '163*11*11cm', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(49, '三米旗杆 Vinil pequeno', '', '', '', '件', '165*14*11cm', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(50, '艺彩专业冷裱膜 50 MIC', '', '1.37', '50', '件', '1.37*50m', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(51, '户外写真耗材 150G哑PP背胶 150G-PP', '', '1.27', '50', '件', '150G-PP', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(52, '十字纹冷裱膜  Vinnil n? de barra 20180717', '', '1.07', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(53, '210G双哑PP纸 Vinnil n? de barra 20180419', '', '0.914', '50', '件', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(54, '单向透视膜 Van virgem', '', '', '', '件', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(55, 'NAME：TGB-140 TGB-140', '', '1.27', '50', '件', '1.27*50M', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(56, '2236 PVC 2236 PVC', '', '1.27', '50', '件', '1.27*50M', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(57, '208G  20180310', '', '1.52', '50', '件', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(58, '弱溶剂哑面化纤油画布 CD-240ECH Vinnil CD-240ECH', '', '0.914', '30', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(59, '弱溶剂半透闪点静电贴 KD051 Vinnil 20180717', '', '1.22', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(60, '弱溶剂透明静电贴 KF001 Vinnil 20180716', '', '1.52', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(61, '弱溶剂白色PVC静电贴 KF002 Vinnil KF002', '', '1.52', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(62, '粗纹环保背胶油画布 YD-5003B Vinnil YD-5003B', '', '1.37', '45', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(63, '弱溶剂无纺双透布  Pano', '', '1.52', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(64, '弱溶剂超透PVC贴 ECO-240MP Vinnil 20180716', '', '1.52', '50', '卷', 'FORA', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(65, '弱溶剂灰背PVC胶片 PF-330SG/易拉宝打印材料 Material para roll up', '', '0.914', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(66, '210MIC粗纹地板膜 Vinnil 20180614', '', '1.27', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(67, '超透冷袜膜 Vinil(20180611)', '', '1.27', '100', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(68, '注水旗座 大 80*40*80cm', '', '', '', '件', '80*40*80cm', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(69, '注水旗座 小 Tampa da base de bandeira', '', '', '', '件', '外加18套', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(70, '铝拉网 Rede de puxar de aluminio', '', '', '', '件', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(71, '无缝背胶晶彩反光膜  Vinil ', '', '1.24', '50', '件', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(72, '晶彩格（背胶） Vinil', '', '1.24', '50', '件', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(73, '弱溶剂光面化纤油画布 Vinnil', '', '', '', '件', '0.914*50m', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(74, '弱溶剂哑面化纤油画布 Vinnil', '', '', '', '件', '0.914*50m', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(75, '黑袋沙子旁 Vinil 20180718', '', '1.37', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(76, '2020vinnil  Vinil 20180416', '', '1.37', '50', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(77, '2020vinnil 1.27*50) ', '', '', '', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(78, '2020vinnil 20180417 Top baner (70G FIAG FABRIC)', '', '1.2', '257', '卷', '一共39卷', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(79, '2020vinnil  Top baner(70G FIAG FABRIC)', '', '1.2', '239', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(80, '70G FIAG FABRIC 旗织机卷材 Top baner (70G FIAG FABRIC)', '', '1.2', '260', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(81, '70G FIAG FABRIC 旗织机卷材 Top baner(70G FIAG FABRIC)', '', '1.2', '226', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(82, '70G FIAG FABRIC 旗织机卷材 Top baner (70G FIAG FABRIC)', '', '1.2', '214', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(83, '70G FIAG FABRIC 旗织机卷材 Top baner (70G FIAG FABRIC)', '', '1.2', '236', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(84, '70G FIAG FABRIC 旗织机卷材 Top baner(145G TIENT F?BRIC)', '', '1.5', '150', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(85, '70G FIAG FABRIC 旗织机卷材 Top baner(145G TIENT F?BRIC)', '', '1.5', '152', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(86, '旗帜布 145G tent fabric  Top baner(145G TIENT F?BRIC)', '', '1.5', '153', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(87, '旗帜布 145G tent fabric  Top baner (145G TIENT FABRIC)', '', '1.5', '142', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(88, '旗帜布 145G tent fabric  Top baner (145G TIENT FABRIC)', '', '1.5', '182', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(89, '旗帜布 145G tent fabric  Top baner(95G GIOSSY SATIN)', '', '1.5', '200', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(90, '旗帜布 145G tent fabric  Top baner (110G WAR IMOTTONG FABRIC)', '', '1.5', '115', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(91, '旗帜布 95g giossy satin Top baner (110G WAR IMOTTONG FABRIC)', '', '1.5', '101', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(92, '旗帜布 110g war[ lmottomg fabric Top baner (110G WAR IMOTTONG FABRIC)', '', '1.5', '122', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(93, '旗帜布 110g war[ lmottomg fabric Top baner (110G WAR IMOTTONG FABRIC)', '', '1.5', '136', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(94, '110g war lmottomg fabric Top baner (110G)', '', '1.6', '120', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(95, '旗帜布 110g war lmottomg fabric Top baner (110G)', '', '1.6', '136', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(96, '旗帜布 110g 轻编旗帜布 Top baner (110G)', '', '1.6', '128', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(97, '旗帜布 110g 轻编旗帜布 Top baner (110G)', '', '1.6', '171', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(98, '旗帜布 110g 轻编旗帜布 Top baner (600D OXFORD FABRIC)', '', '1.5', '80', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(99, '旗帜布 110g 轻编旗帜布 Top baner (120G MESH)', '', '1.6', '100', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(100, '账蓬', '3*3', '', '', '个', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(101, '账蓬', '3*6', '', '', '个', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(102, '卷材薄纸 KT BOARD', '', '', '', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(103, '未知名 Mesa de promocao', '', '', '', '卷', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(104, '双面亮光板', '', '', '', '', '', 0, 0, 0, '2019-10-28 17:38:03', NULL),
	(105, '广告桌/架子', '', '', '', '', '\r\n', 0, 0, 0, '2019-10-28 17:38:03', NULL);
/*!40000 ALTER TABLE `t_product_information` ENABLE KEYS */;

-- 导出  表 cedar.t_product_outbound_order 结构
DROP TABLE IF EXISTS `t_product_outbound_order`;
CREATE TABLE IF NOT EXISTS `t_product_outbound_order` (
  `fOrderID` char(20) NOT NULL COMMENT '订单号',
  `fPrice` decimal(10,2) DEFAULT NULL COMMENT '单价',
  `fCustomerID` int(11) NOT NULL COMMENT '客户编号',
  `fOrderDate` date NOT NULL COMMENT '订单日期',
  `fRequiredDeliveryDate` date DEFAULT NULL COMMENT '客户要求交货日期',
  `fAmount` decimal(11,2) DEFAULT NULL COMMENT '金额',
  `fTax` decimal(11,2) DEFAULT NULL COMMENT '税金',
  `fPayable` decimal(11,2) DEFAULT NULL COMMENT '应付金额',
  `fDesconto` decimal(11,2) DEFAULT NULL COMMENT '折扣',
  `fEntryID` int(11) DEFAULT NULL COMMENT '录入人',
  `fSubmited` bit(1) NOT NULL DEFAULT b'0' COMMENT '提交',
  `fSubmitID` int(11) DEFAULT NULL COMMENT '提交人',
  `fReviewed` bit(1) NOT NULL DEFAULT b'0' COMMENT '已审核',
  `fReviewerID` int(11) DEFAULT NULL COMMENT '审核人',
  `fConfirmed` bit(1) NOT NULL DEFAULT b'0' COMMENT '已确认',
  `fConfirmID` int(11) DEFAULT NULL COMMENT '确认人',
  `fDelivered` bit(1) NOT NULL DEFAULT b'0' COMMENT '已交付',
  `fDelivererID` int(11) DEFAULT NULL COMMENT '交付人',
  `fCanceled` bit(1) NOT NULL DEFAULT b'0' COMMENT '已作废',
  `fCancelID` int(11) DEFAULT NULL COMMENT '作废人',
  `fDeliveryDate` date DEFAULT NULL COMMENT '交付日期',
  `fQuant` int(11) DEFAULT NULL COMMENT '数量',
  `fSucursal` bit(1) DEFAULT NULL COMMENT 'Sucursal 分公司',
  `fVendedorID` int(11) DEFAULT NULL COMMENT '销售人员',
  `fContato` varchar(20) DEFAULT NULL COMMENT '联系人',
  `fCelular` varchar(15) DEFAULT NULL COMMENT '手机',
  `fTelefone` varchar(15) DEFAULT NULL COMMENT '电话',
  `fNote` varchar(255) DEFAULT NULL COMMENT '备注',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fOrderID`),
  KEY `iDelivererID` (`fDelivererID`),
  KEY `iOrderDate` (`fOrderDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_product_outbound_order 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_product_outbound_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_product_outbound_order` ENABLE KEYS */;

-- 导出  表 cedar.t_product_outbound_order_detail 结构
DROP TABLE IF EXISTS `t_product_outbound_order_detail`;
CREATE TABLE IF NOT EXISTS `t_product_outbound_order_detail` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fOrderID` char(20) DEFAULT NULL,
  `fQuant` smallint(6) DEFAULT NULL,
  `fProductID` int(11) DEFAULT NULL,
  `fPrice` decimal(11,2) DEFAULT NULL,
  `fNote` char(50) DEFAULT NULL,
  `fAmount` decimal(11,2) NOT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_product_outbound_order_detail 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_product_outbound_order_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_product_outbound_order_detail` ENABLE KEYS */;

-- 导出  表 cedar.t_product_warehousereceipt_order 结构
DROP TABLE IF EXISTS `t_product_warehousereceipt_order`;
CREATE TABLE IF NOT EXISTS `t_product_warehousereceipt_order` (
  `fOrderID` char(20) NOT NULL COMMENT '订单号',
  `fPrice` decimal(10,2) DEFAULT NULL COMMENT '单价',
  `fSupplierID` int(11) NOT NULL COMMENT '客户编号',
  `fPurchaserID` int(11) NOT NULL COMMENT '采购人员',
  `fOrderDate` date NOT NULL COMMENT '订单日期',
  `fWarehousingDate` date DEFAULT NULL COMMENT '入库日期',
  `fAmount` decimal(11,2) unsigned zerofill DEFAULT NULL COMMENT '金额',
  `fTax` decimal(11,2) DEFAULT NULL COMMENT '税金',
  `fPayable` decimal(11,2) DEFAULT NULL COMMENT '应付金额',
  `fDesconto` decimal(11,2) DEFAULT NULL COMMENT '折扣',
  `fEntryID` int(11) DEFAULT NULL COMMENT '录入人',
  `fSubmited` bit(1) NOT NULL DEFAULT b'0' COMMENT '提交',
  `fSubmitID` int(11) DEFAULT NULL COMMENT '提交人',
  `fCanceled` bit(1) NOT NULL DEFAULT b'0' COMMENT '已作废',
  `fCancelID` int(11) DEFAULT NULL COMMENT '作废人',
  `fContato` varchar(20) DEFAULT NULL COMMENT '联系人',
  `fCelular` varchar(15) DEFAULT NULL COMMENT '手机',
  `fTelefone` varchar(15) DEFAULT NULL COMMENT '电话',
  `fNote` varchar(255) DEFAULT NULL COMMENT '备注',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fOrderID`),
  KEY `iOrderDate` (`fOrderDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_product_warehousereceipt_order 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_product_warehousereceipt_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_product_warehousereceipt_order` ENABLE KEYS */;

-- 导出  表 cedar.t_product_warehousereceipt_order_detail 结构
DROP TABLE IF EXISTS `t_product_warehousereceipt_order_detail`;
CREATE TABLE IF NOT EXISTS `t_product_warehousereceipt_order_detail` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fOrderID` char(20) DEFAULT NULL,
  `fQuant` smallint(6) DEFAULT NULL,
  `fProductID` int(11) DEFAULT NULL,
  `fPrice` decimal(11,2) DEFAULT NULL,
  `fNote` char(50) DEFAULT NULL,
  `fAmount` decimal(11,2) NOT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_product_warehousereceipt_order_detail 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_product_warehousereceipt_order_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_product_warehousereceipt_order_detail` ENABLE KEYS */;

-- 导出  表 cedar.t_quotation 结构
DROP TABLE IF EXISTS `t_quotation`;
CREATE TABLE IF NOT EXISTS `t_quotation` (
  `fOrderID` char(20) NOT NULL COMMENT '订单号',
  `fPrice` decimal(10,0) DEFAULT NULL COMMENT '单价_印刷',
  `fCustomerID` int(11) NOT NULL COMMENT '客户编号',
  `fOrderDate` date NOT NULL COMMENT '订单日期',
  `fEspecieID` int(11) DEFAULT NULL COMMENT '印刷分类',
  `fRequiredDeliveryDate` date DEFAULT NULL COMMENT '客户要求交货日期',
  `fCategoryID` int(11) DEFAULT NULL COMMENT '类别',
  `fBrandMateriaID` int(11) DEFAULT NULL COMMENT '品牌材料',
  `fAmount` decimal(11,2) DEFAULT NULL COMMENT '金额',
  `fTax` decimal(11,2) DEFAULT NULL COMMENT '税金',
  `fPayable` decimal(11,2) DEFAULT NULL COMMENT '应付金额',
  `fDesconto` decimal(11,2) DEFAULT NULL COMMENT '折扣',
  `fColorID` int(11) DEFAULT NULL COMMENT '颜色',
  `fEntryID` int(11) DEFAULT NULL COMMENT '录入人',
  `fSubmited` bit(1) NOT NULL DEFAULT b'0' COMMENT '提交',
  `fSubmitID` int(11) DEFAULT NULL COMMENT '提交人',
  `fReviewed` bit(1) NOT NULL DEFAULT b'0' COMMENT '已审核',
  `fReviewerID` int(11) DEFAULT NULL COMMENT '审核人',
  `fConfirmed` bit(1) NOT NULL DEFAULT b'0' COMMENT '已确认',
  `fConfirmID` int(11) DEFAULT NULL COMMENT '确认人',
  `fDelivered` bit(1) NOT NULL DEFAULT b'0' COMMENT '已交付',
  `fDelivererID` int(11) DEFAULT NULL COMMENT '交付人',
  `fCanceled` bit(1) NOT NULL DEFAULT b'0' COMMENT '已作废',
  `fCancelID` int(11) DEFAULT NULL COMMENT '作废人',
  `fDeliveryDate` date DEFAULT NULL COMMENT '交付日期',
  `fNumerBegin` int(11) DEFAULT NULL COMMENT '起始编号',
  `fQuant` int(11) DEFAULT NULL COMMENT '数量',
  `fPagePerVolumn` tinyint(4) DEFAULT NULL COMMENT '每本号数',
  `fNumerEnd` int(11) DEFAULT NULL COMMENT '结束编号',
  `fAvistaID` int(11) DEFAULT NULL COMMENT '每页单据数',
  `fTamanhoID` int(11) DEFAULT NULL COMMENT '尺寸',
  `fSucursal` bit(1) DEFAULT NULL COMMENT 'Sucursal 分公司',
  `fLogo` bit(1) DEFAULT b'0' COMMENT '标志',
  `fVendedorID` int(11) DEFAULT NULL COMMENT '销售人员',
  `fNrCopyID` int(11) DEFAULT NULL COMMENT '联次',
  `fContato` varchar(20) DEFAULT NULL COMMENT '联系人',
  `fCelular` varchar(15) DEFAULT NULL COMMENT '手机',
  `fTelefone` varchar(15) DEFAULT NULL COMMENT '电话',
  `fNote` varchar(255) DEFAULT NULL COMMENT '备注',
  `fDeliverViewed` bit(1) DEFAULT b'0' COMMENT '生产部已查阅',
  `fCreatedOrder` bit(1) DEFAULT b'0' COMMENT '已生成订单',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fOrderID`),
  KEY `iDelivererID` (`fDelivererID`),
  KEY `iOrderDate` (`fOrderDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_quotation 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_quotation` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_quotation` ENABLE KEYS */;

-- 导出  表 cedar.t_quotation_detail 结构
DROP TABLE IF EXISTS `t_quotation_detail`;
CREATE TABLE IF NOT EXISTS `t_quotation_detail` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fOrderID` varchar(50) DEFAULT NULL,
  `fQuant` smallint(6) DEFAULT NULL,
  `fProductName` varchar(50) DEFAULT NULL,
  `fLength` decimal(10,3) DEFAULT NULL,
  `fWidth` decimal(10,3) DEFAULT NULL,
  `fPrice` decimal(11,2) DEFAULT NULL,
  `fAmount` decimal(11,2) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_quotation_detail 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_quotation_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_quotation_detail` ENABLE KEYS */;

-- 导出  表 cedar.t_receivables 结构
DROP TABLE IF EXISTS `t_receivables`;
CREATE TABLE IF NOT EXISTS `t_receivables` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fCustomerID` int(11) NOT NULL,
  `fPaymentMethodID` int(11) NOT NULL COMMENT '收款方式',
  `fReceiptDate` date NOT NULL COMMENT '收款日期',
  `fAmountCollected` decimal(11,2) NOT NULL COMMENT '金额',
  `fPayeeID` int(11) NOT NULL COMMENT '收款人',
  `fNote` varchar(255) DEFAULT NULL COMMENT '备注',
  `TS` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fOrderID` char(20) DEFAULT NULL COMMENT '对应单号',
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_receivables 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_receivables` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_receivables` ENABLE KEYS */;

-- 导出  表 cedar.t_supplier 结构
DROP TABLE IF EXISTS `t_supplier`;
CREATE TABLE IF NOT EXISTS `t_supplier` (
  `fSupplierID` int(11) NOT NULL AUTO_INCREMENT,
  `fSupplierName` varchar(50) NOT NULL COMMENT '客户名',
  `fNUIT` varchar(25) DEFAULT NULL COMMENT '税号',
  `fCity` varchar(30) DEFAULT NULL COMMENT '所在地 Mordo',
  `fContato` varchar(20) DEFAULT NULL COMMENT '联系人',
  `fAreaCode` varchar(15) DEFAULT NULL COMMENT '区号',
  `fCelular` varchar(15) DEFAULT NULL COMMENT '手机',
  `fTelefone` varchar(15) DEFAULT NULL COMMENT '电话',
  `fEndereco` varchar(15) DEFAULT NULL COMMENT '地址',
  `fEmail` varchar(50) DEFAULT NULL COMMENT '电子邮件',
  `fWeb` varchar(50) DEFAULT NULL COMMENT '主页',
  `fFax` varchar(15) DEFAULT NULL COMMENT '传真',
  `fNote` varchar(255) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fTaxRegCer` varchar(50) DEFAULT NULL COMMENT '税务登记证',
  PRIMARY KEY (`fSupplierID`),
  UNIQUE KEY `OnlyOne` (`fSupplierName`),
  UNIQUE KEY `fNUIT` (`fNUIT`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cedar.t_supplier 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `t_supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_supplier` ENABLE KEYS */;

-- 导出  视图 cedar.v_enumeration 结构
DROP VIEW IF EXISTS `v_enumeration`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_enumeration` (
	`fTypeID` INT(11) NOT NULL,
	`fTypeName` VARCHAR(20) NOT NULL COLLATE 'utf8_general_ci',
	`fItemID` INT(11) NULL COMMENT '选项编号',
	`fTitle` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fSpare1` VARCHAR(50) NULL COMMENT '备用1' COLLATE 'utf8_general_ci',
	`fSpare2` VARCHAR(50) NULL COMMENT '备用2' COLLATE 'utf8_general_ci',
	`fNote` VARCHAR(255) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 cedar.v_order 结构
DROP VIEW IF EXISTS `v_order`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_order` (
	`fOrderID` CHAR(20) NOT NULL COMMENT '订单号' COLLATE 'utf8_general_ci',
	`fPrice` DECIMAL(10,2) NULL COMMENT '单价_印刷',
	`fCustomerID` INT(11) NOT NULL COMMENT '客户编号',
	`fOrderDate` DATE NOT NULL COMMENT '订单日期',
	`fEspecieID` INT(11) NULL COMMENT '印刷分类',
	`fRequiredDeliveryDate` DATE NULL COMMENT '客户要求交货日期',
	`fCategoryID` INT(11) NULL COMMENT '类别',
	`fBrandMateriaID` INT(11) NULL COMMENT '品牌材料',
	`fAmount` DECIMAL(11,2) NULL COMMENT '金额',
	`fTax` DECIMAL(11,2) NULL COMMENT '税金',
	`fPayable` DECIMAL(11,2) NULL COMMENT '应付金额',
	`fDesconto` DECIMAL(11,2) NULL COMMENT '折扣',
	`fColorID` INT(11) NULL COMMENT '颜色',
	`fEntryID` INT(11) NULL COMMENT '录入人',
	`fSubmited` INT(2) UNSIGNED NOT NULL,
	`fSubmitID` INT(11) NULL COMMENT '提交人',
	`fReviewed` INT(2) UNSIGNED NOT NULL,
	`fReviewerID` INT(11) NULL COMMENT '审核人',
	`fConfirmed` INT(2) UNSIGNED NOT NULL,
	`fConfirmID` INT(11) NULL COMMENT '确认人',
	`fDelivered` INT(2) UNSIGNED NOT NULL,
	`fDelivererID` INT(11) NULL COMMENT '交付人',
	`fCanceled` INT(2) UNSIGNED NOT NULL,
	`fDeliverViewed` INT(2) UNSIGNED NULL,
	`fCancelID` INT(11) NULL COMMENT '作废人',
	`fDeliveryDate` DATE NULL COMMENT '交付日期',
	`fNumerBegin` INT(11) NULL COMMENT '起始编号',
	`fQuant` INT(11) NULL COMMENT '数量',
	`fPagePerVolumn` SMALLINT(6) NULL COMMENT '每本号数',
	`fNumerEnd` INT(11) NULL COMMENT '结束编号',
	`fAvistaID` INT(11) NULL COMMENT '每页单据数',
	`fTamanhoID` INT(11) NULL COMMENT '尺寸',
	`fSucursal` INT(2) UNSIGNED NULL,
	`fLogo` INT(2) UNSIGNED NULL,
	`fVendedorID` INT(11) NULL COMMENT '销售人员',
	`fNrCopyID` INT(11) NULL COMMENT '联次',
	`fContato` VARCHAR(20) NULL COMMENT '联系人' COLLATE 'utf8_general_ci',
	`fCelular` VARCHAR(15) NULL COMMENT '手机' COLLATE 'utf8_general_ci',
	`fTelefone` VARCHAR(15) NULL COMMENT '电话' COLLATE 'utf8_general_ci',
	`fNote` VARCHAR(255) NULL COMMENT '备注' COLLATE 'utf8_general_ci',
	`fTaxRegCer` VARCHAR(50) NULL COMMENT '税务登记证' COLLATE 'utf8_general_ci',
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fNUIT` VARCHAR(25) NULL COMMENT '税号' COLLATE 'utf8_general_ci',
	`fCity` VARCHAR(30) NULL COMMENT '所在地 Mordo' COLLATE 'utf8_general_ci',
	`fEndereco` VARCHAR(50) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fEmail` VARCHAR(50) NULL COMMENT '电子邮件' COLLATE 'utf8_general_ci',
	`fSucursal1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fSubmited1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fConfirmed1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fDelivered1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fCanceled1` VARCHAR(8) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fDeliverViewed1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fLogo1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fSubmit_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fEntry_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fReviewer_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fDeliverer_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fConfirm_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fCancel_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fEspecie` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fCategory` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fBrandMateria` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fColor` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fAvista` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fTamanho` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fVendedor` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fNrCopy` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 cedar.v_order_readonly 结构
DROP VIEW IF EXISTS `v_order_readonly`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_order_readonly` (
	`fOrderID` CHAR(20) NOT NULL COMMENT '订单号' COLLATE 'utf8_general_ci',
	`fPrice` DECIMAL(10,2) NULL COMMENT '单价_印刷',
	`fCustomerID` INT(11) NOT NULL COMMENT '客户编号',
	`fOrderDate` DATE NOT NULL COMMENT '订单日期',
	`fEspecieID` INT(11) NULL COMMENT '印刷分类',
	`fRequiredDeliveryDate` DATE NULL COMMENT '客户要求交货日期',
	`fCategoryID` INT(11) NULL COMMENT '类别',
	`fBrandMateriaID` INT(11) NULL COMMENT '品牌材料',
	`fAmount` DECIMAL(11,2) NULL COMMENT '金额',
	`fTax` DECIMAL(11,2) NULL COMMENT '税金',
	`fPayable` DECIMAL(11,2) NULL COMMENT '应付金额',
	`fDesconto` DECIMAL(11,2) NULL COMMENT '折扣',
	`fColorID` INT(11) NULL COMMENT '颜色',
	`fEntryID` INT(11) NULL COMMENT '录入人',
	`fSubmited` BIT(1) NOT NULL COMMENT '提交',
	`fSubmitID` INT(11) NULL COMMENT '提交人',
	`fReviewed` BIT(1) NOT NULL COMMENT '已审核',
	`fReviewerID` INT(11) NULL COMMENT '审核人',
	`fConfirmed` BIT(1) NOT NULL COMMENT '已确认',
	`fConfirmID` INT(11) NULL COMMENT '确认人',
	`fDelivered` BIT(1) NOT NULL COMMENT '已交付',
	`fDelivererID` INT(11) NULL COMMENT '交付人',
	`fCanceled` BIT(1) NOT NULL COMMENT '已作废',
	`fCancelID` INT(11) NULL COMMENT '作废人',
	`fDeliveryDate` DATE NULL COMMENT '交付日期',
	`fNumerBegin` INT(11) NULL COMMENT '起始编号',
	`fQuant` INT(11) NULL COMMENT '数量',
	`fPagePerVolumn` SMALLINT(6) NULL COMMENT '每本号数',
	`fNumerEnd` INT(11) NULL COMMENT '结束编号',
	`fAvistaID` INT(11) NULL COMMENT '每页单据数',
	`fTamanhoID` INT(11) NULL COMMENT '尺寸',
	`fSucursal` BIT(1) NULL COMMENT 'Sucursal 分公司',
	`fLogo` BIT(1) NULL COMMENT '标志',
	`fVendedorID` INT(11) NULL COMMENT '销售人员',
	`fNrCopyID` INT(11) NULL COMMENT '联次',
	`fContato` VARCHAR(20) NULL COMMENT '联系人' COLLATE 'utf8_general_ci',
	`fCelular` VARCHAR(15) NULL COMMENT '手机' COLLATE 'utf8_general_ci',
	`fTelefone` VARCHAR(15) NULL COMMENT '电话' COLLATE 'utf8_general_ci',
	`fNote` VARCHAR(255) NULL COMMENT '备注' COLLATE 'utf8_general_ci',
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fNUIT` VARCHAR(25) NULL COMMENT '税号' COLLATE 'utf8_general_ci',
	`fCity` VARCHAR(30) NULL COMMENT '所在地 Mordo' COLLATE 'utf8_general_ci',
	`fAreaCode` VARCHAR(15) NULL COMMENT '区号' COLLATE 'utf8_general_ci',
	`fEndereco` VARCHAR(50) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fEmail` VARCHAR(50) NULL COMMENT '电子邮件' COLLATE 'utf8_general_ci',
	`fWeb` VARCHAR(50) NULL COMMENT '主页' COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 cedar.v_product_outbound_order 结构
DROP VIEW IF EXISTS `v_product_outbound_order`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_product_outbound_order` (
	`fOrderID` CHAR(20) NOT NULL COMMENT '订单号' COLLATE 'utf8_general_ci',
	`fPrice` DECIMAL(10,2) NULL COMMENT '单价',
	`fCustomerID` INT(11) NOT NULL COMMENT '客户编号',
	`fOrderDate` DATE NOT NULL COMMENT '订单日期',
	`fRequiredDeliveryDate` DATE NULL COMMENT '客户要求交货日期',
	`fAmount` DECIMAL(11,2) NULL COMMENT '金额',
	`fTax` DECIMAL(11,2) NULL COMMENT '税金',
	`fPayable` DECIMAL(11,2) NULL COMMENT '应付金额',
	`fDesconto` DECIMAL(11,2) NULL COMMENT '折扣',
	`fEntryID` INT(11) NULL COMMENT '录入人',
	`fSubmited` INT(2) UNSIGNED NOT NULL,
	`fSubmitID` INT(11) NULL COMMENT '提交人',
	`fReviewed` INT(2) UNSIGNED NOT NULL,
	`fReviewerID` INT(11) NULL COMMENT '审核人',
	`fConfirmed` INT(2) UNSIGNED NOT NULL,
	`fConfirmID` INT(11) NULL COMMENT '确认人',
	`fDelivered` INT(2) UNSIGNED NOT NULL,
	`fDelivererID` INT(11) NULL COMMENT '交付人',
	`fCanceled` INT(2) UNSIGNED NOT NULL,
	`fCancelID` INT(11) NULL COMMENT '作废人',
	`fDeliveryDate` DATE NULL COMMENT '交付日期',
	`fQuant` INT(11) NULL COMMENT '数量',
	`fSucursal` INT(2) UNSIGNED NULL,
	`fVendedorID` INT(11) NULL COMMENT '销售人员',
	`fContato` VARCHAR(20) NULL COMMENT '联系人' COLLATE 'utf8_general_ci',
	`fCelular` VARCHAR(15) NULL COMMENT '手机' COLLATE 'utf8_general_ci',
	`fTelefone` VARCHAR(15) NULL COMMENT '电话' COLLATE 'utf8_general_ci',
	`fNote` VARCHAR(255) NULL COMMENT '备注' COLLATE 'utf8_general_ci',
	`fTaxRegCer` VARCHAR(50) NULL COMMENT '税务登记证' COLLATE 'utf8_general_ci',
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fNUIT` VARCHAR(25) NULL COMMENT '税号' COLLATE 'utf8_general_ci',
	`fCity` VARCHAR(30) NULL COMMENT '所在地 Mordo' COLLATE 'utf8_general_ci',
	`fEndereco` VARCHAR(50) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fEmail` VARCHAR(50) NULL COMMENT '电子邮件' COLLATE 'utf8_general_ci',
	`fSucursal1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fSubmited1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fConfirmed1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fDelivered1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fCanceled1` VARCHAR(8) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fSubmit_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fEntry_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fReviewer_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fDeliverer_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fConfirm_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fCancel_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fVendedor` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 cedar.v_product_warehousereceipt_order 结构
DROP VIEW IF EXISTS `v_product_warehousereceipt_order`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_product_warehousereceipt_order` (
	`fOrderID` CHAR(20) NOT NULL COMMENT '订单号' COLLATE 'utf8_general_ci',
	`fPrice` DECIMAL(10,2) NULL COMMENT '单价',
	`fSupplierID` INT(11) NOT NULL COMMENT '客户编号',
	`fOrderDate` DATE NOT NULL COMMENT '订单日期',
	`fWarehousingDate` DATE NULL COMMENT '入库日期',
	`fAmount` DECIMAL(11,2) UNSIGNED ZEROFILL NULL COMMENT '金额',
	`fTax` DECIMAL(11,2) NULL COMMENT '税金',
	`fPayable` DECIMAL(11,2) NULL COMMENT '应付金额',
	`fDesconto` DECIMAL(11,2) NULL COMMENT '折扣',
	`fEntryID` INT(11) NULL COMMENT '录入人',
	`fSubmited` INT(2) UNSIGNED NOT NULL,
	`fSubmitID` INT(11) NULL COMMENT '提交人',
	`fCanceled` INT(2) UNSIGNED NOT NULL,
	`fCancelID` INT(11) NULL COMMENT '作废人',
	`fPurchaserID` INT(11) NOT NULL COMMENT '采购人员',
	`fContato` VARCHAR(20) NULL COMMENT '联系人' COLLATE 'utf8_general_ci',
	`fCelular` VARCHAR(15) NULL COMMENT '手机' COLLATE 'utf8_general_ci',
	`fTelefone` VARCHAR(15) NULL COMMENT '电话' COLLATE 'utf8_general_ci',
	`fNote` VARCHAR(255) NULL COMMENT '备注' COLLATE 'utf8_general_ci',
	`fTaxRegCer` VARCHAR(50) NULL COMMENT '税务登记证' COLLATE 'utf8_general_ci',
	`fSupplierName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fNUIT` VARCHAR(25) NULL COMMENT '税号' COLLATE 'utf8_general_ci',
	`fCity` VARCHAR(30) NULL COMMENT '所在地 Mordo' COLLATE 'utf8_general_ci',
	`fEndereco` VARCHAR(15) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fEmail` VARCHAR(50) NULL COMMENT '电子邮件' COLLATE 'utf8_general_ci',
	`fSubmited1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fCanceled1` VARCHAR(8) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fSubmit_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fEntry_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fCancel_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fPurchaser` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 cedar.v_quotation 结构
DROP VIEW IF EXISTS `v_quotation`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_quotation` (
	`fOrderID` CHAR(20) NOT NULL COMMENT '订单号' COLLATE 'utf8_general_ci',
	`fPrice` DECIMAL(10,0) NULL COMMENT '单价_印刷',
	`fCustomerID` INT(11) NOT NULL COMMENT '客户编号',
	`fOrderDate` DATE NOT NULL COMMENT '订单日期',
	`fEspecieID` INT(11) NULL COMMENT '印刷分类',
	`fRequiredDeliveryDate` DATE NULL COMMENT '客户要求交货日期',
	`fCategoryID` INT(11) NULL COMMENT '类别',
	`fBrandMateriaID` INT(11) NULL COMMENT '品牌材料',
	`fAmount` DECIMAL(11,2) NULL COMMENT '金额',
	`fTax` DECIMAL(11,2) NULL COMMENT '税金',
	`fPayable` DECIMAL(11,2) NULL COMMENT '应付金额',
	`fDesconto` DECIMAL(11,2) NULL COMMENT '折扣',
	`fColorID` INT(11) NULL COMMENT '颜色',
	`fEntryID` INT(11) NULL COMMENT '录入人',
	`fSubmited` INT(2) UNSIGNED NOT NULL,
	`fSubmitID` INT(11) NULL COMMENT '提交人',
	`fReviewed` INT(2) UNSIGNED NOT NULL,
	`fReviewerID` INT(11) NULL COMMENT '审核人',
	`fConfirmed` INT(2) UNSIGNED NOT NULL,
	`fConfirmID` INT(11) NULL COMMENT '确认人',
	`fDelivered` INT(2) UNSIGNED NOT NULL,
	`fDelivererID` INT(11) NULL COMMENT '交付人',
	`fCanceled` INT(2) UNSIGNED NOT NULL,
	`fDeliverViewed` INT(2) UNSIGNED NULL,
	`fCancelID` INT(11) NULL COMMENT '作废人',
	`fDeliveryDate` DATE NULL COMMENT '交付日期',
	`fNumerBegin` INT(11) NULL COMMENT '起始编号',
	`fQuant` INT(11) NULL COMMENT '数量',
	`fPagePerVolumn` TINYINT(4) NULL COMMENT '每本号数',
	`fNumerEnd` INT(11) NULL COMMENT '结束编号',
	`fAvistaID` INT(11) NULL COMMENT '每页单据数',
	`fTamanhoID` INT(11) NULL COMMENT '尺寸',
	`fSucursal` INT(2) UNSIGNED NULL,
	`fLogo` INT(2) UNSIGNED NULL,
	`fVendedorID` INT(11) NULL COMMENT '销售人员',
	`fNrCopyID` INT(11) NULL COMMENT '联次',
	`fContato` VARCHAR(20) NULL COMMENT '联系人' COLLATE 'utf8_general_ci',
	`fCelular` VARCHAR(15) NULL COMMENT '手机' COLLATE 'utf8_general_ci',
	`fTelefone` VARCHAR(15) NULL COMMENT '电话' COLLATE 'utf8_general_ci',
	`fNote` VARCHAR(255) NULL COMMENT '备注' COLLATE 'utf8_general_ci',
	`fCreatedOrder` INT(2) UNSIGNED NULL,
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fNUIT` VARCHAR(25) NULL COMMENT '税号' COLLATE 'utf8_general_ci',
	`fCity` VARCHAR(30) NULL COMMENT '所在地 Mordo' COLLATE 'utf8_general_ci',
	`fEndereco` VARCHAR(50) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fSucursal1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fSubmited1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fConfirmed1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fDelivered1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fCanceled1` VARCHAR(8) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fDeliverViewed1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fLogo1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fSubmit_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fEntry_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fReviewer_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fDeliverer_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fConfirm_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fCancel_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fEspecie` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fCategory` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fBrandMateria` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fColor` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fAvista` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fTamanho` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fVendedor` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fNrCopy` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 cedar.v_receivables 结构
DROP VIEW IF EXISTS `v_receivables`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_receivables` (
	`fID` INT(11) NOT NULL,
	`fCustomerID` INT(11) NOT NULL,
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fReceiptDate` DATE NOT NULL COMMENT '收款日期',
	`fAmountCollected` DECIMAL(11,2) NOT NULL COMMENT '金额',
	`fOrderID` CHAR(20) NULL COMMENT '对应单号' COLLATE 'utf8_general_ci',
	`fPayee` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`fPaymentMethod` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`fNote` VARCHAR(255) NULL COMMENT '备注' COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 cedar.v_enumeration 结构
DROP VIEW IF EXISTS `v_enumeration`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_enumeration`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_enumeration` AS select `t`.`fTypeID` AS `fTypeID`,`t`.`fTypeName` AS `fTypeName`,`e`.`fItemID` AS `fItemID`,`e`.`fTitle` AS `fTitle`,`e`.`fSpare1` AS `fSpare1`,`e`.`fSpare2` AS `fSpare2`,`e`.`fNote` AS `fNote` from (`t_enumeration_type` `t` left join `t_enumeration` `e` on((`t`.`fTypeID` = `e`.`fTypeID`))) ;

-- 导出  视图 cedar.v_order 结构
DROP VIEW IF EXISTS `v_order`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_order`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_order` AS SELECT `o`.`fOrderID` AS `fOrderID`, `o`.`fPrice` AS `fPrice`, `o`.`fCustomerID` AS `fCustomerID`, `o`.`fOrderDate` AS `fOrderDate`, `o`.`fEspecieID` AS `fEspecieID`
	, `o`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`, `o`.`fCategoryID` AS `fCategoryID`, `o`.`fBrandMateriaID` AS `fBrandMateriaID`, `o`.`fAmount` AS `fAmount`, `o`.`fTax` AS `fTax`
	, `o`.`fPayable` AS `fPayable`, `o`.`fDesconto` AS `fDesconto`, `o`.`fColorID` AS `fColorID`, `o`.`fEntryID` AS `fEntryID`
	, `o`.`fSubmited` + 0 AS `fSubmited`, `o`.`fSubmitID` AS `fSubmitID`
	, `o`.`fReviewed` + 0 AS `fReviewed`, `o`.`fReviewerID` AS `fReviewerID`
	, `o`.`fConfirmed` + 0 AS `fConfirmed`, `o`.`fConfirmID` AS `fConfirmID`
	, `o`.`fDelivered` + 0 AS `fDelivered`, `o`.`fDelivererID` AS `fDelivererID`
	, `o`.`fCanceled` + 0 AS `fCanceled`, `o`.`fDeliverViewed` + 0 AS `fDeliverViewed`
	, `o`.`fCancelID` AS `fCancelID`, `o`.`fDeliveryDate` AS `fDeliveryDate`, `o`.`fNumerBegin` AS `fNumerBegin`, `o`.`fQuant` AS `fQuant`, `o`.`fPagePerVolumn` AS `fPagePerVolumn`
	, `o`.`fNumerEnd` AS `fNumerEnd`, `o`.`fAvistaID` AS `fAvistaID`, `o`.`fTamanhoID` AS `fTamanhoID`, `o`.`fSucursal` + 0 AS `fSucursal`
	, `o`.`fLogo` + 0 AS `fLogo`, `o`.`fVendedorID` AS `fVendedorID`, `o`.`fNrCopyID` AS `fNrCopyID`
	, `o`.`fContato` AS `fContato`, `o`.`fCelular` AS `fCelular`, `o`.`fTelefone` AS `fTelefone`, `o`.`fNote` AS `fNote`, `c`.`fTaxRegCer` AS `fTaxRegCer`
	, `c`.`fCustomerName` AS `fCustomerName`, `c`.`fNUIT` AS `fNUIT`, `c`.`fCity` AS `fCity`, `c`.`fEndereco` AS `fEndereco`
,`c`.`fEmail` AS `fEmail`
	, CASE `o`.`fSucursal`
		WHEN 1 THEN 'SIM'
		ELSE 'Non'
	END AS `fSucursal1`
	, CASE `o`.`fSubmited`
		WHEN 1 THEN 'SIM'
		ELSE ''
	END AS `fSubmited1`
	, CASE `o`.`fConfirmed`
		WHEN 1 THEN 'SIM'
		ELSE ''
	END AS `fConfirmed1`
	, CASE `o`.`fDelivered`
		WHEN 1 THEN 'SIM'
		ELSE ''
	END AS `fDelivered1`
	, CASE `o`.`fCanceled`
		WHEN 1 THEN 'Canceled'
		ELSE ''
	END AS `fCanceled1`
	, CASE `o`.`fDeliverViewed`
		WHEN 1 THEN 'SIM'
		ELSE ''
	END AS `fDeliverViewed1`
	, CASE `o`.`fLogo`
		WHEN 1 THEN 'SIM'
		ELSE 'Non'
	END AS `fLogo1`, `u_Submited`.`fUsername` AS `fSubmit_Name`, `u_Entry`.`fUsername` AS `fEntry_Name`, `u_Reviewer`.`fUsername` AS `fReviewer_Name`, `u_Deliverer`.`fUsername` AS `fDeliverer_Name`
	, `u_Confirm`.`fUsername` AS `fConfirm_Name`, `u_Cancel`.`fUsername` AS `fCancel_Name`, `e_fEspecieID`.`fTitle` AS `fEspecie`, `e_fCategoryID`.`fTitle` AS `fCategory`, `e_fBrandMateriaID`.`fTitle` AS `fBrandMateria`
	, `e_fColorID`.`fTitle` AS `fColor`, `e_fAvistaID`.`fTitle` AS `fAvista`, `e_fTamanhoID`.`fTitle` AS `fTamanho`, `e_fVendedorID`.`fTitle` AS `fVendedor`, `e_fNrCopyID`.`fTitle` AS `fNrCopy`
FROM `t_order` `o`
	LEFT JOIN `t_customer` `c` ON `o`.`fCustomerID` = `c`.`fCustomerID`
	LEFT JOIN `sysusers` `u_Submited` ON `o`.`fSubmitID` = `u_Submited`.`fUserID`
	LEFT JOIN `sysusers` `u_Entry` ON `o`.`fEntryID` = `u_Entry`.`fUserID`
	LEFT JOIN `sysusers` `u_Reviewer` ON `o`.`fReviewerID` = `u_Reviewer`.`fUserID`
	LEFT JOIN `sysusers` `u_Deliverer` ON `o`.`fDelivererID` = `u_Deliverer`.`fUserID`
	LEFT JOIN `sysusers` `u_Confirm` ON `o`.`fConfirmID` = `u_Confirm`.`fUserID`
	LEFT JOIN `sysusers` `u_Cancel` ON `o`.`fCancelID` = `u_Cancel`.`fUserID`
	LEFT JOIN `t_enumeration` `e_fEspecieID` ON `o`.`fEspecieID` = `e_fEspecieID`.`fItemID`
	LEFT JOIN `t_enumeration` `e_fCategoryID` ON `o`.`fCategoryID` = `e_fCategoryID`.`fItemID`
	LEFT JOIN `t_enumeration` `e_fBrandMateriaID` ON `o`.`fBrandMateriaID` = `e_fBrandMateriaID`.`fItemID`
	LEFT JOIN `t_enumeration` `e_fColorID` ON `o`.`fColorID` = `e_fColorID`.`fItemID`
	LEFT JOIN `t_enumeration` `e_fAvistaID` ON `o`.`fAvistaID` = `e_fAvistaID`.`fItemID`
	LEFT JOIN `t_enumeration` `e_fTamanhoID` ON `o`.`fTamanhoID` = `e_fTamanhoID`.`fItemID`
	LEFT JOIN `t_enumeration` `e_fVendedorID` ON `o`.`fVendedorID` = `e_fVendedorID`.`fItemID`
	LEFT JOIN `t_enumeration` `e_fNrCopyID` ON `o`.`fNrCopyID` = `e_fNrCopyID`.`fItemID` ;

-- 导出  视图 cedar.v_order_readonly 结构
DROP VIEW IF EXISTS `v_order_readonly`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_order_readonly`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_order_readonly` AS select `t`.`fOrderID` AS `fOrderID`,`t`.`fPrice` AS `fPrice`,`t`.`fCustomerID` AS `fCustomerID`,`t`.`fOrderDate` AS `fOrderDate`,`t`.`fEspecieID` AS `fEspecieID`,`t`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,`t`.`fCategoryID` AS `fCategoryID`,`t`.`fBrandMateriaID` AS `fBrandMateriaID`,`t`.`fAmount` AS `fAmount`,`t`.`fTax` AS `fTax`,`t`.`fPayable` AS `fPayable`,`t`.`fDesconto` AS `fDesconto`,`t`.`fColorID` AS `fColorID`,`t`.`fEntryID` AS `fEntryID`,`t`.`fSubmited` AS `fSubmited`,`t`.`fSubmitID` AS `fSubmitID`,`t`.`fReviewed` AS `fReviewed`,`t`.`fReviewerID` AS `fReviewerID`,`t`.`fConfirmed` AS `fConfirmed`,`t`.`fConfirmID` AS `fConfirmID`,`t`.`fDelivered` AS `fDelivered`,`t`.`fDelivererID` AS `fDelivererID`,`t`.`fCanceled` AS `fCanceled`,`t`.`fCancelID` AS `fCancelID`,`t`.`fDeliveryDate` AS `fDeliveryDate`,`t`.`fNumerBegin` AS `fNumerBegin`,`t`.`fQuant` AS `fQuant`,`t`.`fPagePerVolumn` AS `fPagePerVolumn`,`t`.`fNumerEnd` AS `fNumerEnd`,`t`.`fAvistaID` AS `fAvistaID`,`t`.`fTamanhoID` AS `fTamanhoID`,`t`.`fSucursal` AS `fSucursal`,`t`.`fLogo` AS `fLogo`,`t`.`fVendedorID` AS `fVendedorID`,`t`.`fNrCopyID` AS `fNrCopyID`,`t`.`fContato` AS `fContato`,`t`.`fCelular` AS `fCelular`,`t`.`fTelefone` AS `fTelefone`,`t`.`fNote` AS `fNote`,`c`.`fCustomerName` AS `fCustomerName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fAreaCode` AS `fAreaCode`,`c`.`fEndereco` AS `fEndereco`,`c`.`fEmail` AS `fEmail`,`c`.`fWeb` AS `fWeb` from (`t_order` `t` left join `t_customer` `c` on((`t`.`fCustomerID` = `c`.`fCustomerID`))) ;

-- 导出  视图 cedar.v_product_outbound_order 结构
DROP VIEW IF EXISTS `v_product_outbound_order`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_product_outbound_order`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_product_outbound_order` AS SELECT `o`.`fOrderID` AS `fOrderID`,
         `o`.`fPrice` AS `fPrice`,
         `o`.`fCustomerID` AS `fCustomerID`,
         `o`.`fOrderDate` AS `fOrderDate`,
         `o`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,
         `o`.`fAmount` AS `fAmount`,
         `o`.`fTax` AS `fTax` ,
         `o`.`fPayable` AS `fPayable`,
         `o`.`fDesconto` AS `fDesconto`,
         `o`.`fEntryID` AS `fEntryID` ,
         `o`.`fSubmited` + 0 AS `fSubmited`,
         `o`.`fSubmitID` AS `fSubmitID` ,
         `o`.`fReviewed` + 0 AS `fReviewed`,
         `o`.`fReviewerID` AS `fReviewerID` ,
         `o`.`fConfirmed` + 0 AS `fConfirmed`,
         `o`.`fConfirmID` AS `fConfirmID` ,
         `o`.`fDelivered` + 0 AS `fDelivered`,
         `o`.`fDelivererID` AS `fDelivererID` ,
         `o`.`fCanceled` + 0 AS `fCanceled`,
         `o`.`fCancelID` AS `fCancelID`,
         `o`.`fDeliveryDate` AS `fDeliveryDate`,
         `o`.`fQuant` AS `fQuant`,
         `o`.`fSucursal` + 0 AS `fSucursal` ,
         `o`.`fVendedorID` AS `fVendedorID`,
         `o`.`fContato` AS `fContato`,
         `o`.`fCelular` AS `fCelular`,
         `o`.`fTelefone` AS `fTelefone`,
         `o`.`fNote` AS `fNote`,
         `c`.`fTaxRegCer` AS `fTaxRegCer` ,
         `c`.`fCustomerName` AS `fCustomerName`,
         `c`.`fNUIT` AS `fNUIT`,
         `c`.`fCity` AS `fCity`,
         `c`.`fEndereco` AS `fEndereco` ,
         `c`.`fEmail` AS `fEmail` ,
        
    CASE `o`.`fSucursal`
    WHEN 1 THEN
    'SIM'
    ELSE 'Non'
    END AS `fSucursal1` ,
    CASE `o`.`fSubmited`
    WHEN 1 THEN
    'SIM'
    ELSE ''
    END AS `fSubmited1` ,
    CASE `o`.`fConfirmed`
    WHEN 1 THEN
    'SIM'
    ELSE ''
    END AS `fConfirmed1` ,
    CASE `o`.`fDelivered`
    WHEN 1 THEN
    'SIM'
    ELSE ''
    END AS `fDelivered1` ,
    CASE `o`.`fCanceled`
    WHEN 1 THEN
    'Canceled'
    ELSE ''
    END AS `fCanceled1` , `u_Submited`.`fUsername` AS `fSubmit_Name`, 
	 `u_Entry`.`fUsername` AS `fEntry_Name`, `u_Reviewer`.`fUsername` AS `fReviewer_Name`, 
	 `u_Deliverer`.`fUsername` AS `fDeliverer_Name` , `u_Confirm`.`fUsername` AS `fConfirm_Name`, 
	 `u_Cancel`.`fUsername` AS `fCancel_Name`, 
	 `e_fVendedorID`.`fTitle` AS `fVendedor`
FROM `t_product_outbound_order` `o`
LEFT JOIN `t_customer` `c`
    ON `o`.`fCustomerID` = `c`.`fCustomerID`
LEFT JOIN `sysusers` `u_Submited`
    ON `o`.`fSubmitID` = `u_Submited`.`fUserID`
LEFT JOIN `sysusers` `u_Entry`
    ON `o`.`fEntryID` = `u_Entry`.`fUserID`
LEFT JOIN `sysusers` `u_Reviewer`
    ON `o`.`fReviewerID` = `u_Reviewer`.`fUserID`
LEFT JOIN `sysusers` `u_Deliverer`
    ON `o`.`fDelivererID` = `u_Deliverer`.`fUserID`
LEFT JOIN `sysusers` `u_Confirm`
    ON `o`.`fConfirmID` = `u_Confirm`.`fUserID`
LEFT JOIN `sysusers` `u_Cancel`
    ON `o`.`fCancelID` = `u_Cancel`.`fUserID`
LEFT JOIN `t_enumeration` `e_fVendedorID`
    ON `o`.`fVendedorID` = `e_fVendedorID`.`fItemID` ;

-- 导出  视图 cedar.v_product_warehousereceipt_order 结构
DROP VIEW IF EXISTS `v_product_warehousereceipt_order`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_product_warehousereceipt_order`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_product_warehousereceipt_order` AS SELECT `o`.`fOrderID` AS `fOrderID`,
         `o`.`fPrice` AS `fPrice`,
         `o`.`fSupplierID` AS `fSupplierID`,
         `o`.`fOrderDate` AS `fOrderDate`,
         `o`.`fWarehousingDate` AS `fWarehousingDate`,
         `o`.`fAmount` AS `fAmount`,
         `o`.`fTax` AS `fTax` ,
         `o`.`fPayable` AS `fPayable`,
         `o`.`fDesconto` AS `fDesconto`,
         `o`.`fEntryID` AS `fEntryID` ,
         `o`.`fSubmited` + 0 AS `fSubmited`,
         `o`.`fSubmitID` AS `fSubmitID` ,


         `o`.`fCanceled` + 0 AS `fCanceled`,
         `o`.`fCancelID` AS `fCancelID`,

         `o`.`fPurchaserID` AS `fPurchaserID`,
         `o`.`fContato` AS `fContato`,
         `o`.`fCelular` AS `fCelular`,
         `o`.`fTelefone` AS `fTelefone`,
         `o`.`fNote` AS `fNote`,
         `c`.`fTaxRegCer` AS `fTaxRegCer` ,
         `c`.`fSupplierName` AS `fSupplierName`,
         `c`.`fNUIT` AS `fNUIT`,
         `c`.`fCity` AS `fCity`,
         `c`.`fEndereco` AS `fEndereco` ,
          `c`.`fEmail` AS `fEmail` ,       

    CASE `o`.`fSubmited`
    WHEN 1 THEN
    'SIM'
    ELSE ''
    END AS `fSubmited1` ,
    
    
    CASE `o`.`fCanceled`
    WHEN 1 THEN
    'Canceled'
    ELSE ''
    END AS `fCanceled1` , `u_Submited`.`fUsername` AS `fSubmit_Name`, 
	 `u_Entry`.`fUsername` AS `fEntry_Name`, 
	 
	 `u_Cancel`.`fUsername` AS `fCancel_Name`, 
	 `e_fPurchaserID`.`fTitle` AS `fPurchaser`
FROM `t_product_warehousereceipt_order` `o`
LEFT JOIN `t_Supplier` `c`
    ON `o`.`fSupplierID` = `c`.`fSupplierID`
LEFT JOIN `sysusers` `u_Submited`
    ON `o`.`fSubmitID` = `u_Submited`.`fUserID`
LEFT JOIN `sysusers` `u_Entry`
    ON `o`.`fEntryID` = `u_Entry`.`fUserID`

LEFT JOIN `sysusers` `u_Cancel`
    ON `o`.`fCancelID` = `u_Cancel`.`fUserID`
LEFT JOIN `t_enumeration` `e_fPurchaserID`
    ON `o`.`fPurchaserID` = `e_fPurchaserID`.`fItemID` ;

-- 导出  视图 cedar.v_quotation 结构
DROP VIEW IF EXISTS `v_quotation`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_quotation`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_quotation` AS select `o`.`fOrderID` AS `fOrderID`,`o`.`fPrice` AS `fPrice`,`o`.`fCustomerID` AS `fCustomerID`,`o`.`fOrderDate` AS `fOrderDate`,`o`.`fEspecieID` AS `fEspecieID`,`o`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,`o`.`fCategoryID` AS `fCategoryID`,`o`.`fBrandMateriaID` AS `fBrandMateriaID`,`o`.`fAmount` AS `fAmount`,`o`.`fTax` AS `fTax`,`o`.`fPayable` AS `fPayable`,`o`.`fDesconto` AS `fDesconto`,`o`.`fColorID` AS `fColorID`,`o`.`fEntryID` AS `fEntryID`,(`o`.`fSubmited` + 0) AS `fSubmited`,`o`.`fSubmitID` AS `fSubmitID`,(`o`.`fReviewed` + 0) AS `fReviewed`,`o`.`fReviewerID` AS `fReviewerID`,(`o`.`fConfirmed` + 0) AS `fConfirmed`,`o`.`fConfirmID` AS `fConfirmID`,(`o`.`fDelivered` + 0) AS `fDelivered`,`o`.`fDelivererID` AS `fDelivererID`,(`o`.`fCanceled` + 0) AS `fCanceled`,(`o`.`fDeliverViewed` + 0) AS `fDeliverViewed`,`o`.`fCancelID` AS `fCancelID`,`o`.`fDeliveryDate` AS `fDeliveryDate`,`o`.`fNumerBegin` AS `fNumerBegin`,`o`.`fQuant` AS `fQuant`,`o`.`fPagePerVolumn` AS `fPagePerVolumn`,`o`.`fNumerEnd` AS `fNumerEnd`,`o`.`fAvistaID` AS `fAvistaID`,`o`.`fTamanhoID` AS `fTamanhoID`,(`o`.`fSucursal` + 0) AS `fSucursal`,(`o`.`fLogo` + 0) AS `fLogo`,`o`.`fVendedorID` AS `fVendedorID`,`o`.`fNrCopyID` AS `fNrCopyID`,`o`.`fContato` AS `fContato`,`o`.`fCelular` AS `fCelular`,`o`.`fTelefone` AS `fTelefone`,`o`.`fNote` AS `fNote`,(`o`.`fCreatedOrder` + 0) AS `fCreatedOrder`,`c`.`fCustomerName` AS `fCustomerName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fEndereco` AS `fEndereco`,(case `o`.`fSucursal` when 1 then 'SIM' else 'Non' end) AS `fSucursal1`,(case `o`.`fSubmited` when 1 then 'SIM' else '' end) AS `fSubmited1`,(case `o`.`fConfirmed` when 1 then 'SIM' else '' end) AS `fConfirmed1`,(case `o`.`fDelivered` when 1 then 'SIM' else '' end) AS `fDelivered1`,(case `o`.`fCanceled` when 1 then 'Canceled' else '' end) AS `fCanceled1`,(case `o`.`fDeliverViewed` when 1 then 'SIM' else '' end) AS `fDeliverViewed1`,(case `o`.`fLogo` when 1 then 'SIM' else 'Non' end) AS `fLogo1`,`u_Submited`.`fUsername` AS `fSubmit_Name`,`u_Entry`.`fUsername` AS `fEntry_Name`,`u_Reviewer`.`fUsername` AS `fReviewer_Name`,`u_Deliverer`.`fUsername` AS `fDeliverer_Name`,`u_Confirm`.`fUsername` AS `fConfirm_Name`,`u_Cancel`.`fUsername` AS `fCancel_Name`,`e_fEspecieID`.`fTitle` AS `fEspecie`,`e_fCategoryID`.`fTitle` AS `fCategory`,`e_fBrandMateriaID`.`fTitle` AS `fBrandMateria`,`e_fColorID`.`fTitle` AS `fColor`,`e_fAvistaID`.`fTitle` AS `fAvista`,`e_fTamanhoID`.`fTitle` AS `fTamanho`,`e_fVendedorID`.`fTitle` AS `fVendedor`,`e_fNrCopyID`.`fTitle` AS `fNrCopy` from (((((((((((((((`t_quotation` `o` left join `t_customer` `c` on((`o`.`fCustomerID` = `c`.`fCustomerID`))) left join `sysusers` `u_Submited` on((`o`.`fSubmitID` = `u_Submited`.`fUserID`))) left join `sysusers` `u_Entry` on((`o`.`fEntryID` = `u_Entry`.`fUserID`))) left join `sysusers` `u_Reviewer` on((`o`.`fReviewerID` = `u_Reviewer`.`fUserID`))) left join `sysusers` `u_Deliverer` on((`o`.`fDelivererID` = `u_Deliverer`.`fUserID`))) left join `sysusers` `u_Confirm` on((`o`.`fConfirmID` = `u_Confirm`.`fUserID`))) left join `sysusers` `u_Cancel` on((`o`.`fCancelID` = `u_Cancel`.`fUserID`))) left join `t_enumeration` `e_fEspecieID` on((`o`.`fEspecieID` = `e_fEspecieID`.`fItemID`))) left join `t_enumeration` `e_fCategoryID` on((`o`.`fCategoryID` = `e_fCategoryID`.`fItemID`))) left join `t_enumeration` `e_fBrandMateriaID` on((`o`.`fBrandMateriaID` = `e_fBrandMateriaID`.`fItemID`))) left join `t_enumeration` `e_fColorID` on((`o`.`fColorID` = `e_fColorID`.`fItemID`))) left join `t_enumeration` `e_fAvistaID` on((`o`.`fAvistaID` = `e_fAvistaID`.`fItemID`))) left join `t_enumeration` `e_fTamanhoID` on((`o`.`fTamanhoID` = `e_fTamanhoID`.`fItemID`))) left join `t_enumeration` `e_fVendedorID` on((`o`.`fVendedorID` = `e_fVendedorID`.`fItemID`))) left join `t_enumeration` `e_fNrCopyID` on((`o`.`fNrCopyID` = `e_fNrCopyID`.`fItemID`))) ;

-- 导出  视图 cedar.v_receivables 结构
DROP VIEW IF EXISTS `v_receivables`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_receivables`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_receivables` AS select `r`.`fID` AS `fID`,`r`.`fCustomerID` AS `fCustomerID`,`c`.`fCustomerName` AS `fCustomerName`,`r`.`fReceiptDate` AS `fReceiptDate`,`r`.`fAmountCollected` AS `fAmountCollected`,`r`.`fOrderID` AS `fOrderID`,`u`.`fUsername` AS `fPayee`,`skfs`.`fTitle` AS `fPaymentMethod`,`r`.`fNote` AS `fNote` from ((((`t_receivables` `r` left join `t_customer` `c` on((`r`.`fCustomerID` = `c`.`fCustomerID`))) left join `t_enumeration` `e` on((`r`.`fPaymentMethodID` = `e`.`fItemID`))) left join `sysusers` `u` on((`r`.`fPayeeID` = `u`.`fUserID`))) left join `t_enumeration` `skfs` on((`r`.`fPaymentMethodID` = `skfs`.`fItemID`))) ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
