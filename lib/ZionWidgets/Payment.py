from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex
from lib.ZionWidgets.ZionFunc import ZionFuncForm
from lib.ZionReport.OrderReportMob import Order_report_Mob
from lib.JPPrintReport import JPPrintSectionType
from PyQt5.QtWidgets import QMessageBox
from lib.ZionPublc import JPDb, JPPub, JPUser


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
                ORDER BY  forderID DESC"""
        sql_2 = sql_0 + """
                WHERE fCanceled=0
                        AND fSubmited=1
                ORDER BY  forderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fConfirmed1']
        self.setListFormSQL(sql_1, sql_2)
        self.checkBox_1.setText('UnConfirmed')
        self.checkBox_2.setText('Confirmed')
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(True)
        #self.tableView.setColumnHidden(13, True)

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
            QMessageBox.information(JPPub().MainForm, '', msg, QMessageBox.Yes,
                                    QMessageBox.Yes)
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
                                QMessageBox.Yes) == QMessageBox.Yes:
            db.executeTransaction(sql)
            self.btnRefreshClick()

    @pyqtSlot()
    def on_CmdEdit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if self.getCurrentColumnValue(13) == 1:
            msg = "付款单【{pk}】已经确认,不能再修改!" + '\n'
            msg = msg + 'The payment [{pk}] has been confirmed and cannot be modified.'
            msg = msg + "  Do you want to confirm this payment form?"
            msg = msg.format(pk=cu_id)
            QMessageBox.information(JPPub().MainForm, '', msg, QMessageBox.Yes,
                                    QMessageBox.Yes)
            return
        super().on_CmdEdit_clicked()


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