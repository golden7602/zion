from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot, pyqtSignal

from PyQt5.QtWidgets import QMessageBox, QWidget, QDialog
from lib.JPPrintReport import JPPrintSectionType
from lib.ZionPublc import JPPub
from lib.ZionWidgets.FuncFormBase import JPFunctionForm
from Ui.Ui_FormOrderMob import Ui_Form
from lib.JPMvc.JPModel import JPFormModelMainSub, JPEditFormDataMode
from lib.JPDatabase.Database import JPDb
from lib.ZionReport.OrderReportMob import Order_report_Mob


class JPFuncForm_Order(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_0 = """
                SELECT fOrderID as 订单号码OrderID,
                        fOrderDate as 日期OrderDate,
                        fCustomerName as 客户名Cliente,
                        fCity as 城市City,
                        fSubmited1 as 提交Submited,
                        fSubmit_Name as 提交人Submitter,
                        fRequiredDeliveryDate as 交货日期RequiredDeliveryDate,
                        fAmount as 金额SubTotal,
                        fDesconto as 折扣Desconto,
                        fTax as 税金IVA,
                        fPayable as `应付金额Valor a Pagar`,
                        fContato as 联系人Contato,
                        fCelular as 手机Celular,
                        fSubmited AS fSubmited
                FROM v_order AS o"""
        sql_1 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                        AND (fSubmited={ch1}
                        OR fSubmited={ch2})
                        AND fOrderDate{date}
                ORDER BY  forderID DESC"""
        sql_2 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                ORDER BY  forderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('UnSubmited')
        self.checkBox_2.setText('Submited')
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(True)
        super().setSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)
        self.fSubmited_column = 13

    def getEditFormClass(self):
        return EditForm_Order


# 继承模型，为了设置重载方法，必要要时也可以用动态绑定到函数
class myMainSubMode(JPFormModelMainSub):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def subModel_AfterSetDataBeforeInsterRowEvent(self, row_data, Index):
        if row_data is None:
            return False
        if row_data[7] is None:
            return False
        data = row_data
        if data[7] == 0:
            return False
        lt = [data[2], data[4], data[5], data[6], data[7]]
        lt = [float(str(i)) if i else 0 for i in lt]
        return int(lt[4] * 100) == int(
            reduce(lambda x, y: x * y, lt[0:4]) * 100)


class EditForm_Order(QDialog):
    afterSaveData = pyqtSignal()

    def __init__(self, edit_mode, PKValue=None, flags=Qt.WindowFlags()):
        pub = JPPub()
        super().__init__(pub.MainForm, flags=flags)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.EditMode = edit_mode
        self.PKValue = PKValue
        self.tv = self.ui.tableView
        self.ui.butSave.setEnabled(False)
        curPK = PKValue if PKValue else ''
        m_sql = """
                SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                    , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                    , fPayable, fDesconto, fNote
                FROM t_order
                WHERE fOrderID = '{}'
                """.format(curPK)
        s_sql = """
                SELECT fID, fOrderID, fQuant AS '数量Qtd', 
                    fProductName AS '名称Descrição', 
                    fLength AS '长Larg.', fWidth AS '宽Comp.', 
                    fPrice AS '单价P. Unitario', fAmount AS '金额Total'
                FROM t_order_detail
                WHERE fOrderID = '{}'    
                """.format(curPK)
        self.MS_Mod = myMainSubMode(self.ui, self.tv)
        self.SubMod = self.MS_Mod.subModel
        self.MainMod = self.MS_Mod.mainModel
        self.MainMod.setFieldsRowSource([('fCustomerID',
                                          pub.getCustomerList()),
                                         ('fVendedorID', pub.getEnumList(10))])
        self.MainMod.setTabelInfo(m_sql)
        self.SubMod.setColumnsHidden(0, 1)
        self.SubMod.setColumnWidths(0, 0, 60, 300, 100, 100, 100, 100)
        self.SubMod.setColumnsReadOnly(7)
        self.SubMod.setTabelInfo(s_sql)
        self.SubMod.setFormula(7, (
            "JPRound(JPRound({2}) * JPRound({4},2) * JPRound({5},2) * JPRound({6},2),2)"
        ))
        self.MS_Mod.firstHasDirty.connect(self.firstDirty)
        self.MS_Mod.dataChanged[QModelIndex].connect(self.Cacu)
        self.MS_Mod.dataChanged[QWidget].connect(self.Cacu)
        self.ui.fCustomerID.currentIndexChanged.connect(
            self.fCustomerID_currentIndexChanged)
        self.MS_Mod.show(edit_mode)

    def firstDirty(self):
        self.ui.butSave.setEnabled(True)

    # 计算金额事件
    def Cacu(self, *args):
        self.MS_Mod.dataChanged[QModelIndex].disconnect(self.Cacu)
        self.MS_Mod.dataChanged[QWidget].disconnect(self.Cacu)
        if self.EditMode != JPEditFormDataMode.ReadOnly:
            v_sum = self.SubMod._model.getColumnSum(7)
            fDesconto = self.MainMod.getObjectValue("fDesconto")
            fTax = (v_sum - fDesconto) * 0.17
            fPayable = v_sum - fDesconto + fTax
            self.MainMod.setObjectValue('fAmount', v_sum)
            self.MainMod.setObjectValue("fTax", fTax)
            self.MainMod.setObjectValue("fPayable", fPayable)
        self.MS_Mod.dataChanged[QWidget].connect(self.Cacu)
        self.MS_Mod.dataChanged[QModelIndex].connect(self.Cacu)

    def fCustomerID_currentIndexChanged(self, r):
        obj = self.ui.fCustomerID
        row = obj.RowSource[r]
        self.ui.fNUIT.setText(row[2])
        self.ui.fCity.setText(row[3])

    @pyqtSlot()
    def on_butSave_clicked(self):
        try:
            lst = self.MS_Mod.getSqls(1)
            isOK, result = JPDb().executeTransaction(lst)
            if isOK:
                self.ui.fOrderID.setText(result)
                self.ui.butSave.setEnabled(False)
                self.MS_Mod.setEditState(False)
                self.afterSaveData.emit()
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()

    @pyqtSlot()
    def on_butPrint_clicked(self):
        rpt = Order_report()
        rpt.PrintCurrentReport(self.ui.fOrderID.text())


class Order_report(Order_report_Mob):
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
