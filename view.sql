
CREATE  VIEW `v_order` AS select o.fOrderID,
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


CREATE  VIEW `v_order_readonly` AS SELECT fOrderID, fPrice, t.fCustomerID, fOrderDate, fEspecieID
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


CREATE  VIEW `v_quotation` AS select o.*,c.fCustomerName,c.fNUIT,c.fCity,c.fEndereco,
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


CREATE  VIEW `v_receivables` AS select r.fID,r.fCustomerID,c.fCustomerName ,fReceiptDate,fAmountCollected,u.fUsername as fPayee from  t_receivables as r
left join t_customer as c on r.fCustomerID=c.fCustomerID 
left join v_enumeration as e on r.fPaymentMethodID=e.fItemID
left join sysusers as u on r.fPayeeID=u.fUserID ;

