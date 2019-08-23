import abc
import datetime
import re
from decimal import Decimal
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())
from PyQt5.QtCore import (QDate, QAbstractItemModel, QModelIndex, QObject, Qt,
                          QVariant, pyqtSignal, pyqtSlot)
from PyQt5.QtWidgets import (QAbstractItemView, QComboBox, QDateEdit, QDialog,
                             QLineEdit, QMenu, QMessageBox, QPushButton,
                             QStyledItemDelegate, QStyleOptionViewItem,
                             QTableView, QWidget, QApplication)

import lib.JPMvc.JPDelegate as myDe
from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Field import JPFieldType
from lib.JPDatabase.Query import (JPQueryFieldInfo, JPTabelFieldInfo,
                                  JPTabelRowData)
from lib.JPException import JPExceptionFieldNull, JPExceptionRowDataNull
from lib.JPMvc.JPModel import (JPTableViewModelEditForm,
                               JPTableViewModelReadOnly)
from lib.JPPrintReport import JPReport
from lib.ZionPublc import JPPub
from Ui.Ui_FormSearch import Ui_DlgSearch

jppath.append(getcwd())

# class myJPTabelFieldInfo(JPTabelFieldInfo):
#     def __init__(self, sql, noData=False):
#         super().__init__(sql, noData=noData)

#     def addRow(self):
#         newRow = [None, None, None, None, None, None, None]
#         newRow._state = JPTabelRowData.New_None
#         self.DataRows.append(newRow)


class myJPTableViewModelEditForm(JPTableViewModelEditForm):
    def __init__(self, tableView, tabelFieldInfo):
        super().__init__(tableView, tabelFieldInfo)

    def clear456(self, r):
        # 只要修改了字段，清除后三项并禁止编辑
        de = myDe.JPDelegate_ReadOnly(self.tableView)
        self.tableView.setItemDelegateForColumn(4, de)
        self.tableView.setItemDelegateForColumn(5, de)
        self.tableView.setItemDelegateForColumn(6, de)
        self.setData(self.createIndex(r, 4), None)
        self.setData(self.createIndex(r, 5), None)
        self.setData(self.createIndex(r, 6), None)
        # self.TabelFieldInfo.DataRows[r].setData(4, None)
        # self.TabelFieldInfo.DataRows[r].setData(5, None)
        # self.TabelFieldInfo.DataRows[r].setData(6, None)
        # self.dataChanged.emit()

    def data(self, index, role=Qt.DisplayRole):
        c = index.column()
        r = index.row()
        if role == Qt.DisplayRole and c == 3:
            cell = self.TabelFieldInfo.DataRows[r].Datas[c]
            if cell is None:
                return None
            else:
                result = cell[1][0]
                return result
        elif role == Qt.DisplayRole and c == 4:
            cell = self.TabelFieldInfo.DataRows[r].Datas[c]
            if cell is None:
                return None
            else:
                result = cell[1]["TiC"] + cell[1]["Tie"]
                return result
        else:
            return super().data(index, role=role)


class JDFieldComboBox(QStyledItemDelegate):
    def __init__(self, tab, parent: QObject = None):
        super().__init__(parent)
        self.tableView = parent
        self.tab = tab

    def setDialog(self, dlg):
        self.Dialog = dlg

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem,
                     index: QModelIndex) -> QWidget:

        list_fld = [[fld.Title, fld.FieldName, fld.TypeCode]
                    for fld in self.tab.Fields]
        wdgt = QComboBox(parent)
        for i, row in enumerate(list_fld):
            wdgt.addItem(row[0], (i, row))
        return wdgt

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        data = index.model().data(index, Qt.EditRole)
        if data is None:
            editor.setCurrentIndex(-1)
        else:
            editor.setCurrentIndex(data[0])
            return

    def setModelData(self, editor: QWidget, model: QAbstractItemModel,
                     index: QModelIndex):
        data = editor.currentData()
        index.model().setData(index, data, Qt.EditRole)
        model.clear456(index.row())
        self.Dialog.fieldChange(index, data)

    def updateEditorGeometry(self, editor: QWidget,
                             StyleOptionViewItem: QStyleOptionViewItem,
                             index: QModelIndex):
        editor.setGeometry(StyleOptionViewItem.rect)


