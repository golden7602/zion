from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtPrintSupport import QPrinter

from lib.JPPrint.JPPrintReport import JPPrintSectionType, JPReport
from lib.JPPublc import JPPub
from lib.JPMvc.JPFuncForm import JPFunctionForm
from lib.ZionWidgets.Order import EditForm_Order
from lib.JPPublc import JPDb
from lib.ZionReport.OrderReportMob import Order_report_Mob
from lib.JPMvc.JPEditFormModel import JPEditFormDataMode
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from PyQt5.QtPrintSupport import QPrinter


class _myMod(JPTableViewModelReadOnly):
    def __init__(self, *args):
        super().__init__(*args)
        self.f = QFont()
        self.f.Black = True
        self.f.setBold(True)
        self._getData = self.TabelFieldInfo.getOnlyData

    def data(self, Index, role: int = Qt.DisplayRole):
        if role == Qt.TextColorRole:
            if self._getData([Index.row(), 17]) == 1:
                return QColor(Qt.blue)
        return super().data(Index, role)


class JPFuncForm_Quotation(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_1 = """
                select 
                    fOrderID as `报价单号OrderID`, 
                    fOrderDate as `报价单日期OrderDate`, 
                    fCustomerName as `客户名Cliente`, 
                    fNUIT as `税号NUIT`, 
                    fCity as `城市City`, 
                    fConfirmed1 as `确认Confirmed`, 
                    fEntry_Name as `录入Entry`, 
                    fConfirm_Name as `fConfirm_Name`, 
                    fAmount as `金额SubTotal`, 
                    fTax as `税金IVA`, 
                    fPayable as `应付金额Valor a Pagar`, 
                    fDesconto as `折扣Desconto`, 
                    fContato as `联系人Contato`, 
                    fCelular as `手机Celular`, 
                    fTelefone as `fTelefone`, 
                    fConfirmed as `已确认Confirmed`, 
                    fCustomerID as `客户编号CustomerID` ,
                    fCreatedOrder
                from v_quotation 
                where  left(fOrderID,2)='QS'
                and fCanceled = 0 
                and fOrderDate{date}
                order by  fOrderID DESC"""
        sql_2 = """
                select 
                    fOrderID as `报价单号OrderID`, 
                    fOrderDate as `报价单日期OrderDate`, 
                    fCustomerName as `客户名Cliente`, 
                    fNUIT as `税号NUIT`, 
                    fCity as `城市City`, 
                    fConfirmed1 as `确认Confirmed`, 
                    fEntry_Name as `录入Entry`, 
                    fConfirm_Name as `fConfirm_Name`, 
                    fAmount as `金额SubTotal`, 
                    fTax as `税金IVA`, 
                    fPayable as `应付金额Valor a Pagar`, 
                    fDesconto as `折扣Desconto`, 
                    fContato as `联系人Contato`, 
                    fCelular as `手机Celular`, 
                    fTelefone as `fTelefone`, 
                    fConfirmed as `已确认Confirmed`, 
                    fCustomerID as `客户编号CustomerID` ,
                    fCreatedOrder
                from v_quotation 
                where  left(fOrderID,2)='QS'
                and fCanceled = 0 
                order by  fOrderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setHidden(True)
        self.checkBox_2.setHidden(True)
        super().setListFormSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(16, True)
        self.tableView.setColumnHidden(17, True)
        m_sql = """
                SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                    , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                    , fPayable, fDesconto, fNote,fEntryID,fSucursal
                FROM t_quotation
                WHERE fOrderID = '{}'
                """
        s_sql = """
                SELECT fID, fOrderID, fQuant AS '数量Qtd',
                    fProductName AS '名称Descrição',
                    fLength AS '长Comp.', fWidth AS '宽Larg.',
                    fPrice AS '单价P. Unitario', fAmount AS '金额Total'
                FROM t_quotation_detail
                WHERE fOrderID = '{}'
                """
        self.setEditFormSQL(m_sql, s_sql)

    def onGetModelClass(self):
        return _myMod

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        frm = Edit_Order_Quotation(sql_main=sql_main,
                                   edit_mode=edit_mode,
                                   sql_sub=sql_sub,
                                   PKValue=PKValue)
        frm.ui.fOrderID.setEnabled(False)
        frm.ui.fCity.setEnabled(False)
        frm.ui.fNUIT.setEnabled(False)
        frm.ui.fEntryID.setEnabled(False)
        frm.ui.fEndereco.setEnabled(False)
        return frm

    @pyqtSlot()
    def on_CmdOrder_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        newPKSQL = JPDb().NewPkSQL(1)
        sql = [
            """
        INSERT INTO t_order (fOrderID, fOrderDate, fVendedorID
            , fRequiredDeliveryDate, fCustomerID
            , fContato, fCelular, fTelefone, fAmount, fTax
            , fPayable, fDesconto, fNote, fEntryID, fSucursal)
            SELECT @PK, fOrderDate, fVendedorID
                , fRequiredDeliveryDate, fCustomerID
                , fContato, fCelular, fTelefone, fAmount, fTax
                , fPayable, fDesconto, fNote, fEntryID, fSucursal
                FROM t_quotation
                WHERE fOrderID = '{id}';""".format(id=cu_id), """
        INSERT INTO t_order_detail (fOrderID, fQuant, fProductName
            , fLength, fWidth, fPrice, fAmount)
            SELECT @PK, fQuant, fProductName, fLength, fWidth
                , fPrice, fAmount
            FROM t_quotation_detail
            WHERE fOrderID = '{id}';""".format(id=cu_id), """
        UPDATE t_quotation SET fCreatedOrder=1 WHERE fOrderID = '{id}';
        """.format(id=cu_id)
        ]
        sql = newPKSQL[0:2] + sql + newPKSQL[2:]
        for q in sql:
            print(q)
        try:
            isOK, result = JPDb().executeTransaction(sql)
            if isOK:
                info = '已经根据报价单生成了订单【{id}】，请修改此订单信息!\n'
                info = info + 'The order [{id}] has been generated according '
                info = info + 'to the quotation. Please modify the order information.'
                QMessageBox.information(self, "提示", info.format(id=result))
                self.refreshListForm()
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()


class Edit_Order_Quotation(EditForm_Order):
    def __init__(self, sql_main, sql_sub=None, edit_mode=None, PKValue=None):
        super().__init__(sql_main,
                         sql_sub=sql_sub,
                         edit_mode=edit_mode,
                         PKValue=PKValue)
        self.setPkRole(6)
        self.ui.label_Title_Chn.setText("报价单")
        self.ui.label_Title_Eng.setText("Cotação")
        if self.EditMode != JPEditFormDataMode.ReadOnly:
            self.ui.fCustomerID.setEditable(True)

    @pyqtSlot()
    def on_butPrint_clicked(self):
        rpt = Order_report()
        rpt.PrintCurrentReport(self.ui.fOrderID.Value())


class Order_report(Order_report_Mob):
    def __init__(self):
        super().__init__()

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        if (SectionType == JPPrintSectionType.PageHeader and CurrentPage == 1):
            return True

    def init_ReportFooter(self):
        RF = self.ReportFooter
        RF.AddItem(1,
                   430,
                   0,
                   140,
                   20,
                   "金额合计SubTotal:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignRight)
        RF.AddItem(3,
                   570,
                   0,
                   80,
                   20,
                   "fAmount",
                   FormatString='{:,.2f}',
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   20,
                   140,
                   20,
                   "折扣Desconto:",
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   570,
                   20,
                   80,
                   20,
                   "fDesconto",
                   AlignmentFlag=Qt.AlignRight,
                   FormatString='{:,.2f}',
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   40,
                   140,
                   20,
                   "税金IVA:",
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   570,
                   40,
                   80,
                   20,
                   "fTax",
                   FormatString='{:,.2f}',
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   60,
                   140,
                   20,
                   "应付金额Valor a Pagar:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignRight)
        RF.AddItem(3,
                   570,
                   60,
                   80,
                   20,
                   "fPayable",
                   FormatString='{:,.2f}',
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   0,
                   0,
                   430,
                   80,
                   "fNote1",
                   FormatString='备注Note:\n{}',
                   Bolder=True,
                   AlignmentFlag=(Qt.AlignLeft | Qt.TextWordWrap),
                   Font=self.font_YaHei_8)
        # 签字部分
        RF.AddItem(1,
                   0,
                   110,
                   100,
                   20,
                   '制作人 Productor:',
                   Bolder=False,
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1, 100, 125, 100, 0, '')

        RF.AddItem(1,
                   420,
                   110,
                   120,
                   20,
                   '审核人 Aprovar::',
                   Bolder=False,
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1, 540, 125, 100, 0, '')
        noteStr = JPDb().getOnConfigValue('Bank_Account', str).split('\n')

        self.Arial_Black = QFont("Arial")
        self.Arial_Black.setPointSize(8)
        self.Arial_Black.setBold(True)

        for i, txt in enumerate(noteStr):
            RF.AddItem(1,
                       5,
                       135 + i * 15,
                       650,
                       20,
                       txt,
                       Bolder=False,
                       AlignmentFlag=(Qt.AlignLeft | Qt.TextWordWrap),
                       Font=self.Arial_Black)
        # 下面的框要删除，因为跨页
        RF.AddItem(1, 0, 135, 650, len(noteStr) * 15, " ", Bolder=True)
        self.PageFooter.AddItem(4,
                                10,
                                0,
                                100,
                                20,
                                '',
                                FormatString='Page: {Page}/{Pages}',
                                Bolder=False,
                                AlignmentFlag=Qt.AlignLeft,
                                Font=self.font_YaHei_8)
        self.PageFooter.AddItem(5,
                                110,
                                0,
                                540,
                                20,
                                '',
                                FormatString="PrintTime: %Y-%m-%d %H:%M:%S",
                                Bolder=False,
                                AlignmentFlag=Qt.AlignRight,
                                Font=self.font_YaHei_8)

    def init_data(self, OrderID: str):
        SQL = """SELECT o.*
                    , if(isnull(fNote), ' ', fNote) AS fNote1
                    , d.fQuant, d.fProductName, d.fLength, d.fWidth, d.fPrice
                    , d.fAmount AS fAmountDetail
                FROM v_quotation o
                    RIGHT JOIN t_quotation_detail d ON o.fOrderID = d.fOrderID
                WHERE d.fOrderID = '{}'"""

        db = JPDb()
        data = db.getDict(SQL.format(OrderID))
        data.sort(key=lambda x: (x['fCustomerName'], x['fCity'], x['fAmount']
                                 is None, x['fAmount']))
        self.DataSource = data

    def PrintCurrentReport(self, OrderID: str):
        self.init_data(OrderID)
        self.init_ReportHeader_title(
            title1="报价单Cotação", title2="(ESTE DOCUMENTO É DO USO INTERNO)")
        self.init_ReportHeader()
        self.init_ReportHeader_Individualization()
        self.init_PageHeader()
        self.init_Detail()
        self.init_ReportFooter()
        # 大于6行自动更改纸型
        if len(self.DataSource) > 6:
            self.PaperSize = QPrinter.A4
            self.Orientation = QPrinter.Orientation(0)
        super().BeginPrint()
