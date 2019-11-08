
/*!40000 ALTER TABLE `sysnavigationmenus` DISABLE KEYS */;
INSERT INTO `sysnavigationmenus` (`fNMID`, `fDispIndex`, `fParentId`, `fEnabled`, `fMenuText`, `fCommand`, `fObjectName`, `fFormMode`, `fArg`, `fIcon`, `fDefault`, `fNodeBackvolor`, `fNodeForeColor`, `fNodeFontBold`, `fExpanded`, `fDescription`, `fLevel`, `fIsCommandButton`, `TS`) VALUES
	(186, 421, 21, b'1', 'ProductInOutDetails', 0, NULL, NULL, NULL, 'reports.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'0', '2019-11-01 09:18:40'),
	(187, 18602, 186, b'1', 'Print', 0, 'CmdPrint', NULL, NULL, 'print.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-11-01 11:34:34'),
	(188, 18703, 186, b'1', 'ExportToExcel', 0, 'CmdExportToExcel', NULL, NULL, 'ExportToExcel.png', b'0', NULL, NULL, 0, 1, NULL, b'0', b'1', '2019-11-01 11:34:38');
/*!40000 ALTER TABLE `sysnavigationmenus` ENABLE KEYS */;
CREATE SQL SECURITY INVOKER VIEW `v_all_sales` AS select fOrderID,fOrderDate,fCustomerID,fPrice,fQuant,fAmount,fTax,fDesconto,fPayable,TS from t_order where fSubmited=1 and fConfirmed=1 and fCanceled=0
