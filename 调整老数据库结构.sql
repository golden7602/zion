

ALTER TABLE `t_customer`
	CHANGE COLUMN `fEndereco` `fEndereco` VARCHAR(50) NULL DEFAULT NULL COMMENT '地址' AFTER `fTelefone`;

DROP View IF EXISTS `v_order`;
CREATE ALGORITHM=UNDEFINED DEFINER=`myorder`@`%` SQL SECURITY INVOKER VIEW `v_order` AS select `o`.`fOrderID` AS `fOrderID`,`o`.`fPrice` AS `fPrice`,`o`.`fCustomerID` AS `fCustomerID`,`o`.`fOrderDate` AS `fOrderDate`,`o`.`fEspecieID` AS `fEspecieID`,`o`.`fRequiredDeliveryDate` AS `fRequiredDeliveryDate`,`o`.`fCategoryID` AS `fCategoryID`,`o`.`fBrandMateriaID` AS `fBrandMateriaID`,`o`.`fAmount` AS `fAmount`,`o`.`fTax` AS `fTax`,`o`.`fPayable` AS `fPayable`,`o`.`fDesconto` AS `fDesconto`,`o`.`fColorID` AS `fColorID`,`o`.`fEntryID` AS `fEntryID`,(`o`.`fSubmited` + 0) AS `fSubmited`,`o`.`fSubmitID` AS `fSubmitID`,(`o`.`fReviewed` + 0) AS `fReviewed`,`o`.`fReviewerID` AS `fReviewerID`,(`o`.`fConfirmed` + 0) AS `fConfirmed`,`o`.`fConfirmID` AS `fConfirmID`,(`o`.`fDelivered` + 0) AS `fDelivered`,`o`.`fDelivererID` AS `fDelivererID`,(`o`.`fCanceled` + 0) AS `fCanceled`,(`o`.`fDeliverViewed` + 0) AS `fDeliverViewed`,`o`.`fCancelID` AS `fCancelID`,`o`.`fDeliveryDate` AS `fDeliveryDate`,`o`.`fNumerBegin` AS `fNumerBegin`,`o`.`fQuant` AS `fQuant`,`o`.`fPagePerVolumn` AS `fPagePerVolumn`,`o`.`fNumerEnd` AS `fNumerEnd`,`o`.`fAvistaID` AS `fAvistaID`,`o`.`fTamanhoID` AS `fTamanhoID`,(`o`.`fSucursal` + 0) AS `fSucursal`,(`o`.`fLogo` + 0) AS `fLogo`,`o`.`fVendedorID` AS `fVendedorID`,`o`.`fNrCopyID` AS `fNrCopyID`,`o`.`fContato` AS `fContato`,`o`.`fCelular` AS `fCelular`,`o`.`fTelefone` AS `fTelefone`,`o`.`fNote` AS `fNote`,`c`.`fTaxRegCer` AS `fTaxRegCer`,`c`.`fCustomerName` AS `fCustomerName`,`c`.`fNUIT` AS `fNUIT`,`c`.`fCity` AS `fCity`,`c`.`fEndereco` AS `fEndereco`,`c`.`fEmail` AS `fEmail`,(case `o`.`fSucursal` when 1 then 'SIM' else 'Non' end) AS `fSucursal1`,(case `o`.`fSubmited` when 1 then 'SIM' else '' end) AS `fSubmited1`,(case `o`.`fConfirmed` when 1 then 'SIM' else '' end) AS `fConfirmed1`,(case `o`.`fDelivered` when 1 then 'SIM' else '' end) AS `fDelivered1`,(case `o`.`fCanceled` when 1 then 'Canceled' else '' end) AS `fCanceled1`,(case `o`.`fDeliverViewed` when 1 then 'SIM' else '' end) AS `fDeliverViewed1`,(case `o`.`fLogo` when 1 then 'SIM' else 'Non' end) AS `fLogo1`,`u_submited`.`fUsername` AS `fSubmit_Name`,`u_entry`.`fUsername` AS `fEntry_Name`,`u_reviewer`.`fUsername` AS `fReviewer_Name`,`u_deliverer`.`fUsername` AS `fDeliverer_Name`,`u_confirm`.`fUsername` AS `fConfirm_Name`,`u_cancel`.`fUsername` AS `fCancel_Name`,`e_fespecieid`.`fTitle` AS `fEspecie`,`e_fcategoryid`.`fTitle` AS `fCategory`,`e_fbrandmateriaid`.`fTitle` AS `fBrandMateria`,`e_fcolorid`.`fTitle` AS `fColor`,`e_favistaid`.`fTitle` AS `fAvista`,`e_ftamanhoid`.`fTitle` AS `fTamanho`,`e_fvendedorid`.`fTitle` AS `fVendedor`,`e_fnrcopyid`.`fTitle` AS `fNrCopy` from (((((((((((((((`t_order` `o` left join `t_customer` `c` on((`o`.`fCustomerID` = `c`.`fCustomerID`))) left join `sysusers` `u_submited` on((`o`.`fSubmitID` = `u_submited`.`fUserID`))) left join `sysusers` `u_entry` on((`o`.`fEntryID` = `u_entry`.`fUserID`))) left join `sysusers` `u_reviewer` on((`o`.`fReviewerID` = `u_reviewer`.`fUserID`))) left join `sysusers` `u_deliverer` on((`o`.`fDelivererID` = `u_deliverer`.`fUserID`))) left join `sysusers` `u_confirm` on((`o`.`fConfirmID` = `u_confirm`.`fUserID`))) left join `sysusers` `u_cancel` on((`o`.`fCancelID` = `u_cancel`.`fUserID`))) left join `t_enumeration` `e_fespecieid` on((`o`.`fEspecieID` = `e_fespecieid`.`fItemID`))) left join `t_enumeration` `e_fcategoryid` on((`o`.`fCategoryID` = `e_fcategoryid`.`fItemID`))) left join `t_enumeration` `e_fbrandmateriaid` on((`o`.`fBrandMateriaID` = `e_fbrandmateriaid`.`fItemID`))) left join `t_enumeration` `e_fcolorid` on((`o`.`fColorID` = `e_fcolorid`.`fItemID`))) left join `t_enumeration` `e_favistaid` on((`o`.`fAvistaID` = `e_favistaid`.`fItemID`))) left join `t_enumeration` `e_ftamanhoid` on((`o`.`fTamanhoID` = `e_ftamanhoid`.`fItemID`))) left join `t_enumeration` `e_fvendedorid` on((`o`.`fVendedorID` = `e_fvendedorid`.`fItemID`))) left join `t_enumeration` `e_fnrcopyid` on((`o`.`fNrCopyID` = `e_fnrcopyid`.`fItemID`)))


