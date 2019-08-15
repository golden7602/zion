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
from PyQt5.QtGui import (QValidator, QDoubleValidator, QIntValidator)
import re


def __getattr__(name):
    return QtWidgets_.__dict__[name]


class _JPDoubleValidator(QDoubleValidator):
    def __init__(self, decima=2):
        super().__init__()
        self.setDecimals(decima)

    def validate(self, vstr, pos):
        return super().validate(vstr.replace(',', ''), pos)


class _JPIntValidator(QValidator):
    def __init__(self, v1, v2):
        super().__init__()
        self.min = v1
        self.max = v2

    def validate(self, vstr, pos):
        str0 = vstr.replace(',', '')
        mt = re.match(r"^-?[1-9]\d*$", str0, flags=(re.I))
        if mt:
            if self.min <= int(str0) <= self.max:
                return QValidator.Acceptable, vstr, pos
        return QValidator.Invalid, vstr, pos


class JPExceptionFieldNull(Exception):
    def __init__(self, obj, msg=None):
        self.Message = obj if isinstance(obj,
                                         str) else "字段的【{}】值不能为空值！".format(msg)

    def __str__(self):
        return self.Message


class __JPWidgetBase(QObject):
    def __init__(self, *args):
        super().__init__(*args)
        self.__FieldInfo: JPFieldType = None
        self.MainModel = None
        self.RowsData = None

    def _onValueChange(self, value):
        self.RowsData.setData(self.FieldInfo._index, self.Value())
        if self.MainModel:
            self.MainModel._emitDataChange(self, value)

    def setMainModel(self, QWidget: QWidget_):
        self.MainModel = QWidget

    def setRowsData(self, rd: JPTabelRowData):
        self.RowsData = rd

    @property
    def FieldInfo(self):
        errsre="窗体字段【{}】的FieldInfo属性为None，可能是窗体SQl查询语句中没有包含此字段！"
        if self.__FieldInfo is None:
            raise AttributeError(
                errStr.format(
                    self.objectName()))
        return self.__FieldInfo
    @FieldInfo.setter
    def FieldInfo(self,fld):
        self.__FieldInfo=fld
    def getNullValue(self):
        if self.FieldInfo.NotNull is False:
            return 'Null'
        else:
            raise JPExceptionFieldNull(
                self, "字段的【{}】值不能为空值！".format(self.FieldInfo.FieldName))

    @abc.abstractmethod
    def getSqlValue(self):
        """返回字段值，可直接用于SQL语句中"""

    @abc.abstractmethod
    def setFieldInfo(self, fld: JPFieldType = None, raiseEvent=True):
        pass

    @abc.abstractmethod
    def Value(self):
        pass

    def refreshValueNotRaiseEvent(self, *value):
        if value:
            self.FieldInfo.Value = value

    def setReadOnly(self, state=True):
        if isinstance(self, (QLineEdit_, QTextEdit_, QDateEdit_)):
            self.setReadOnly(state)
        elif isinstance(self, QComboBox_):
            self.setEnabled(not state)
        elif isinstance(self, QCheckBox_):
            self.setCheckable(not state)


