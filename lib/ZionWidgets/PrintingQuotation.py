from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtPrintSupport import QPrinter

from lib.JPPrintReport import JPPrintSectionType, JPReport
from lib.ZionPublc import JPPub
from lib.ZionWidgets.FuncFormBase import JPFunctionForm


class JPFuncForm_PrintingQuotation(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_1 = """
                select 
                    fOrderID as `报价单号fOrderID`,
                    fOrderDate as `报价单日期fOrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fNUIT as `税号NUIT`,
                    fCity as `城市City`,
                    fConfirmed1 as `确认Confirmed`,
                    fEntry_Name as `录入Entry`,
                    fConfirm_Name as `确认人Confirm_Name`,
                    fAmount as `金额SubTotal`,
                    fTax as `税金IVA`,
                    fPayable as `应付金额Valor a Pagar`,
                    fDesconto as `折扣Desconto`,
                    fContato as `联系人Contato`,
                    fCelular as `手机Celular`,
                    fTelefone as `电话Telefone`,
                    fConfirmed as `已确认Confirmed`,
                    fCustomerID as `客户编号CustomerID`
                from v_quotation 
                where  left(fOrderID,2)='QP'
                and fCanceled = 0 
                and fOrderDate{date}
                order by  fOrderID DESC"""
        sql_2 = """
                select 
                    fOrderID as `报价单号fOrderID`,
                    fOrderDate as `报价单日期fOrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fNUIT as `税号NUIT`,
                    fCity as `城市City`,
                    fConfirmed1 as `确认Confirmed`,
                    fEntry_Name as `录入Entry`,
                    fConfirm_Name as `确认人Confirm_Name`,
                    fAmount as `金额SubTotal`,
                    fTax as `税金IVA`,
                    fPayable as `应付金额Valor a Pagar`,
                    fDesconto as `折扣Desconto`,
                    fContato as `联系人Contato`,
                    fCelular as `手机Celular`,
                    fTelefone as `电话Telefone`,
                    fConfirmed as `已确认Confirmed`,
                    fCustomerID as `客户编号CustomerID`
                from v_quotation 
                where  left(fOrderID,2)='QP'
                and fCanceled = 0 
                order by  fOrderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setHidden(True)
        self.checkBox_2.setHidden(True)
        super().setSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)

    def but_click(self, name):
        for n, fun in JPFuncForm_Order.__dict__.items():
            if n.upper() == 'BTN{}CLICKED'.format(name.upper()):
                fun(self)

    def getCurrentCustomerID(self):
        index = self.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.model.TabelFieldInfo.getOnlyData([index.row(), 0])

    @pyqtSlot()
    def on_CMDEXPORTTOEXCEL_clicked(self):
        print('单击了CMDEXPORTTOEXCEL按钮')

    @pyqtSlot()
    def on_CMDNEW_clicked(self):
        print("CMDNEW被下")
        #showEditForm_Order(self.MainForm, JPFormModelMainSub.New)

    @pyqtSlot()
    def on_CMDBROWSE_clicked(self):
        cu_id = self.getCurrentCustomerID()
        if not cu_id:
            return
        #showEditForm_Order(self.MainForm, JPFormModelMainSub.ReadOnly, cu_id)
        print("CMDBROWSE被下", cu_id)