-- 导出  表 myorder_python.t_product_information 结构
DROP TABLE IF EXISTS `t_product_information`;
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
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_product_outbound_order 结构
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

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_product_outbound_order_detail 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_product_warehousereceipt_order 结构
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

-- 数据导出被取消选择。
-- 导出  表 myorder_python.t_product_warehousereceipt_order_detail 结构
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  视图 myorder_python.v_product_outbound_order 结构
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

-- 导出  视图 myorder_python.v_product_warehousereceipt_order 结构
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

-- 导出  视图 myorder_python.v_product_outbound_order 结构
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

-- 导出  视图 myorder_python.v_product_warehousereceipt_order 结构
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
LEFT JOIN `t_supplier` `c`
    ON `o`.`fSupplierID` = `c`.`fSupplierID`
LEFT JOIN `sysusers` `u_Submited`
    ON `o`.`fSubmitID` = `u_Submited`.`fUserID`
LEFT JOIN `sysusers` `u_Entry`
    ON `o`.`fEntryID` = `u_Entry`.`fUserID`

LEFT JOIN `sysusers` `u_Cancel`
    ON `o`.`fCancelID` = `u_Cancel`.`fUserID`
LEFT JOIN `t_enumeration` `e_fPurchaserID`
    ON `o`.`fPurchaserID` = `e_fPurchaserID`.`fItemID` ;