class QLineEdit(QLineEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.textChanged[str].connect(self.refreshValueNotRaiseEvent)

    def getSqlValue(self) -> str:
        t = self.text()
        if t is None or len(t) == 0:
            return self.getNullValue()
        else:
            return "'{}'".format(t.replace(',', ''))

    def refreshValueNotRaiseEvent(self, v, changeDisplayText: bool = False):
        tp = self.FieldInfo.TypeCode
        if tp == JPFieldType.Int:
            self.FieldInfo.Value = int(str(v).replace(',', '')) if v else 0
        elif tp == JPFieldType.Float:
            self.FieldInfo.Value = float(str(v).replace(',',
                                                         '')) if v else 0.0
        else:
            self.FieldInfo.Value = v
        if changeDisplayText:
            self.__setDisplayText()

    def refreshValueRaiseEvent(self, v, changeDisplayText: bool = False):
        self.refreshValueNotRaiseEvent(v, changeDisplayText)
        super()._onValueChange(self.FieldInfo.Value)

    def Value(self):
        # 这里是为了处理在主窗体中使用了一些主数据库中没有的字段时
        if self.FieldInfo is None:
            return self.text()
        tp = self.FieldInfo.TypeCode
        v = self.text()
        if tp == JPFieldType.Int:
            return int(v.replace(',', '')) if v else 0
        if tp == JPFieldType.Float:
            return float(v.replace(',', '')) if v else 0.0
        if tp == JPFieldType.String:
            return v if v else ''
        return v

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self.FieldInfo = fld
        # 设置编辑状态
        self.setReadOnly(self.MainModel.isReadOnlyMode)
        if not self.MainModel.isNewMode:
            self.__setDisplayText()
        # if self.FieldInfo.TypeCode == JPFieldType.Int:
        #     self.setValidator(_JPIntValidator())
        # if self.FieldInfo.TypeCode == JPFieldType.Float:
        #     self.setValidator(_JPDoubleValidator())

    def __setDisplayText(self):
        v = self.FieldInfo.Value
        if v:
            self.setText(JPGetDisplayText(v))
        else:
            self.setText('')

    def setDoubleValidator(self, v_Min, v_Max, Decimals: int = 2):
        Validator = _JPDoubleValidator()
        Validator.setRange(float(v_Min), float(v_Max))
        Validator.setDecimals(Decimals)
        self.setValidator(Validator)

    def setIntValidator(self, v_Min: int, v_Max: int):
        Validator = _JPIntValidator(v_Min, v_Max)
        self.setValidator(Validator)

    def focusInEvent(self, e):
        if self.FieldInfo.TypeCode in (JPFieldType.Int, JPFieldType.Float):
            t = self.text()
            self.textChanged[str].disconnect(self.refreshValueNotRaiseEvent)
            self.setText(t.replace(',', ''))
            self.textChanged[str].connect(self.refreshValueNotRaiseEvent)
        QLineEdit_.focusInEvent(self, e)

    def focusOutEvent(self, e):
        self.__setDisplayText()
        super()._onValueChange(self.FieldInfo.Value)
        QLineEdit_.focusOutEvent(self, e)


class QTextEdit(QTextEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.textChanged.connect(self.refreshValueNotRaiseEvent)

    def getSqlValue(self) -> str:
        t = self.toPlainText()
        if t is None or len(t) == 0:
            return self.getNullValue()
        return t

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self.FieldInfo = fld
        # 设置编辑状态
        self.setReadOnly(self.MainModel.isReadOnlyMode)
        if not self.MainModel.isNewMode:
            self.setPlainText(fld.Value)

    def Value(self):
        return self.FieldInfo.Value

    def refreshValueNotRaiseEvent(self, *Value):
        if Value:
            self.FieldInfo.Value = Value[0]
        else:
            self.FieldInfo.Value = self.toPlainText()

    def refreshValueRaiseEvent(self, *Value):
        self.refreshValueNotRaiseEvent(Value)
        super()._onValueChange(self.FieldInfo.Value)

    def focusOutEvent(self, e):
        super()._onValueChange(self.FieldInfo.Value)
        QTextEdit_.focusOutEvent(self, e)


class QComboBox(QComboBox_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.setEditable(False)
        self.BindingData = []
        self.currentIndexChanged[int].connect(self._onValueChange)

    def getSqlValue(self) -> str:
        if self.count() == 0:
            raise JPExceptionFieldNull("字段【{}】的枚举数据源不能为空！".format(
                self.FieldInfo.FieldName))
        if self.currentData():
            tempV = self.BindingData[self.currentIndex()]
            if tempV:
                return "'{}'".format(tempV)
            else:
                return self.getNullValue()
        else:
            return self.getNullValue()

    def _onValueChange(self, index):
        self.FieldInfo.Value = self.BindingData[index]
        super()._onValueChange(self.FieldInfo.Value)

    def Value(self):
        return self.FieldInfo.Value

    def __setCurrentData(self, value):
        if value is None:
            self.setCurrentIndex(-1)
            return -1
        for i, data in enumerate(self.BindingData):
            if data == value:
                self.FieldInfo.Value = data
                self.setCurrentIndex(i)
                return i

    def refreshValueNotRaiseEvent(self, value):
        self.currentIndexChanged[int].disconnect(self._onValueChange)
        self.__setCurrentData(value)
        self.currentIndexChanged[int].connect(self._onValueChange)

    def refreshValueRaiseEvent(self, value):
        i = self.__setCurrentData(value)
        super()._onValueChange(i)

    @property
    def RowSource(self) -> list:
        return self.FieldInfo.RowSource

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self.currentIndexChanged[int].disconnect(self._onValueChange)
        self.FieldInfo = fld
        if self.FieldInfo.RowSource:
            qcom = QCompleter([str(r[0]) for r in self.FieldInfo.RowSource])
            qcom.setCaseSensitivity(Qt.CaseInsensitive)
            qcom.setCompletionMode(QCompleter.PopupCompletion)
            qcom.setFilterMode(Qt.MatchContains)
            self.setCompleter(qcom)
            for r in self.FieldInfo.RowSource:
                self.addItem(str(r[0]), r)
        c = self.FieldInfo.BindingColumn
        if self.FieldInfo.RowSource is None:
            raise AttributeError("窗体字段【{}】没有设置行来源数据".format(self.objectName()))
        self.BindingData = [row[c] for row in self.FieldInfo.RowSource]
        # 设置编辑状态
        self.setEnabled(not self.MainModel.isReadOnlyMode)
        self.__setCurrentData(fld.Value)
        self.currentIndexChanged[int].connect(self._onValueChange)

    # def keyPressEvent(self, event):
    #     return
    #     QComboBox_.keyPressEvent(self, event)


class QDateEdit(QDateEdit_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.__RaiseEvent = False
        self.dateChanged.connect(self._onValueChange)

    def getSqlValue(self) -> str:
        return "'{}'".format(JPDateConver(self.date(), str))

    def _onValueChange(self):
        self.FieldInfo.Value = JPDateConver(self.date(), datetime.date)
        if self.__RaiseEvent:
            super()._onValueChange(self.FieldInfo.Value)

    def refreshValueNotRaiseEvent(self, value):
        self.__RaiseEvent = False
        value = value if value else QDate.currentDate()
        self.FieldInfo.Value = JPDateConver(value, datetime.date)
        self.setDate(JPDateConver(self.FieldInfo.Value, QDate))
        self.__RaiseEvent = True

    def refreshValueRaiseEvent(self, value):
        self.refreshValueNotRaiseEvent(value)
        super()._onValueChange(self.FieldInfo.Value)

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self.FieldInfo = fld
        # 设置编辑状态
        self.setReadOnly(self.MainModel.isReadOnlyMode)
        self.refreshValueNotRaiseEvent(fld.Value)

    def Value(self):
        return JPDateConver(self.date(), datetime.date)


class QCheckBox(QCheckBox_, __JPWidgetBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.__RaiseEvent = False
        self.stateChanged[int].connect(self._onValueChange)

    def getSqlValue(self) -> str:
        if self.checkState() is None:
            return 'Null'
        return '1' if self.checkState() is True else '0'

    def _onValueChange(self):
        self.FieldInfo.Value = self.checkState()
        if self.__RaiseEvent:
            super()._onValueChange(self.FieldInfo.Value)

    def refreshValueNotRaiseEvent(self, value):
        self.__RaiseEvent = False
        if value is None:
            v = True if value else False
            self.FieldInfo.Value = v
            self.setChecked(v)
        self.__RaiseEvent = True

    def refreshValueRaiseEvent(self, value):
        self.refreshValueNotRaiseEvent(value)
        super()._onValueChange(self.FieldInfo.Value)

    def setFieldInfo(self, fld: JPFieldType, raiseEvent=True):
        self.FieldInfo = fld
        self.refreshValueNotRaiseEvent(self.FieldInfo.Value)
        # 设置编辑状态
        self.setCheckable(not self.MainModel.isReadOnlyMode)
        self.refreshValueNotRaiseEvent(fld.Value)

    def Value(self):
        return 1 if self.checkState() == Qt.Checked else 0
