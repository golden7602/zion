from functools import reduce
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import pyqtSlot, Qt, QRect
from PyQt5.QtGui import QIcon, QIntValidator, QPixmap, QKeyEvent, QColor
from PyQt5.QtWidgets import QAction, QLineEdit, QMessageBox

from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPEditFormModel import JPFormModelMain
from lib.JPMvc.JPFuncForm import JPFunctionForm, JPEditFormDataMode
from lib.JPPrintReport import JPPrintSectionType
from lib.ZionPublc import JPPub, JPUser
from lib.ZionReport.PrintingOrderReportMob import PrintOrder_report_Mob
from Ui.Ui_FormPrintingOrder import Ui_Form
from lib.JPFunction import JPRound
from lib.JPMvc.JPModel import JPTableViewModelReadOnly


class JPFuncForm_PrintingOrder(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_0 = """
                SELECT   fOrderID as `订单号码OrderID`, 
                    fCustomerName as `客户名Cliente`, 
                    fOrderDate as `日期OrderDate`, 
                    fRequiredDeliveryDate as `fRequiredDeliveryDate`, 
                    fSubmited1 as `提交Submited`, 
                    fSubmit_Name as `fSubmit_Name`, 
                    fEspecie as `类别Especie`, 
                    fAmount as `金额SubTotal`, 
                    fTax as `税金IVA`, 
                    fPayable as `应付金额Valor a Pagar`, 
                    fDesconto as `折扣Desconto`, 
                    fNumerBegin as `起始号码fNumerBegin`, 
                    fNumerEnd as `结束号码fNumerEnd`, 
                    fQuant as `数量fQuant`, 
                    fPagePerVolumn as `每本页数 Page/Vol`, 
                    fAvista as `每页序号Avista`, 
                    fTamanho as `尺寸Tamanho`, 
                    fVendedor as `联系人fVendedor`, 
                    fNrCopy as `联数Nr.Copy`, 
                    fContato as `联系人Contato`, 
                    fCelular as `手机Celular`, 
                    fTelefone as `fTelefone`, 
                    fEntry_Name as `录入Entry`, 
                    fCustomerID as `客户编号CustomerID`,  
                    cast(fSubmited as SIGNED) AS `fSubmited`
                FROM v_order AS o"""
        sql_1 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='TP'
                        AND (fSubmited={ch1}
                        OR fSubmited={ch2})
                        AND fOrderDate{date}
                ORDER BY  fOrderID DESC"""
        sql_2 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='TP'
                ORDER BY  fOrderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('UnSubmited')
        self.checkBox_2.setText('Submited')
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(True)
        super().setListFormSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(23, True)
        self.tableView.setColumnHidden(24, True)
        self.fSubmited_column = 13
        m_sql = """
                SELECT fOrderID, fCelular, fRequiredDeliveryDate, fContato
                    , fTelefone, fVendedorID, fCustomerID, fOrderDate
                    , fSucursal, fQuant, fNumerBegin, fNumerEnd
                    , fPrice, fLogo, fEspecieID, fAvistaID, fTamanhoID
                    , fNrCopyID, fPagePerVolumn, fNote, fAmount, fDesconto
                    , fTax, fPayable,fEntryID
                FROM t_order
                WHERE fOrderID = '{}'
                """
        self.setEditFormSQL(m_sql, None)

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        return EditForm_PrintingOrder(sql_main=sql_main,
                                      edit_mode=edit_mode,
                                      sql_sub=sql_sub,
                                      PKValue=PKValue)

    @pyqtSlot()
    def on_CmdSubmit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        db = JPDb()
        info = self.model.TabelFieldInfo
        submitted = info.getOnlyData([
            self.tableView.selectionModel().currentIndex().row(),
            self.fSubmited_column
        ])
        if submitted == 1:
            msg = '记录【{cu_id}】已经提交，不能重复提交!\nThe order [{cu_id}] '
            msg = msg + 'has been submitted, can not be repeated submission!'
            msg = msg.replace("{cu_id}", str(cu_id))
            QMessageBox.warning(self, '提示', msg, QMessageBox.Ok,
                                QMessageBox.Ok)
            return
        msg = '提交后订单将不能修改！确定继续提交记录【{cu_id}】吗？\n'
        msg = msg + 'The order "{cu_id}" will not be modified after submission. '
        msg = msg + 'Click OK to continue submitting?'
        msg = msg.replace("{cu_id}", str(cu_id))
        if QMessageBox.question(self, '确认', msg, QMessageBox.Ok,
                                QMessageBox.Ok) == QMessageBox.Ok:
            sql = "update {tn} set fSubmited=1 where {pk_n}='{pk_v}';"
            sql1 = "select '{pk_v}';"
            sql = sql.format(tn=self.EditFormMainTableName,
                             pk_n=self.EditFormPrimarykeyFieldName,
                             pk_v=cu_id)
            if db.executeTransaction([sql, sql1.format(pk_v=cu_id)]):
                self.btnRefreshClick()


class myHistoryView(JPTableViewModelReadOnly):
    def __init__(self, tableView, tabelFieldInfo):
        super().__init__(tableView, tabelFieldInfo)

    def data(self, Index, role):

        if role == Qt.BackgroundColorRole:
            if Index.row() == 0 and Index.column() == 4:
                return QColor(Qt.blue)
            else:
                return super().data(Index, role)
        if role == Qt.TextColorRole:
            if Index.row() == 0 and Index.column() == 4:
                return QColor(Qt.white)
            else:
                return super().data(Index, role)
        return super().data(Index, role)


class EditForm_PrintingOrder(JPFormModelMain):
    def __init__(self, sql_main, sql_sub=None, edit_mode=None, PKValue=None):
        super().__init__(Ui_Form(),
                         sql_main,
                         PKValue=PKValue,
                         edit_mode=edit_mode)
        pix = QPixmap(getcwd() + "\\res\\Zions_100.png")
        self.ui.label_logo.setPixmap(pix)
        self.setPkRole(5)
        self.cacuTax = True
        self.__historyOrderSQL = '''
                SELECT fOrderID AS 单据号码OrderID,
                    fOrderDate as 单据日期OrderDate,
                    CAST(e.fTitle AS char(20)) AS 类别Especie,
                    CAST(fNumerBegin AS SIGNED) AS 起始号码NumerBegin,
                    CAST(fNumerEnd AS SIGNED) AS 结束号码NumerEnd
                FROM t_order o
                    LEFT JOIN t_enumeration e ON o.fEspecieID = e.fItemID
            '''
        self.ui.fTax.keyPressEvent = self.__onTaxKeyPress
        self.readData()
        if self.isNewMode:
            self.ui.fEntryID.refreshValueNotRaiseEvent(
                JPUser().currentUserID())
        if self.EditMode != JPEditFormDataMode.New:
            self.__refreshBeginNum()

    def __onTaxKeyPress(self, KeyEvent: QKeyEvent):
        if (KeyEvent.modifiers() == Qt.AltModifier
                and KeyEvent.key() == Qt.Key_Delete):
            self.ui.fTax.refreshValueRaiseEvent(None, True)
            self.cacuTax = False
        elif (KeyEvent.modifiers() == Qt.AltModifier
              and KeyEvent.key() == Qt.Key_T):
            self.cacuTax = True

    def onGetFieldsRowSources(self):
        pub = JPPub()
        u_lst = [[item[1], item[0]] for item in JPUser().getAllUserList()]
        return [('fCustomerID', pub.getCustomerList(), 1),
                ('fVendedorID', pub.getEnumList(10), 1),
                ('fEspecieID', pub.getEnumList(2), 1),
                ('fAvistaID', pub.getEnumList(7), 1),
                ('fTamanhoID', pub.getEnumList(8), 1),
                ('fNrCopyID', pub.getEnumList(9), 1), ('fEntryID', u_lst, 1)]

    def onGetPrintReport(self):
        return PrintOrder_report_Mob()

    def onGetReadOnlyFields(self):
        return [
            'fOrderID', "fNumerEnd", "fEntryID", 'fAmount', 'fPayable', 'fNUIT'
        ]

    def afterSaveDate(self, data):
        self.ui.fOrderID.refreshValueNotRaiseEvent(data, True)

    def __customerIDChanged(self):
        sql = '''select fCelular, fContato, fTelefone 
            from t_customer where fCustomerID={}'''
        sql = sql.format(self.ui.fCustomerID.Value())
        tab = JPQueryFieldInfo(sql)
        self.ui.fCelular.refreshValueNotRaiseEvent(tab.getOnlyData([0, 0]),
                                                   True)
        self.ui.fContato.refreshValueNotRaiseEvent(tab.getOnlyData([0, 1]),
                                                   True)
        self.ui.fTelefone.refreshValueNotRaiseEvent(tab.getOnlyData([0, 2]),
                                                    True)

    def onDateChangeEvent(self, obj, value):
        nm = obj.objectName()
        if nm in ('fCustomerID', 'fEspecieID'):
            if nm == 'fCustomerID':
                if self.ui.fCustomerID.currentIndex() != -1:
                    self.__customerIDChanged()
            self.__refreshBeginNum()
        if nm in ('fAvistaID', 'fQuant', 'fPagePerVolumn'):
            self.__refreshEndNum()
        if nm == 'fNumerBegin':
            v = obj.Value()
            self.ui.fNumerEnd.setIntValidator(v + 1, v + 1000000)
            self.__refreshEndNum()
        if nm in ('fQuant', 'fPrice', 'fDesconto', "fTax"):
            fQuant = self.ui.fQuant.Value()
            fPrice = self.ui.fPrice.Value()
            temp_fDesconto = self.ui.fDesconto.Value()
            fDesconto = temp_fDesconto if temp_fDesconto else 0
            fAmount = (fQuant * fPrice if all((fQuant, fPrice)) else None)
            self.ui.fAmount.refreshValueNotRaiseEvent(fAmount, True)
            if fAmount is None:
                self.ui.fTax.refreshValueNotRaiseEvent(None, True)
                self.ui.fPayable.refreshValueNotRaiseEvent(None, True)
                return
            if nm == "fTax":
                temp_fTax = self.ui.fTax.Value()
                fTax = temp_fTax if temp_fTax else 0
            else:
                fTax = JPRound((fAmount - fDesconto) * 0.17) if fAmount else 0
            if self.cacuTax:
                self.ui.fTax.refreshValueNotRaiseEvent(fTax, True)
            else:
                fTax = 0
            fPayable = fAmount + fTax - fDesconto
            self.ui.fPayable.refreshValueNotRaiseEvent(fPayable, True)

    def __refreshEndNum(self):
        temp_fAvistaID = self.ui.fAvistaID.currentData()
        fNumerBegin = self.ui.fNumerBegin.Value()
        fAvistaID = int(temp_fAvistaID[2]) if temp_fAvistaID else None
        fQuant = self.ui.fQuant.Value()
        fPagePerVolumn = self.ui.fPagePerVolumn.Value()
        if all((fAvistaID, fQuant, fPagePerVolumn)):
            fNumerEnd = fNumerBegin + fAvistaID * fQuant * fPagePerVolumn - 1
        else:
            fNumerEnd = fNumerBegin
        self.ui.fNumerEnd.refreshValueNotRaiseEvent(fNumerEnd, True)

    def __refreshBeginNum(self):
        obj_begin = self.ui.fNumerBegin
        obj_end = self.ui.fNumerEnd

        def clearNum():
            obj_begin.refreshValueNotRaiseEvent(None, True)
            obj_end.refreshValueNotRaiseEvent(None, True)
            sql = self.__historyOrderSQL + JPDb().getOnlyStrcFilter()
            tab = JPQueryFieldInfo(sql)
            mod = myHistoryView(self.ui.listPrintingOrder, tab)
            self.ui.listPrintingOrder.setModel(mod)
            self.ui.listPrintingOrder.resizeColumnsToContents()

        # 如果没有选择客户或单据管理标志不为1时，清空单据信息并退出
        temp = (self.ui.fEspecieID.currentIndex() == -1
                or self.ui.fCustomerID.currentIndex() == -1)
        if temp:
            clearNum()
            return

        if self.ui.fEspecieID.currentData()[2] != '1':
            obj_begin.setEnabled(False)
            self.ui.listPrintingOrder.setEnabled(False)
            clearNum()
            return
        else:
            obj_begin.setEnabled(True)
            self.ui.listPrintingOrder.setEnabled(True)

        self.ui.fNumerBegin.setEnabled(True)
        new_beginNum = self.__getHistoryOrderMaxNum()
        obj_begin.refreshValueNotRaiseEvent(new_beginNum + 1, True)
        obj_begin.setIntValidator(new_beginNum + 1, 999999999999)
        # 引发一次事件
        obj_begin._onValueChange(new_beginNum)

    def __getHistoryOrderMaxNum(self):
        sql = self.__historyOrderSQL + '''
                WHERE fCustomerID ={fCustomerID}
                    AND fEspecieID = {fEspecieID}
                    AND fConfirmed='1'
                    {WhereID}
                ORDER BY fNumerEnd DESC
            '''
        ID = self.ui.fOrderID.Value()
        WhereID = "AND fOrderID<>'{}'".format(ID) if ID else ''
        tab = JPQueryFieldInfo(
            sql.format(fCustomerID=self.ui.fCustomerID.Value(),
                       fEspecieID=self.ui.fEspecieID.Value(),
                       WhereID=WhereID))
        mod = myHistoryView(self.ui.listPrintingOrder, tab)
        self.ui.listPrintingOrder.setModel(mod)
        self.ui.listPrintingOrder.resizeColumnsToContents()
        return tab.getOnlyData([0, 4]) if len(tab.DataRows) > 0 else 0

    @pyqtSlot()
    def on_butPrint_clicked(self):
        rpt = Order_Printingreport()
        rpt.PrintCurrentReport(self.ui.fOrderID.Value())


class Order_Printingreport(PrintOrder_report_Mob):
    def __init__(self):
        super().__init__()

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        if (SectionType == JPPrintSectionType.PageHeader and CurrentPage == 1):
            return True

    def PrintCurrentReport(self, OrderID: str):
        self.init_data(OrderID)
        self.init_ReportHeader_title(
            title1="NOTA DE PAGAMENTO",
            title2="(ESTE DOCUMENTO É DO USO INTERNO)")
        self.init_ReportHeader()
        self.init_ReportHeader_Individualization()
        self.init_PageHeader()
        self.init_Detail()
        self.init_ReportFooter()
        super().BeginPrint()
