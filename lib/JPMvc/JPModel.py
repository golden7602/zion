# -*- coding: utf-8 -*-

import datetime
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import (QAbstractTableModel, QDate, QModelIndex, Qt,
                          QVariant, pyqtSignal, QObject)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QAbstractItemView, QTableView

import lib.JPMvc.JPDelegate as myDe
from lib.JPDatabase.Field import JPFieldType
from lib.JPDatabase.Query import JPTabelRowData,JPTabelFieldInfo,JPQueryFieldInfo
#from lib.JPDatebase import (JPTabelFieldInfo, JPFieldType, JPTabelRowData)

from lib.JPFunction import (JPBooleanString, JPDateConver, JPRound,
                            JPGetDisplayText)
# from lib.JPMvc.JPWidgets import (QWidget, QCheckBox, QComboBox, QDateEdit,
#                                 QLineEdit, QTextEdit)
from lib.JPEnum import JPEditFormDataMode
from lib.JPMvc import JPWidgets
from decimal import Decimal


class __JPTableViewModelBase(QAbstractTableModel):
    dataChanged = pyqtSignal(QModelIndex)

    def __init__(self, tabelFieldInfo: JPTabelFieldInfo = None):
        super().__init__()
        # tabelFieldInfo.Data = [
        #     JPTabelRowData(item) for item in tabelFieldInfo.Data
        # ]
        self.TabelFieldInfo = tabelFieldInfo
        # self.del_data = []
        self.tableView = None

    def setTabelFieldInfo(self, tabelFieldInfo: JPTabelFieldInfo):
        tabelFieldInfo.Data = [
            JPTabelRowData(item) for item in tabelFieldInfo.Data
        ]
        self.TabelFieldInfo = tabelFieldInfo

    def getDataDict(self, role: int = Qt.DisplayRole):
        ''''按行返回数据字典的列表,一般用于打印'''
        r = []
        dic = [row.getDataDict() for row in self.TabelFieldInfo]
        if role == Qt.EditRole:
            return dic
        if role == Qt.DisplayRole:
            return {k: JPGetDisplayText(v) for k, v in dic.items()}
        return r

    # def setModelDataAndFields(self, data: list, fields: list):
    #     """设置模型数据源及字段信息
    #     data:列表，数据源。列表每一项为一行数据的列表，不能是元组
    #     fields：存储列表字段信息的列表，每一项为一个JPFieldInfo对象
    #     """
    #     self.TabelFieldInfo.Data= ([list(row) for row in data] if isinstance(
    #         data, tuple) else data)
    #     self.TabelFieldInfo.Fields = fields

    def __getPara(self, Index):
        c = Index.column()
        return (Index.row(), c, self.TabelFieldInfo.Fields[c].FieldName,
                self.TabelFieldInfo.Fields[c].TypeCode,
                self.TabelFieldInfo.Fields[c].RowSource)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.TabelFieldInfo)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.TabelFieldInfo.Fields)

    def _GetHeaderAlignment(self, Index: QModelIndex) -> int:
        return Qt.AlignCenter

    # def _GetDispText(self, Index: QModelIndex) -> str:
    #     r, c, = Index.row(), Index.column()
    #     rs = self.TabelFieldInfo.Fields[c].RowSource
    #     data_i = self.TabelFieldInfo.getOnlyData(Index)
    #     if data_i is None:
    #         return
    #     if rs:
    #         sel = [item for item in rs if item[1] == data_i]
    #         if len(sel) == 0:
    #             return QVariant()
    #         else:
    #             return QVariant(str(sel[0][0]))
    #     return JPGetDisplayText(data_i)

    def _getDecoration(self, Index: QModelIndex) -> QVariant():
        """返回 (QColor, QIcon or QPixmap)"""
        return QVariant()

    def data(self, Index: QModelIndex,
             role: int = Qt.DisplayRole) -> QVariant():
        r, c = Index.row(), Index.column()
        if not Index.isValid():
            raise Exception("行数或列数设置有误！")
        if role == Qt.TextAlignmentRole:
            return (
                Qt.AlignLeft
                | Qt.AlignVCenter) if self.TabelFieldInfo.Fields[
                    c].RowSource else self.TabelFieldInfo.Fields[c].Alignment
            #return int(self._GetDataAlignment(Index))
        elif role == Qt.DisplayRole:
            # return self._GetDispText(Index)
            return self.TabelFieldInfo.getDispText(Index)
        elif role == Qt.DecorationRole:
            return self._getDecoration(Index)
        elif role == Qt.TextColorRole:
            return QColor(Qt.black)
        elif role == Qt.BackgroundColorRole:
            return QColor(Qt.white)
        elif role == Qt.EditRole:
            r, c, fn, tp, rs = self.__getPara(Index)
            return self.TabelFieldInfo.getOnlyData(Index)

    def _formulaCacu(self, row_data: int):
        # 这个可能要重新写
        if isinstance(row_data, JPTabelRowData):
            d = row_data.InteriorData
        for i, fld in enumerate(self.TabelFieldInfo.Fields):
            if fld.Formula:
                try:
                    d[i] = eval(fld.Formula.format(*d))
                except Exception:
                    pass

    def setData(self, Index: QModelIndex, Any,
                role: int = Qt.EditRole) -> bool:
        #r, c = Index.row(), Index.column()
        self.TabelFieldInfo.setData(Index,Any)
        #self.TabelFieldInfo.Data[r].setData(c, Any)
        # cur_fld = self.TabelFieldInfo[r][c]

        # tp = cur_fld.TypeCode
        # if Any is None:
        #     self.TabelFieldInfo.Data[r][c] = None
        #     return True
        # if cur_fld.RowSource:
        #     self.TabelFieldInfo.Data[r][c] = Any
        #     return True
        # elif tp == JPFieldType.Int:
        #     if Any == '':
        #         return True
        #     self.TabelFieldInfo.Data[r][c] = int(str(Any).replace(',', ''))
        # elif tp == JPFieldType.Float:
        #     if Any == '':
        #         return True
        #     self.TabelFieldInfo.Data[r][c] = float(str(Any).replace(',', ''))
        # elif tp == JPFieldType.Boolean:
        #     self.TabelFieldInfo.Data[r][c] = (0 if Any == self.BooleanString[0]
        #                                       else 1)
        # elif tp == JPFieldType.Date:
        #     self.TabelFieldInfo.Data[r][c] = Any
        # else:
        #     self.TabelFieldInfo.Data[r][c] = Any
        self.dirty = True
        row_data=self.TabelFieldInfo.getRowData(Index.row())
        self._formulaCacu(row_data)
        # 执行重载函数，判断行数据是否合法
        tempv = self.AfterSetDataBeforeInsterRowEvent(row_data, Index)
        if isinstance(tempv, bool):
            if tempv:
                self.insertRows(self.rowCount())
        else:
            raise TypeError('AfterSetDataBeforeInsterRowEvent函数的返回值必须为逻辑值！')
        self.dataChanged[QModelIndex].emit(Index)
        return True

    def AfterSetDataBeforeInsterRowEvent(self, row_data,
                                         Index: QModelIndex) -> True:
        '''子窗体更新数据后,执行此事件，可重载，返回值必须为逻辑值
        不重载时，默认不增加行，返回True时增加行
       '''
        return False

    def setFormula(self, key: int, formula: str):
        """
        设置计算公式 {字段名}代表一个值
        本公式也用于增加新行前的检查，也用于列间的运算
        key为列号或字段名;formula格式示例如下：
        {7}=(JPRound({1},2) + NV({2},float))/2
        列2的值转换成浮点数与列3的值转换成浮点数和的一半
        等号左边为目标字段值，右边为公式，遵照python语法
        如果可以保证公式右边字段值不包含0，也可以不使用NV函数
        NV函数为一个自定义函数，用于防止None值并转换成指定类型
        JPRound函数为一个自定义函数,四舍五入
        """
        if isinstance(key, str):
            self.FieldsDict[key].Formula = formula
        if isinstance(key, int):
            self.Fields[key].Formula = formula

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(
            QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable)

    def headerData(self, section, Orientation,
                   role: int = Qt.DisplayRole) -> QVariant():
        if role != Qt.DisplayRole:
            return QVariant()
        if Orientation == Qt.Horizontal:
            return QVariant(self.TabelFieldInfo.Fields[section].Title if self.
                            TabelFieldInfo.Fields[section].Title else self.
                            TabelFieldInfo.Fields[section].FieldName)
        return QVariant(int(section + 1))

    def getColumnSum(self, col):
        """得到某一列的合计值"""
        tp = self.TabelFieldInfo.Fields[col].TypeCode
        if tp in [tp == JPFieldType.Int, JPFieldType.Float]:
            if tp == JPFieldType.Int:
                r, con = 0, lambda v: int(v.to_eng_string())
            if tp == JPFieldType.Float:
                r, con = 0.0, lambda v: float(v.to_eng_string())
            for row in self.TabelFieldInfo.Data:
                v = row[col] if row[col] else 0
                if isinstance(v, Decimal):
                    r += con(v)
                else:
                    r += v
            return r
        raise TypeError("指定的列[{}]不能进行数值运算".format(col))

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        self.TabelFieldInfo.addRow()
        # self.TabelFieldInfo.Data = (
        #     self.TabelFieldInfo.Data[:position] +
        #     [[None] * len(self.TabelFieldInfo.Fields)] +
        #     self.TabelFieldInfo.Data[position:])
        self.endInsertRows()
        self.dirty = True
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        #self.del_data.append(self.TabelFieldInfo.Data[position])
        self.TabelFieldInfo.deleteRow(position)
        #del self.TabelFieldInfo.Data[position]
        self.endRemoveRows()
        self.dirty = True
        return True

    def setColumnsDetegate(self):
        """setColumnsDetegate(TableView: QTableViewt)\n
        参数为需要设置代理的TableView控件"""
        tw = self.tableView
        if not isinstance(tw, QTableView):
            raise TypeError("setColumnsDetegate()方法有参数必须为QTableView")
        for col, fld in enumerate(self.TabelFieldInfo.Fields):
            tp = fld.TypeCode
            de = None
            if fld.RowSource:
                de = myDe.JPDelegate_ComboBox(tw, fld.RowSource)
            elif tp == JPFieldType.Int:
                de = myDe.JPDelegate_LineEdit(tw, 1)
            elif tp == JPFieldType.Float:
                de = myDe.JPDelegate_LineEdit(tw, 2, fld.Scale)
            elif tp == JPFieldType.Boolean:
                boostr = fld.RowSource if fld.RowSource else self.BooleanString
                de = myDe.JPDelegate_ComboBox(tw, boostr)
            elif tp == JPFieldType.Date:
                de = myDe.JPDelegate_DateEdit(tw)
            else:
                de = myDe.JPDelegate_LineEdit(tw)
            if de:
                tw.setItemDelegateForColumn(col, de)


