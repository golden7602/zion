ALTER TABLE `t_receivables`
	ADD COLUMN `fOrderID` CHAR(20) NULL COMMENT '对应单号' AFTER `TS`;
ALTER TABLE `t_order`
	CHANGE COLUMN `fPrice` `fPrice` DECIMAL(10,2) NULL DEFAULT NULL COMMENT '单价_印刷' AFTER `fOrderID`;



update t_receivables as r left join 
(select fPayable,fCustomerID,fOrderDate,fOrderID from t_order where fConfirmed) as Q
on r.fReceiptDate=Q.fOrderDate and r.fAmountCollected=Q.fPayable set r.fOrderID= Q.fOrderID;

ALTER VIEW `v_receivables` AS
SELECT `r`.`fID` AS `fID`, `r`.`fCustomerID` AS `fCustomerID`, `c`.`fCustomerName` AS `fCustomerName`, `r`.`fReceiptDate` AS `fReceiptDate`, `r`.`fAmountCollected` AS `fAmountCollected`,`r`.`fOrderID`
	, `u`.`fUsername` AS `fPayee`, `skfs`.`fTitle` AS `fPaymentMethod`, `r`.`fNote` AS `fNote`
FROM `t_receivables` `r`
	LEFT JOIN `t_customer` `c` ON `r`.`fCustomerID` = `c`.`fCustomerID`
	LEFT JOIN `t_enumeration` `e` ON `r`.`fPaymentMethodID` = `e`.`fItemID`
	LEFT JOIN `sysusers` `u` ON `r`.`fPayeeID` = `u`.`fUserID`
	LEFT JOIN `t_enumeration` `skfs` ON `r`.`fPaymentMethodID` = `skfs`.`fItemID`;

update t_receivables set fPaymentMethodID=59 where fPaymentMethodID=100;
update t_receivables set fPaymentMethodID=60 where fPaymentMethodID=101;
update t_receivables set fPaymentMethodID=62 where fPaymentMethodID=102;
update t_receivables set fPaymentMethodID=61 where fPaymentMethodID=103;
update t_receivables set fPaymentMethodID=99 where fPaymentMethodID=104;
update t_receivables set fPaymentMethodID=63 where fPaymentMethodID=109;
delete from t_enumeration where fItemID>=100 and fItemID<=109;

