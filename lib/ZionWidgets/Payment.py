from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex
from lib.JPMvc.JPFuncForm import JPFunctionForm
from lib.ZionWidgets.Order import EditForm_Order
from lib.ZionWidgets.PrintingOrder import EditForm_PrintingOrder
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
        self.tableView.setColumnHidden(13, True)
        self.CP_m_sql = """
                SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                    , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                    , fPayable, fDesconto, fNote,fEntryID,fSucursal
                FROM t_order
                WHERE fOrderID = '{}'
                """
        self.CP_s_sql = """
                SELECT fID, fOrderID, fQuant AS '数量Qtd',
                    fProductName AS '名称Descrição',
                    fLength AS '长Larg.', fWidth AS '宽Comp.',
                    fPrice AS '单价P. Unitario', fAmount AS '金额Total'
                FROM t_order_detail
                WHERE fOrderID = '{}'
                """
        self.TP_m_sql = """
            SELECT fOrderID, fCelular, fRequiredDeliveryDate, fContato
                , fTelefone, fVendedorID, fCustomerID, fOrderDate
                , fSucursal, fQuant, fNumerBegin, fNumerEnd
                , fPrice, fLogo, fEspecieID, fAvistaID, fTamanhoID
                , fNrCopyID, fPagePerVolumn, fNote, fAmount, fDesconto
                , fTax, fPayable,fEntryID
            FROM t_order
            WHERE fOrderID = '{}'
            """

    def onGetEditFormSQL_CP(self):
        return self.CP_m_sql, self.CP_s_sql

    def onGetEditFormSQL_TP(self):
        return self.TP_m_sql, None

    def onCurrentRowChanged(self, QModelIndex1, QModelIndex2):
        cur_tp = self.getCurrentSelectPKValue()[0:2]
        if cur_tp == 'CP':
            self.onGetEditFormSQL = self.onGetEditFormSQL_CP
        if cur_tp == 'TP':
            self.onGetEditFormSQL = self.onGetEditFormSQL_TP

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        cur_tp = self.getCurrentSelectPKValue()[0:2]
        if cur_tp == 'CP':
            return Edit_CP(sql_main=sql_main,
                           edit_mode=edit_mode,
                           sql_sub=sql_sub,
                           PKValue=PKValue)
        if cur_tp == 'TP':
            return Edit_TP(sql_main=sql_main,
                           edit_mode=edit_mode,
                           sql_sub=sql_sub,
                           PKValue=PKValue)


class Edit_CP(EditForm_Order):
    def __init__(self, sql_main, sql_sub=None, edit_mode=None, PKValue=None):
        super().__init__(sql_main=sql_main,
                         edit_mode=edit_mode,
                         sql_sub=sql_sub,
                         PKValue=PKValue)
        self.ui.label_Title_Chn.setText('付款书')
        self.ui.label_Title_Eng.setText('NOTA DE PAGAMENTO')

    @pyqtSlot()
    def on_butPrint_clicked(self):
        rpt = Payment_report()
        rpt.PrintCurrentReport(self.ui.fOrderID.text())


class Edit_TP(EditForm_PrintingOrder):
    def __init__(self, sql_main, PKValue=None, sql_sub=None, edit_mode=None):
        super().__init__(sql_main=sql_main,
                         edit_mode=edit_mode,
                         sql_sub=sql_sub,
                         PKValue=PKValue)
        self.ui.label_Title_Chn.setText('付款书')
        self.ui.label_Title_Eng.setText('NOTA DE PAGAMENTO')


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