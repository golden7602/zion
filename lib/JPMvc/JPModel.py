# -*- coding: utf-8 -*-

import datetime
import os
import sys
sys.path.append(os.getcwd())
from PyQt5.QtCore import (QAbstractTableModel, QDate, QModelIndex, Qt,
                          QVariant, pyqtSignal, QObject)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QAbstractItemView, QTableView

import lib.JPMvc.JPDelegate as myDe
from lib.JPDatebase import (JPTabelFieldInfo, JPFieldType)

from lib.JPFunction import (JPBooleanString, JPDateConver, JPRound,
                            JPGetDisplayText)
# from lib.JPMvc.JPWidgets import (QWidget, QCheckBox, QComboBox, QDateEdit,
#                                 QLineEdit, QTextEdit)
from lib.JPMvc import JPWidgets
from decimal import Decimal


class __JPTableViewModelBase(QAbstractTableModel):
    dataChanged = pyqtSignal(QModelIndex)

    def __init__(self, tabelFieldInfo: JPTabelFieldInfo = None):
        super().__init__()
        self.TabelFieldInfo = tabelFieldInfo
        self.fields = self.TabelFieldInfo.Fields if tabelFieldInfo else []
        self.basedata = self.TabelFieldInfo.Data if tabelFieldInfo else []
        self.del_data = []
        self.tableView = None

    def setTabelFieldInfo(self, tabelFieldInfo: JPTabelFieldInfo):
        self.TabelFieldInfo = tabelFieldInfo
        self.fields = self.TabelFieldInfo.Fields
        self.basedata = self.TabelFieldInfo.Data

    # def __init__(self, data: list = [], fields: list = []):
    #     super().__init__()
    #     self.db = JPDb()
    #     self.dirty = False
    #     self.del_data = []
    #     self.update_index = {}
    #     self.tableView = None
    #     self.basedata = []
    #     if data:
    #         self.basedata = ([list(row) for row in data] if isinstance(
    #             data, tuple) else data)
    #     if fields:
    #         self.fields = fields

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
    #     self.basedata = ([list(row) for row in data] if isinstance(
    #         data, tuple) else data)
    #     self.fields = fields

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

    # def _GetDataAlignment(self, Index: QModelIndex) -> int:
    #     if self.fields[Index.column()].RowSource:
    #         return (Qt.AlignLeft | Qt.AlignVCenter)
    #     else:
    #         return self.result_DataAlignment[self.fields[
    #             Index.column()].TypeCode]

    # def _GetDispText(self, Index: QModelIndex) -> int:
    #     r, c, fn, tp, rs = self.__getPara(Index)
    #     data_i = self.basedata[r][c]
    #     if data_i is None:
    #         return
    #     if rs:
    #         sel = [item for item in rs if item[1] == data_i]
    #         if len(sel) == 0:
    #             return QVariant()
    #         else:
    #             return QVariant(str(sel[0][0]))
    #     return JPGetDisplayText(data_i)
    def _GetDispText(self, Index: QModelIndex) -> str:
        r, c, = Index.row(), Index.column()
        rs = self.fields[c].RowSource
        data_i = self.basedata[r][c]
        if data_i is None:
            return
        if rs:
            sel = [item for item in rs if item[1] == data_i]
            if len(sel) == 0:
                return QVariant()
            else:
                return QVariant(str(sel[0][0]))
        return JPGetDisplayText(data_i)

    def _getDecoration(self, Index: QModelIndex) -> QVariant():
        """返回 (QColor, QIcon or QPixmap)"""
        return QVariant()

    def data(self, Index: QModelIndex,
             role: int = Qt.DisplayRole) -> QVariant():
        r, c = Index.row(), Index.column()
        if not Index.isValid():
            raise Exception("行数或列数设置有误！")
        if role == Qt.TextAlignmentRole:
            return (Qt.AlignLeft
                    | Qt.AlignVCenter
                    ) if self.fields[c].RowSource else self.fields[c].Alignment
            #return int(self._GetDataAlignment(Index))
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
            return self.TabelFieldInfo[r][c].Value

    def _formulaCacu(self, row_data: int):
        # 这个可能要重新写
        for i, fld in enumerate(self.fields):
            if fld.Formula:
                try:
                    row_data[i] = eval(fld.Formula.format(*row_data))
                except Exception:
                    pass

    def setData(self, Index: QModelIndex, Any,
                role: int = Qt.EditRole) -> bool:
        r, c = Index.row(), Index.column()
        cur_fld = self.TabelFieldInfo[r][c]
        tp = cur_fld.TypeCode
        if Any is None:
            cur_fld.value = None
            return True
        if cur_fld.RowSource:
            cur_fld.value = Any
            return True
        elif tp == JPFieldType.Int:
            if Any == '':
                return True
            cur_fld.value = int(str(Any).replace(',', ''))
        elif tp == JPFieldType.Float:
            if Any == '':
                return True
            cur_fld.value = float(str(Any).replace(',', ''))
        elif tp == JPFieldType.Boolean:
            cur_fld.value = (0 if Any == self.BooleanString[0] else 1)
        elif tp == JPFieldType.Date:
            cur_fld.value = Any
        else:
            cur_fld.value = Any
        self.dirty = True
        self._formulaCacu(self.basedata[r])
        # 执行重载函数，判断行数据是否合法
        tempv = self.AfterSetDataBeforeInsterRowEvent(self.basedata[r], Index)
        if isinstance(tempv, bool):
            if tempv:
                self.insertRows(self.rowCount())
        else:
            raise TypeError('AfterSetDataBeforeInsterRowEvent函数的返回值必须为逻辑值！')
        self.dataChanged[QModelIndex].emit(Index)
        return True

    def AfterSetDataBeforeInsterRowEvent(row_data, Index: QModelIndex) -> True:
        '''更新数据后，计算公式值,可重载，返回值必须为逻辑值
       不重载时，默认不增加行
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
            return QVariant(self.fields[section].Title if self.fields[section].
                            Title else self.fields[section].FieldName)
        return QVariant(int(section + 1))

    def getColumnSum(self, col):
        """得到某一列的合计值"""
        tp = self.fields[col].TypeCode
        if tp in [tp == JPFieldType.Int, JPFieldType.Float]:
            if tp == JPFieldType.Int:
                r, con = 0, lambda v: int(v.to_eng_string())
            if tp == JPFieldType.Float:
                r, con = 0.0, lambda v: float(v.to_eng_string())
            for row in self.basedata:
                v = row[col] if row[col] else 0
                if isinstance(v, Decimal):
                    r += con(v)
                else:
                    r += v
            return r
        raise TypeError("指定的列[{}]不能进行数值运算".format(col))

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

    def setColumnsDetegate(self):
        """setColumnsDetegate(TableView: QTableViewt)\n
        参数为需要设置代理的TableView控件"""
        tw = self.tableView
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
        self.__sql = None
        self.autoPkRole = None
        self.__editMode = JPEditFormDataMode.ReadOnly
        self._queryResult = None
        self.__fieldsRowSource = None
        self.ObjectDict = {
            obj.objectName(): obj
            for obj in self.mainForm.findChildren((JPWidgets.QLineEdit,
                                                   JPWidgets.QDateEdit,
                                                   JPWidgets.QComboBox,
                                                   JPWidgets.QTextEdit,
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

    def setFieldsRowSource(self, lst: list):
        self.__fieldsRowSource = lst

    def readData(self):
        nodata = True if self.EditMode in [
            JPEditFormDataMode.Edit, JPEditFormDataMode.ReadOnly
        ] else False
        self.tableFieldsInfo = JPTabelFieldInfo(self.__sql, nodata)
        fld_dict = self.tableFieldsInfo.FieldsDict
        if fld_dict:
            for k, v in self.ObjectDict.items():
                if k in fld_dict:
                    v.setFieldInfo(fld_dict[k])
                    v.setMainModel(self)

        # self._queryResult = JPMySqlSingleTableQuery(
        #     self.__sql, True if md == JPEditFormDataMode.New else None)
        # if self.__fieldsRowSource:
        #     self._queryResult.setFieldsRowSource(self.__fieldsRowSource)
        # # 更新主窗体属性的语句
        # if md in [JPEditFormDataMode.Edit, JPEditFormDataMode.ReadOnly]:
        #     if len(self._queryResult.data) == 0:
        #         raise ValueError(
        #             '查询未返回数据，无法更新窗体！\nQuery did not return data, can not update the form!'
        #         )
        #     flds = {
        #         fld.FieldName: fld
        #         for fld in self._queryResult.getRecordFieldInfo(0)
        #     }
        #     for k, v in self.ObjectDict.items():
        #         if k in flds:
        #             v.setFieldInfo(flds[k])
        #         v.setMainModel(self)
        # if md == JPEditFormDataMode.ReadOnly:
        #     for obj in self.ObjectDict.values():
        #         obj.setFocusPolicy(Qt.NoFocus)
        #         v.setMainModel(self)
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

    def setTabelInfo(self, sql: str):
        self.__sql = sql

    def getModel(self):
        return self._model

    def readData(
            self,
            subTableView: QTableView,
    ):
        self.__tableView = subTableView
        if self.EditMode is None:
            raise ValueError("没有指定子窗体的编辑模式！")
        # 建立子窗体模型
        self.__tableInfo = JPTabelFieldInfo(
            self.__sql,
            True if self.EditMode == JPEditFormDataMode.New else None)
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
        # 设置子窗体的输入委托控件
        self._model.setColumnsDetegate(self.__tableView)

        # self._queryResult = JPMySqlSingleTableQuery(
        #     self.__sql,
        #     True if self.EditMode == JPEditFormDataMode.New else None)
        # if self.__fieldsRowSource:
        #     mod.setModelDataAndFields(que.data, self.__fieldsRowSource)
        # mod.setTabelFieldInfo(self.__ta)
        # mod.setModelDataAndFields(que.data, que.Fields)
        # tv.setModel(mod)
        # no_ed = QAbstractItemView.NoEditTriggers
        # all_ed = QAbstractItemView.AllEditTriggers
        # tv.setEditTriggers(no_ed if self.EditMode ==
        #                    JPEditFormDataMode.ReadOnly else all_ed)

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
