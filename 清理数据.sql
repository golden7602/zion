delete from sysuserright where 1=1;
ALTER TABLE sysuserright	AUTO_INCREMENT=1;


delete from sysusers where fUserID>1;
ALTER TABLE sysusers	AUTO_INCREMENT=20;


delete from t_customer where 1=1;
ALTER TABLE t_customer	AUTO_INCREMENT=1;

delete from t_enumeration where fItemID>96;
ALTER TABLE t_enumeration	AUTO_INCREMENT=97;

delete from t_order where 1=1;
delete from t_order_detail where 1=1;
ALTER TABLE t_order_detail	AUTO_INCREMENT=1;


delete from t_quotation where 1=1;
delete from t_quotation_detail where 1=1;
ALTER TABLE t_quotation_detail AUTO_INCREMENT=1;

delete from t_receivables where 1=1;
ALTER TABLE t_receivables	AUTO_INCREMENT=1;

update systabelautokeyroles set fCurrentValue=0 where 1=1;
