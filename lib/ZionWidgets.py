# -*- coding: utf-8 -*-

from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce
import datetime
from dateutil.relativedelta import relativedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex, Qt, pyqtSignal
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QWidget, QDialog

from lib.JPDatabase.Database import JPDb
from lib.JPDatebase import JPMySqlSingleTableQuery as JPQ, JPTabelFieldInfo, JPQueryFieldInfo
from lib.JPFunction import NV, JPRound
from lib.JPMvc.JPModel import JPFormModelMainSub, JPTableViewModelReadOnly
from lib.JPPrintReport import JPReport
from lib.ZionPublc import JPPub
from PyQt5.QtGui import QIcon, QPixmap
from lib.JPDatabase.Query import JPQueryFieldInfo


class FunctionForm(QWidget):
    def __init__(self, parent, flags=Qt.WindowFlags()):
        super().__init__(parent, flags=flags)
        # 把本窗体加入主窗体
        parent.addForm(self)
        self.MainForm = parent
        self.DefauleParaSQL = ''
        self.DefauleBaseSQL = ''
        self.backgroundWhenValueIsTrueFieldName = []

        self.setObjectName("Form")
        self.resize(742, 300)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_FuncFullPath = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FuncFullPath.setFont(font)
        self.label_FuncFullPath.setObjectName("label_FuncFullPath")
        self.horizontalLayout_2.addWidget(self.label_FuncFullPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_Button = QtWidgets.QWidget(self)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.widget_Button.setFont(font)
        self.widget_Button.setObjectName("widget_Button")
        self.horizontalLayout_Button = QtWidgets.QHBoxLayout(
            self.widget_Button)
        self.horizontalLayout_Button.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Button.setSpacing(0)
        self.horizontalLayout_Button.setObjectName("horizontalLayout_Button")
        self.horizontalLayout_3.addWidget(self.widget_Button)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.checkBox_1 = QtWidgets.QCheckBox(self)
        self.checkBox_1.setObjectName("checkBox_1")
        self.horizontalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setEditTriggers(
            QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setMinimumSectionSize(23)
        self.tableView.verticalHeader().setDefaultSectionSize(24)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(self)

        # 以下为初始化部分，不能删除
        self.comboBox.addItems(['Today', 'Last Month', 'Last Year', 'All'])
        self.checkBox_1.clicked.connect(self.btnRefreshClick)
        self.checkBox_2.clicked.connect(self.btnRefreshClick)
        self.comboBox.activated['int'].connect(self.btnRefreshClick)
        # 行交错颜色
        self.tableView.setAlternatingRowColors(True)

    def setSQL(self, sql_with_where, sql_base):
        '''setSQL(sql_without_para, where_string)\n
        sql_without_para: 不带Where子句的sql
        where_string： where子句，参数用{}表示
        '''
        self.DefauleParaSQL = sql_with_where
        self.DefauleBaseSQL = sql_base
        self.btnRefreshClick()

    def getModelClass(self):
        '''此类或以重写，改写Model的行为,必须返回一个模型类
        重写时可以在重载方法中内部继承一个类，将该类返回
        '''
        return JPTableViewModelReadOnly

    def btnRefreshClick(self):
        if self.DefauleParaSQL:
            #self.tableView.clear()
            self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
            ch1 = 1 if self.checkBox_1.isChecked() else 0
            ch2 = 0 if self.checkBox_2.isChecked() else 1
            cb = {
                0:
                '=CURRENT_DATE()',
                1: (datetime.date.today() -
                    relativedelta(months=1)).strftime(">='%Y-%m-%d'"),
                2: (datetime.date.today() -
                    relativedelta(years=1)).strftime(">='%Y-%m-%d'"),
                3:
                '=fOrderDate'
            }
            sql = self.DefauleParaSQL.format(ch1, ch2,
                                             cb[self.comboBox.currentIndex()])
            info = JPTabelFieldInfo(sql)
            self.model = self.getModelClass()(self.tableView, info)
            self.tableView.setModel(self.model)
            self.tableView.resizeColumnsToContents()

    @QtCore.pyqtSlot()
    def on_CMDEXPORTTOEXCEL_clicked(self):
        print("CMDEXPORTTOEXCEL 请重新写")

    @QtCore.pyqtSlot()
    def on_CMDSEARCH_clicked(self):
        print("CMDSEARCH 请重新写")

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QtWidgets.QPushButton(item[0])
            btn.setObjectName(item[2].upper())
            icon = QIcon()
            icon.addPixmap(QPixmap(getcwd() + "\\res\\ico\\" + item[1]),
                           QIcon.Normal, QIcon.Off)
            btn.setIcon(icon)
            self.horizontalLayout_Button.addWidget(btn)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_FuncFullPath.setText(_translate("Form", "Function Path"))
        self.label_2.setText(_translate("Form", "Filter:"))
        self.checkBox_1.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))


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
    year = getDataListAndFields('''select year(fOrderDate) as y  
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


def showEditForm_Order(MainForm, edit_mode, PKValue=None):
    from Ui.Ui_FormOrderMob import Ui_Form
    pb = JPPub()
    Form = QDialog(MainForm)
    Form.setWindowModality(Qt.WindowModal)
    ui = Ui_Form()
    ui.setupUi(Form)
    curPK = PKValue
    m_sql = """
            SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                , fPayable, fDesconto, fNote
            FROM t_order
            WHERE fOrderID = '{}'
            """.format(curPK)
    s_sql = """
            SELECT fID, fOrderID, fQuant AS '数量Qtd', 
                fProductName AS '名称Descrição', 
                fLength AS '长Larg.', fWidth AS '宽Comp.', 
                fPrice AS '单价P. Unitario', fAmount AS '金额Total'
            FROM t_order_detail
            WHERE fOrderID = '{}'    
            """.format(curPK)

    # 继承模型，为了设置重载方法，必要要时也可以用动态绑定到函数
    class myMainMode(JPFormModelMainSub):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def subModel_AfterSetDataBeforeInsterRowEvent(self, row_data, Index):
            if row_data is None:
                return False
            if row_data[7] is None:
                return False
            data = row_data
            if data[7] == 0:
                return False
            lt = [data[2], data[4], data[5], data[6], data[7]]
            lt = [float(str(i)) if i else 0 for i in lt]
            return int(lt[4] * 100) == int(
                reduce(lambda x, y: x * y, lt[0:4]) * 100)

    tv = ui.tableView
    MF = myMainMode(Form, tv)
    MF.setUi(ui)
    MF_S = MF.subModel
    MF_M = MF.mainModel
    MF_M.setFieldsRowSource([('fCustomerID', pb.getCustomerList()),
                             ('fVendedorID', pb.getEnumList(10))])
    MF_M.setTabelInfo(m_sql, 1)
    MF_S.setColumnsHidden(0, 1)
    MF_S.setColumnWidths(0, 0, 60, 300, 100, 100, 100, 100)
    MF_S.setColumnsReadOnly(7)
    MF_S.setTabelInfo(s_sql)
    MF_S.setFormula(
        7,
        "JPRound(JPRound({2}) * JPRound({4}) * JPRound({5}) * JPRound({6}))")

    def butSave():
        try:
            MF.subModel.GetSQLS()
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()

    def cusChange(r):
        obj = ui.fCustomerID
        row = obj.RowSource[r]
        ui.fNUIT.setText(row[2])
        ui.fCity.setText(row[3])

    def Cacu(*args):
        M = MF.mainModel
        v_sum = MF.subModel._model.getColumnSum(7)
        fDesconto = M.getObjectValue("fDesconto")
        fTax = (v_sum - fDesconto) * 0.17
        fPayable = v_sum - fDesconto + fTax
        M.setObjectValue('fAmount', v_sum)
        M.setObjectValue("fTax", fTax)
        M.setObjectValue("fPayable", fPayable)

    ui.fCustomerID.currentIndexChanged.connect(cusChange)
    ui.butSave.clicked.connect(butSave)
    MF.dataChanged[QModelIndex].connect(Cacu)
    MF.dataChanged[QWidget].connect(Cacu)

    MF.show(edit_mode)


class FuncForm_Order(FunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_1 = """
                SELECT fOrderID as 订单号码OrderID,
                        fOrderDate as 日期OrderDate,
                        fCustomerName as 客户名Cliente,
                        fCity as 城市City,
                        fSubmited1 as 提交Submited,
                        fSubmit_Name as 提交人Submitter,
                        fAmount as 金额SubTotal,
                        fRequiredDeliveryDate as 交货日期RDD,
                        fDesconto as 折扣Desconto,
                        fTax as 税金IVA,
                        fPayable as `应付金额Valor a Pagar`,
                        fContato as 联系人Contato,
                        fCelular as 手机Celular,
                        cast(fSubmited as SIGNED) AS fSubmited
                FROM v_order AS o
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                        AND (fSubmited={}
                        OR fSubmited={})
                        AND fOrderDate{}
                ORDER BY  forderID DESC"""
        sql_2 = """
                SELECT fOrderID as 订单号码OrderID,
                        fOrderDate as 日期OrderDate,
                        fCustomerName as 客户名Cliente,
                        fCity as 城市City,
                        fSubmited1 as 提交Submited,
                        fSubmit_Name as 提交人Submitter,
                        fAmount as 金额SubTotal,
                        fRequiredDeliveryDate as 交货日期RDD,
                        fDesconto as 折扣Desconto,
                        fTax as 税金IVA,
                        fPayable as `应付金额Valor a Pagar`,
                        fContato as 联系人Contato,
                        fCelular as 手机Celular,
                        cast(fSubmited as SIGNED) AS fSubmited
                FROM v_order AS o
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                ORDER BY  forderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('UnSubmited')
        self.checkBox_2.setText('Submited')
        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(False)
        super().setSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)

    def but_click(self, name):
        for n, fun in FuncForm_Order.__dict__.items():
            if n.upper() == 'BTN{}CLICKED'.format(name.upper()):
                fun(self)

    def getCurrentCustomerID(self):
        index = self.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.model.TabelFieldInfo.Data[index.row()][0]

    @QtCore.pyqtSlot()
    def on_CMDEXPORTTOEXCEL_clicked(self):
        print('单击了CMDEXPORTTOEXCEL按钮')

    @QtCore.pyqtSlot()
    def on_CMDNEW_clicked(self):
        print("CMDNEW被下")
        showEditForm_Order(self.MainForm, JPFormModelMainSub.New)

    @QtCore.pyqtSlot()
    def on_CMDBROWSE_clicked(self):
        cu_id = self.getCurrentCustomerID()
        if not cu_id:
            return
        showEditForm_Order(self.MainForm, JPFormModelMainSub.ReadOnly, cu_id)
        print("CMDBROWSE被下")


def getFuncForm_Enum(mainform):
    from Ui.Ui_FormEnum import Ui_Form
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    mainform.addForm(Form)


def getFuncForm_FormReceivables(mainform):
    from Ui.Ui_FormReceivables import Ui_Form
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    mainform.addForm(Form)


def getStackedWidget(mainForm, sysnavigationmenus_data):
    pub = JPPub()
    menus = pub.getSysNavigationMenusDict()
    menu_id = sysnavigationmenus_data['fNMID']
    buts = [[m['fMenuText'], m['fIcon'], m['fObjectName']] for m in menus
            if m['fParentId'] == menu_id and m['fIsCommandButton']]
    widget = None
    if menu_id == 2:  # Order
        widget = FuncForm_Order(mainForm)
        widget.addButtons(buts)
    elif menu_id == 22:  #Report_day
        getFuncForm_FormReport_Day(mainForm)
    elif menu_id == 10:
        getFuncForm_Enum(mainForm)
    elif menu_id == 20:
        getFuncForm_FormReceivables(mainForm)
    return
