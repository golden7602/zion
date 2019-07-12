# -*- coding: utf-8 -*-

import abc
from collections import OrderedDict
import datetime
from enum import IntEnum

from PyQt5 import QtWidgets as QtWidgets_
from PyQt5.QtCore import QDate, QModelIndex, Qt, pyqtSignal
from PyQt5.QtGui import (QDoubleValidator, QIntValidator, QRegExpValidator,
                         QValidator)
from PyQt5.QtWidgets import QCheckBox as QCheckBox_
from PyQt5.QtWidgets import QComboBox as QComboBox_
from PyQt5.QtWidgets import QDateEdit as QDateEdit_
from PyQt5.QtWidgets import QLineEdit as QLineEdit_
from PyQt5.QtWidgets import QPushButton, QStyledItemDelegate
from PyQt5.QtWidgets import QTableWidget as QTableWidget_
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QTextEdit as QTextEdit_
from PyQt5.QtWidgets import QWidget as QWidget_

from JPDatebase import JPDb, JPFieldInfo
from JPFunction import JPBooleanString
from JPValidator import JPDoubleValidator, JPValidator


def __getattr__(name):
    return QtWidgets_.__dict__[name]


class JPExceptionFieldNull(Exception):
    def __init__(self, obj, msg=None):
        self.Message = obj if isinstance(obj,
                                         str) else "字段的【{}】值不能为空值！".format(msg)

    def __str__(self):
        return self.Message


# class __JPEditFormMode(IntEnum):
#     """本类为编辑窗口类型的枚举"""
#     Main = 1
#     MainSub = 2


class JPEditFormDataMode(IntEnum):
    """本类为编辑窗口数据类型的枚举"""
    Edit = 1
    ReadOnly = 2
    New = 3


class _JPDelegate_Base(object):
    editNext = pyqtSignal(QModelIndex)

    def getRealvalue(self, index):
        item = self.parent.item(index.row(), index.column())
        return item.RealValue

    def setRealValue(self, index, value):
        item = self.parent.item(index.row(), index.column())
        self.setItemOriginal(value,item)

    @abc.abstractmethod
    def createEditor(self, parent, option, index):
        pass

    @abc.abstractmethod
    def setEditorData(self, editor, index):
        pass

    #@classmethod
    def setModelData(self, editor, model, index):
        tb = self.parent
        tb.UpdateRowKeys.append(tb.item(index.row(), 0).text())
        self.setModelData_(editor, model, index)
        self.editNext.emit(index)

    @abc.abstractmethod
    def setModelData_(self, editor, model, index):
        pass

    @classmethod
    def getSqlValue(self, fldinfo: JPFieldInfo, item: QTableWidgetItem):
        if item.RealValue is None:
            if fldinfo.NullOK == True:
                return 'Null'
            else:
                raise JPExceptionFieldNull(
                    self, "字段的【{}】值不能为空值！".format(fldinfo.Name))
        return self.getSqlValue_(self, fldinfo, item)

    @abc.abstractmethod
    def getSqlValue_(self, item: QTableWidgetItem) -> str:
        pass

    @abc.abstractmethod
    def setItemOriginal(self, value, item: QTableWidgetItem):
        pass


class JPDelegate_NoEdit(QStyledItemDelegate, _JPDelegate_Base):
    def createEditor(self, parent, option, index):
        return

    def setEditorData(self, editor, index):
        return

    def setModelData_(self, editor, model, index):
        return

    def getSqlValue_(self, fldinfo: JPFieldInfo,
                     item: QTableWidgetItem) -> str:
        return "'{}'".format(item.RealValue)

    def setItemOriginal(self, value, item: QTableWidgetItem):
        item.setText(value)

    def getRealValue(self, item: QTableWidgetItem):
        return item.RealValue


class JPDelegate_Text(QStyledItemDelegate, _JPDelegate_Base):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        return QLineEdit(parent)

    def setEditorData(self, editor, index):
        editor.setText(self.getRealvalue(index))

    def setModelData_(self, editor, model, index):
        t = editor.text()
        model.setData(index, t if t else None)
        self.setRealValue(index, t)

    def getSqlValue_(self, fldinfo: JPFieldInfo,
                     item: QTableWidgetItem) -> str:
        return "'{}'".format(item.RealValue)

    def setItemOriginal(self, value, item: QTableWidgetItem):
        item.setText(value)
        item.RealValue = value


