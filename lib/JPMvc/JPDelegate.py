# -*- coding: utf-8 -*-
# @Time    : 19-12-1 下午3:26
# @Author  : JPT
# @Site    :
# @File    : JPTableModel\__init__.py
# @Software: VS Code

import abc
import datetime
import sys
import os
sys.path.append(os.getcwd())
from lib.JPFunction import JPBooleanString, JPDateConver
from PyQt5.QtCore import (QAbstractItemModel, QModelIndex, QObject, Qt, QDate,
                          pyqtSignal)
from PyQt5.QtWidgets import (QPushButton, QStyledItemDelegate,
                             QStyleOptionViewItem, QWidget, QLineEdit,
                             QComboBox, QDateEdit)
from lib.JPDatabase.Field import JPFieldType
from PyQt5.QtGui import (QDoubleValidator, QIntValidator)


class _JPDelegate_Base(QStyledItemDelegate):
    editNext = pyqtSignal(QModelIndex)

    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    @abc.abstractmethod
    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem,
                     index: QModelIndex) -> QWidget:
        pass

    @abc.abstractmethod
    def setEditorData(self, editor: QWidget, index: QModelIndex):
        pass

    @abc.abstractmethod
    def setModelData(self, editor: QWidget, model: QAbstractItemModel,
                     index: QModelIndex):
        pass

    def updateEditorGeometry(self, editor: QWidget,
                             StyleOptionViewItem: QStyleOptionViewItem,
                             index: QModelIndex):
        editor.setGeometry(StyleOptionViewItem.rect)


class JPDelegate_ReadOnly(_JPDelegate_Base):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        return

    def setEditorData(self, editor, index):
        return

    def setModelData_(self, editor, model, index):
        return


class JPDelegate_LineEdit(_JPDelegate_Base):
    def __init__(self, parent: QObject = None, value_type=None, decimal=2):
        '''JPDelegate_LineEdit(parent: QObject = None, value_type=None, decimal)\n
        value_type 为数据类型，1整数、2小数 None或不赋值时为文本或其他值'''
        super().__init__(parent)
        self.__ValueType = value_type
        self.__Decimal = decimal

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem,
                     index: QModelIndex) -> QWidget:
        wdgt = QLineEdit(parent)
        if self.__ValueType == JPFieldType.Int:
            wdgt.setValidator(QIntValidator())
        if self.__ValueType == JPFieldType.Float:
            va = QDoubleValidator()
            va.setDecimals(self.__Decimal)
            wdgt.setValidator(va)
        return wdgt

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        text = index.model().data(index, Qt.EditRole)
        if text:
            editor.setText(str(text))

    def setModelData(self, editor: QWidget, model: QAbstractItemModel,
                     index: QModelIndex):
        txt = editor.text()
        if txt is None:
            index.model().setData(index, None, Qt.EditRole)
            return
        index.model().setData(
            index,
            txt.replace(",", "") if self.__ValueType in [1, 2] else txt,
            Qt.EditRole)


class JPDelegate_ComboBox(_JPDelegate_Base):
    def __init__(self, parent: QObject = None, RowSource=[]):
        '''JPDelegate_ComboBox(parent: QObject = None, RowSource=[])\n
        RowSource为行来源 '''
        super().__init__(parent)
        self.RowSource = RowSource

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem,
                     index: QModelIndex) -> QWidget:
        wdgt = QComboBox(parent)
        
        for row in self.RowSource:
            wdgt.addItem(row[0], row[1])
        return wdgt

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        data = index.model().data(index, Qt.EditRole)
        if data is None:
            editor.setCurrentIndex(-1)
            return
        data = ord(data) if isinstance(data, bytes) else data
        for i, row in enumerate(self.RowSource):
            if row[1] == data:
                editor.setCurrentIndex(i)
                return

    def setModelData(self, editor: QWidget, model: QAbstractItemModel,
                     index: QModelIndex):
        index.model().setData(index, editor.currentData(), Qt.EditRole)


class JPDelegate_DateEdit(_JPDelegate_Base):
    def __init__(self, parent: QObject = None):
        '''JPDelegate_DateEdit(parent: QObject = None)'''
        super().__init__(parent)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem,
                     index: QModelIndex) -> QWidget:
        wdgt = QDateEdit(parent)
        return wdgt

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        data = index.model().data(index, Qt.EditRole)
        if data is None:
            return
        editor.setDate(JPDateConver(data, QDate))

    def setModelData(self, editor: QWidget, model: QAbstractItemModel,
                     index: QModelIndex):
        index.model().setData(index, JPDateConver(editor.date(),
                                                  datetime.date), Qt.EditRole)
