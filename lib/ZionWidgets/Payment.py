from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex
from lib.ZionWidgets.ZionFunc import ZionFuncForm
from lib.ZionReport.OrderReportMob import Order_report_Mob
from lib.JPPrint.JPPrintReport import JPPrintSectionType
from PyQt5.QtWidgets import QMessageBox
from lib.JPPublc import JPDb, JPPub, JPUser
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from PyQt5.QtGui import QColor


class myJPTableViewModelReadOnly(JPTableViewModelReadOnly):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ok_icon = JPPub().MainForm.getIcon('yes.ico')

    def data(self, index, role=Qt.DisplayRole):
        r = index.row()
        c = index.column()
        tab = self.TabelFieldInfo
        if c == 4:
            if role == Qt.DecorationRole:
                if tab.getOnlyData((r, c)):
                    return self.ok_icon
            else:
                return super().data(index, role=role)
        else:
            return super().data(index, role=role)


class JPFuncForm_Payment(ZionFuncForm):
    def __init__(self, parent):
        super().__init__(parent)
        sql_0 = """
            SELECT fOrderID AS 订单号码OrderID,
                    fOrderDate AS 日期OrderDate,
                    fCustomerName AS 客户名Cliente,
                    fCity AS 城市City,
                    fConfirmed1 AS 确认Confirmed,
                    fConfirm_Name AS 确认人Confirm,
                    fAmount AS 金额SubTotal,
                    fRequiredDeliveryDate AS 交货日期RDD,
                    fDesconto AS 折扣Desconto,
                    fTax AS 税金IVA,
                    fPayable AS `应付金额Valor a Pagar`,
                    fContato AS 联系人Contato,
                    fCelular AS 手机Celular,
                    cast(fConfirmed AS SIGNED) AS fConfirmed
            FROM v_order AS o
        """
        sql_1 = sql_0 + """
                WHERE fCanceled=0
                        AND fSubmited=1
                        AND fOrderDate{date}
                        AND (fConfirmed={ch1}
                        OR fConfirmed={ch2})
                ORDER BY  forderDate DESC,fOrderID DESC"""
        sql_2 = sql_0 + """
                WHERE fCanceled=0
                        AND fSubmited=1
                ORDER BY  forderDate DESC,fOrderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fConfirmed1']
        self.setListFormSQL(sql_1, sql_2)
        self.checkBox_1.setText('Confirmed')
        self.checkBox_2.setText('UnConfirmed')
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(True)
        self.tableView.setColumnHidden(13, True)

    def onGetModelClass(self):
        return myJPTableViewModelReadOnly

    @pyqtSlot()
    def on_butPrint_clicked(self):
        rpt = Payment_report()
        rpt.PrintCurrentReport(self.ui.fOrderID.text())

    @pyqtSlot()
    def on_CmdConfirm_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if self.getCurrentColumnValue(13) == 1:
            msg = '付款书已经确认，无法重复确认!\n'
            msg = msg + 'The payment has been confirmed and cannot be repeated.'
            QMessageBox.information(JPPub().MainForm, '提示', msg)
            return
        sql = "update t_order set fConfirmed=1,fConfirmID={uid} where fOrderID='{pk}'"
        db = JPDb()
        us = JPUser()
        sql = sql.format(pk=cu_id, uid=us.currentUserID())
        msg = "付款单【{pk}】确认后将不能修改。是否要确认此付款单？" + '\n'
        msg = msg + 'The bill [{pk}] of payment will not be amended after confirmation.'
        msg = msg + "  Do you want to confirm this payment form?"
        msg = msg.format(pk=cu_id)
        if QMessageBox.question(JPPub().MainForm, '确认', msg,
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:
            db.executeTransaction(sql)
            JPPub().broadcastMessage(tablename="t_order",
                                     action='confirmation',
                                     PK=cu_id)
            self.refreshListForm()

    @pyqtSlot()
    def on_CmdEdit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if self.getCurrentColumnValue(13) == 1:
            msg = "付款单【{pk}】已经确认,不能再修改!" + '\n'
            msg = msg + 'The payment [{pk}] has been confirmed and cannot be modified.'
            msg = msg + "  Do you want to confirm this payment form?"
            msg = msg.format(pk=cu_id)
            QMessageBox.information(JPPub().MainForm, '提示', msg)
            return
        super().on_CmdEdit_clicked()

    def onAfterCreatedForm(self, cur_tp, form):
        form.ui.fOrderID.setEnabled(False)
        form.ui.fOrderDate.setEnabled(False)
        form.ui.fCustomerID.setEnabled(False)
        form.ui.fRequiredDeliveryDate.setEnabled(False)
        form.ui.fEntryID.setEnabled(False)


class Payment_report(Order_report_Mob):
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