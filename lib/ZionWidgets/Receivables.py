from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormReceivables import Ui_Form
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from lib.JPFunction import JPDateConver, findButtonAndSetIcon


class Form_Receivables(Ui_Form):
    def __init__(self, mainform):
        super().__init__()
        self.Widget = QWidget()
        self.setupUi(self.Widget)
        findButtonAndSetIcon(self.Widget)
        self.SelectDate.setDate(QDate.currentDate())
        #QMetaObject.connectSlotsByName(self.Widget)
        mainform.addForm(self.Widget)
        self.SQLCustomerArrearsList = """
            select c.fCustomerID,
                c.fCustomerName as `客户名Cliente`,
                c.fCity,
            if(	YS.fYS=0,null,YS.fYS) as `应收合计TotalReceivables`,
                if(SK.fSK=0,null,SK.fSK) as `收款累计SumRec`,
                if(if(isnull(YS.fYS),0,YS.fYS)-if(isnull(SK.fSK),0,SK.fSK)=0,null,if(isnull(YS.fYS),0,YS.fYS)-if(isnull(SK.fSK),0,SK.fSK)) as `欠款Arrears`,
                r1.fReceiptDate as `最后收款日LastfReceiptDate`,
                cast(r1.fAmountCollected as DECIMAL) as `最后收款额LastAmountCollected`
            from t_customer as c left join 
                (select o.fCustomerID,
                    cast(sum(o.fPayable) as DECIMAL) as fYS 
                    from t_order as o 
                    where o.fCanceled=0 and o.fSubmited=1 and o.fConfirmed=1 group by o.fCustomerID) as YS
            on c.fCustomerID=YS.fCustomerID left join 
                (select r.fCustomerID,
                    cast(sum(r.fAmountCollected) as DECIMAL) as fSK,
                    max(r.fID) as LastRecID 
                    from t_receivables as r 
                    group by r.fCustomerID ) as SK
                on c.fCustomerID=SK.fCustomerID
                left join t_receivables as r1 
                on r1.fID=SK.LastRecID
            where c.fCustomerID={CustomerID}
        """
        self.SQLCustomerRecorder = """
                select 
                Q.fDate as 日期OrderDate, 
                Q.fOrderID as 订单号码OrderID, 
                Q.fPayable as 应收金额Payable, 
                Q.fAmountCollected as 收款fAmountCollected 
                from 
                (
                    select 
                    o.fOrderDate as fDate, 
                    o.fOrderID, 
                    cast(o.fPayable as DECIMAL) as fPayable, 
                    null as fAmountCollected, 
                    o.ts 
                    from 
                    t_order as o 
                    where 
                    o.fCustomerID ={CustomerID} 
                    and o.fCanceled = 0 
                    and o.fSubmited = 1 
                    and o.fConfirmed = 1 
                    union all 
                    select 
                    r.fReceiptDate as fDate, 
                    Null as fOrderID, 
                    Null as fPayable, 
                    cast(r.fAmountCollected as DECIMAL) as fAmountCollected, 
                    r.ts 
                    from 
                    t_receivables as r 
                    where 
                    r.fCustomerID ={CustomerID} 
                    union all 
                    select 
                    null as fDate, 
                    'Sum' as fOrderID, 
                    cast(
                        sum(Q1.fPayable) as DECIMAL
                    ) as fPayable, 
                    cast(
                        sum(Q1.fAmountCollected) as DECIMAL
                    ) as fAmountCollected, 
                    null as ts 
                    from 
                    (
                        select 
                        o.fOrderDate as fDate, 
                        o.fOrderID, 
                        cast(o.fPayable as DECIMAL) as fPayable, 
                        null as fAmountCollected, 
                        o.ts 
                        from 
                        t_order as o 
                        where 
                        o.fCustomerID ={CustomerID} 
                        and o.fCanceled = 0 
                        and o.fSubmited = 1 
                        and o.fConfirmed = 1 
                        union all 
                        select 
                        r.fReceiptDate as fDate, 
                        Null as fOrderID, 
                        Null as fPayable, 
                        cast(r.fAmountCollected as DECIMAL), 
                        r.ts 
                        from 
                        t_receivables as r 
                        where 
                        r.fCustomerID ={CustomerID}
                    ) as Q1
                ) as Q 
                order by 
                Q.TS DESC
        """
        self.SQLCurrentDayRec = """
            select 
            fid as 流水号ID, 
            fCustomerID as 客户编号CustomerID, 
            fCustomerName as 客户名Cliente, 
            fReceiptDate as 收款日期ReceiptDate, 
            fAmountCollected as 收款额AmountCollected, 
            fPayee as 收款人fPayee 
            from  v_receivables as r 
            where 
            r.fReceiptDate = STR_TO_DATE('{dateString}', '%Y-%m-%d') 
            order by 
            fID DESC
        """

        self.QinfoCurrentDayRec = JPQueryFieldInfo(
            self.SQLCurrentDayRec.format(dateString='1900-01-01'))
        self.QinfoCustomerRecorder = JPQueryFieldInfo(
            self.SQLCustomerRecorder.format(CustomerID=-1))
        self.QinfoCustomerArrearsList = JPQueryFieldInfo(
            self.SQLCustomerArrearsList.format(CustomerID=-1))
        self.modCurrentDayRec = JPTableViewModelReadOnly(
            self.tabCurrentDayRec, self.QinfoCurrentDayRec)
        self.modCustomerRecorder = JPTableViewModelReadOnly(
            self.tabCustomerRecorder, self.QinfoCustomerRecorder)
        self.modCustomerArrearsList = JPTableViewModelReadOnly(
            self.tabCustomerArrearsList, self.QinfoCustomerArrearsList)
        self.tabCurrentDayRec.setModel(self.modCurrentDayRec)
        self.tabCustomerRecorder.setModel(self.modCustomerRecorder)
        self.tabCustomerArrearsList.setModel(self.modCustomerArrearsList)

        self.SelectDate.dateChanged.connect(self.mmm)

    @pyqtSlot()
    def on_SelectDate_dateChanged(self, *args):
        print(args)