class JPTableViewModelReadOnly(__JPTableViewModelBase):
    def __init__(self, tableView, tabelFieldInfo: JPTabelFieldInfo):
        ''' 
        建立一个只读型模型，仅仅用于展示内容，不可编辑\n
        JPTableModelReadOnly(tableView,tabelFieldInfo:TabelFieldInfo)
        '''
        super().__init__(tabelFieldInfo)
        # 设置只读
        self.tableView = tableView
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)


class JPTableViewModelEditForm(__JPTableViewModelBase):
    def __init__(self, tableView, tabelFieldInfo: JPTabelFieldInfo):
        ''' 
        建立一个可编辑模型\n
        JPTableViewModelEditForm(tableView,tabelFieldInfo:TabelFieldInfo)\n
        '''
        super().__init__(tabelFieldInfo)
        self.tableView = tableView



class JPFormModelMain(JPEditFormDataMode):
    dataChanged = pyqtSignal([JPWidgets.QWidget])

    def __init__(self, mainform):
        super().__init__()
        self.mainForm = mainform
        self.__JPFormModelMainSub = None
        self.__sql = None
        self.autoPkRole = None
        self.__editMode = JPEditFormDataMode.ReadOnly
        self._queryResult = None
        self.__fieldsRowSource = None
        self.ObjectDict = {}

    def setUi(self, ui):
        cls_tup = (JPWidgets.QLineEdit, JPWidgets.QDateEdit,
                   JPWidgets.QComboBox, JPWidgets.QTextEdit,
                   JPWidgets.QCheckBox)
        d = ui.__dict__
        self.ObjectDict = {
            n: c
            for n, c in d.items() if isinstance(c, cls_tup)
        }

    def setFormModelMainSub(self, mod):
        self.__JPFormModelMainSub = mod

    def _emmitDataChange(self, arg):
        #print(arg.objectName() + "   emit")
        self.dataChanged.emit(arg)
        if self.__JPFormModelMainSub:
            self.__JPFormModelMainSub._emmitDataChange(arg)

    def setTabelInfo(self, sql: str, auto_pk_role: int = None):
        self.__sql = sql
        self.autoPkRole = auto_pk_role

    def setFieldsRowSource(self, lst: list):
        self.__fieldsRowSource = lst

    def readData(self):
        nodata = False if self.EditMode in [
            JPEditFormDataMode.Edit, JPEditFormDataMode.ReadOnly
        ] else True
        self.tableFieldsInfo = JPTabelFieldInfo(self.__sql, nodata)
        if (self.EditMode == JPEditFormDataMode.New
                and len(self.tableFieldsInfo.Data)) == 0:
            self.tableFieldsInfo.addRowWithOutValue()
        # 设置字段行来源
        for item in self.__fieldsRowSource:
            self.tableFieldsInfo.setFieldsRowSource(*item)
        fld_dict = self.tableFieldsInfo[0].getFieldsDict()
        if fld_dict:
            for k, v in self.ObjectDict.items():
                if k in fld_dict:
                    v.setFieldInfo(fld_dict[k])
                    v.setMainModel(self)
        self.mainForm.show()

    def setObjectValue(self, obj_name: str, value):
        """按名称设置一个控件的值"""
        if obj_name in self.ObjectDict:
            obj = self.ObjectDict[obj_name]
            fld = obj.FieldInfo
            fld.Value = value
            obj.setFieldInfo(fld, False)
        else:
            raise KeyError(
                '字段[{}]不在主窗体中未找到，请检查主窗体控件名，或指定的对象名！\n主窗体中的控件有[{}]'.format(
                    obj_name, ','.join(self.ObjectDict.keys())))

    def getObjectValue(self, obj_name: str):
        """返回指定控件的实际值，可用于计算，数值型字段为None时，将返回0"""
        return self.ObjectDict[obj_name].Value()


