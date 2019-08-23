from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import Qt, QDate, pyqtSlot  #, QMetaObject, pyqtSlot
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QWidget, QAbstractItemView
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from Ui.Ui_FormReport_Day import Ui_Form
from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPFunction import findButtonAndSetIcon
from lib.JPPrintReport import JPReport
from PyQt5.QtPrintSupport import QPrinter
from lib.JPExcel.JPExportToExcel import JPExpExcelFromTabelFieldInfo


class _myMod(JPTableViewModelReadOnly):
    def __init__(self, *args):
        super().__init__(*args)
        self.f = QFont()
        self.f.Black = True
        self.f.setBold(True)

    def data(self, Index, role: int = Qt.DisplayRole):
        if Index.column() == 0 and role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        if Index.column() == 0 and role == Qt.BackgroundColorRole:
            return QColor(Qt.gray)
        if Index.column() == 0 and role == Qt.FontRole:
            return self.f
        if Index.row() == (super().rowCount() -
                           1) and role == Qt.BackgroundColorRole:
            return QColor(Qt.gray)
        if Index.row() == (super().rowCount() - 1) and role == Qt.FontRole:
            return self.f
        return super().data(Index, role)


class Form_Repoet_Day(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        mainform.addForm(self)
        findButtonAndSetIcon(self)
        year_sql = """
                select year(fOrderDate) as y  
                from t_order union select year(fReceiptDate) 
                as y from t_receivables
        """
        self.sql_none = """
            SELECT 
            Null as M1, Null as M2, Null as M3, Null as M4, 
            Null as M5, Null as M6, Null as M7, Null as M8, 
            Null as M9, Null as M10, Null as M11, Null as M12 
            from  t_order {}
        """
        sql_receivables = """
            SELECT IF(ISNULL(Q3.d), 'Sum', Q3.d) AS Day0
                , M1, M2, M3, M4, M5, M6, M7, M8, M9, M10
                , M11, M12
            FROM (
                SELECT Q1.d
                    , IF(Q1.m = 1, Q1.j1, NULL) AS M1
                    , IF(Q1.m = 2, Q1.j1, NULL) AS M2
                    , IF(Q1.m = 3, Q1.j1, NULL) AS M3
                    , IF(Q1.m = 4, Q1.j1, NULL) AS M4
                    , IF(Q1.m = 5, Q1.j1, NULL) AS M5
                    , IF(Q1.m = 6, Q1.j1, NULL) AS M6
                    , IF(Q1.m = 7, Q1.j1, NULL) AS M7
                    , IF(Q1.m = 8, Q1.j1, NULL) AS M8
                    , IF(Q1.m = 9, Q1.j1, NULL) AS M9
                    , IF(Q1.m = 10, Q1.j1, NULL) AS M10
                    , IF(Q1.m = 11, Q1.j1, NULL) AS M11
                    , IF(Q1.m = 12, Q1.j1, NULL) AS M12
                FROM (
                    SELECT MONTH(fReceiptDate) AS m, DAY(fReceiptDate) AS d
                        , SUM(fAmountCollected) AS j1
                    FROM t_receivables
                    WHERE YEAR(fReceiptDate) = {}
                    GROUP BY MONTH(fReceiptDate), DAY(fReceiptDate)
                ) Q1
                GROUP BY Q1.d WITH ROLLUP
            ) Q3
        """
        sql_payment = """
                SELECT if(isnull(Q3.d), 'Sum', Q3.d) AS Day0
                    , M1, M2, M3, M4, M5, M6, M7, M8, M9, M10
                    , M11, M12
                FROM (
                    SELECT Q1.d
                        , IF(Q1.m = 1, Q1.j1, NULL) AS M1
                        , IF(Q1.m = 2, Q1.j1, NULL) AS M2
                        , IF(Q1.m = 3, Q1.j1, NULL) AS M3
                        , IF(Q1.m = 4, Q1.j1, NULL) AS M4
                        , IF(Q1.m = 5, Q1.j1, NULL) AS M5
                        , IF(Q1.m = 6, Q1.j1, NULL) AS M6
                        , IF(Q1.m = 7, Q1.j1, NULL) AS M7
                        , IF(Q1.m = 8, Q1.j1, NULL) AS M8
                        , IF(Q1.m = 9, Q1.j1, NULL) AS M9
                        , IF(Q1.m = 10, Q1.j1, NULL) AS M10
                        , IF(Q1.m = 11, Q1.j1, NULL) AS M11
                        , IF(Q1.m = 12, Q1.j1, NULL) AS M12
                    FROM (
                        SELECT MONTH(fOrderDate) AS m, DAY(fOrderDate) AS d
                            , SUM(fPayable) AS j1
                        FROM t_order
                        WHERE (Year(fOrderDate) = {}
                            AND fCanceled = 0
                            AND fSubmited = 1
                            AND fConfirmed = 1)
                        GROUP BY MONTH(fOrderDate), DAY(fOrderDate)
                    ) Q1
                    GROUP BY Q1.d WITH ROLLUP
                ) Q3        """
        self.cbo_base = self.ui.cbo_base
        self.cbo_year = self.ui.cbo_year
        self.tableView = self.ui.tableView
        self.cbo_base.addItem('Payment', sql_payment)
        self.cbo_base.addItem('Receivables', sql_receivables)
        db = JPDb()
        year_list = db.getDataList(year_sql)
        year_list = [str(y[0]) for y in year_list if y[0]]
        for y in year_list:
            self.cbo_year.addItem(y)
        self.cbo_year.setCurrentIndex(-1)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cbo_base.currentTextChanged.connect(self._search)
        self.cbo_year.currentTextChanged.connect(self._search)
        #self.butPrint.clicked.connect(self.onbutPrint)
        self._search()

    def _search(self):
        db = JPDb()
        sql = self.cbo_base.currentData() if (
            self.cbo_base.currentIndex() != -1
            and self.cbo_year.currentIndex() != -1) else self.sql_none.format(
                db.getOnlyStrcFilter())
        self.queryInfo = JPQueryFieldInfo(
            sql.format(self.cbo_year.currentText()))
        self.mod = _myMod(self.tableView, self.queryInfo)
        self.tableView.setModel(self.mod)

    @pyqtSlot()
    def on_CmdPrint_clicked(self):
        if len(self.queryInfo) == 0:
            return
        flds = self.queryInfo.Fields
        rpt = FormReport_Day_print(flds, self.cbo_year.currentText())
        rpt.DataSource = self.mod.getDataDict(Qt.EditRole)
        rpt.BeginPrint()

    @pyqtSlot()
    def on_CmdExportToExcel_clicked(self):
        exp = JPExpExcelFromTabelFieldInfo(self.model.TabelFieldInfo,
                                           self.MainForm)
        exp.run()


class FormReport_Day_print(JPReport):
    def __init__(self,
                 flds,
                 myyear,
                 PaperSize=QPrinter.A3,
                 Orientation=QPrinter.Orientation(1)):
        super().__init__(PaperSize, Orientation)

        self.font_YaHei = QFont("微软雅黑")
        self.font_YaHei_8 = QFont(self.font_YaHei)
        self.font_YaHei_8.setPointSize(8)
        self.font_YaHei_10 = QFont(self.font_YaHei)
        self.font_YaHei_10.setPointSize(20)
        self.font_YaHei_10.setBold(True)
        rpt = self
        rpt.ReportHeader.AddItem(1,
                                 0,
                                 0,
                                 100 * 13,
                                 40,
                                 'Rec Year Report收款日报表',
                                 Bolder=False,
                                 AlignmentFlag=(Qt.AlignCenter),
                                 Font=self.font_YaHei_10)
        self.ReportHeader.AddItem(1,
                                  100 * 11,
                                  20,
                                  200,
                                  20,
                                  '年度Year: {}'.format(myyear),
                                  Bolder=False,
                                  AlignmentFlag=(Qt.AlignRight))

        title = [fld.Title for fld in flds]
        fns = [fld.FieldName for fld in flds]
        cols = len(flds)
        al_c = Qt.AlignCenter
        al_r = (Qt.AlignVCenter | Qt.AlignRight)
        rpt.SetMargins(30, 60, 30, 30)
        rpt.ReportHeader.AddPrintLables(0,
                                        50,
                                        50,
                                        Texts=title,
                                        Widths=[100] * cols,
                                        Aligns=[al_c] * cols)
        rpt.Detail.AddPrintFields(0,
                                  0,
                                  25,
                                  FieldNames=[fns[0]],
                                  Widths=[100],
                                  Aligns=[al_c])
        for i in range(1, cols):
            rpt.Detail.AddItem(3,
                               i * 100,
                               0,
                               100,
                               25,
                               fns[i],
                               AlignmentFlag=al_r,
                               FormatString='{:,.2f}')
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
                                100 * 10,
                                0,
                                100 * 3,
                                20,
                                '',
                                FormatString="PrintTime: %Y-%m-%d %H:%M:%S",
                                Bolder=False,
                                AlignmentFlag=Qt.AlignRight,
                                Font=self.font_YaHei_8)

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        return False


