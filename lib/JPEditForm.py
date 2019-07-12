# -*- coding: utf-8 -*-

from enum import IntEnum

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QLineEdit, QComboBox, QStyledItemDelegate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSignal, QModelIndex
from globalVar import pub
from JPValidator import JPValidator, JPDoubleValidator
from JPFunction import JPReadLineToTableWidgetItem, JPReadDataToWidget


class JPEditFormMode(IntEnum):
    """本类为编辑窗口类型的枚举"""
    Main = 1
    MainSub = 2


class JPEditFormDataMode(IntEnum):
    """本类为编辑窗口数据类型的枚举"""
    Edit = 1
    ReadOnly = 2
    New = 3


class JPDelegate(QStyledItemDelegate):
    """自定义委托
    参数一：归属于的QTableWidget控件
    参数二：委托的数据验证类型
        0: 禁止编辑  1: 字符串 2：整形 3：小数  4: 日期
        10: 参照字典，健为显示文本，值为文本对应的值
    """
    editNext = pyqtSignal(QModelIndex)

    def __init__(self, parent=None, validator_mode=0, select_value: dict = {}):
        self.parent = parent
        self.validator_mode = validator_mode
        self.select_value = select_value
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        md = self.validator_mode
        if md == 0:
            return
        if md == 1:
            return QLineEdit(parent)
        if md == 2:
            wdgt = QLineEdit(parent)
            wdgt.setValidator(QIntValidator())
            return wdgt
        if md == 3:
            wdgt = QLineEdit(parent)
            wdgt.setValidator(JPDoubleValidator(2))
            return wdgt
        if md == 10:
            wdgt = QComboBox(parent)
            wdgt.addItems(self.select_value.keys())
            return wdgt

    def setEditorData(self, editor, index):
        if self.validator_mode == 0: return
        value = index.model().data(index)
        if value:
            if self.validator_mode == 10:
                editor.setCurrentText(str(value))
            else:
                editor.setText(str(value))

    def setModelData(self, editor, model, index):
        md = self.validator_mode
        t = editor.text() if md < 10 else editor.currentText()
        item = self.parent.currentItem()
        fs = {
            1: ('{}', lambda x: x),
            2: ('{:,}', lambda x: int(x)),
            3: ('{:,.2f}', lambda x: float(x)),
            10: ('{}', lambda x: x)
        }
        model.setData(index, fs[md][0].format(fs[md][1](t)))
        item.__dict__["NewValue"] = t.replace(',', '') if md < 10 else t
        tmp = index.sibling(index.row(), index.column() + 1)
        if tmp.isValid():
            self.editNext.emit(tmp)


class JPEditForm(object):
    """编辑窗口处理类
    必备参数：
    可选初始化参数：SubForm,SubTabelName,SubFormFieldsName
    """
    pk_sql = "SELECT column_name as pkname FROM INFORMATION_SCHEMA.`KEY_COLUMN_USAGE` \
            WHERE table_name='{}' AND constraint_name='PRIMARY'"

    def __init__(self,
                 UI: object = None,
                 FormMode: JPEditFormMode = None,
                 MainForm: QWidget = None,
                 EditMode: JPEditFormDataMode = JPEditFormDataMode.ReadOnly,
                 MainTabelName: str = None,
                 ReadViewName: str = None,
                 AuToPkRoleID: str = None,
                 **kwargs):
        self.UI = UI
        self.FormMode = FormMode
        self.MainForm = MainForm
        self.EditMode = EditMode
        self.MainTabelName = MainTabelName
        self.ReadViewName = ReadViewName
        self.AuToPkRoleID = AuToPkRoleID
        if self.FormMode == JPEditFormMode.MainSub:
            self.SubForm = kwargs.get("SubForm")
            self.SubTabelName = kwargs.get("SubTabelName")
            self.SubFormFieldsName = kwargs.get("SubFormFieldsName")
        self.butSave = self.UI.butSave
        self.butPrint = self.UI.butPrint
        self.butPrint.clicked.connect(self.__Print)
        self.butSave.clicked.connect(self.__SaveDate)
        self.FeildsType = pub.GetFieldsTypeDict(ReadViewName)
        self.MainTabelPKName = pub.getDict(
            JPEditForm.pk_sql.format(MainTabelName))[0]['pkname']

    def Show(self, PK=None):
        if PK and (self.EditMode == JPEditFormDataMode.ReadOnly
                   or self.EditMode == JPEditFormDataMode.Edit):
            self.__ReadDataToForm(PK)
            self.CurrentPK = PK
            self.MainForm.show()

    def __ReadDataToForm(self, PK):
        base_sql = "select * from {} where {}='{}'"
        if PK is None:
            return

        # 读取主表
        tn = self.ReadViewName if self.ReadViewName else self.MainTabelName
        read_sql = base_sql.format(tn, self.MainTabelPKName, PK)
        sql_resule = pub.getDict(read_sql)[0].items()
        data = {k: v for k, v in sql_resule if k in self.UI.__dict__}
        for k, v in data.items():
            if not v: continue
            JPReadDataToWidget(self.UI.__dict__[k], self.FeildsType[k], v)

        # 读取子表
        read_sql = base_sql.format(self.SubTabelName, self.MainTabelPKName, PK)
        SubTabelFeildsType = pub.GetFieldsTypeDict(self.SubTabelName)
        if self.FormMode == JPEditFormMode.MainSub:
            data = pub.getDict(read_sql)
            for row, rowdata in enumerate(data):
                for col, fld_name in enumerate(self.SubFormFieldsName):
                    if rowdata[fld_name]:
                        JPReadLineToTableWidgetItem(
                            self.SubForm.item(row, col),
                            SubTabelFeildsType[fld_name], rowdata[fld_name])

    def __SaveDate(self):
        print("Save")

    def __Print(self):
        print("打印")
