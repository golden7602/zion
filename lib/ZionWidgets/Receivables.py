from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormReceivables import Ui_Form
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot, Qt, QModelIndex
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from lib.JPFunction import JPDateConver, findButtonAndSetIcon
from lib.JPMvc.JPEditFormModel import JPFormModelMain, JPEditFormDataMode
from Ui.Ui_FormReceivableEdit import Ui_Form as Edit_ui
from PyQt5.QtGui import QPixmap
from lib.ZionPublc import JPPub, JPUser
from lib.JPMvc import JPWidgets


class Form_Receivables(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        findButtonAndSetIcon(self)
        mainform.addForm(self)
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
        self.ui.SelectDate.dateChanged.connect(self.dateChanged)
        self.ui.SelectDate.setDate(QDate.currentDate())
        self.currentCustomerChanged()

    @pyqtSlot()
    def on_SelectDate_dateChanged(self, *args):
        return

    @pyqtSlot()
    def on_butRecibido_clicked(self):
        frm = RecibidoEdit()
        frm.ListForm = self
        frm.ui.fCustomerID.setEditable(True)
        frm.ui.fCity.setEnabled(False)
        frm.ui.fNUIT.setEnabled(False)
        frm.ui.fEndereco.setEnabled(False)
        frm.ui.fEndereco.setEnabled(False)
        frm.ui.fCelular.setEnabled(False)
        frm.ui.fContato.setEnabled(False)
        frm.ui.fTelefone.setEnabled(False)
        frm.ui.fAmountPayable.setEnabled(False)
        frm.ui.fAmountPaid.setEnabled(False)
        frm.ui.fArrears.setEnabled(False)
        frm.exec_()

    def dateChanged(self, s_date):
        str_date = JPDateConver(self.ui.SelectDate.date(), str)
        self.QinfoCurrentDayRec = JPQueryFieldInfo(
            self.SQLCurrentDayRec.format(dateString=str_date))
        self.modCurrentDayRec = JPTableViewModelReadOnly(
            self.ui.tabCurrentDayRec, self.QinfoCurrentDayRec)
        self.ui.tabCurrentDayRec.setModel(self.modCurrentDayRec)
        self.ui.tabCurrentDayRec.selectionModel(
        ).currentRowChanged[QModelIndex, QModelIndex].connect(
            self.currentCustomerChanged)
        self.currentCustomerChanged()

    def currentCustomerChanged(self):
        id = -1
        index = self.ui.tabCurrentDayRec.selectionModel().currentIndex()
        if index.isValid():
            id = self.modCurrentDayRec.TabelFieldInfo.getOnlyData(
                [index.row(), 1])
        self.QinfoCustomerRecorder = JPQueryFieldInfo(
            self.SQLCustomerRecorder.format(CustomerID=id))
        self.QinfoCustomerArrearsList = JPQueryFieldInfo(
            self.SQLCustomerArrearsList.format(CustomerID=id))
        self.modCustomerRecorder = JPTableViewModelReadOnly(
            self.ui.tabCustomerRecorder, self.QinfoCustomerRecorder)
        self.modCustomerArrearsList = JPTableViewModelReadOnly(
            self.ui.tabCustomerArrearsList, self.QinfoCustomerArrearsList)
        self.ui.tabCurrentDayRec.setModel(self.modCurrentDayRec)
        self.ui.tabCurrentDayRec.resizeColumnsToContents()
        self.ui.tabCustomerRecorder.setModel(self.modCustomerRecorder)
        self.ui.tabCustomerRecorder.resizeColumnsToContents()
        self.ui.tabCustomerArrearsList.setModel(self.modCustomerArrearsList)
        self.ui.tabCustomerArrearsList.resizeColumnsToContents()


class RecibidoEdit(JPFormModelMain):
    def __init__(self):
        m_sql = '''select fID,fCustomerID,fPaymentMethodID,
                fReceiptDate,fAmountCollected,fPayeeID,fNote 
                from t_receivables
                where fID='{}'
                '''
        super().__init__(Edit_ui(),
                         sql_main=m_sql,
                         PKValue=None,
                         edit_mode=JPEditFormDataMode.New,
                         flags=Qt.WindowFlags())
        pix = QPixmap(getcwd() + "\\res\\Zions_100.png")
        self.ui.label_logo.setPixmap(pix)
        self.ui.fID.hide()
        self.readData()

    def onGetFieldsRowSources(self):
        pub = JPPub()
        u_lst = [[item[1], item[0]] for item in JPUser().getAllUserList()]
        return [('fCustomerID', pub.getCustomerList(), 1),
                ('fPaymentMethodID', pub.getEnumList(3), 1),
                ('fPayeeID', u_lst, 1)]

    def onGetPrintReport(self):
        return  #PrintOrder_report_Mob()

    # def onGetReadOnlyFields(self):
    #     return [
    #         'fAmountPayable', 'fAmountPaid', 'fArrears', 'fSucursal',
    #         'fTelefone', 'fCelular', "fEntryID", "fEndereco", 'fCity', 'fNUIT'
    #     ]
    def onGetDisableFields(self):
        return [
            'fNUIT', 'fCity', 'fEndereco', 'fCelular', 'fContato', 'fTelefone',
            'fAmountPayable', 'fAmountPaid', 'fArrears'
        ]

    def onDateChangeEvent(self, obj, value):
        nm = obj.objectName()
        if nm == 'fCustomerID':
            self.__customerIDChanged()

    def __customerIDChanged(self):
        sql = '''
            SELECT fNUIT, fCity, fEndereco, fCelular, fContato
                , fTelefone, Q0.fAmountPayable  , Q1.fAmountPaid,
                Q0.fAmountPayable-Q1.fAmountPaid as fArrears,-1 as fPaymentMethodID
            FROM t_customer c
                LEFT JOIN (
                    SELECT fCustomerID, SUM(fPayable) AS fAmountPayable
                    FROM t_order
                    WHERE fCustomerID = {CustomerID}
                        AND fConfirmed = 1
                ) Q0
                ON c.fCustomerID = Q0.fCustomerID
                LEFT JOIN (
                    SELECT fCustomerID, SUM(fAmountCollected) AS fAmountPaid
                    FROM t_receivables
                    WHERE fCustomerID = {CustomerID}
                ) Q1
                ON c.fCustomerID = Q1.fCustomerID
            WHERE c.fCustomerID = {CustomerID}
        '''
        sql = sql.format(CustomerID=self.ui.fCustomerID.Value())
        tab = JPQueryFieldInfo(sql)
        obj_name = [
            'fNUIT', 'fCity', 'fEndereco', 'fCelular', 'fContato', 'fTelefone',
            'fAmountPayable', 'fAmountPaid', 'fArrears'
        ]
        tup = (JPWidgets.QLineEdit, JPWidgets.QDateEdit, JPWidgets.QComboBox,
               JPWidgets.QTextEdit, JPWidgets.QCheckBox)
        fld_dict = tab.getRowFieldsInfoDict(0)
        for i, nm in enumerate(obj_name):
            obj = self.findChild(tup, nm)
            if obj:
                obj.setRowsData(tab.DataRows[0])
                obj.setMainModel(self)
                obj.setFieldInfo(fld_dict[nm])
                obj.refreshValueNotRaiseEvent(tab.getOnlyData([0, i]), True)

    def onAfterSaveData(self, data):
        self.ui.butSave.setEnabled(False)
        self.ui.butPrint.setEnabled(False)
        self.ui.butPDF.setEnabled(False)
        self.ListForm.dateChanged()