class mySYCombobox(QStyledItemDelegate):
    SY_CHAR = (
        {
            "Sy": "`{0}` like '%{1}%'",
            "En1": 1,
            "En2": 0,
            "TiC": "包含",
            "Tie": "Include"
        },
        {
            "Sy": "`{0}`='{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "等于",
            "Tie": "Equal"
        },
        {
            "Sy": "`{0}`>'{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "大于",
            "Tie": "GreaterThan"
        },
        {
            "Sy": "`{0}`>='{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "大于或等于",
            "Tie": "GreaterOrEqual"
        },
        {
            "Sy": "`{0}`<'{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "小于",
            "Tie": "LessThan"
        },
        {
            "Sy": "`{0}`<='{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "小于或等于",
            "Tie": "LessOrEqual"
        },
        {
            "Sy": "`{0}`<>'{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "不等于",
            "Tie": "NotEqual"
        },
        {
            "Sy": "`{0}` like '{1}%'",
            "En1": 1,
            "En2": 0,
            "TiC": "开头是",
            "Tie": "BeginLike"
        },
        {
            "Sy": "Not `{0}` like '{1}%'",
            "En1": 1,
            "En2": 0,
            "TiC": "开头不是",
            "Tie": "NotBeginLike"
        },
        {
            "Sy": "`{0}` like '%{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "结束是",
            "Tie": "EndLike"
        },
        {
            "Sy": "Not `{0}` like '%{1}'",
            "En1": 1,
            "En2": 0,
            "TiC": "结束不是",
            "Tie": "NotEndLike"
        },
        {
            "Sy": "IsNull(`{0}`)",
            "En1": 0,
            "En2": 0,
            "TiC": "为空",
            "Tie": "IsNull"
        },
        {
            "Sy": "Not IsNull(`{0}`)",
            "En1": 0,
            "En2": 0,
            "TiC": "不为空",
            "Tie": "NotNull"
        },
        #Ext
        {
            "Sy": "LENGTH(`{0}`)={1}",
            "En1": 1,
            "En2": 0,
            "TiC": "长度为",
            "Tie": "LengthIs"
        },
        {
            "Sy": "LENGTH(`{0}`)>={1}",
            "En1": 1,
            "En2": 0,
            "TiC": "长度大于等于",
            "Tie": "LengthGreaterOrEqual"
        },
        {
            "Sy": "LENGTH(`{0}`)<={1}",
            "En1": 1,
            "En2": 0,
            "TiC": "长度小于等于",
            "Tie": "LengthLessOrEqual"
        },
        {
            "Sy": "LENGTH(`{0}`)>{1}",
            "En1": 1,
            "En2": 0,
            "TiC": "长度大于",
            "Tie": "LengthGreaterThan"
        },
        {
            "Sy": "LENGTH(`{0}`)<{1}",
            "En1": 1,
            "En2": 0,
            "TiC": "长度小于",
            "Tie": "LengthLessThan"
        },
        {
            "Sy": "`{0}`=''",
            "En1": 0,
            "En2": 0,
            "TiC": "为空字符",
            "Tie": "IsEmptyString"
        })
    SY_BOOL = ({
        "Sy": "`{0}`=1",
        "En1": 0,
        "En2": 0,
        "TiC": "值为是",
        "Tie": "IsTrue"
    }, {
        "Sy": "`{0}`=0",
        "En1": 0,
        "En2": 0,
        "TiC": "值为否",
        "Tie": "ISFalse"
    }, {
        "Sy": "IsNull(`{0}`)",
        "En1": 0,
        "En2": 0,
        "TiC": "为空",
        "Tie": "IsNull"
    }, {
        "Sy": "Not IsNull(`{0}`)",
        "En1": 0,
        "En2": 0,
        "TiC": "不为空",
        "Tie": "NotNull"
    })
    SY_DATE = ({
        "Sy": "`{0}`<'{1}'",
        "En1": 1,
        "En2": 0,
        "TiC": "早于",
        "Tie": "EarluThan"
    }, {
        "Sy": "`{0}`<='{1}'",
        "En1": 1,
        "En2": 0,
        "TiC": "早于等于",
        "Tie": "EarlyOrEqual"
    }, {
        "Sy": "`{0}`>'{1}'",
        "En1": 1,
        "En2": 0,
        "TiC": "晚于",
        "Tie": "LaterThan"
    }, {
        "Sy": "`{0}`>='{1}'",
        "En1": 1,
        "En2": 0,
        "TiC": "晚于等于",
        "Tie": "LaterOrEqual"
    }, {
        "Sy": "`{0}`<>'{1}'",
        "En1": 1,
        "En2": 0,
        "TiC": "不等于",
        "Tie": "NotEqual"
    }, {
        "Sy": "`{0}` Between '{1}' And '{2}'",
        "En1": 1,
        "En2": 1,
        "TiC": "在区间内",
        "Tie": "Between"
    }, {
        "Sy": "Not (`{0}` Between '{1}' And '{2}')",
        "En1": 1,
        "En2": 1,
        "TiC": "不在区间内",
        "Tie": "NotBetween"
    }, {
        "Sy": "IsNull(`{0}`)",
        "En1": 0,
        "En2": 0,
        "TiC": "为空",
        "Tie": "IsNull"
    }, {
        "Sy": "Not IsNull(`{0}`)",
        "En1": 0,
        "En2": 0,
        "TiC": "不为空",
        "Tie": "NotNull"
    })
    SY_NUM = ({
        "Sy": "`{0}`={1}",
        "En1": 1,
        "En2": 0,
        "TiC": "等于",
        "Tie": "Equal"
    }, {
        "Sy": "`{0}`>{1}",
        "En1": 1,
        "En2": 0,
        "TiC": "大于",
        "Tie": "GreaterThan"
    }, {
        "Sy": "`{0}`>={1}",
        "En1": 1,
        "En2": 0,
        "TiC": "大于或等于",
        "Tie": "GreaterOrEqual"
    }, {
        "Sy": "`{0}`<{1}",
        "En1": 1,
        "En2": 0,
        "TiC": "小于",
        "Tie": "LessThan"
    }, {
        "Sy": "`{0}`<={1}",
        "En1": 1,
        "En2": 0,
        "TiC": "小于或等于",
        "Tie": "LessOrEqual"
    }, {
        "Sy": "`{0}`<>{1}",
        "En1": 1,
        "En2": 0,
        "TiC": "不等于",
        "Tie": "NotEqual"
    }, {
        "Sy": "`{0}` Between {1} and {2}",
        "En1": 1,
        "En2": 1,
        "TiC": "在区间内",
        "Tie": "Between"
    }, {
        "Sy": "Not (`{0}` Between {1} and {2})",
        "En1": 1,
        "En2": 1,
        "TiC": "不在区间内",
        "Tie": "NotBetween"
    }, {
        "Sy": "IsNull(`{0}`)",
        "En1": 0,
        "En2": 0,
        "TiC": "为空",
        "Tie": "IsNull"
    }, {
        "Sy": "Not IsNull(`{0}`)",
        "En1": 0,
        "En2": 0,
        "TiC": "不为空",
        "Tie": "NotNull"
    })
    SY = {
        JPFieldType.String: SY_CHAR,
        JPFieldType.Int: SY_NUM,
        JPFieldType.Float: SY_NUM,
        JPFieldType.Boolean: SY_BOOL,
        JPFieldType.Date: SY_DATE
    }

    def __init__(self, typecode, parent=None):
        super().__init__(parent=parent)
        self.tup = self.SY[typecode]

    def setDialog(self, dlg):
        self.Dialog = dlg

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem,
                     index: QModelIndex) -> QWidget:
        wdgt = QComboBox(parent)
        for i, row in enumerate(self.tup):
            wdgt.addItem(row["TiC"] + row["Tie"], (i, row))
        return wdgt

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        data = index.model().data(index, Qt.EditRole)
        if data is None:
            editor.setCurrentIndex(-1)
        else:
            if data[0] > -1:
                editor.setCurrentIndex(data[0])
            return

    def setModelData(self, editor: QWidget, model: QAbstractItemModel,
                     index: QModelIndex):
        data = editor.currentData()
        index.model().setData(index, data, Qt.EditRole)
        self.Dialog.syChange(index, data)

    def updateEditorGeometry(self, editor: QWidget,
                             StyleOptionViewItem: QStyleOptionViewItem,
                             index: QModelIndex):
        editor.setGeometry(StyleOptionViewItem.rect)


