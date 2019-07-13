# -*- coding: utf-8 -*-
# @Time    : 19-12-1 下午3:26
# @Author  : JPT
# @Site    :
# @File    : JPTableModel\__init__.py
# @Software: VS Code
#  测试提交
import datetime
import os
import sys
sys.path.append(os.getcwd())
from PyQt5.QtCore import (QAbstractTableModel, QDate, QModelIndex, Qt,
                          QVariant, pyqtSignal, QObject)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QAbstractItemView, QTableView

import lib.JPMvc.JPDelegate as myDe
from lib.JPDatebase import JPDb, JPMySQLFieldInfo, JPMySqlSingleTableQuery
from lib.JPDatebase import JPFieldType
from lib.JPFunction import (JPBooleanString, JPDateConver, JPRound,
                            JPGetDisplayText)
# from lib.JPMvc.JPWidgets import (QWidget, QCheckBox, QComboBox, QDateEdit,
#                                 QLineEdit, QTextEdit)
from lib.JPMvc import JPWidgets
from decimal import Decimal


class __JPTableViewModelBase(QAbstractTableModel):
    dataChanged = pyqtSignal(QModelIndex)
    # BooleanString = JPBooleanString().getBooleanString()
    result_DataAlignment = {
        JPFieldType.Int: (Qt.AlignRight | Qt.AlignVCenter),
        JPFieldType.Float: (Qt.AlignRight | Qt.AlignVCenter),
        JPFieldType.String: (Qt.AlignLeft | Qt.AlignVCenter),
        JPFieldType.Date: (Qt.AlignCenter),
        JPFieldType.Boolean: (Qt.AlignCenter),
        JPFieldType.Other: (Qt.AlignRight | Qt.AlignVCenter)
    }

    def __init__(self, data: list = [], fields: list = []):
        super().__init__()
        self.db = JPDb()
        self.dirty = False
        self.del_data = []
        self.update_index = {}
        self.tableView = None

        if data:
            self.basedata = ([list(row) for row in data] if isinstance(
                data, tuple) else data)
        if fields:
            self.fields = fields

    def setModelDataAndFields(self, data: list, fields: list):
        """设置模型数据源及字段信息
        data:列表，数据源。列表每一项为一行数据的列表，不能是元组
        fields：存储列表字段信息的列表，每一项为一个JPFieldInfo对象
        """
        self.basedata = ([list(row) for row in data] if isinstance(
            data, tuple) else data)
        self.fields = fields

    def __getPara(self, Index):
        c = Index.column()
        return (Index.row(), c, self.fields[c].FieldName,
                self.fields[c].TypeCode, self.fields[c].RowSource)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.basedata)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.fields)

    def _GetHeaderAlignment(self, Index: QModelIndex) -> int:
        return Qt.AlignCenter

    def _GetDataAlignment(self, Index: QModelIndex) -> int:
        if self.fields[Index.column()].RowSource:
            return (Qt.AlignLeft | Qt.AlignVCenter)
        else:
            return self.result_DataAlignment[self.fields[
                Index.column()].TypeCode]

    def _GetDispText(self, Index: QModelIndex) -> int:
        r, c, fn, tp, rs = self.__getPara(Index)
        data_i = self.basedata[r][c]
        if data_i is None:
            return
        if rs:
            sel = [item for item in rs if item[1] == data_i]
            if len(sel) == 0:
                return QVariant()
            else:
                return QVariant(str(sel[0][0]))
        # return self.Result_DispText[tp](data_i)
        return JPGetDisplayText(data_i)

    def _getDecoration(self, Index: QModelIndex) -> QVariant():
        """返回 (QColor, QIcon or QPixmap)"""
        return QVariant()

    def data(self, Index: QModelIndex,
             role: int = Qt.DisplayRole) -> QVariant():
        if not Index.isValid():
            raise Exception("行数或列数设置有误！")
        if role == Qt.TextAlignmentRole:
            return int(self._GetDataAlignment(Index))
        elif role == Qt.DisplayRole:
            return self._GetDispText(Index)
        elif role == Qt.DecorationRole:
            return self._getDecoration(Index)
        elif role == Qt.TextColorRole:
            return QColor(Qt.black)
        elif role == Qt.BackgroundColorRole:
            return QColor(Qt.white)
        elif role == Qt.EditRole:
            r, c, fn, tp, rs = self.__getPara(Index)
            return self.basedata[r][c]

    def _formulaCacu(self, row_data: int):
        for i, fld in enumerate(self.fields):
            if fld.Formula:
                try:
                    row_data[i] = eval(fld.Formula.format(*row_data))
                except Exception:
                    pass

    def setData(self, Index: QModelIndex, Any,
                role: int = Qt.EditRole) -> bool:
        r, c, fn, tp, rs = self.__getPara(Index)
        try:
            self.update_index[r].append(c)
            self.update_index[r] = list(set(self.update_index[r]))
        except KeyError:
            self.update_index[r] = [c]
        if Any is None:
            self.basedata[r][c] = None
            return True

        if rs:
            self.basedata[r][c] = Any
            return True

        elif tp == JPFieldType.Int:
            if Any == '':
                return True
            self.basedata[r][c] = int(str(Any).replace(',', ''))
        elif tp == JPFieldType.Float:
            if Any == '':
                return True
            self.basedata[r][c] = float(str(Any).replace(',', ''))
        elif tp == JPFieldType.Boolean:
            self.basedata[r][c] = (0 if Any == self.BooleanString[0] else 1)
        elif tp == JPFieldType.Date:
            self.basedata[r][c] = Any
        else:
            self.basedata[r][c] = Any
        self.dirty = True
        self._formulaCacu(self.basedata[r])
        self._afterSetData(self.basedata[r], Index)

        self.dataChanged[QModelIndex].emit(Index)
        return True

    def _afterSetData(self, row_data=None, index=None):
        '''更新数据后，计算公式值,可重载'''
        return

    def setFormula(self, col: int, formula: str):
        """
        设置计算公式 {字段名}代表一个值
        本公式也用于增加新行前的检查，也用于列间的运算
        col为列号;formula格式示例如下：
        {7}=(JPRound({1},2) + NV({2},float))/2
        列2的值转换成浮点数与列3的值转换成浮点数和的一半
        等号左边为目标字段值，右边为公式，遵照python语法
        如果可以保证公式右边字段值不包含0，也可以不使用NV函数
        NV函数为一个自定义函数，用于防止None值并转换成指定类型
        JPRound函数为一个自定义函数,四舍五入
        """
        self.fields[col].Formula = formula

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
            return QVariant(self.fields[section].Title if self.fields[section].
                            Title else self.fields[section].FieldName)
        return QVariant(int(section + 1))

    def getColumnSum(self, col):
        """得到某一列的合计值"""
        tp = self.fields[col].TypeCode
        if tp == JPFieldType.Int:
            r = 0
            for row in self.basedata:
                v = row[col] if row[col] else 0
                if isinstance(v, Decimal):
                    r += int(v.to_eng_string())
                else:
                    r += v
            return r
        if tp == JPFieldType.Float:
            r = 0.0
            for row in self.basedata:
                v = row[col] if row[col] else 0.0
                if isinstance(v, Decimal):
                    r += float(v.to_eng_string())
                else:
                    r += v
            return r
        raise TypeError("指定的列[{}]不能进行数值运算".format(col))
        # if self.fields[col].TypeCode in [JPFieldType.Int, JPFieldType.Float]:
        #     v = sum([row[col] if row[col] else 0 for row in self.basedata])
        #     return float(v.to_eng_string()) if isinstance(v, Decimal) else v
        # else:

        # return None