# def getFuncForm_FormReport_Day(mainform):
#     from Ui.Ui_FormReport_Day import Ui_Form
#     Form = QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     mainform.addForm(Form)

#     cbo_year, cbo_base = ui.cbo_year, ui.cbo_base
#     tw = ui.tableView

#     db = JPDb
#     year = db.getDataList('''select year(fOrderDate) as y
#                 from t_order union select year(fReceiptDate)
#                 as y from t_receivables''')[0]
#     ui.mod = None

#     def _search():
#         if cbo_year.currentIndex() != -1 and cbo_base.currentIndex() != -1:
#             sql = cbo_base.currentData()
#             queryInfo = JPQueryFieldInfo(sql.format(cbo_year.currentText()))
#             ui.mod = myMod(tw, queryInfo)

#     cbo_year.addItems([str(y[0]) for y in year if y[0]])
#     cbo_year.setCurrentIndex(-1)
#     cbo_base.clear()
#     cbo_base.addItem('Payment', self.sql_payment)
#     cbo_base.addItem('Receivables', sql_receivables)
#     cbo_base.setCurrentIndex(-1)
#     tw.setSelectionMode(QAbstractItemView.SingleSelection)
#     tw.setSelectionBehavior(QAbstractItemView.SelectRows)
#     cbo_base.currentTextChanged.connect(_search)
#     cbo_year.currentTextChanged.connect(_search)
#     ui.butPrint.clicked.connect(butPrint)
#     return Form
