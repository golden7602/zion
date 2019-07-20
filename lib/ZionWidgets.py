# -*- coding: utf-8 -*-

from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

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
