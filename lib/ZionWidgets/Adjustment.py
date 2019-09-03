from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtPrintSupport import QPrinter

from lib.JPPrintReport import JPPrintSectionType, JPReport
from lib.ZionPublc import JPPub, JPDb
from lib.ZionWidgets.ZionFunc import ZionFuncForm
from lib.JPMvc.JPModel import JPTableViewModelReadOnly


class myJPTableViewModelReadOnly(JPTableViewModelReadOnly):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def data(self, index, role=Qt.DisplayRole):
        c = index.column()
        if c in (3, 5, 7, 9) and role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        elif c == 3 and role == Qt.TextColorRole:
            return QColor(Qt.red)
        else:
            return super().data(index, role)


class JPFuncForm_Adjustment(ZionFuncForm):
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
        self.setListFormSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)

    def onGetModelClass(self):
        return myJPTableViewModelReadOnly

    @pyqtSlot()
    def on_CmdCancel_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        sql = "update t_order set fCanceled=1 where fOrderID='{pk}'"
        db = JPDb()
        sql = sql.format(pk=cu_id)
        msg = '您确认要作废此订单？\n'
        msg = msg + "Are you sure you want to cancel this order?"
        msg = msg.format(pk=cu_id)
        if QMessageBox.question(JPPub().MainForm, '确认', msg,
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:
            db.executeTransaction(sql)
            self.refreshListForm()

    @pyqtSlot()
    def on_CmdAdjustment_clicked(self):
        super().on_CmdEdit_clicked()

    def onAfterCreatedForm(self, cur_tp, form):
        for nm in form.ObjectDict.keys():
            form.ObjectDict[nm].setEnabled(False)
        try:
            if form.isEditMode:
                form.ui.fPrice.setEnabled(True)
                form.ui.fTax.setEnabled(True)
        except Exception as identifier:
            pass


        return super().onAfterCreatedForm(cur_tp, form)