class JPTableViewModelReadOnly(__JPTableViewModelBase):
    def __init__(self, tableView, data: list = [], fields: list = []):
        ''' 
        建立一个只读型模型，仅仅用于展示内容，不可编辑\n
        JPTableModelReadOnly(tableView, data, fields)\n
        参数：\n
        data 一个数据列表或元组\n
        field字段信息列表
        '''
        super().__init__(data, fields)
        # 设置只读
        self.tableView=tableView
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setModel(self)


class JPTableViewModelEditForm(__JPTableViewModelBase):
    def __init__(self, data: list = [], fields: list = []):
        ''' 
        建立一个可编辑模型\n
        JPTableModelReadOnly(tableView,data,fields)\n
        参数：\n
        tableView 使用此列表的tableView对象\n
        data 一个数据列表或元组\n
        field字段信息列表
        '''
        super().__init__(data, fields)
        self.__RowValidatableFunction = None
        self.__ChangeCurrentItemToNewRow = False

    def __checkAndAddRow(self, index, *args, **kwargs):
        data = self.basedata
        if self.__RowValidatableFunction(data, index.row(), index.column()):
            row_num = self.rowCount()
            self.insertRows(row_num)

    def _afterSetData(self, row_data=None, Index=None):
        '''更新数据后，计算公式值,重载'''
        self._formulaCacu(row_data)
        if self.__RowValidatableFunction and self.__checkAndAddRow:
            self.__checkAndAddRow(Index)

    def setAutoAddRow(self,
                      RowValidatableFunction=None,
                      ChangeCurrentItemToNewRow=False):
        '''
        setAutoAddRow(RowValidatableFunction->bool)
        设置是否进行自动加行
        RowValidatableFunction为一个回调函数。
        该回调函数可接收以下参数：
        data:int 当前正在修改的数据列表;row,当前行，col:当前列号
        该函数返回值为True将在表尾增加一行
        ChangeCurrentItemToNewRow为真时，增加新行后，光标定位到新行
        '''
        self.__autoAddNewState = True
        self.__RowValidatableFunction = RowValidatableFunction
        self.__ChangeCurrentItemToNewRow = ChangeCurrentItemToNewRow

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        self.basedata = (self.basedata[:position] +
                         [[None] * len(self.fields)] +
                         self.basedata[position:])
        self.endInsertRows()
        self.dirty = True
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.del_data.append(self.basedata[position])
        del self.basedata[position]
        self.endRemoveRows()
        self.dirty = True
        return True

    def setColumnsDetegate(self, tableView: QTableView):
        """setColumnsDetegate(TableView: QTableViewt)\n
        参数为需要设置代理的TableView控件"""
        tw = tableView
        if not isinstance(tw, QTableView):
            raise TypeError("setColumnsDetegate()方法有参数必须为QTableView")
        for col, fld in enumerate(self.fields):
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

    # def GetSQLS(self) -> dict:
    #     d = self.basedata
    #     fs = self.fields
    #     pk_col = [i for i, f in enumerate(fs) if f.IsPrimarykey]
    #     if len[pk_col] == 0:
    #         raise ValueError("数据表中未包含主键字段！")
    #     else:
    #         pk_col = pk_col[0]
    #     no_pk_fld = {
    #         i: f
    #         for i, f in enumerate(fs)
    #         if f.IsPrimarykey is False and f.Auto_Increment is False
    #     }

    #     # 检查空值
    #     not_null_cols = [k for k, f in no_pk_fld.items if f.NotNull is True]

    #     for r, line in enumerate(d):
    #         for i in not_null_cols:
    #             if line[i] is None:
    #                 raise ValueError("第{}行[{}]字段的值不能为空！".format(
    #                     r + 1, fs[i].FieldName))
    #     sqls = {}
    #     sqls["DELETE"] = []
    #     if self.del_data:
    #         s = str(tuple(self.del_data))
    #         sqls["DELETE"] = "delete from {} where {} in {}".format(s)
    #     sqls["INSERT"] = []
    #     sqls["UPDATE"] = []

    #     def getRow():
    #         for i, r in enumerate(d):
    #             bz = 1 if r[pk_col] is None else 0
    #             yield bz, i, r

    #     for bz, i, r in getRow():
    #         if bz == 1:
    #             pass