class _JPFormModelSub(JPEditFormDataMode):
    def __init__(self):
        super().__init__()
        self.__tableView = None
        self.__sql = None
        self._model = None
        self.__hideColumns = []
        self.__columnWidths = []
        self.__readOnlyColumns = []
        self.__fieldsRowSource = []
        self.__formulas = []
        self.__editMode = JPEditFormDataMode.ReadOnly

    def setTabelInfo(self, sql: str):
        self.__sql = sql

    def getModel(self):
        return self._model

    def readData(self, subTableView: QTableView):
        self.__tableView = subTableView
        if self.EditMode is None:
            raise ValueError("没有指定子窗体的编辑模式！")
        # 建立子窗体模型
        self.__tableInfo = JPTabelFieldInfo(
            self.__sql,
            True if self.EditMode == JPEditFormDataMode.New else None)
        if self.EditMode == JPEditFormDataMode.New and len(
                self.__tableInfo.Data) == 0:
            self.__tableInfo.addRowWithOutValue()
        if self.EditMode == JPEditFormDataMode.ReadOnly:
            self._model = JPTableViewModelReadOnly(subTableView,
                                                   self.__tableInfo)
        if self.EditMode in [JPEditFormDataMode.Edit, JPEditFormDataMode.New]:
            self._model = JPTableViewModelEditForm(subTableView,
                                                   self.__tableInfo)
        self.__tableView.setModel(self._model)
        # 设置子窗体可编辑状态
        if self.EditMode == JPEditFormDataMode.ReadOnly:
            self.__tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        if self.EditMode in [JPEditFormDataMode.Edit, JPEditFormDataMode.New]:
            self.__tableView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        # 设置子窗体的输入委托控件及格式等
        tv = self.__tableView
        self._model.setColumnsDetegate()
        for col in self.__readOnlyColumns:
            tv.setItemDelegateForColumn(col, myDe.JPDelegate_ReadOnly(tv))
        for col in self.__hideColumns:
            tv.setColumnHidden(col, True)
        for i, w in enumerate(self.__columnWidths):
            subTableView.setColumnWidth(i, w)
        for field_key, data in self.__fieldsRowSource:
            self._model.TabelFieldInfo.setFieldsRowSource(field_key, data)
        # 设置字段计算公式
        for i, f in self.__formulas:
            self._model.TabelFieldInfo.Fields[i].Formula = f

    def setFormula(self, key: [int, str], formula: str):
        """
        设置计算公式 {字段名}代表一个值
        本公式也用于增加新行前的检查，也用于列间的运算
        key为列号或字段名;formula格式示例如下：
        {7}=(JPRound({1},2) + NV({2},float))/2
        列2的值转换成浮点数与列3的值转换成浮点数和的一半
        等号左边为目标字段值，右边为公式，遵照python语法
        如果可以保证公式右边字段值不包含0，也可以不使用NV函数
        NV函数为一个自定义函数，用于防止None值并转换成指定类型
        JPRound函数为一个自定义函数,四舍五入
        """
        self.__formulas.append((key, formula))

    def setFieldsRowSource(self, *args):
        self.__fieldsRowSource = args

    def setColumnsHidden(self, *args: int):
        """设置隐藏列的列号，如有多个列，请设置一个列表"""
        self.__hideColumns = args

    def setColumnWidths(self, *args: int):
        self.__columnWidths = args

    def setColumnsReadOnly(self, *args: int):
        self.__readOnlyColumns = args

    def GetSQLS(self):
        return self._model.GetSQLS()


