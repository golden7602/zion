# -*- coding: utf-8 -*-

import abc
import datetime
import os
import sys
sys.path.append(os.getcwd())

# from collections import OrderedDict

from PyQt5 import QtWidgets as QtWidgets_

from PyQt5.QtCore import QDate, pyqtSignal, Qt
from PyQt5.QtWidgets import (QCheckBox as QCheckBox_, QComboBox as QComboBox_,
                             QDateEdit as QDateEdit_, QLineEdit as QLineEdit_,
                             QTextEdit as QTextEdit_, QWidget as QWidget_,
                             QCompleter)
from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Field import JPFieldType
from lib.JPDatabase.Query import JPTabelRowData
from lib.JPFunction import JPBooleanString, JPDateConver, JPGetDisplayText
from PyQt5.QtGui import (QDoubleValidator, QIntValidator)


def __getattr__(name):
    return QtWidgets_.__dict__[name]


class JPExceptionFieldNull(Exception):
    def __init__(self, obj, msg=None):
        self.Message = obj if isinstance(obj,
                                         str) else "字段的【{}】值不能为空值！".format(msg)

    def __str__(self):
        return self.Message


class __JPWidgetBase(object):
    def __init__(self, *args):
        self._FieldInfo: JPFieldType = None
        self.__MainModel = None
        self.__RowsData = None

    def _onValueChange(self):
        self.__RowsData.setData(self._FieldInfo._index, self.Value())
        if self.__MainModel:
            self.__MainModel._emitDataChange(self)

    def setMainModel(self, QWidget: QWidget_):
        self.__MainModel = QWidget

    def setRowsData(self, rd: JPTabelRowData):
        self.__RowsData = rd

    @property
    def FieldInfo(self):
        return self._FieldInfo

    @classmethod
    def getNullValue(self):
        if self._FieldInfo.NullOK:
            return 'Null'
        else:
            raise JPExceptionFieldNull(
                self, "字段的【{}】值不能为空值！".format(self._FieldInfo.Name))

    @abc.abstractmethod
    def getSqlValue(self):
        """返回字段值，可直接用于SQL语句中"""

    def setFieldInfo(self, fld: JPFieldType = None):
        """设置字段信息"""
        self.textChanged.connect(self._onValueChange)

    def refreshValueNotRaiseEvent(self, value):
        self._FieldInfo.Value = value
        self.setFieldInfo(self._FieldInfo, False)

    @abc.abstractmethod
    def Value(self):
        pass


class QLineEdit(QLineEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)

    def getSqlValue(self) -> str:
        t = self.text()
        if t is None or len(t) == 0:
            return self.getNullValue()
        else:
            return "'{}'".format(t.replace(',', ''))

    def Value(self):
        # 这里是为了处理在主窗体中使用了一些主数据库中没有的字段时
        if self._FieldInfo is None:
            return self.text()
        tp = self._FieldInfo.TypeCode
        v = self.text()
        if tp == JPFieldType.Int:
            return int(v.replace(',', '')) if v else 0
        if tp == JPFieldType.Float:
            return float(v.replace(',', '')) if v else 0.0
        if tp == JPFieldType.String:
            return v if v else ''
        return v

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self._FieldInfo = fld
        if fld.Value:
            self.setText(JPGetDisplayText(fld.Value))
            if fld.TypeCode == JPFieldType.Int:
                self.setValidator(QIntValidator())
            if fld.TypeCode == JPFieldType.Float:
                va = QDoubleValidator()
                va.setDecimals(fld.Scale)
                self.setValidator(va)
        else:
            self.setText('')
        if raiseEvent:
            super().setFieldInfo()

    def focusOutEvent(self, e):
        self.setText(JPGetDisplayText(self.Value()))
        #self._dataChange()
        QLineEdit_.focusOutEvent(self, e)


class QTextEdit(QTextEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)

    def getSqlValue(self) -> str:
        t = self.text()
        if t is None or len(t) == 0:
            return self.getNullValue()
        return t

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self._FieldInfo = fld
        self.setText(fld.Value)
        if raiseEvent:
            super().setFieldInfo()

    def Value(self):
        return self.toPlainText()