class Form_Search(QDialog):
    def __init__(self, tabinfo, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.ui = Ui_DlgSearch()
        self.ui.setupUi(self)
        self.tv = self.ui.tableView

        sql = """
        SELECT fID,'' AS Guanxi, '' AS ZuoKuoHao, 
            '' AS Ziduan, '' AS YunSuan, '' AS Zhi1,
            '' AS Zhi2, '' AS YouKuoHao
        FROM sysconfig
        LIMIT 0
        """
        tab = JPTabelFieldInfo(sql, True)
        tab.Fields[0].Title = " "
        tab.Fields[1].Title = "关系"
        tab.Fields[2].Title = "("
        tab.Fields[3].Title = "字段Field"
        tab.Fields[4].Title = "运算Symbols"
        tab.Fields[5].Title = "值1 Value1"
        tab.Fields[6].Title = "值2 Value2"
        tab.Fields[7].Title = ")"
        self.tab = tab
        self.tab.addRow()

        self.Model = myJPTableViewModelEditForm(self.tv, self.tab)

        self.tv.setModel(self.Model)
        self.tv.setColumnWidth(0, 50)
        self.tv.setColumnWidth(1, 50)
        self.tv.setColumnWidth(2, 20)
        self.tv.setColumnWidth(3, 200)
        self.tv.setColumnWidth(4, 200)
        self.tv.setColumnWidth(5, 150)
        self.tv.setColumnWidth(6, 150)
        self.tv.setColumnWidth(7, 20)

        de_sy = myDe.JPDelegate_ComboBox(
            self.tv, [['And', 'And'], ['Or', 'Or'], ['Not', 'Not']])
        self.tv.setItemDelegateForColumn(1, de_sy)

        de_kh_left = myDe.JPDelegate_ComboBox(self.tv, [['(', '(']])
        self.tv.setItemDelegateForColumn(2, de_kh_left)
        de_kh_right = myDe.JPDelegate_ComboBox(self.tv, [[')', ')']])
        self.tv.setItemDelegateForColumn(7, de_kh_right)

        self.de_field = JDFieldComboBox(tabinfo)
        self.de_field.setDialog(self)
        self.tv.setItemDelegateForColumn(3, self.de_field)
        self.de_no = myDe.JPDelegate_ReadOnly(self.tv)
        self.tv.setItemDelegateForColumn(4, self.de_no)
        self.tv.setItemDelegateForColumn(5, self.de_no)
        self.tv.setItemDelegateForColumn(6, self.de_no)

    def fieldChange(self, index, data):

        print(data)
        tp = data[1][2]
        de = mySYCombobox(tp, self.tv)
        de.setDialog(self)
        self.tv.setItemDelegateForColumn(4, de)

    def syChange(self, index, data):
        de_bool = myDe.JPDelegate_ComboBox(self.tv, [['SIM', 1], ['Non', 0]])
        de_date = myDe.JPDelegate_DateEdit(self.tv)
        de_int = myDe.JPDelegate_LineEdit(self.tv, 1)
        de_float = myDe.JPDelegate_LineEdit(self.tv, 2)
        de_str = myDe.JPDelegate_LineEdit(self.tv)
        self.des = {
            JPFieldType.String: de_str,
            JPFieldType.Int: de_int,
            JPFieldType.Float: de_float,
            JPFieldType.Boolean: de_bool,
            JPFieldType.Date: de_date
        }
        if data:
            r= index.row()
            tp = self.tab.DataRows[r].Datas[3][1][2]
            dic = data[1]
            if dic["En1"]:
                self.tv.setItemDelegateForColumn(5, self.des[tp])
            if dic["En2"]:
                self.tv.setItemDelegateForColumn(6, self.des[tp])



if __name__ == "__main__":
    import sys
    db = JPDb()
    db.setDatabaseType(1)
    app = QApplication(sys.argv)
    sql_0 = """
                SELECT fOrderID as 订单号码OrderID,
                        fOrderDate as 日期OrderDate,
                        fCustomerName as 客户名Cliente,
                        fCity as 城市City,
                        fSubmited1 as 提交Submited,
                        fSubmit_Name as 提交人Submitter,
                        fRequiredDeliveryDate as 交货日期RequiredDeliveryDate,
                        fAmount as 金额SubTotal,
                        fDesconto as 折扣Desconto,
                        fTax as 税金IVA,
                        fPayable as `应付金额Valor a Pagar`,
                        fContato as 联系人Contato,
                        fCelular as 手机Celular,
                        fSubmited AS fSubmited,
                        fEntry_Name as 录入Entry
                FROM v_order AS o"""

    s = Form_Search(JPTabelFieldInfo(sql_0, True))
    s.exec_()

    db = JPDb()
    db.setDatabaseType(1)
    sql = "select '' as Guanxi,'' as ZuoKuoHao, '' as Ziduan, '' as YunSuan,'' as Zhi1,'' as Zhi2, '' as YouKuoHao,fID from sysconfig Limit 0 "
    tab = JPTabelFieldInfo(sql, True)
    del tab.Fields[0]
    a = 1