class JPFormModelMainSub(JPEditFormDataMode):
    dataChanged = pyqtSignal([QModelIndex], [JPWidgets.QWidget])

    def __init__(self, mainform, subTableView: QTableView):
        super().__init__()
        self.mainModel = JPFormModelMain(mainform)
        self.mainModel.setFormModelMainSub(self)
        self.tableView = subTableView
        self.subModel = _JPFormModelSub()

    def setUi(self, ui):
        self.mainModel.setUi(ui)

    def _emmitDataChange(self, arg):
        try:
            print(arg.row(), arg.column())
        except AttributeError:
            print(arg.objectName())
        if isinstance(arg, QModelIndex):
            self.dataChanged[QModelIndex].emit(arg)
        if isinstance(arg, JPWidgets.QWidget):
            self.dataChanged[JPWidgets.QWidget].emit(arg)

    def setTabelInfo(self, tabelName):
        self.tableView = tabelName

    def show(self, edit_mode, pk_value: str = None):
        # 处理子窗体

        self.mainModel.EditMode = edit_mode
        self.subModel.EditMode = edit_mode
        self.subModel.readData(self.tableView)
        self.mainModel.readData()
        self.subModel._model.dataChanged.connect(self._emmitDataChange)
        # 设置更新数据后计算重载方法
        t = self.subModel_AfterSetDataBeforeInsterRowEvent
        self.subModel._model.AfterSetDataBeforeInsterRowEvent = t

    def subModel_AfterSetDataBeforeInsterRowEvent(self, row_data,
                                                  Index: QModelIndex) -> True:
        '''子窗体更新数据后,执行此事件，可重载，返回值必须为逻辑值
        不重载时，默认不增加行，返回True时增加行
        '''
        return False