class JPDelegate_Int(QStyledItemDelegate, _JPDelegate_Base):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        #print("int createEditor 行={},列={}".format(index.row(), index.column()))
        wdgt = QLineEdit(parent)
        wdgt.setValidator(QIntValidator())
        return wdgt

    def setEditorData(self, editor, index):

        v=self.getRealvalue(index)
        #print("int setEditorData在 行={},列={} Value={}".format(
        #    index.row(), index.column(), v))
        if v:
            editor.setText('{:,}'.format(v))

    def setModelData_(self, editor, model, index):
        value = editor.text()
        #print("int setModelData_ 行={},列={} Value={}".format(
        #    index.row(), index.column(), value))
        model.setData(
            index,
            '{:,}'.format(int(str(value).replace(',', ''))) if value else None)
        self.setRealValue(index, int(str(value).replace(',', '')))

    def getSqlValue_(self, fldinfo: JPFieldInfo,
                     item: QTableWidgetItem) -> str:
        return "'{}'".format(item.RealValue)

    def setItemOriginal(self, value, item: QTableWidgetItem):
        item.setText('{:,}'.format(int(str(value).replace(',', ''))))
        item.RealValue = value


class JPDelegate_Float(QStyledItemDelegate, _JPDelegate_Base):
    def __init__(self, parent=None, decimal=2):
        self.parent = parent
        self.__Decimal = decimal
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        #print("float createEditor 行={},列={}".format(index.row(), index.column()))
        wdgt = QLineEdit(parent)
        wdgt.setValidator(JPDoubleValidator(self.__Decimal))
        return wdgt

    def setEditorData(self, editor, index):
        v=self.getRealvalue(index)
        #print("float setEditorData在 行={},列={} Value={}".format(
        #            index.row(), index.column(), v))
        if v:
            editor.setText('{:,.2f}'.format(
                float(str(v).replace(',', ''))))

    def setModelData_(self, editor, model, index):
        t = editor.text()
        #print("int setModelData_ 行={},列={} Value={}".format(
        #    index.row(), index.column(), t))
        model.setData(
            index,
            '{:,.2f}'.format(float(str(t).replace(',', ''))) if t else None)
        self.setRealValue(index, float(str(t).replace(',', '')))

    def getSqlValue_(self, fldinfo: JPFieldInfo,
                     item: QTableWidgetItem) -> str:
        return "'{}'".format(item.RealValue)

    def setItemOriginal(self, value, item: QTableWidgetItem):
        item.setText('{:,.2f}'.format(float(str(value).replace(',', ''))))
        item.RealValue = value


class JPDelegate_Date(QStyledItemDelegate, _JPDelegate_Base):
    def __init__(self, parent=None):
        self.parent = parent
        self.__FormatString = "yyyy-MM-dd"
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        return QDateEdit(parent)

    def setEditorData(self, editor, index):
        v=self.getRealvalue(index)
        if v:
            editor.setDate(QDate(rv.year, rv.month, rv.day))

    def setModelData_(self, editor, model, index):
        d = editor.date()
        model.setData(index, d.toString(self.__FormatString))
        self.setRealValue(index,
                               datetime.date(d.year(), d.month(), d.day()))

    def getSqlValue_(self, fldinfo: JPFieldInfo,
                     item: QTableWidgetItem) -> str:
        return item.RealValue.strftime("'%Y-%m-%d'")

    def setItemOriginal(self, value, item: QTableWidgetItem):
        item.RealValue = value
        if value is None:
            item.setText('')
        item.setText(value.strftime("%Y-%m-%d"))


