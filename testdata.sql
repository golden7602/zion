-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.63-MariaDB - mariadb.org binary distribution
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 myorder_python 的数据库结构
DROP DATABASE IF EXISTS `myorder_python`;
CREATE DATABASE IF NOT EXISTS `myorder_python` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `myorder_python`;

-- 导出  表 myorder_python.syslanguage 结构
DROP TABLE IF EXISTS `syslanguage`;
CREATE TABLE IF NOT EXISTS `syslanguage` (
  `fID` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `fParentId` int(11) NOT NULL DEFAULT '0' COMMENT '上级编号',
  `fObjectName` varchar(60) DEFAULT NULL COMMENT '对象名',
  `fCaption` varchar(255) DEFAULT NULL COMMENT '标题',
  `fFontSize` tinyint(2) DEFAULT NULL COMMENT '字号',
  `fFontName` varchar(255) DEFAULT NULL COMMENT '字体',
  `fIndex` smallint(6) DEFAULT NULL COMMENT '顺序',
  `fLanguage1` varchar(255) DEFAULT NULL COMMENT '语言1',
  `fLanguage2` varchar(255) DEFAULT NULL COMMENT '语言2',
  `fType` tinyint(4) DEFAULT NULL COMMENT '类型',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=1006477 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.sysnavigationmenus 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.syssql 结构
DROP TABLE IF EXISTS `syssql`;
CREATE TABLE IF NOT EXISTS `syssql` (
  `ID` int(11) DEFAULT NULL,
  `UseFor` varchar(50) DEFAULT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `ObjectName` varchar(50) DEFAULT NULL,
  `ControlName` varchar(50) DEFAULT NULL,
  `MariaDB` text,
  `MariaDB_NoPara` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.systabelautokeyroles 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.sysuserright 结构
DROP TABLE IF EXISTS `sysuserright`;
CREATE TABLE IF NOT EXISTS `sysuserright` (
  `fID` smallint(6) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `fRightID` smallint(6) NOT NULL COMMENT '权限编号',
  `fUserID` smallint(6) NOT NULL COMMENT '用户编号',
  `fHasRight` bit(1) DEFAULT b'0' COMMENT '有权限',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`),
  UNIQUE KEY `UserID` (`fUserID`,`fRightID`)
) ENGINE=InnoDB AUTO_INCREMENT=2932 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.sysusers 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_customer 结构
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
  `fEndereco` varchar(15) DEFAULT NULL COMMENT '地址',
  `fEmail` varchar(50) DEFAULT NULL COMMENT '电子邮件',
  `fWeb` varchar(50) DEFAULT NULL COMMENT '主页',
  `fFax` varchar(15) DEFAULT NULL COMMENT '传真',
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fCustomerID`),
  UNIQUE KEY `OnlyOne` (`fCustomerName`)
) ENGINE=InnoDB AUTO_INCREMENT=178 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_enumeration 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_enumeration_type 结构
DROP TABLE IF EXISTS `t_enumeration_type`;
CREATE TABLE IF NOT EXISTS `t_enumeration_type` (
  `fTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `fTypeName` varchar(20) NOT NULL,
  `fNote` varchar(50) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fTypeID`),
  UNIQUE KEY `fTypeName` (`fTypeName`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_order 结构
DROP TABLE IF EXISTS `t_order`;
CREATE TABLE IF NOT EXISTS `t_order` (
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
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fDeliverViewed` bit(1) DEFAULT NULL COMMENT '已查阅',
  PRIMARY KEY (`fOrderID`),
  KEY `iDelivererID` (`fDelivererID`),
  KEY `iOrderDate` (`fOrderDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_order_detail 结构
DROP TABLE IF EXISTS `t_order_detail`;
CREATE TABLE IF NOT EXISTS `t_order_detail` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fOrderID` char(20) DEFAULT NULL,
  `fQuant` smallint(6) DEFAULT NULL,
  `fProductName` varchar(50) DEFAULT NULL,
  `fLength` smallint(6) DEFAULT NULL,
  `fWidth` smallint(6) DEFAULT NULL,
  `fPrice` decimal(11,2) DEFAULT NULL,
  `fAmount` decimal(11,2) NOT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=750 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_quotation 结构
DROP TABLE IF EXISTS `t_quotation`;
CREATE TABLE IF NOT EXISTS `t_quotation` (
  `fOrderID` char(20) NOT NULL COMMENT '订单号',
  `fPrice` decimal(10,0) DEFAULT NULL COMMENT '单价_印刷',
  `fCustomerID` int(11) DEFAULT NULL COMMENT '客户编号',
  `fOrderDate` date DEFAULT NULL COMMENT '订单日期',
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
  `fConfirmed` bit(1) NOT NULL DEFAULT b'0' COMMENT '已确认',
  `fConfirmID` int(11) DEFAULT NULL COMMENT '确认人',
  `fCanceled` bit(1) NOT NULL DEFAULT b'0' COMMENT '已作废',
  `fCancelID` int(11) DEFAULT NULL COMMENT '作废人',
  `fNumerBegin` int(11) DEFAULT NULL COMMENT '起始编号',
  `fQuant` int(11) DEFAULT NULL COMMENT '数量',
  `fPagePerVolumn` int(11) DEFAULT NULL COMMENT '每本号数',
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
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fOrderID`),
  KEY `iOrderDate` (`fOrderDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_quotation_detail 结构
DROP TABLE IF EXISTS `t_quotation_detail`;
CREATE TABLE IF NOT EXISTS `t_quotation_detail` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `fOrderID` varchar(50) DEFAULT NULL,
  `fQuant` smallint(6) DEFAULT NULL,
  `fProductName` varchar(50) DEFAULT NULL,
  `fLength` decimal(11,2) DEFAULT NULL,
  `fWidth` decimal(11,2) DEFAULT NULL,
  `fPrice` decimal(11,2) DEFAULT NULL,
  `fAmount` decimal(11,2) DEFAULT NULL,
  `TS` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_receivables 结构
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
  PRIMARY KEY (`fID`)
) ENGINE=InnoDB AUTO_INCREMENT=426 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  视图 myorder_python.v_enumeration 结构
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

-- 导出  视图 myorder_python.v_order 结构
DROP VIEW IF EXISTS `v_order`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_order` (
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
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fNUIT` VARCHAR(25) NULL COMMENT '税号' COLLATE 'utf8_general_ci',
	`fCity` VARCHAR(30) NULL COMMENT '所在地 Mordo' COLLATE 'utf8_general_ci',
	`fEndereco` VARCHAR(15) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fSucursal1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
	`fSubmited1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fConfirmed1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fDelivered1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fCanceled1` VARCHAR(8) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fDeliverViewed1` VARCHAR(3) NULL COLLATE 'utf8mb4_general_ci',
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

-- 导出  视图 myorder_python.v_order_readonly 结构
DROP VIEW IF EXISTS `v_order_readonly`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_order_readonly` (
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
	`fPagePerVolumn` TINYINT(4) NULL COMMENT '每本号数',
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
	`fEndereco` VARCHAR(15) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fEmail` VARCHAR(50) NULL COMMENT '电子邮件' COLLATE 'utf8_general_ci',
	`fWeb` VARCHAR(50) NULL COMMENT '主页' COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 myorder_python.v_quotation 结构
DROP VIEW IF EXISTS `v_quotation`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_quotation` (
	`fOrderID` CHAR(20) NOT NULL COMMENT '订单号' COLLATE 'utf8_general_ci',
	`fPrice` DECIMAL(10,0) NULL COMMENT '单价_印刷',
	`fCustomerID` INT(11) NULL COMMENT '客户编号',
	`fOrderDate` DATE NULL COMMENT '订单日期',
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
	`fConfirmed` BIT(1) NOT NULL COMMENT '已确认',
	`fConfirmID` INT(11) NULL COMMENT '确认人',
	`fCanceled` BIT(1) NOT NULL COMMENT '已作废',
	`fCancelID` INT(11) NULL COMMENT '作废人',
	`fNumerBegin` INT(11) NULL COMMENT '起始编号',
	`fQuant` INT(11) NULL COMMENT '数量',
	`fPagePerVolumn` INT(11) NULL COMMENT '每本号数',
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
	`TS` TIMESTAMP NOT NULL,
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fNUIT` VARCHAR(25) NULL COMMENT '税号' COLLATE 'utf8_general_ci',
	`fCity` VARCHAR(30) NULL COMMENT '所在地 Mordo' COLLATE 'utf8_general_ci',
	`fEndereco` VARCHAR(15) NULL COMMENT '地址' COLLATE 'utf8_general_ci',
	`fConfirmed1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fCanceled1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci',
	`fEntry_Name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
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

-- 导出  视图 myorder_python.v_receivables 结构
DROP VIEW IF EXISTS `v_receivables`;
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_receivables` (
	`fID` INT(11) NOT NULL,
	`fCustomerID` INT(11) NOT NULL,
	`fCustomerName` VARCHAR(50) NULL COMMENT '客户名' COLLATE 'utf8_general_ci',
	`fReceiptDate` DATE NOT NULL COMMENT '收款日期',
	`fAmountCollected` DECIMAL(11,2) NOT NULL COMMENT '金额',
	`fPayee` VARCHAR(20) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  视图 myorder_python.v_enumeration 结构
DROP VIEW IF EXISTS `v_enumeration`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_enumeration`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_enumeration` AS select t.fTypeID,t.fTypeName,e.fItemID,e.fTitle,e.fSpare1,e.fSpare2,e.fNote from t_enumeration_type as t left join t_enumeration as e on t.fTypeID=e.fTypeID ;

-- 导出  视图 myorder_python.v_order 结构
DROP VIEW IF EXISTS `v_order`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_order`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_order` AS select o.fOrderID,
o.fPrice,
o.fCustomerID,
o.fOrderDate,
o.fEspecieID,
o.fRequiredDeliveryDate,
o.fCategoryID,
o.fBrandMateriaID,
o.fAmount,
o.fTax,
o.fPayable,
o.fDesconto,
o.fColorID,
o.fEntryID,
o.fSubmited+0 as fSubmited,
o.fSubmitID,
o.fReviewed+0 as fReviewed,
o.fReviewerID,
o.fConfirmed+0 as fConfirmed,
o.fConfirmID,
o.fDelivered+0 as fDelivered,
o.fDelivererID,
o.fCanceled+0 as fCanceled,
o.fDeliverViewed+0 as fDeliverViewed,
o.fCancelID,
o.fDeliveryDate,
o.fNumerBegin,
o.fQuant,
o.fPagePerVolumn,
o.fNumerEnd,
o.fAvistaID,
o.fTamanhoID,
o.fSucursal+0 as fSucursal,
o.fLogo+0 as fLogo,
o.fVendedorID,
o.fNrCopyID,
o.fContato,
o.fCelular,
o.fTelefone,
o.fNote,
c.fCustomerName,c.fNUIT,c.fCity,c.fEndereco,
case o.fSucursal when 1 then 'SIM' else 'Non' end as fSucursal1,
case o.fSubmited when 1 then 'SIM' else '' end as fSubmited1,
case o.fConfirmed when 1 then 'SIM' else '' end as fConfirmed1,
case o.fDelivered when 1 then 'SIM' else '' end as fDelivered1,
case o.fCanceled when 1 then 'Canceled' else '' end as fCanceled1,
case o.fDeliverViewed when 1 then 'SIM' else '' end as fDeliverViewed1,
u_Submited.fUsername as fSubmit_Name,
u_Entry.fUsername as fEntry_Name,
u_Reviewer.fUsername as fReviewer_Name,
u_Deliverer.fUsername as fDeliverer_Name,
u_Confirm.fUsername as fConfirm_Name,
u_Cancel.fUsername as fCancel_Name,
e_fEspecieID.fTitle as fEspecie,
e_fCategoryID.fTitle as fCategory,
e_fBrandMateriaID.fTitle as fBrandMateria,
e_fColorID.fTitle as fColor,
e_fAvistaID.fTitle as fAvista,
e_fTamanhoID.fTitle as fTamanho,
e_fVendedorID.fTitle as fVendedor,
e_fNrCopyID.fTitle as fNrCopy
from t_order as o 
left join t_customer as c on o.fCustomerID=c.fCustomerID 
left join sysusers as u_Submited on o.fSubmitID=u_Submited.fUserID
left join sysusers as u_Entry on o.fEntryID=u_Entry.fUserID
left join sysusers as u_Reviewer on o.fReviewerID= u_Reviewer.fUserID
left join sysusers as u_Deliverer on o.fDelivererID= u_Deliverer.fUserID
left join sysusers as u_Confirm on o.fConfirmID=u_Confirm.fUserID 
left join sysusers as u_Cancel on o.fCancelID=u_Cancel.fUserID
left join t_enumeration as e_fEspecieID on o.fEspecieID=e_fEspecieID.fItemID
left join t_enumeration as e_fCategoryID on o.fCategoryID=e_fCategoryID.fItemID
left join t_enumeration as e_fBrandMateriaID on o.fBrandMateriaID=e_fBrandMateriaID.fItemID
left join t_enumeration as e_fColorID on o.fColorID=e_fColorID.fItemID
left join t_enumeration as e_fAvistaID on o.fAvistaID=e_fAvistaID.fItemID
left join t_enumeration as e_fTamanhoID on o.fTamanhoID=e_fTamanhoID.fItemID
left join t_enumeration as e_fVendedorID on o.fVendedorID=e_fVendedorID.fItemID
left join t_enumeration as e_fNrCopyID on o.fNrCopyID=e_fNrCopyID.fItemID ;

-- 导出  视图 myorder_python.v_order_readonly 结构
DROP VIEW IF EXISTS `v_order_readonly`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_order_readonly`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_order_readonly` AS SELECT fOrderID, fPrice, t.fCustomerID, fOrderDate, fEspecieID
	, fRequiredDeliveryDate, fCategoryID, fBrandMateriaID, fAmount, fTax
	, fPayable, fDesconto, fColorID, fEntryID, fSubmited
	, fSubmitID, fReviewed, fReviewerID, fConfirmed, fConfirmID
	, fDelivered, fDelivererID, fCanceled, fCancelID, fDeliveryDate
	, fNumerBegin, fQuant, fPagePerVolumn, fNumerEnd, fAvistaID
	, fTamanhoID, fSucursal, fLogo, fVendedorID, fNrCopyID
	, t.fContato, t.fCelular, t.fTelefone, fNote, c.fCustomerName
	, c.fNUIT, c.fCity, c.fAreaCode, c.fEndereco, c.fEmail
	, c.fWeb
FROM t_order t
	LEFT JOIN t_customer c ON t.fCustomerID = c.fCustomerID ;

-- 导出  视图 myorder_python.v_quotation 结构
DROP VIEW IF EXISTS `v_quotation`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_quotation`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_quotation` AS select o.*,c.fCustomerName,c.fNUIT,c.fCity,c.fEndereco,
case o.fConfirmed when 1 then 'SIM' else '' end as fConfirmed1,
case o.fCanceled when 1 then 'SIM' else '' end as fCanceled1,
u_Entry.fUsername as fEntry_Name,
u_Confirm.fUsername as fConfirm_Name,
u_Cancel.fUsername as fCancel_Name,
e_fEspecieID.fTitle as fEspecie,
e_fCategoryID.fTitle as fCategory,
e_fBrandMateriaID.fTitle as fBrandMateria,
e_fColorID.fTitle as fColor,
e_fAvistaID.fTitle as fAvista,
e_fTamanhoID.fTitle as fTamanho,
e_fVendedorID.fTitle as fVendedor,
e_fNrCopyID.fTitle as fNrCopy
from t_quotation as o 
left join t_customer as c on o.fCustomerID=c.fCustomerID 
left join sysusers as u_Entry on o.fEntryID=u_Entry.fUserID
left join sysusers as u_Confirm on o.fConfirmID=u_Confirm.fUserID 
left join sysusers as u_Cancel on o.fCancelID=u_Cancel.fUserID
left join t_enumeration as e_fEspecieID on o.fEspecieID=e_fEspecieID.fItemID
left join t_enumeration as e_fCategoryID on o.fCategoryID=e_fCategoryID.fItemID
left join t_enumeration as e_fBrandMateriaID on o.fBrandMateriaID=e_fBrandMateriaID.fItemID
left join t_enumeration as e_fColorID on o.fColorID=e_fColorID.fItemID
left join t_enumeration as e_fAvistaID on o.fAvistaID=e_fAvistaID.fItemID
left join t_enumeration as e_fTamanhoID on o.fTamanhoID=e_fTamanhoID.fItemID
left join t_enumeration as e_fVendedorID on o.fVendedorID=e_fVendedorID.fItemID
left join t_enumeration as e_fNrCopyID on o.fNrCopyID=e_fNrCopyID.fItemID ;

-- 导出  视图 myorder_python.v_receivables 结构
DROP VIEW IF EXISTS `v_receivables`;
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_receivables`;
CREATE ALGORITHM=TEMPTABLE DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_receivables` AS select r.fID,r.fCustomerID,c.fCustomerName ,fReceiptDate,fAmountCollected,u.fUsername as fPayee from  t_receivables as r
left join t_customer as c on r.fCustomerID=c.fCustomerID 
left join v_enumeration as e on r.fPaymentMethodID=e.fItemID
left join sysusers as u on r.fPayeeID=u.fUserID ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