class JPEditFormDataMode(QObject):
    """本类为编辑窗口数据类型的枚举"""
    Edit = 1
    ReadOnly = 2
    New = 3

    def __init__(self):
        super().__init__()
        self.EditMode = JPEditFormDataMode.ReadOnly


class JPFormModelMain(JPEditFormDataMode):
    dataChanged = pyqtSignal([JPWidgets.QWidget])

    def __init__(self, mainform):
        super().__init__()
        self.mainForm = mainform
        self.__JPFormModelMainSub = None
        # self.fieldsdict = {}
        # self.PKName = None
        self.__sql = None
        self.autoPkRole = None
        self.__editMode = JPEditFormDataMode.ReadOnly
        self._queryResult = None
        self.__fieldsRowSource = None
        self.ObjectDict = {
            obj.objectName(): obj
            for obj in self.mainForm.findChildren((JPWidgets.QLineEdit, JPWidgets.QDateEdit,
                                                   JPWidgets.QComboBox, JPWidgets.QTextEdit,
                                                   JPWidgets.QCheckBox))
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

    def setFieldsRowSource(self, lst:list):
        self.__fieldsRowSource = lst

    def readData(self):
        md = self.EditMode
        self._queryResult = JPMySqlSingleTableQuery(
            self.__sql, True if md == JPEditFormDataMode.New else None)
        if self.__fieldsRowSource:
            self._queryResult.setFieldsRowSource(self.__fieldsRowSource)
        # 更新主窗体属性的语句
        if md in [JPEditFormDataMode.Edit, JPEditFormDataMode.ReadOnly]:
            if len(self._queryResult.data) == 0:
                raise ValueError(
                    '查询未返回数据，无法更新窗体！\nQuery did not return data, can not update the form!'
                )
            flds = {
                fld.FieldName: fld
                for fld in self._queryResult.getRecordFieldInfo(0)
            }
            for k, v in self.ObjectDict.items():
                if k in flds:
                    v.setFieldInfo(flds[k])
                v.setMainModel(self)
        if md == JPEditFormDataMode.ReadOnly:
            for obj in self.ObjectDict.values():
                obj.setFocusPolicy(Qt.NoFocus)
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
        self.__fieldsRowSource = None
        self.__sql = None
        self._model = JPTableViewModelEditForm()
        self.__hideColumns = []
        self.__columnWidths = []
        self.__readOnlyColumns = []
        self.__formulas = []

    def setTabelInfo(self, sql: str):
        self.__sql = sql

    def setFieldsRowSource(self, *args):
        self.__fieldsRowSource = args

    def setAutoAddRow(self,
                      RowValidatableFunction=None,
                      ChangeCurrentItemToNewRow=False):
        '''
        setAutoAddRow(RowValidatableFunction->bool)
        设置是否进行自动加行
        RowValidatableFunction为一个回调函数。
        该回调函数可接收以下参数：
        data:int 当前正在修改的数据列表;row,当前行，col:当前列号
        该函数返回值为True将在表尾增加一行
        ChangeCurrentItemToNewRow为真时，增加新行后，光标定位到新行
        '''

        self._model.setAutoAddRow(RowValidatableFunction,
                                  ChangeCurrentItemToNewRow)

    def setColumnsHidden(self, *args: int):
        """设置隐藏列的列号，如有多个列，请设置一个列表"""
        self.__hideColumns = args

    def setColumnWidths(self, *args: int):
        self.__columnWidths = args

    def setColumnsReadOnly(self, *args: int):
        self.__readOnlyColumns = args

    def setFormula(self, col: int, formula: str):
        """
        设置计算公式 {字段名}代表一个值
        本公式也用于增加新行前的检查，也用于列间的运算
        col为列号;formula格式示例如下：
        {7}=(JPRound({1},2) + NV({2},float))/2
        列2的值转换成浮点数与列3的值转换成浮点数和的一半
        等号左边为目标字段值，右边为公式，遵照python语法
        如果可以保证公式右边字段值不包含0，也可以不使用NV函数
        NV函数为一个自定义函数，用于防止None值并转换成指定类型
        JPRound函数为一个自定义函数,四舍五入
        """
        self.__formulas.append((col, formula))

    def getColumnSum(self, col):
        """得到某一列的合计值"""
        return self._model.getColumnSum(col)

    def readData(
            self,
            subTableView: QTableView,
    ):
        mod = self._model
        tv = subTableView
        self.__tableView = subTableView
        self._queryResult = JPMySqlSingleTableQuery(
            self.__sql,
            True if self.EditMode == JPEditFormDataMode.New else None)
        que = self._queryResult
        if self.__fieldsRowSource:
            mod.setModelDataAndFields(que.data, self.__fieldsRowSource)
        mod.setModelDataAndFields(que.data, que.Fields)
        tv.setModel(mod)
        for i, f in self.__formulas:
            mod.setFormula(i, f)
        no_ed = QAbstractItemView.NoEditTriggers
        all_ed = QAbstractItemView.AllEditTriggers
        tv.setEditTriggers(no_ed if self.EditMode ==
                           JPEditFormDataMode.ReadOnly else all_ed)
        mod.setColumnsDetegate(tv)
        for col in self.__readOnlyColumns:
            tv.setItemDelegateForColumn(col, myDe.JPDelegate_ReadOnly(tv))
        for col in self.__hideColumns:
            tv.setColumnHidden(col, True)
        for i, w in enumerate(self.__columnWidths):
            subTableView.setColumnWidth(i, w)

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
        self.subModel._model.dataChanged.connect(self._emmitDataChange)
        self.mainModel.EditMode = edit_mode
        self.subModel.EditMode = edit_mode
        self.subModel.readData(self.tableView)
        self.mainModel.readData()