class JPDelegate_Boolean(QStyledItemDelegate, _JPDelegate_Base):
    def __init__(self, parent=None):
        self.parent = parent
        b = JPBooleanString()
        self.__boolstr = b.getBooleanString()
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        wdgt = QComboBox(parent)
        wdgt.addItems(self.__boolstr)
        return wdgt

    def setEditorData(self, editor, index):
        value = self.getRealvalue(index)
        if value is None:
            return
        elif value is True or value == self.__boolstr[1]:
            editor.setCheckState(Qt.Checked)
        elif value is False or value == self.__boolstr[0]:
            editor.setCheckState(Qt.unChecked)

    def setModelData_(self, editor, model, index):
        t = QComboBox.currentText()
        model.setData(index, t if t else None)
        self.setRealValue(index,
                               None if t is None else editor.currentIndex)

    def getSqlValue_(self, fldinfo: JPFieldInfo,
                     item: QTableWidgetItem) -> str:
        return "'{}'".format(item.RealValue)

    def setItemOriginal(self, value, item: QTableWidgetItem):
        item.RealValue = value
        if value is None:
            item.setText('')
        item.setText(self.__boolstr[1 if value else 0])


class JPDelegate_ComboBox(QStyledItemDelegate, _JPDelegate_Base):
    def __init__(self,
                 parent=None,
                 rowList: list = [],
                 Binding_column: int = 0):
        self.parent = parent
        self.__RowList = rowList
        self.Binding_column = Binding_column
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        wdgt = QComboBox(parent, self.rowList, self.Binding_column)
        wdgt.setRowDict(self.__RowList)
        return wdgt

    def setEditorData(self, editor, index):
        v=self.getRealvalue(index)
        if v:
            editor.setEnumValue(self.getRealvalue)

    def setModelData_(self, editor, model, index):
        t = editor.currentData()
        tmp = index.sibling(index.row(), index.column())
        model.setData(index, t if editor.currentText() else None)
        self.setRealValue(index, editor.getEnumValue())

    def getSqlValue_(self, fldinfo: JPFieldInfo,
                     item: QTableWidgetItem) -> str:
        return "'{}'".format(item.RealValue)

    def setItemOriginal(self, value, item: QTableWidgetItem):
        item.RealValue = value
        if value is None:
            return
        for i, data in enumerate(self.__RowList):
            if value == data[self.Binding_column]:
                item.setText(str(data[0]))
                return


class _JPWidgetBase(object):
    def __init__(self, *args):
        self.FieldInfo: JPFieldInfo = None

    @classmethod
    def getNullValue(self):
        if self.FieldInfo.NullOK:
            return 'Null'
        else:
            raise JPExceptionFieldNull(
                self, "字段的【{}】值不能为空值！".format(self.FieldInfo.Name))

    @abc.abstractmethod
    def getSqlValue(self):
        """返回字段值，可直接用于SQL语句中"""

    @abc.abstractmethod
    def setFieldInfo(self, fld: JPFieldInfo):
        """设置字段信息"""


class QLineEdit(QLineEdit_, _JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)

    def getSqlValue(self) -> str:
        t = self.text()
        if t is None or len(t) == 0:
            return self.getNullValue()
        else:
            return "'{}'".format(t.replace(',', ''))

    def setFieldInfo(self, fld: JPFieldInfo):
        db = JPDb()
        self.FieldInfo = fld
        if self.FieldInfo.Value is None:
            return
        if self.FieldInfo.TypeCode in db.getIntTypeCode():
            self.setText('{:,}'.format(self.FieldInfo.Value))
            return
        if self.FieldInfo.TypeCode in db.getFloatTypeCode():
            self.setText('{:,.2f}'.format(self.FieldInfo.Value))
            return
        self.setText(fld.Value)

    def focusOutEvent(self, e):
        if isinstance(self.parent, QTableWidget):
            db = JPDb()
            try:
                if self.FieldInfo.TypeCode in db.getIntTypeCode():
                    self.setText('{:,}'.format(self.FieldInfo.Value))
                    return
                if self.FieldInfo.TypeCode in db.getFloatTypeCode():
                    self.setText('{:,.2f}'.format(self.FieldInfo.Value))
                    return
            except AttributeError as err:
                print(err)
        QLineEdit_.focusOutEvent(self, e)


class QTextEdit(QTextEdit_, _JPWidgetBase):
    def getSqlValue(self) -> str:
        t = self.text()
        if t is None or len(t) == 0:
            return self.getNullValue()
        return t

    def setFieldInfo(self, fld: JPFieldInfo):
        self.FieldInfo = fld
        self.setText(fld.Value)


