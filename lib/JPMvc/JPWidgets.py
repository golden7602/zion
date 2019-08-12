# -*- coding: utf-8 -*-

import abc
import datetime
import os
import sys
sys.path.append(os.getcwd())

# from collections import OrderedDict

from PyQt5 import QtWidgets as QtWidgets_

from PyQt5.QtCore import QDate, pyqtSignal, Qt, QObject
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


class _JPDoubleValidator(QDoubleValidator):
    def __init__(self, decima=2):
        super().__init__()
        self.setDecimals(decima)

    def validate(self, vstr, pos):
        return super().validate(vstr.replace(',', ''), pos)


class _JPIntValidator(QIntValidator):
    def __init__(self):
        super().__init__()

    def validate(self, vstr, pos):
        return super().validate(vstr.replace(',', ''), pos)


class JPExceptionFieldNull(Exception):
    def __init__(self, obj, msg=None):
        self.Message = obj if isinstance(obj,
                                         str) else "字段的【{}】值不能为空值！".format(msg)

    def __str__(self):
        return self.Message


class __JPWidgetBase(QObject):
    def __init__(self, *args):
        super().__init__(*args)
        self._FieldInfo: JPFieldType = None
        self.MainModel = None
        self.RowsDatal = None
        # self._changeMethod = None

    # def setChangeMethod(self, methon):
    #     self._changeMethod = methon
    #     self._changeMethod.connect(self._onValueChange)
    #     if self.objectName() == 'fEspecieID':
    #         pass

    def _onValueChange(self):
        self.RowsDatal.setData(self._FieldInfo._index, self.Value())
        if self.MainModel:
            self.MainModel._emitDataChange(self)

    def setMainModel(self, QWidget: QWidget_):
        self.MainModel = QWidget

    def setRowsData(self, rd: JPTabelRowData):
        self.RowsDatal = rd

    @property
    def FieldInfo(self):
        return self._FieldInfo

    def getNullValue(self):
        if self._FieldInfo.NotNull is False:
            return 'Null'
        else:
            raise JPExceptionFieldNull(
                self, "字段的【{}】值不能为空值！".format(self._FieldInfo.FieldName))

    @abc.abstractmethod
    def getSqlValue(self):
        """返回字段值，可直接用于SQL语句中"""
    @abc.abstractmethod
    def setFieldInfo(self, fld: JPFieldType = None, raiseEvent=True):
        pass

    # def setFieldInfo(self, fld: JPFieldType = None, raiseEvent=True):
    #     """设置字段信息"""
    #     bz = (raiseEvent is False or self.MainModel._loadDdata)
    #     if bz:
    #         print(self.objectName())
    #         self._changeMethod.disconnect(self._onValueChange)
    #     self._setFieldInfo(fld, raiseEvent)
    #     if bz:
    #         self._changeMethod.connect(self._onValueChange)

    def refreshValueNotRaiseEvent(self, *value):
        if value:
            self._FieldInfo.Value = value
        self.setFieldInfo(self._FieldInfo, False)

    @abc.abstractmethod
    def Value(self):
        pass


