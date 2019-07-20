
def getFuncForm_FormReport_Day(mainform):
    from Ui.Ui_FormReport_Day import Ui_Form
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    mainform.addForm(Form)

    class myMod(JPTableViewModelReadOnly):
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

    cbo_year, cbo_base = ui.cbo_year, ui.cbo_base
    tw = ui.tableView
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
        ) Q3
        """
    db=JPDb
    year = db.getDataList('''select year(fOrderDate) as y  
                from t_order union select year(fReceiptDate) 
                as y from t_receivables''')[0]
    ui.mod = None

    def _search():
        if cbo_year.currentIndex() != -1 and cbo_base.currentIndex() != -1:
            sql = cbo_base.currentData()
            queryInfo = JPQueryFieldInfo(sql.format(cbo_year.currentText()))
            ui.mod = myMod(tw, queryInfo)

    def butPrint():
        if ui.mod is None:
            return
        flds = ui.mod.fields
        rpt = JPReport(QPrinter.A4, QPrinter.Orientation(1))
        rpt.ReportHeader.AddItem(1,
                                 0,
                                 0,
                                 100 * 13,
                                 40,
                                 '收款日报表',
                                 Bolder=False,
                                 AlignmentFlag=(QtCore.Qt.AlignCenter))
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
        rpt.DataSource = ui.mod.getDataDict(Qt.EditRole)
        rpt.BeginPrint()

    cbo_year.addItems([str(y[0]) for y in year if y[0]])
    cbo_year.setCurrentIndex(-1)
    cbo_base.clear()
    cbo_base.addItem('Payment', sql_payment)
    cbo_base.addItem('Receivables', sql_receivables)
    cbo_base.setCurrentIndex(-1)
    tw.setSelectionMode(QAbstractItemView.SingleSelection)
    tw.setSelectionBehavior(QAbstractItemView.SelectRows)
    cbo_base.currentTextChanged.connect(_search)
    cbo_year.currentTextChanged.connect(_search)
    ui.butPrint.clicked.connect(butPrint)
    return Form

