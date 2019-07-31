from os import getcwd
from sys import path as jppath
jppath.append(getcwd())


from PyQt5.QtCore import pyqtSlot
from lib.ZionWidgets.FuncFormBase import JPFunctionForm
from lib.ZionWidgets.Order import EditForm_Order
from lib.ZionReport.OrderReportMob import Order_report_Mob
from lib.JPPrintReport import JPPrintSectionType

class JPFuncForm_Payment(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
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
                        cast(fSubmited AS SIGNED) AS fSubmited
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
        self.checkBox_1.setText('UnConfirmed')
        self.checkBox_2.setText('Confirmed')
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(True)
        super().setSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)

    def getCurrentCustomerID(self):
        index = self.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.model.TabelFieldInfo.getOnlyData([index.row(), 0])

    def getEditFormClass(self):
        cur_id = self.getCurrentCustomerID()
        if cur_id[0:2] == 'CP':
            return EditForm_Payment_Order
        if cur_id[0:2] == 'TP':
            return


class EditForm_Payment_Order(EditForm_Order):
    def __init__(self, edit_mode, PKValue=None, flags=Qt.WindowFlags()):
        super().__init__(edit_mode, PKValue, flags)
        self.ui.label_Title_Chn.setText('付款书')
        self.ui.label_Title_Eng.setText('NOTA DE PAGAMENTO')

    @pyqtSlot()
    def on_butPrint_clicked(self):
        rpt = Payment_report()
        rpt.PrintCurrentReport(self.ui.fOrderID.text())

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
        super().BeginPrint()NOTA DE PAGAMENTO