class QComboBox(QComboBox_, _JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.__RowList = None
        self.BindingColumn = 0

    def setRowDict(self, value: list, Binding_column: int = 0):
        """value为一个行，行可为可为列表或元组
        列表或元组第一列为显示值，其后为其他需要返回的值
        Binding_column为返回值对应的列，从0开始。
        默认情况下，返回值就是列表显示文本（第0列）
        """
        self.__RowList = value
        self.BindingColumn = Binding_column
        for row in self.__RowList:
            self.addItem(str(row[0]), row)

    def getSqlValue(self) -> str:
        if self.__RowList is None:
            raise JPExceptionFieldNull("字段【{}】的枚举数据源不能为空！".format(
                self.FieldInfo.Name))
        if self.currentData():
            return "'{}'".format(self.currentData()[self.BindingColumn])
        else:
            return self.getNullValue()

    def getEnumValue(self):
        if self.currentData():
            return self.currentData()[self.BindingColumn]

    def setEnumValue(self, value):
        if value is None:
            return
        for i, row in enumerate(self.__RowList):
            if row[self.BindingColumn] == value:
                self.setCurrentIndex = i
                return

    def setFieldInfo(self, fld: JPFieldInfo):
        self.FieldInfo = fld
        if self.__RowList is None:
            return
        self.setEnumValue(fld.Value)


class QDateEdit(QDateEdit_, _JPWidgetBase):
    def __init__(self, parent):
        super().__init__(QDate.currentDate(), parent)

    def getSqlValue(self) -> str:
        t = self.date()
        if t == QDate():
            return self.getNullValue()
        else:
            return "'{}'".format(t.toString('yyyy-MM-dd'))

    def setFieldInfo(self, fld: JPFieldInfo):
        self.FieldInfo = fld
        if self.FieldInfo.Value is None:
            return
        d = self.FieldInfo.Value
        if self.FieldInfo.Value is None:
            self.setDate(QDate())
            return
        if isinstance(self.FieldInfo.Value,
                      (datetime.date, datetime.datetime)):
            self.setDate(QDate(d.year, d.month, d.day))
        else:
            self.setDate(QDate())


class QCheckBox(QCheckBox_, _JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.FieldInfo: JPFieldInfo = None

    def getSqlValue(self) -> str:
        if self.checkState() is None:
            return 'Null'
        return '1' if self.checkState() is True else '0'

    def setFieldInfo(self, fld: JPFieldInfo):
        self.FieldInfo = fld
        if self.FieldInfo.Value is None:
            return
        self.setChecked(self.FieldInfo.Value)


class JPTableWidgetItem(QTableWidgetItem):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

    def getSqlValue(self) -> str:
        t = super.text()
        if t is None or len(t) == 0:
            return self.getNullValue()
        else:
            return t
    def setData(self, int, Any):
        
        return super().setData(int, Any)


class QTableWidget(QTableWidget_):
    def __init__(self, parent):
        self.DeletedPK = []
        self.TabelName = None
        self.MainForm = None
        self.EditFormDataMode = None
        self.FieldsAllInfo = None
        self.UpdateRowKeys = []
        self.DisableEditColumns=[]
        super().__init__(parent)

    # def setDisableEditColumns(self, *args):
    #     """设置禁止编辑列的列号，从0列开始,逗号分隔"""
    #     self.DisableEditColumns=args
    #     for c in args:

    def setBaseInfo(self, mainForm, sub_table_name, fieldlist):
        if len(fieldlist) != self.columnCount():
            raise JPExceptionFieldNull("给定的字段列表中字段个数与子表格列数不同")
        self.MainForm = mainForm
        self.TabelName = sub_table_name
        db = JPDb()
        flds, pkname = db.getRecordFields(sub_table_name)
        if pkname != fieldlist[0]:
            raise ValueError("fieldlist 第一个字段必须为子表的主键字段！")
        else:
            # 隐藏第一列
            self.setColumnHidden(0, True)
        self.FieldsAllInfo = OrderedDict()
        for fn in fieldlist:
            fld = flds[fn]
            tempDelegate = None
            tempAlign = None
            if fld.TypeCode in db.getIntTypeCode():
                tempDelegate = JPDelegate_Int(self)
                tempAlign = (Qt.AlignRight | Qt.AlignVCenter)
            elif fld.TypeCode in db.getFloatTypeCode():
                tempDelegate = JPDelegate_Float(self)
                tempAlign = (Qt.AlignRight | Qt.AlignVCenter)
            elif fld.TypeCode in db.getBooleanTypeCode():
                tempDelegate = JPDelegate_Boolean(self)
                tempAlign = (Qt.AlignCenter)
            elif fld.TypeCode in db.getDateTypeCode():
                tempDelegate = JPDelegate_Date(self)
                tempAlign = (Qt.AlignCenter)
            else:
                tempDelegate = JPDelegate_Text(self)
                tempAlign = (Qt.AlignLeft | Qt.AlignVCenter)
            self.FieldsAllInfo[fn] = (fld, tempDelegate, tempAlign)
        for i, de in enumerate(
            [info[1] for info in self.FieldsAllInfo.values()]):
            de.editNext[QModelIndex].connect(self.__EditNext)
            self.setItemDelegateForColumn(i, de)
        self.cellPressed[int, int].connect(self.__cellPressed)
        self.cellChanged[int, int].connect(self.__cellPressed)

    def EventAddNewRow(self,tableWidget:QTableWidget_):
        """检查表中数据,可重定向到自定义函数，返回值为真时增加一行"""
        return
    def __cellPressed(self, *args):

        if self.MainForm.EditMode == JPEditFormDataMode.ReadOnly:
            return
        if self.EventAddNewRow(self):
            self.__AddRow()

    def __EditNext(self, index):
        return
        # 回车后向右,到最右后到下一行首单元
        print("判断向右或向下，基于{},{}".format(index.row(), index.column()))
        target = ((index.row(), index.column() + 1), (index.row() + 1, 0))
        for r, c in target:
            tmp = index.sibling(r, c)
            if tmp.isValid():
                self.setCurrentCell(r, c)

    def __AddRow(self, rowdata=None):
        self.cellPressed[int, int].disconnect(self.__cellPressed)
        self.cellChanged[int, int].disconnect(self.__cellPressed)
        r = self.rowCount()
        self.setRowCount(r + 1)
        c = 0
        for fn, info in self.FieldsAllInfo.items():
            item = JPTableWidgetItem()
            item.setData(1,"value")
            if rowdata:
                info[1].setItemOriginal(rowdata[fn], item)
            item.setTextAlignment(info[2])
            self.setItem(r, c, item)
            c += 1
        self.cellPressed[int, int].connect(self.__cellPressed)
        self.cellChanged[int, int].connect(self.__cellPressed)

    def readTableData(self, PK=None):
        '''读取子表数据'''
        # 选中单元格开始编辑
        self.setEditTriggers(QtWidgets_.QAbstractItemView.AllEditTriggers)
        if self.MainForm.EditMode == JPEditFormDataMode.New:
            self.__AddRow()
            return
        if PK:
            self.__MainPKValue = PK
        sql = "select {} from {} where {}='{}'"
        sql = sql.format(','.join([key for key in self.FieldsAllInfo.keys()]),
                         self.TabelName, self.MainForm.PKFieldName, PK)
        db = JPDb()
        rows, self.FieldInfo = db.getRecordsDict(sql)
        for row in rows:
            self.__AddRow(row)

    def GetSqls(self) -> list:
        self.CheckDateSignal.emit(self)  # 检查数据。删除无用的尾行
        Sqls = []
        sub_pkname = self.__FieldsList[0]
        if len(self.DeletedPK) > 0:
            delstr = "delete from {} where {} in {}"
            Sqls.append(
                delstr.format(self.TabelName, sub_pkname,
                              str(tuple(self.DeletedPK))))

        def CreateInsertSQL(row):
            # 生成插入语句
            values = []
            sql = 'insert into {} {} values {}'
            for c, fn in enumerate(self.FieldsList[1:]):
                values.append(self.Delegates[c + 1].getSqlValue(
                    self.FieldInfo[c + 1], self.item(row, c + 1)))
            return sql.format(self.TabelName, str(self.FieldsList),
                              str(values))

        def CreateUpdateSQL(row):
            # 生成更新语句
            sql = "update {} set {} where {}='{}'"
            for col in range(1, len(self.FieldsList)):
                fn = self.FieldsList[col]
                return "{}={}".format(
                    fn,
                    self.Delegates[col].getSqlValue(self.FieldInfo[fn],
                                                    self.item(row, col)))

        for r in range(self.rowCount()):
            if self.MainForm.EditMode == JPEditFormDataMode.New:
                if self.item(r, 0).text():
                    # 如果第一列无值，说明是一个新列，生成插入语句
                    continue
                else:
                    Sqls.append(CreateInsertSQL(r))
            if self.MainForm.EditMode == JPEditFormDataMode.Edit:
                for r in set(self.UpdateRowKeys):
                    Sqls.append(CreateUpdateSQL(r))
        return Sqls


class QWidget(QWidget_):
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        self.__TabelName = None
        self.__EditFormDataMode = JPEditFormDataMode.New
        self.__SubForm: QTableWidget = None
        self.__EditFormMode = 1  # 1:单独窗体 2:母子窗体
        self.__PKvalue = None
        self.__ReadViewName = None
        self.__AutoPkRole = None
        self.PKFieldName = None
        self.ObjectList = {}  # 存放需要保存数据的类

    @property
    def SubForm(self)->QTableWidget:
        """返回子表控件"""
        return self.__SubForm

    def setMainTabelInfo(self,
                         main_table_name: str,
                         main_view_name: str = None,
                         auto_pk_role: int = None):
        '''设置主表基本信息'''
        self.__TabelName = main_table_name
        self.__ReadViewName = main_view_name
        self.__AutoPkRole = auto_pk_role

    def setSubTabelInfo(self, sub_table_name: str, sub_form: QTableWidget,
                        fieldlist: list):
        '''设置子表、子窗体基本信息'''
        self.__EditFormMode = 2
        self.__SubForm = sub_form
        self.__SubForm.setBaseInfo(self, sub_table_name, fieldlist)

    def setFieldRowDict(self, *args):
        '''设置字段数据来源，给一个字段设置数据来源，会使该字段的编辑控件为Combo
        可以同时设置多个，按字段名、行来源顺序设置就行
        '''
        if (len(args) % 2) != 0 or len(args) == 0:
            raise ValueError("参数个数必须为偶数，按字段名、行来源顺序排列")
        for i in range(int(len(args) / 2)):
            if isinstance(args[i * 2], str) and isinstance(
                    args[i * 2 + 1], (dict, list)):
                obj = self.findChild(QComboBox, args[i * 2])
                obj.setRowDict(args[i * 2 + 1])
            else:
                raise ValueError("参数类型错误，奇数参数为字段名，偶数参数为字典")

    def readTableData(self, pk=None):
        '''读取主表数据，并设置主表相关信息'''
        db = JPDb()
        viewname = (self.__TabelName
                    if self.__ReadViewName is None else self.__ReadViewName)
        flds, self.PKFieldName = db.getRecordFields(self.__TabelName, viewname,
                                                    pk)
        # 查找所有自定义控件类型
        self.ObjectList = {
            obj.objectName(): obj
            for obj in self.findChildren((QLineEdit, QDateEdit, QComboBox,
                                          QTextEdit, QCheckBox))
        }
        # 设置 {} 的字段信息
        for obj in self.ObjectList.values():
            obj.setFieldInfo(flds[obj.objectName()])

    def show(self,
             edit_mode: JPEditFormDataMode = JPEditFormDataMode.New,
             pk_value: str = None):
        '''显示窗体'''
        self.EditMode = edit_mode
        if edit_mode != JPEditFormDataMode.New and pk_value is None:
            raise JPExceptionFieldNull("没有设置主表的主键字段值")
        self.__PKvalue = pk_value
        self.butSave = self.findChild(QPushButton, 'butSave')
        self.butPrint = self.findChild(QPushButton, 'butPrint')
        if self.butSave:
            self.butPrint.clicked.connect(self.__Print)
        if self.butPrint:
            self.butSave.clicked.connect(self.__SaveDate)

        self.readTableData(pk_value)
        self.__SubForm.readTableData(pk_value)
        super().show()

    def __SaveDate(self):
        print(self.SubForm.item(0,0).data(1))
        print("以下是子表生成的SQL：")
        print(self.__SubForm.GetSqls())

    def __Print(self):
        print("打印")


if __name__ == "__main__":
    print(dir())
    print(dir())
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = QWidget()
    aa = QLineEdit(w)
    aa.setText("aksdjlghlsdkjg")

    def p(self):
        print(self.text())

    aa.p = p