class QComboBox(QComboBox_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.setEditable(True)
        self.BindingColumn = 1

    # def setRowDict(self, value: list, Binding_column: int = 1):
    #     """value为一个行，行可为可为列表或元组
    #     列表或元组第一列为显示值，其后为其他需要返回的值
    #     Binding_column为返回值对应的列，从0开始。
    #     默认情况下，返回值就是列表显示文本（第0列）
    #     """
    #     self.__RowList = value
    #     self.BindingColumn = Binding_column
    #     for row in self.__RowList:
    #         self.addItem(str(row[0]), row)

    def getSqlValue(self) -> str:
        if self.__RowList is None:
            raise JPExceptionFieldNull("字段【{}】的枚举数据源不能为空！".format(
                self._FieldInfo.Name))
        if self.currentData():
            return "'{}'".format(self.currentData()[self.BindingColumn])
        else:
            return self.getNullValue()

    def Value(self):
        if self.currentData():
            return self.currentData()[self.BindingColumn]

    def setEnumValue(self, value):
        if value is None:
            return
        for i, row in enumerate(self._FieldInfo.RowSource):
            if row[self.BindingColumn] == value:
                self.setCurrentIndex(i)
                self.setCurrentText(row[0])
                return

    # def editTextChanged(self, text):
    #     txt = text.upper()
    #     self.lineEdit().textChanged.disconnect(self.editTextChanged)
    #     for i in reversed(range(self.count())):
    #         self.removeItem(i)
    #     if self._FieldInfo.RowSource:

    #         lst = [
    #             item for item in self._FieldInfo.RowSource
    #             if str(item[0]).upper().find(txt) > -1
    #         ]
    #         lst = lst if lst else self._FieldInfo.RowSource
    #         for r in lst:
    #             self.addItem(r[0], r)
    #         self.showPopup()
    #         self.lineEdit().setFocus()
    #     self.lineEdit().textChanged.connect(self.editTextChanged)

    @property
    def RowSource(self) -> list:
        return self._FieldInfo.RowSource

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self._FieldInfo = fld
        rs = self._FieldInfo.RowSource
        if rs:
            # self.lineEdit().textChanged.connect(self.editTextChanged)
            qcom = QCompleter([str(r[0]) for r in rs])
            qcom.setCaseSensitivity(Qt.CaseInsensitive)
            qcom.setCompletionMode(QCompleter.PopupCompletion)
            qcom.setFilterMode(Qt.MatchContains)
            self.setCompleter(qcom)
            for r in rs:
                self.addItem(str(r[0]), r)
            self.setEnumValue(fld.Value)
        if raiseEvent:
            self.currentIndexChanged.connect(self._onValueChange)

    def focusOutEvent(self, e):
        t = self.currentText()
        if not t or (t not in [item[0] for item in self._FieldInfo.RowSource]):
            self.setCurrentIndex(-1)
            self.lineEdit().setText('')
        QComboBox_.focusOutEvent(self, e)

    def focusInEvent(self, e):
        self.lineEdit().selectAll()
        QComboBox_.focusInEvent(self, e)

    def keyPressEvent(self, event):
        QComboBox_.keyPressEvent(self, event)
        #self.setEditText(self.currentText().upper())


class QDateEdit(QDateEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)

    def getSqlValue(self) -> str:
        return "'{}'".format(JPDateConver(self.date(), str))

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self._FieldInfo = fld
        if not (self._FieldInfo.Value is None):
            self.setDate(JPDateConver(self._FieldInfo.Value, datetime.date))
        else:
            self.setDate(QDate.currentDate())
        if raiseEvent:
            self.dateChanged[QDate].connect(self._onValueChange)

    def Value(self):
        return JPDateConver(self.date(), datetime.date)


class QCheckBox(QCheckBox_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self._FieldInfo: JPFieldType = None

    def getSqlValue(self) -> str:
        if self.checkState() is None:
            return 'Null'
        return '1' if self.checkState() is True else '0'

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self._FieldInfo = fld
        v = True if self._FieldInfo.Value else False
        self.setChecked(v)
        if raiseEvent:
            self.stateChanged.connect(self._onValueChange)

    def Value(self):
        return 1 if self.checkState() == Qt.Checked else 0
