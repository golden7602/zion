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
from lib.JPMvc.JPFuncForm import JPFunctionForm


class JPFuncForm_Adjustment(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_1 = """
                SELECT fOrderID as `订单号码OrderID`,
                    fOrderDate as `日期OrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fCanceled1 as `已作废Canceled`,
                    fCancel_Name as `作废提交人CancelUser`,
                    fSubmited1 as `提交Submited`,
                    fSubmit_Name as `Submit_User`,
                    fConfirmed1 as `确认Confirmed`,
                    fConfirm_Name as `确认人fConfirm_Name`,
                    fDelivered1 as `交付Delivered`,
                    fDeliverer_Name as `交付人Deliverer_Name`,
                    fAmount as `金额SubTotal`,
                    fTax as `税金IVA`,
                    fPayable as `应付金额Valor a Pagar`,
                    fDesconto as `折扣Desconto`,
                    fCustomerID as `客户编号CustomerID`,
                    fCanceled as `fCanceled`
                FROM v_order AS o
                WHERE fOrderDate{date}
                        AND (fCanceled={ch1} OR fCanceled={ch2})
                ORDER BY  forderID DESC"""

        sql_2 = """
                SELECT fOrderID as `订单号码OrderID`,
                    fOrderDate as `日期OrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fCanceled1 as `已作废Canceled`,
                    fCancel_Name as `作废提交人CancelUser`,
                    fSubmited1 as `提交Submited`,
                    fSubmit_Name as `Submit_User`,
                    fConfirmed1 as `确认Confirmed`,
                    fConfirm_Name as `确认人fConfirm_Name`,
                    fDelivered1 as `交付Delivered`,
                    fDeliverer_Name as `交付人Deliverer_Name`,
                    fAmount as `金额SubTotal`,
                    fTax as `税金IVA`,
                    fPayable as `应付金额Valor a Pagar`,
                    fDesconto as `折扣Desconto`,
                    fCustomerID as `客户编号CustomerID`,
                    fCanceled as `fCanceled`
                FROM v_order AS o
                ORDER BY  forderID DESC"""

        self.backgroundWhenValueIsTrueFieldName = ['fCanceled']
        self.checkBox_1.setText('Normal')
        self.checkBox_2.setText('Cancelled')
        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(False)
        super().setSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)

    def but_click(self, name):
        for n, fun in JPFuncForm_Complete.__dict__.items():
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