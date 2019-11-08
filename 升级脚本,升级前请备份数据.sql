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



ALTER TABLE `t_customer`
	CHANGE COLUMN `fEndereco` `fEndereco` VARCHAR(50) NULL DEFAULT NULL COMMENT '地址' AFTER `fTelefone`;

/*!40000 ALTER TABLE `sysnavigationmenus` DISABLE KEYS */;
INSERT INTO `sysnavigationmenus` (`fNMID`, `fDispIndex`, `fParentId`, `fEnabled`, `fMenuText`, `fCommand`, `fObjectName`, `fFormMode`, `fArg`, `fIcon`, `fDefault`, `fNodeBackvolor`, `fNodeForeColor`, `fNodeFontBold`, `fExpanded`, `fDescription`, `fLevel`, `fIsCommandButton`, `TS`) VALUES
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
	(185, 16810, 168, b'1', 'Print', 0, 'CmdPrint', NULL, NULL, 'print.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-10-18 09:39:54'),
	(186, 421, 21, b'1', 'ProductInOutDetails', 0, NULL, NULL, NULL, 'reports.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-11-01 09:18:40'),
	(187, 18602, 186, b'1', 'Print', 0, 'CmdPrint', NULL, NULL, 'print.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-11-01 11:34:34'),
	(188, 18703, 186, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-11-01 11:34:38');
/*!40000 ALTER TABLE `sysnavigationmenus` ENABLE KEYS */;

-- 导出  表 cedar.t_product_information 结构
CREATE TABLE IF NOT EXISTS `t_product_information` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fProductName` varchar(250) CHARACTER SET utf8 NOT NULL,
  `fSpesc` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `fWidth` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `fLength` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `fUint` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `fNote` varchar(250) CHARACTER SET utf8 DEFAULT NULL,
  `fCurrentQuantity` decimal(13,3) NOT NULL DEFAULT '0.000',
  `fMinimumStock` decimal(13,3) NOT NULL DEFAULT '0.000',
  `fCancel` tinyint(4) NOT NULL DEFAULT '0',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fProductPic` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 数据导出被取消选择。
-- 导出  表 cedar.t_product_outbound_order 结构
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

-- 数据导出被取消选择。
-- 导出  表 cedar.t_product_outbound_order_detail 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 cedar.t_product_warehousereceipt_order 结构
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

-- 数据导出被取消选择。
-- 导出  表 cedar.t_product_warehousereceipt_order_detail 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 cedar.t_supplier 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  视图 cedar.v_all_sales 结构
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_all_sales` (
	`fOrderID` CHAR(20) NOT NULL COLLATE 'utf8_general_ci',
	`fOrderDate` DATE NOT NULL,
	`fCustomerID` INT(11) NOT NULL,
	`fPrice` DECIMAL(10,2) NULL,
	`fQuant` INT(11) NULL,
	`fAmount` DECIMAL(11,2) NULL,
	`fTax` DECIMAL(11,2) NULL,
	`fDesconto` DECIMAL(11,2) NULL,
	`fPayable` DECIMAL(11,2) NULL,
	`TS` TIMESTAMP NOT NULL
) ENGINE=MyISAM;


-- 导出  视图 cedar.v_all_sales 结构
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_all_sales`;
CREATE ALGORITHM=UNDEFINED  SQL SECURITY INVOKER VIEW `v_all_sales` AS SELECT `t_order`.`fOrderID` AS `fOrderID`, `t_order`.`fOrderDate` AS `fOrderDate`, `t_order`.`fCustomerID` AS `fCustomerID`, `t_order`.`fPrice` AS `fPrice`, `t_order`.`fQuant` AS `fQuant`
	, `t_order`.`fAmount` AS `fAmount`, `t_order`.`fTax` AS `fTax`, `t_order`.`fDesconto` AS `fDesconto`, `t_order`.`fPayable` AS `fPayable`, `t_order`.`TS` AS `TS`
FROM `t_order`
WHERE (`t_order`.`fSubmited` = 1)
	AND (`t_order`.`fConfirmed` = 1)
	AND (`t_order`.`fCanceled` = 0)
UNION ALL
SELECT t_product_outbound_order.`fOrderID` AS `fOrderID`, t_product_outbound_order.`fOrderDate` AS `fOrderDate`, t_product_outbound_order.`fCustomerID` AS `fCustomerID`, t_product_outbound_order.`fPrice` AS `fPrice`, t_product_outbound_order.`fQuant` AS `fQuant`
	, t_product_outbound_order.`fAmount` AS `fAmount`, t_product_outbound_order.`fTax` AS `fTax`, t_product_outbound_order.`fDesconto` AS `fDesconto`, t_product_outbound_order.`fPayable` AS `fPayable`, t_product_outbound_order.`TS` AS `TS`
FROM t_product_outbound_order
WHERE t_product_outbound_order.`fSubmited` = 1
AND t_product_outbound_order.`fConfirmed` = 1
	AND t_product_outbound_order.`fCanceled` = 0 ;

-- 导出  视图 cedar.v_order 结构
-- 移除临时表并创建最终视图结构
DROP VIEW IF EXISTS `v_order`;
CREATE ALGORITHM=UNDEFINED  SQL SECURITY INVOKER VIEW `v_order` AS select `o`.`fOrderID` AS `fOrderID`,`o`.`fPrice` AS `fPrice`,`o`.`fCustomerID` AS `fCustomerID`,`o`.`fOrderDate` AS `fOrderDate`,`o`.`fEspecieID` AS `fEspecieID`,`o`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,`o`.`fCategoryID` AS `fCategoryID`,`o`.`fBrandMateriaID` AS `fBrandMateriaID`,`o`.`fAmount` AS `fAmount`,`o`.`fTax` AS `fTax`,`o`.`fPayable` AS `fPayable`,`o`.`fDesconto` AS `fDesconto`,`o`.`fColorID` AS `fColorID`,`o`.`fEntryID` AS `fEntryID`,(`o`.`fSubmited` + 0) AS `fSubmited`,`o`.`fSubmitID` AS `fSubmitID`,(`o`.`fReviewed` + 0) AS `fReviewed`,`o`.`fReviewerID` AS `fReviewerID`,(`o`.`fConfirmed` + 0) AS `fConfirmed`,`o`.`fConfirmID` AS `fConfirmID`,(`o`.`fDelivered` + 0) AS `fDelivered`,`o`.`fDelivererID` AS `fDelivererID`,(`o`.`fCanceled` + 0) AS `fCanceled`,(`o`.`fDeliverViewed` + 0) AS `fDeliverViewed`,`o`.`fCancelID` AS `fCancelID`,`o`.`fDeliveryDate` AS `fDeliveryDate`,`o`.`fNumerBegin` AS `fNumerBegin`,`o`.`fQuant` AS `fQuant`,`o`.`fPagePerVolumn` AS `fPagePerVolumn`,`o`.`fNumerEnd` AS `fNumerEnd`,`o`.`fAvistaID` AS `fAvistaID`,`o`.`fTamanhoID` AS `fTamanhoID`,(`o`.`fSucursal` + 0) AS `fSucursal`,(`o`.`fLogo` + 0) AS `fLogo`,`o`.`fVendedorID` AS `fVendedorID`,`o`.`fNrCopyID` AS `fNrCopyID`,`o`.`fContato` AS `fContato`,`o`.`fCelular` AS `fCelular`,`o`.`fTelefone` AS `fTelefone`,`o`.`fNote` AS `fNote`,`c`.`fTaxRegCer` AS `fTaxRegCer`,`c`.`fCustomerName` AS `fCustomerName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fEndereco` AS `fEndereco`,`c`.`fEmail` AS `fEmail`,(case `o`.`fSucursal` when 1 then 'SIM' else 'Non' end) AS `fSucursal1`,(case `o`.`fSubmited` when 1 then 'SIM' else '' end) AS `fSubmited1`,(case `o`.`fConfirmed` when 1 then 'SIM' else '' end) AS `fConfirmed1`,(case `o`.`fDelivered` when 1 then 'SIM' else '' end) AS `fDelivered1`,(case `o`.`fCanceled` when 1 then 'Canceled' else '' end) AS `fCanceled1`,(case `o`.`fDeliverViewed` when 1 then 'SIM' else '' end) AS `fDeliverViewed1`,(case `o`.`fLogo` when 1 then 'SIM' else 'Non' end) AS `fLogo1`,`u_Submited`.`fUsername` AS `fSubmit_Name`,`u_Entry`.`fUsername` AS `fEntry_Name`,`u_Reviewer`.`fUsername` AS `fReviewer_Name`,`u_Deliverer`.`fUsername` AS `fDeliverer_Name`,`u_Confirm`.`fUsername` AS `fConfirm_Name`,`u_Cancel`.`fUsername` AS `fCancel_Name`,`e_fEspecieID`.`fTitle` AS `fEspecie`,`e_fCategoryID`.`fTitle` AS `fCategory`,`e_fBrandMateriaID`.`fTitle` AS `fBrandMateria`,`e_fColorID`.`fTitle` AS `fColor`,`e_fAvistaID`.`fTitle` AS `fAvista`,`e_fTamanhoID`.`fTitle` AS `fTamanho`,`e_fVendedorID`.`fTitle` AS `fVendedor`,`e_fNrCopyID`.`fTitle` AS `fNrCopy` from (((((((((((((((`t_order` `o` left join `t_customer` `c` on((`o`.`fCustomerID` = `c`.`fCustomerID`))) left join `sysusers` `u_Submited` on((`o`.`fSubmitID` = `u_Submited`.`fUserID`))) left join `sysusers` `u_Entry` on((`o`.`fEntryID` = `u_Entry`.`fUserID`))) left join `sysusers` `u_Reviewer` on((`o`.`fReviewerID` = `u_Reviewer`.`fUserID`))) left join `sysusers` `u_Deliverer` on((`o`.`fDelivererID` = `u_Deliverer`.`fUserID`))) left join `sysusers` `u_Confirm` on((`o`.`fConfirmID` = `u_Confirm`.`fUserID`))) left join `sysusers` `u_Cancel` on((`o`.`fCancelID` = `u_Cancel`.`fUserID`))) left join `t_enumeration` `e_fEspecieID` on((`o`.`fEspecieID` = `e_fEspecieID`.`fItemID`))) left join `t_enumeration` `e_fCategoryID` on((`o`.`fCategoryID` = `e_fCategoryID`.`fItemID`))) left join `t_enumeration` `e_fBrandMateriaID` on((`o`.`fBrandMateriaID` = `e_fBrandMateriaID`.`fItemID`))) left join `t_enumeration` `e_fColorID` on((`o`.`fColorID` = `e_fColorID`.`fItemID`))) left join `t_enumeration` `e_fAvistaID` on((`o`.`fAvistaID` = `e_fAvistaID`.`fItemID`))) left join `t_enumeration` `e_fTamanhoID` on((`o`.`fTamanhoID` = `e_fTamanhoID`.`fItemID`))) left join `t_enumeration` `e_fVendedorID` on((`o`.`fVendedorID` = `e_fVendedorID`.`fItemID`))) left join `t_enumeration` `e_fNrCopyID` on((`o`.`fNrCopyID` = `e_fNrCopyID`.`fItemID`))) ;

-- 导出  视图 cedar.v_order_readonly 结构
-- 移除临时表并创建最终视图结构
DROP VIEW IF EXISTS `v_order_readonly`;
CREATE ALGORITHM=UNDEFINED  SQL SECURITY INVOKER VIEW `v_order_readonly` AS select `t`.`fOrderID` AS `fOrderID`,`t`.`fPrice` AS `fPrice`,`t`.`fCustomerID` AS `fCustomerID`,`t`.`fOrderDate` AS `fOrderDate`,`t`.`fEspecieID` AS `fEspecieID`,`t`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,`t`.`fCategoryID` AS `fCategoryID`,`t`.`fBrandMateriaID` AS `fBrandMateriaID`,`t`.`fAmount` AS `fAmount`,`t`.`fTax` AS `fTax`,`t`.`fPayable` AS `fPayable`,`t`.`fDesconto` AS `fDesconto`,`t`.`fColorID` AS `fColorID`,`t`.`fEntryID` AS `fEntryID`,`t`.`fSubmited` AS `fSubmited`,`t`.`fSubmitID` AS `fSubmitID`,`t`.`fReviewed` AS `fReviewed`,`t`.`fReviewerID` AS `fReviewerID`,`t`.`fConfirmed` AS `fConfirmed`,`t`.`fConfirmID` AS `fConfirmID`,`t`.`fDelivered` AS `fDelivered`,`t`.`fDelivererID` AS `fDelivererID`,`t`.`fCanceled` AS `fCanceled`,`t`.`fCancelID` AS `fCancelID`,`t`.`fDeliveryDate` AS `fDeliveryDate`,`t`.`fNumerBegin` AS `fNumerBegin`,`t`.`fQuant` AS `fQuant`,`t`.`fPagePerVolumn` AS `fPagePerVolumn`,`t`.`fNumerEnd` AS `fNumerEnd`,`t`.`fAvistaID` AS `fAvistaID`,`t`.`fTamanhoID` AS `fTamanhoID`,`t`.`fSucursal` AS `fSucursal`,`t`.`fLogo` AS `fLogo`,`t`.`fVendedorID` AS `fVendedorID`,`t`.`fNrCopyID` AS `fNrCopyID`,`t`.`fContato` AS `fContato`,`t`.`fCelular` AS `fCelular`,`t`.`fTelefone` AS `fTelefone`,`t`.`fNote` AS `fNote`,`c`.`fCustomerName` AS `fCustomerName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fAreaCode` AS `fAreaCode`,`c`.`fEndereco` AS `fEndereco`,`c`.`fEmail` AS `fEmail`,`c`.`fWeb` AS `fWeb` from (`t_order` `t` left join `t_customer` `c` on((`t`.`fCustomerID` = `c`.`fCustomerID`))) ;

-- 导出  视图 cedar.v_product_outbound_order 结构
-- 移除临时表并创建最终视图结构
DROP VIEW IF EXISTS `v_product_outbound_order`;
CREATE ALGORITHM=UNDEFINED  SQL SECURITY INVOKER VIEW `v_product_outbound_order` AS select `o`.`fOrderID` AS `fOrderID`,`o`.`fPrice` AS `fPrice`,`o`.`fCustomerID` AS `fCustomerID`,`o`.`fOrderDate` AS `fOrderDate`,`o`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,`o`.`fAmount` AS `fAmount`,`o`.`fTax` AS `fTax`,`o`.`fPayable` AS `fPayable`,`o`.`fDesconto` AS `fDesconto`,`o`.`fEntryID` AS `fEntryID`,(`o`.`fSubmited` + 0) AS `fSubmited`,`o`.`fSubmitID` AS `fSubmitID`,(`o`.`fReviewed` + 0) AS `fReviewed`,`o`.`fReviewerID` AS `fReviewerID`,(`o`.`fConfirmed` + 0) AS `fConfirmed`,`o`.`fConfirmID` AS `fConfirmID`,(`o`.`fDelivered` + 0) AS `fDelivered`,`o`.`fDelivererID` AS `fDelivererID`,(`o`.`fCanceled` + 0) AS `fCanceled`,`o`.`fCancelID` AS `fCancelID`,`o`.`fDeliveryDate` AS `fDeliveryDate`,`o`.`fQuant` AS `fQuant`,(`o`.`fSucursal` + 0) AS `fSucursal`,`o`.`fVendedorID` AS `fVendedorID`,`o`.`fContato` AS `fContato`,`o`.`fCelular` AS `fCelular`,`o`.`fTelefone` AS `fTelefone`,`o`.`fNote` AS `fNote`,`c`.`fTaxRegCer` AS `fTaxRegCer`,`c`.`fCustomerName` AS `fCustomerName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fEndereco` AS `fEndereco`,`c`.`fEmail` AS `fEmail`,(case `o`.`fSucursal` when 1 then 'SIM' else 'Non' end) AS `fSucursal1`,(case `o`.`fSubmited` when 1 then 'SIM' else '' end) AS `fSubmited1`,(case `o`.`fConfirmed` when 1 then 'SIM' else '' end) AS `fConfirmed1`,(case `o`.`fDelivered` when 1 then 'SIM' else '' end) AS `fDelivered1`,(case `o`.`fCanceled` when 1 then 'Canceled' else '' end) AS `fCanceled1`,`u_Submited`.`fUsername` AS `fSubmit_Name`,`u_Entry`.`fUsername` AS `fEntry_Name`,`u_Reviewer`.`fUsername` AS `fReviewer_Name`,`u_Deliverer`.`fUsername` AS `fDeliverer_Name`,`u_Confirm`.`fUsername` AS `fConfirm_Name`,`u_Cancel`.`fUsername` AS `fCancel_Name`,`e_fVendedorID`.`fTitle` AS `fVendedor` from ((((((((`t_product_outbound_order` `o` left join `t_customer` `c` on((`o`.`fCustomerID` = `c`.`fCustomerID`))) left join `sysusers` `u_Submited` on((`o`.`fSubmitID` = `u_Submited`.`fUserID`))) left join `sysusers` `u_Entry` on((`o`.`fEntryID` = `u_Entry`.`fUserID`))) left join `sysusers` `u_Reviewer` on((`o`.`fReviewerID` = `u_Reviewer`.`fUserID`))) left join `sysusers` `u_Deliverer` on((`o`.`fDelivererID` = `u_Deliverer`.`fUserID`))) left join `sysusers` `u_Confirm` on((`o`.`fConfirmID` = `u_Confirm`.`fUserID`))) left join `sysusers` `u_Cancel` on((`o`.`fCancelID` = `u_Cancel`.`fUserID`))) left join `t_enumeration` `e_fVendedorID` on((`o`.`fVendedorID` = `e_fVendedorID`.`fItemID`))) ;

-- 导出  视图 cedar.v_product_warehousereceipt_order 结构
-- 移除临时表并创建最终视图结构
DROP VIEW IF EXISTS `v_product_warehousereceipt_order`;
CREATE ALGORITHM=UNDEFINED  SQL SECURITY INVOKER VIEW `v_product_warehousereceipt_order` AS select `o`.`fOrderID` AS `fOrderID`,`o`.`fPrice` AS `fPrice`,`o`.`fSupplierID` AS `fSupplierID`,`o`.`fOrderDate` AS `fOrderDate`,`o`.`fWarehousingDate` AS `fWarehousingDate`,`o`.`fAmount` AS `fAmount`,`o`.`fTax` AS `fTax`,`o`.`fPayable` AS `fPayable`,`o`.`fDesconto` AS `fDesconto`,`o`.`fEntryID` AS `fEntryID`,(`o`.`fSubmited` + 0) AS `fSubmited`,`o`.`fSubmitID` AS `fSubmitID`,(`o`.`fCanceled` + 0) AS `fCanceled`,`o`.`fCancelID` AS `fCancelID`,`o`.`fPurchaserID` AS `fPurchaserID`,`o`.`fContato` AS `fContato`,`o`.`fCelular` AS `fCelular`,`o`.`fTelefone` AS `fTelefone`,`o`.`fNote` AS `fNote`,`c`.`fTaxRegCer` AS `fTaxRegCer`,`c`.`fSupplierName` AS `fSupplierName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fEndereco` AS `fEndereco`,`c`.`fEmail` AS `fEmail`,(case `o`.`fSubmited` when 1 then 'SIM' else '' end) AS `fSubmited1`,(case `o`.`fCanceled` when 1 then 'Canceled' else '' end) AS `fCanceled1`,`u_Submited`.`fUsername` AS `fSubmit_Name`,`u_Entry`.`fUsername` AS `fEntry_Name`,`u_Cancel`.`fUsername` AS `fCancel_Name`,`e_fPurchaserID`.`fTitle` AS `fPurchaser` from (((((`t_product_warehousereceipt_order` `o` left join `t_supplier` `c` on((`o`.`fSupplierID` = `c`.`fSupplierID`))) left join `sysusers` `u_Submited` on((`o`.`fSubmitID` = `u_Submited`.`fUserID`))) left join `sysusers` `u_Entry` on((`o`.`fEntryID` = `u_Entry`.`fUserID`))) left join `sysusers` `u_Cancel` on((`o`.`fCancelID` = `u_Cancel`.`fUserID`))) left join `t_enumeration` `e_fPurchaserID` on((`o`.`fPurchaserID` = `e_fPurchaserID`.`fItemID`))) ;

-- 导出  视图 cedar.v_quotation 结构
-- 移除临时表并创建最终视图结构
DROP VIEW IF EXISTS `v_quotation`;
CREATE ALGORITHM=UNDEFINED  SQL SECURITY INVOKER VIEW `v_quotation` AS select `o`.`fOrderID` AS `fOrderID`,`o`.`fPrice` AS `fPrice`,`o`.`fCustomerID` AS `fCustomerID`,`o`.`fOrderDate` AS `fOrderDate`,`o`.`fEspecieID` AS `fEspecieID`,`o`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,`o`.`fCategoryID` AS `fCategoryID`,`o`.`fBrandMateriaID` AS `fBrandMateriaID`,`o`.`fAmount` AS `fAmount`,`o`.`fTax` AS `fTax`,`o`.`fPayable` AS `fPayable`,`o`.`fDesconto` AS `fDesconto`,`o`.`fColorID` AS `fColorID`,`o`.`fEntryID` AS `fEntryID`,(`o`.`fSubmited` + 0) AS `fSubmited`,`o`.`fSubmitID` AS `fSubmitID`,(`o`.`fReviewed` + 0) AS `fReviewed`,`o`.`fReviewerID` AS `fReviewerID`,(`o`.`fConfirmed` + 0) AS `fConfirmed`,`o`.`fConfirmID` AS `fConfirmID`,(`o`.`fDelivered` + 0) AS `fDelivered`,`o`.`fDelivererID` AS `fDelivererID`,(`o`.`fCanceled` + 0) AS `fCanceled`,(`o`.`fDeliverViewed` + 0) AS `fDeliverViewed`,`o`.`fCancelID` AS `fCancelID`,`o`.`fDeliveryDate` AS `fDeliveryDate`,`o`.`fNumerBegin` AS `fNumerBegin`,`o`.`fQuant` AS `fQuant`,`o`.`fPagePerVolumn` AS `fPagePerVolumn`,`o`.`fNumerEnd` AS `fNumerEnd`,`o`.`fAvistaID` AS `fAvistaID`,`o`.`fTamanhoID` AS `fTamanhoID`,(`o`.`fSucursal` + 0) AS `fSucursal`,(`o`.`fLogo` + 0) AS `fLogo`,`o`.`fVendedorID` AS `fVendedorID`,`o`.`fNrCopyID` AS `fNrCopyID`,`o`.`fContato` AS `fContato`,`o`.`fCelular` AS `fCelular`,`o`.`fTelefone` AS `fTelefone`,`o`.`fNote` AS `fNote`,(`o`.`fCreatedOrder` + 0) AS `fCreatedOrder`,`c`.`fCustomerName` AS `fCustomerName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fEndereco` AS `fEndereco`,(case `o`.`fSucursal` when 1 then 'SIM' else 'Non' end) AS `fSucursal1`,(case `o`.`fSubmited` when 1 then 'SIM' else '' end) AS `fSubmited1`,(case `o`.`fConfirmed` when 1 then 'SIM' else '' end) AS `fConfirmed1`,(case `o`.`fDelivered` when 1 then 'SIM' else '' end) AS `fDelivered1`,(case `o`.`fCanceled` when 1 then 'Canceled' else '' end) AS `fCanceled1`,(case `o`.`fDeliverViewed` when 1 then 'SIM' else '' end) AS `fDeliverViewed1`,(case `o`.`fLogo` when 1 then 'SIM' else 'Non' end) AS `fLogo1`,`u_Submited`.`fUsername` AS `fSubmit_Name`,`u_Entry`.`fUsername` AS `fEntry_Name`,`u_Reviewer`.`fUsername` AS `fReviewer_Name`,`u_Deliverer`.`fUsername` AS `fDeliverer_Name`,`u_Confirm`.`fUsername` AS `fConfirm_Name`,`u_Cancel`.`fUsername` AS `fCancel_Name`,`e_fEspecieID`.`fTitle` AS `fEspecie`,`e_fCategoryID`.`fTitle` AS `fCategory`,`e_fBrandMateriaID`.`fTitle` AS `fBrandMateria`,`e_fColorID`.`fTitle` AS `fColor`,`e_fAvistaID`.`fTitle` AS `fAvista`,`e_fTamanhoID`.`fTitle` AS `fTamanho`,`e_fVendedorID`.`fTitle` AS `fVendedor`,`e_fNrCopyID`.`fTitle` AS `fNrCopy` from (((((((((((((((`t_quotation` `o` left join `t_customer` `c` on((`o`.`fCustomerID` = `c`.`fCustomerID`))) left join `sysusers` `u_Submited` on((`o`.`fSubmitID` = `u_Submited`.`fUserID`))) left join `sysusers` `u_Entry` on((`o`.`fEntryID` = `u_Entry`.`fUserID`))) left join `sysusers` `u_Reviewer` on((`o`.`fReviewerID` = `u_Reviewer`.`fUserID`))) left join `sysusers` `u_Deliverer` on((`o`.`fDelivererID` = `u_Deliverer`.`fUserID`))) left join `sysusers` `u_Confirm` on((`o`.`fConfirmID` = `u_Confirm`.`fUserID`))) left join `sysusers` `u_Cancel` on((`o`.`fCancelID` = `u_Cancel`.`fUserID`))) left join `t_enumeration` `e_fEspecieID` on((`o`.`fEspecieID` = `e_fEspecieID`.`fItemID`))) left join `t_enumeration` `e_fCategoryID` on((`o`.`fCategoryID` = `e_fCategoryID`.`fItemID`))) left join `t_enumeration` `e_fBrandMateriaID` on((`o`.`fBrandMateriaID` = `e_fBrandMateriaID`.`fItemID`))) left join `t_enumeration` `e_fColorID` on((`o`.`fColorID` = `e_fColorID`.`fItemID`))) left join `t_enumeration` `e_fAvistaID` on((`o`.`fAvistaID` = `e_fAvistaID`.`fItemID`))) left join `t_enumeration` `e_fTamanhoID` on((`o`.`fTamanhoID` = `e_fTamanhoID`.`fItemID`))) left join `t_enumeration` `e_fVendedorID` on((`o`.`fVendedorID` = `e_fVendedorID`.`fItemID`))) left join `t_enumeration` `e_fNrCopyID` on((`o`.`fNrCopyID` = `e_fNrCopyID`.`fItemID`))) ;

-- 导出  视图 cedar.v_receivables 结构
-- 移除临时表并创建最终视图结构
DROP VIEW IF EXISTS `v_receivables`;
CREATE ALGORITHM=UNDEFINED  SQL SECURITY INVOKER VIEW `v_receivables` AS select `r`.`fID` AS `fID`,`r`.`fCustomerID` AS `fCustomerID`,`c`.`fCustomerName` AS `fCustomerName`,`r`.`fReceiptDate` AS `fReceiptDate`,`r`.`fAmountCollected` AS `fAmountCollected`,`r`.`fOrderID` AS `fOrderID`,`u`.`fUsername` AS `fPayee`,`skfs`.`fTitle` AS `fPaymentMethod`,`r`.`fNote` AS `fNote` from ((((`t_receivables` `r` left join `t_customer` `c` on((`r`.`fCustomerID` = `c`.`fCustomerID`))) left join `t_enumeration` `e` on((`r`.`fPaymentMethodID` = `e`.`fItemID`))) left join `sysusers` `u` on((`r`.`fPayeeID` = `u`.`fUserID`))) left join `t_enumeration` `skfs` on((`r`.`fPaymentMethodID` = `skfs`.`fItemID`))) ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