class QLineEdit(QLineEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        #self.textChanged[str].connect(self._onValueChange)

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
        # if (raiseEvent is False or self.MainModel._loadDdata):
        #     self.textChanged[str].disconnect(self._onValueChange)
        if fld.Value:
            self.setText(JPGetDisplayText(fld.Value))
            if fld.TypeCode == JPFieldType.Int:
                pass
                #self.setValidator(_JPIntValidator())
            if fld.TypeCode == JPFieldType.Float:
                va = _JPDoubleValidator()
                va.setDecimals(fld.Scale)
                #self.setValidator(va)
        else:
            self.setText('')
        # self.textChanged[str].connect(self._onValueChange)
    def focusInEvent(self, e):
        if self._FieldInfo.TypeCode in (JPFieldType.Int, JPFieldType.Float)
            t=self.text()
            self.setText(t.replace(',', ''))
        QLineEdit_.focusInEvent(self,e)
    def focusOutEvent(self, e):
        self.setText(JPGetDisplayText(self.Value()))
        self._onValueChange()
        QLineEdit_.focusOutEvent(self, e)


class QTextEdit(QTextEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.textChanged.connect(self._onValueChange)

    def getSqlValue(self) -> str:
        t = self.toPlainText()
        if t is None or len(t) == 0:
            return self.getNullValue()
        return t

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        if (raiseEvent is False or self.MainModel._loadDdata):
            self.textChanged.disconnect(self._onValueChange)
        self._FieldInfo = fld
        self.setPlainText(fld.Value)
        self.textChanged.connect(self._onValueChange)

    def Value(self):
        return self.toPlainText()


class QComboBox(QComboBox_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.setEditable(True)
        self.BindingColumn = 1
        self.currentIndexChanged[int].connect(self._onValueChange)

    def getSqlValue(self) -> str:
        if self.count() == 0:
            raise JPExceptionFieldNull("字段【{}】的枚举数据源不能为空！".format(
                self._FieldInfo.FieldName))
        if self.currentData():
            tempV = self.currentData()[self.BindingColumn]
            if tempV:
                return "'{}'".format(tempV)
            else:
                return self.getNullValue()
        else:
            return self.getNullValue()

    def Value(self):
        if self.currentData():
            return self.currentData()[self.BindingColumn]

    def setEnumValue(self, value):
        if value is None:
            self.setCurrentIndex(-1)
            return
        for i, row in enumerate(self._FieldInfo.RowSource):
            if row[self.BindingColumn] == value:
                self.setCurrentIndex(i)
                self.setCurrentText(row[0])
                return

    @property
    def RowSource(self) -> list:
        return self._FieldInfo.RowSource

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        if (raiseEvent is False or self.MainModel._loadDdata):
            self.currentIndexChanged[int].disconnect(self._onValueChange)
        self._FieldInfo = fld
        rs = self._FieldInfo.RowSource

        if rs:
            qcom = QCompleter([str(r[0]) for r in rs])
            qcom.setCaseSensitivity(Qt.CaseInsensitive)
            qcom.setCompletionMode(QCompleter.PopupCompletion)
            qcom.setFilterMode(Qt.MatchContains)
            self.setCompleter(qcom)
            if self.count() == 0:
                for r in rs:
                    self.addItem(str(r[0]), r)
            self.setEnumValue(fld.Value)
        self.currentIndexChanged[int].connect(self._onValueChange)

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
        # self.setEditText(self.currentText().upper())


class QDateEdit(QDateEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.dateChanged.connect(self._onValueChange)

    def getSqlValue(self) -> str:
        return "'{}'".format(JPDateConver(self.date(), str))

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        if (raiseEvent is False or self.MainModel._loadDdata):
            self.dateChanged.disconnect(self._onValueChange)
        self._FieldInfo = fld
        if not (self._FieldInfo.Value is None):
            self.setDate(JPDateConver(self._FieldInfo.Value, datetime.date))
        else:
            self.setDate(QDate.currentDate())
        self.dateChanged.connect(self._onValueChange)

    def Value(self):
        return JPDateConver(self.date(), datetime.date)


class QCheckBox(QCheckBox_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self._FieldInfo: JPFieldType = None
        self.stateChanged[int].connect(self._onValueChange)

    def getSqlValue(self) -> str:
        if self.checkState() is None:
            return 'Null'
        return '1' if self.checkState() is True else '0'

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        if (raiseEvent is False or self.MainModel._loadDdata):
            self.stateChanged[int].disconnect(self._onValueChange)
        self._FieldInfo = fld
        v = True if self._FieldInfo.Value else False
        self.setChecked(v)
        self.stateChanged[int].connect(self._onValueChange)

    def Value(self):
        return 1 if self.checkState() == Qt.Checked else 0
