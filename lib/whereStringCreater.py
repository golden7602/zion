# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.getcwd())
from PyQt5.QtWidgets import (QPushButton, QDialog, QHeaderView,
                             QComboBox, QTabWidget, QStyledItemDelegate,
                             QApplication, QWidget)
from lib.Ui_WhereStringCreater import Ui_DlgSearch
from lib.JPDatabase.Field import JPFieldInfo, JPFieldType
from lib.JPMvc import JPDelegate


class _JPWhereStringCreater(Ui_DlgSearch):
    """本类是查询条件生成窗口的处理类"""
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

    def __init__(self, fields, MainForm):
        self.ui = Ui_DlgSearch()
        self.Dlg = QDialog()
        self.ui.setupUi(self.Dlg)
        self.tab = self.ui.tableWidget
        self.tab.setRowCount(1)
        # 取得所有字段信息
        self.list_fld = [[fld.Title, fld.FieldName, fld.TypeCode]
                         for fld in fields]

        self.de_boo = JPDelegate.JPDelegate_ComboBox(
            self.tab, [['And', 'And'], ['Or', 'Or'], ['Not', 'Not']])

        self.de_fld = JPDelegate.JPDelegate_ComboBox(self.tab, self.list_fld)

        self.de_kh_left = JPDelegate.JPDelegate_ComboBox(
            self.tab, [['(', '(']])

        self.de_kh_right = JPDelegate.JPDelegate_ComboBox(
            self.tab, [[')', ')']])

        self.de_date = JPDelegate.JPDelegate_DateEdit(self.tab)

        self.de_int = JPDelegate.JPDelegate_LineEdit(self.tab, 1)

        self.de_float = JPDelegate.JPDelegate_LineEdit(self.tab, 2)

        self.de_no = JPDelegate.JPDelegate_ReadOnly(self.tab)

        self.tab.setColumnWidth(0, 50)
        self.tab.setColumnWidth(1, 20)
        self.tab.setColumnWidth(2, 200)
        self.tab.setColumnWidth(3, 100)
        self.tab.setColumnWidth(4, 150)
        self.tab.setColumnWidth(5, 150)
        self.tab.setColumnWidth(6, 20)

        self.tab.setItemDelegate(self.de_no)
        self.tab.setItemDelegateForColumn(1, self.de_kh_left)
        self.tab.setItemDelegateForColumn(2, self.de_fld)
        self.tab.setItemDelegateForColumn(6, self.de_kh_right)

        self.tab.currentCellChanged.connect(self.cell_change)

    def getFieldType(self, FieldName):
        if FieldName:
            return [r[2] for r in self.list_fld if r[0] == FieldName]

    def cell_change(self, x1, y1, x2, y2):
        if y2 == 2:
            print(self.getFieldType(self.tab.item(x1, y2).text()))
        return
        if x1 == 0 and y1 == 0:
            self.tab.setItemDelegate(self.de_no)
        elif y1 == 1:
            self.tab.setItemDelegate(self.de_fld)
        print(x1, y1, x2, y2)
        # self.btnAddNew = QPushButton("+")
        # self.btnAddNew.clicked.connect(self.btnAddNewClick)
        # self.tab.setCellWidget(0, 7, self.btnAddNew)
        # self.Dlg.accepted.connect(self.createWhereString)
        # self.FieldList = []
        # self.FieldType = []
        # for i in range(0, len(tableWidget.FieldDict)):
        #     self.FieldList.append(tableWidget.FieldDict[i].name)
        #     self.FieldType.append(tableWidget.FieldDict[i].type_code)
        # self.comboBoxField = QComboBox()
        # self.comboBoxField.addItems(self.FieldList)
        # self.comboBoxField.setFixedWidth(True)
        # self.tab.setCellWidget(0, 6, self.comboBoxField)

    def createWhereString(self):
        pass

    def show(self):
        #self.Dlg.setModal(True)
        self.Dlg.show()

    def btnAddNewClick(self):
        row = self.tab.rowCount() + 1
        self.tab.setRowCount(row)
        self.tab.setCellWidget(row - 1, 7, self.btnAddNew)


# class _JPDelegate_Base(QStyledItemDelegate):
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)

#     #@abc.abstractmethod
#     def createEditor(self, parent: QWidget, option: QStyleOptionViewItem,
#                      index: QModelIndex) -> QWidget:
#         pass

#     #@abc.abstractmethod
#     def setEditorData(self, editor: QWidget, index: QModelIndex):
#         pass

#     #@abc.abstractmethod
#     def setModelData(self, editor: QWidget, model: QAbstractItemModel,
#                      index: QModelIndex):
#         pass

#     def updateEditorGeometry(self, editor: QWidget,
#                              StyleOptionViewItem: QStyleOptionViewItem,
#                              index: QModelIndex):
#         editor.setGeometry(StyleOptionViewItem.rect)

if __name__ == "__main__":
    import sys
    from lib.JPDatabase.Query import JPQueryFieldInfo
    from lib.JPDatabase.Database import JPDb
    db = JPDb()
    db.setDatabaseType(1)
    app = QApplication(sys.argv)
    SQL = """select fID,fOrderID,fQuant as '数量Qtd',
            fProductName as '名称Descrição',fLength as '长Comp.',
            fWidth as '宽Larg.',fPrice as '单价P. Unitario',
            fAmount as '金额Total' from t_order_detail limit 0"""
    Qi = JPQueryFieldInfo(SQL)
    dlg = _JPWhereStringCreater(Qi.Fields, app)
    dlg.show()
    sys.exit(app.exec_())
