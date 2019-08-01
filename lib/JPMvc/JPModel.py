# -*- coding: utf-8 -*-

import datetime
from decimal import Decimal
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import (QAbstractTableModel, QDate, QModelIndex, QObject, Qt,
                          QVariant, pyqtSignal)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QTableView

import lib.JPMvc.JPDelegate as myDe
from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Field import JPFieldType
from lib.JPDatabase.Query import (JPQueryFieldInfo, JPTabelFieldInfo,
                                  JPTabelRowData)
from lib.JPFunction import (JPBooleanString, JPDateConver, JPGetDisplayText,
                            JPRound, PrintFunctionRunTime)
from lib.JPMvc import JPWidgets
from lib.ZionPublc import JPPub


class __JPTableViewModelBase(QAbstractTableModel):
    dataChanged = pyqtSignal(QModelIndex)
    firstHasDirty = pyqtSignal()
    editNext = pyqtSignal(QModelIndex)
    def __init__(self, tabelFieldInfo: JPTabelFieldInfo = None):
        super().__init__()
        self.TabelFieldInfo = tabelFieldInfo
        self.tableView = None
        self.__dirty = False
        self.__isCalculating = False

    def __setdirty(self, state: bool = True):
        # 第一次存在脏数据时，发送一个信号
        if self.__dirty is False and state is True:
            self.__dirty = True
            self.firstHasDirty.emit()

    @property
    def dirty(self) -> bool:
        """返回模型中是否有脏数据"""
        return self.__dirty

    def setTabelFieldInfo(self, tabelFieldInfo: JPTabelFieldInfo):
        tabelFieldInfo.Data = [
            JPTabelRowData(item) for item in tabelFieldInfo.Data
        ]
        self.TabelFieldInfo = tabelFieldInfo

    def getDataDict(self, role: int = Qt.DisplayRole):
        ''''按行返回数据字典的列表,一般用于打印'''
        dic = [
            self.TabelFieldInfo.getRowValueDict(i)
            for i in range(len(self.TabelFieldInfo))
        ]
        if role == Qt.EditRole:
            return dic
        if role == Qt.DisplayRole:
            r = {k: JPGetDisplayText(v) for k, v in dic.items()}
        return r

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

    def _getDecoration(self, Index: QModelIndex) -> QVariant():
        """返回 (QColor, QIcon or QPixmap)"""
        return QVariant()

    def data(self, Index: QModelIndex,
             role: int = Qt.DisplayRole) -> QVariant():
        c = Index.column()
        tf = self.TabelFieldInfo
        if not Index.isValid():
            raise Exception("行数或列数设置有误！")
        if role == Qt.TextAlignmentRole:
            return (Qt.AlignLeft
                    | Qt.AlignVCenter
                    ) if tf.Fields[c].RowSource else tf.Fields[c].Alignment
        elif role == Qt.DisplayRole:
            return tf.getDispText(Index)
        elif role == Qt.DecorationRole:
            return self._getDecoration(Index)
        elif role == Qt.TextColorRole:
            return QColor(Qt.black)
        elif role == Qt.BackgroundColorRole:
            return QColor(Qt.white)
        elif role == Qt.EditRole:
            # r, c, fn, tp, rs = self.__getPara(Index)
            return tf.getOnlyData(Index)

    def __formulaCacu(self, row_num: int):
        # 这个可能要重新写
        rd = self.TabelFieldInfo.RowsData[row_num]
        fms = [f for f in self.TabelFieldInfo.Fields if f.Formula]
        for fld in fms:
            try:
                d = rd.Datas
                v = eval(fld.Formula.format(*d))
                self.__isCalculating = True
                rd.setData(fld._index, v)
                self.__isCalculating = False
            except Exception:
                pass

    def setData(self, Index: QModelIndex, Any,
                role: int = Qt.EditRole) -> bool:
        t_inof = self.TabelFieldInfo
        t_inof.setData(Index, Any)
        self.__setdirty()
        if self.__isCalculating is False:
            self.__formulaCacu(Index.row())
        # 执行重载函数，判断行数据是否合法
        # 给函数参数的值 是最后一行的数据list
        row_data = t_inof.getRowData(len(t_inof.RowsData) - 1)
        tempv = self.AfterSetDataBeforeInsterRowEvent(row_data, Index)

        if isinstance(tempv, bool):
            if tempv:
                self.insertRows(self.rowCount())
        else:
            strErr = 'AfterSetDataBeforeInsterRowEvent函数的返回值必须为逻辑值！'
            raise TypeError(strErr)
        # 回车向右
        r, c = Index.row(), Index.column()
        tmp = None
        tmp = Index.sibling(r if r == self.rowCount() - 1 else r + 1,
                            0 if self.columnCount() - 1 else c + 1)
        if tmp.isValid():
            self.editNext.emit(tmp)

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
            flds = self.TabelFieldInfo.Fields
            return QVariant(flds[section].Title if flds[section].
                            Title else flds[section].FieldName)
        return QVariant(int(section + 1))

    def getColumnSum(self, col):
        """得到某一列的合计值"""
        tp = self.TabelFieldInfo.Fields[col].TypeCode
        rd = self.TabelFieldInfo.getOnlyData
        if tp in [tp == JPFieldType.Int, JPFieldType.Float]:
            if tp == JPFieldType.Int:
                r, con = 0, lambda v: int(v.to_eng_string())
            if tp == JPFieldType.Float:
                r, con = 0.0, lambda v: float(v.to_eng_string())
            for i in range(len(self.TabelFieldInfo.RowsData)):
                tempValue = rd([i, col])
                tempValue = tempValue if tempValue else 0
                r += tempValue
            return r
        raise TypeError("指定的列[{}]不能进行数值运算".format(col))

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        self.TabelFieldInfo.addRow()
        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.TabelFieldInfo.deleteRow(position)
        self.endRemoveRows()
        self.__setdirty()
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
    firstHasDirty = pyqtSignal()

    def __init__(self, Ui):
        super().__init__()
        self.__JPFormModelMainSub = None
        self.__sql = None
        self.__editMode = JPEditFormDataMode.ReadOnly
        #self._queryResult = None
        self.__dirty = False
        self.__fieldsRowSource = None
        self.ObjectDict = {}
        self.__findJPObject(Ui)

    def __setdirty(self, state: bool = True):
        # 第一次存在脏数据时，发送一个信号
        if self.__dirty is False and state is True:
            self.__dirty = True
            self.firstHasDirty.emit()

    @property
    def dirty(self) -> bool:
        """返回模型中是否有脏数据"""
        return self.__dirty

    def __findJPObject(self, Ui):
        cls_tup = (JPWidgets.QLineEdit, JPWidgets.QDateEdit,
                   JPWidgets.QComboBox, JPWidgets.QTextEdit,
                   JPWidgets.QCheckBox)
        d = Ui.__dict__
        self.ObjectDict = {
            n: c
            for n, c in d.items() if isinstance(c, cls_tup)
        }
        if len(self.ObjectDict) == 0:
            raise ValueError("请检查UI文件有没有更换Qwidgets的引用！")

    def setFormModelMainSub(self, mod):
        self.__JPFormModelMainSub = mod

    def _emitDataChange(self, arg):
        self.dataChanged.emit(arg)
        self.__setdirty()
        if self.__JPFormModelMainSub:
            self.__JPFormModelMainSub._emitDataChange(arg)

    def setTabelInfo(self, sql: str):
        self.__sql = sql
        #self.autoPkRole = auto_pk_role

    def setFieldsRowSource(self, lst: list):
        self.__fieldsRowSource = lst

    def readData(self):
        em = self.EditMode
        jpem = JPEditFormDataMode
        if em == jpem.ReadOnly:
            self.tableFieldsInfo = JPQueryFieldInfo(self.__sql)
        if em == jpem.Edit:
            self.tableFieldsInfo = JPTabelFieldInfo(self.__sql)
        if em == jpem.New:
            self.tableFieldsInfo = JPTabelFieldInfo(self.__sql, True)
        tf = self.tableFieldsInfo
        # 如果是亲增加或修改模式，主表增加一行数据
        if em != jpem.ReadOnly:
            tf.addRow()
        # 设置字段行来源
        if isinstance(self.__fieldsRowSource, (list, tuple)):
            for item in self.__fieldsRowSource:
                tf.setFieldsRowSource(*item)
        fld_dict = tf.getRowFieldsInfoAndDataDict(0)
        if fld_dict:
            for k, v in self.ObjectDict.items():
                if k in fld_dict:
                    v.setRowsData(tf.RowsData[0])
                    v.setFieldInfo(fld_dict[k])
                    v.setMainModel(self)
                    # 给输入控件指定查询的或增加的第一行数据

        # 设置编辑状态
        self.setEditState(self.EditMode != JPEditFormDataMode.ReadOnly)

        #self.mainForm.show()
    def setEditState(self, can_edit: bool = False):
        for item in self.ObjectDict.values():
            if isinstance(item, JPWidgets.QLineEdit):
                item.setReadOnly(not can_edit)
            if isinstance(item, JPWidgets.QDateEdit):
                item.setReadOnly(not can_edit)
            if isinstance(item, JPWidgets.QComboBox):
                item.setEnabled(can_edit)
            if isinstance(item, JPWidgets.QTextEdit):
                item.setReadOnly(not can_edit)
            if isinstance(item, JPWidgets.QCheckBox):
                item.setCheckable(not can_edit)

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

    def getSqls(self, pk_role: int = None):
        """返回主表的SQL语句，如果有检查空值错误，则引发一个错误，错误信息中包含字段名"""
        sqls = []
        pb = JPPub()
        appform = pb.MainForm
        nm_lst = []
        v_lst = []
        ds = self.tableFieldsInfo.RowsData[0].Datas
        st = self.EditMode
        # 空值检查
        for fld in self.tableFieldsInfo.Fields:
            if fld.IsPrimarykey or fld.Auto_Increment:
                continue
            if fld.NotNull:
                if ds[fld._index] is None:
                    raise ValueError(fld)
                    msg = '字段【{fn}】的值不能为空！\n'
                    msg = msg + 'Field [{fn}] cannot be empty!'.format(
                        fn=fld.FieldName)
                    QMessageBox.warning(appform, '提示', msg, QMessageBox.Ok,
                                        QMessageBox.Ok)
        # 空值检查完成
        TN = self.tableFieldsInfo.TableName

        sql_i = 'INSERT INTO ' + TN + ' ({}) VALUES ({});\n'
        sql_u = 'UPDATE ' + TN + ' SET {} WHERE {}={};\n'
        row_st = self.tableFieldsInfo.RowsData[0].State
        if (row_st == JPTabelRowData.New_None
                or row_st == JPTabelRowData.OriginalValue):
            return ''
        if st == self.New:
            for fld in self.tableFieldsInfo.Fields:
                if fld.IsPrimarykey:
                    if fld.Auto_Increment:
                        continue
                    else:
                        nm_lst.append(fld.FieldName)
                        v_lst.append('@PK')
                else:
                    nm_lst.append(fld.FieldName)
                    v_lst.append(fld.sqlValue(ds[fld._index]))
            sqls.append(sql_i.format(",".join(nm_lst), ",".join(v_lst)))
            if pk_role:
                newPKSQL = JPDb().NewPkSQL(pk_role)
                sqls = newPKSQL[0:2] + sqls + newPKSQL[2:]
            return sqls
        if st == self.Edit:
            for fld in self.tableFieldsInfo.Fields:
                if fld.IsPrimarykey:
                    r_pk_name = fld.FieldName
                    r_pk_v = fld.sqlValue(ds[fld._index])
                else:
                    nm_lst.append(fld.FieldName)
                    v_lst.append(fld.sqlValue(ds[fld._index]))
            temp = ['{}={}'.format(n, v) for n, v in zip(nm_lst, v_lst)]
            sqls.append(sql_u.format(",".join(temp), r_pk_name, r_pk_v))
            return sqls


class _JPFormModelSub(JPEditFormDataMode):
    dataChanged = pyqtSignal([QModelIndex])
    firstHasDirty = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__tableView = None
        self.__sql = None
        self._model = None
        self.__JPFormModelMainSub = None
        self.__hideColumns = []
        self.__columnWidths = []
        self.__readOnlyColumns = []
        self.__fieldsRowSource = []
        self.__formulas = []
        self.__dirty = False
        self.__editMode = JPEditFormDataMode.ReadOnly

    def setFormModelMainSub(self, mod):
        self.__JPFormModelMainSub = mod

    def _emitDataChange(self, arg):
        self.dataChanged.emit(arg)
        self.__setdirty()
        if self.__JPFormModelMainSub:
            self.__JPFormModelMainSub._emitDataChange(arg)

    def __setdirty(self, state: bool = True):
        # 第一次存在脏数据时，发送一个信号
        if self.__dirty is False and state is True:
            self.__dirty = True
            self.firstHasDirty.emit()

    @property
    def dirty(self) -> bool:
        """返回模型中是否有脏数据"""
        return self.__dirty

    @property
    def MainModel(self) -> JPFormModelMain:
        return self.__mainModel

    @MainModel.setter
    def MainModel(self, model: JPFormModelMain):
        self.__mainModel = model

    def setTabelInfo(self, sql: str):
        self.__sql = sql

    def getModel(self):
        return self._model

    def readData(self, subTableView: QTableView):
        self.__tableView = subTableView
        if self.EditMode is None:
            raise ValueError("没有指定子窗体的编辑模式！")
        # 建立子窗体模型
        self.tableFieldsInfo = JPTabelFieldInfo(
            self.__sql,
            True if self.EditMode == JPEditFormDataMode.New else None)
        if self.EditMode == JPEditFormDataMode.New and len(
                self.tableFieldsInfo.DeleteRows) == 0:
            self.tableFieldsInfo.addRow()
        if self.EditMode == JPEditFormDataMode.ReadOnly:
            self._model = JPTableViewModelReadOnly(subTableView,
                                                   self.tableFieldsInfo)
        if self.EditMode in [JPEditFormDataMode.Edit, JPEditFormDataMode.New]:
            self._model = JPTableViewModelEditForm(subTableView,
                                                   self.tableFieldsInfo)
        self.__tableView.setModel(self._model)
        self._model.dataChanged.connect(self._emitDataChange)
        # 设置子窗体可编辑状态
        self.setEditState(self.EditMode != JPEditFormDataMode.ReadOnly)
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

    def setEditState(self, can_edit: bool = False):
        st = {
            True: QAbstractItemView.AllEditTriggers,
            False: QAbstractItemView.NoEditTriggers
        }
        self.__tableView.setEditTriggers(st[can_edit])

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

    def getSqls(self):
        """返回子表的保存数据用SQL语句"""
        appform = JPPub().MainForm
        # 计算主窗体键名、键名列及键值
        m_main = self.MainModel
        if m_main.EditMode == self.readData:
            return ''
        t_main = m_main.tableFieldsInfo
        sub_main_pk_index = None
        main_pk_value = None
        for fld in self.tableFieldsInfo.Fields:
            if fld.FieldName == t_main.PrimarykeyFieldName:
                sub_main_pk_index = fld._index
        if sub_main_pk_index is None:
            raise ValueError("主窗体模型中竟然没有找到主键名，或子窗体模型中没有找到主键名")
        if self.EditMode == self.Edit:
            # 如果是编辑模式，则要取得主表的键值
            pk_i = t_main.PrimarykeyFieldIndex
            main_pk_value = t_main.Fields[pk_i].sqlValue(
                t_main.getOnlyData([0, pk_i]))
        else:
            main_pk_value = '@PK'
        if main_pk_value is None:
            raise ValueError("获取主表主键值失败！")
        # 检查空值
        null_msg = '第{row}行【{fn}】字段的值不能为空！\n'
        null_msg = null_msg + 'Row {row} field [{fn}] cannot be empty!'
        for r in range(len(self.tableFieldsInfo)):
            for c in range(len(self.tableFieldsInfo.Fields)):
                fld = self.tableFieldsInfo.Fields[c]
                if fld.Auto_Increment or fld.IsPrimarykey:
                    continue
                else:
                    if self.tableFieldsInfo.RowsData[
                            r].State == JPTabelRowData.New_None:
                        continue
                    if self.tableFieldsInfo.getOnlyData([r, c]) is None:
                        if fld.NotNull:
                            msg = null_msg.format(
                                row=r + 1,
                                fn=self.tableFieldsInfo.Fields[c].FieldName)
                            QMessageBox.warning(appform, '提示', msg,
                                                QMessageBox.Yes,
                                                QMessageBox.Yes)
                            return r

        # 开始生成SQL
        sqls = []
        TN = self.tableFieldsInfo.TableName
        sql_i = 'INSERT INTO ' + TN + ' ({}) VALUES ({});\n'
        sql_u = 'UPDATE ' + TN + ' SET {} WHERE {}={};\n'
        if self.EditMode == self.New:
            for row in self.tableFieldsInfo.RowsData:
                fn_lst = []
                v_lst = []
                r_st = row.State
                if (r_st == JPTabelRowData.OriginalValue
                        or r_st == JPTabelRowData.New_None):
                    continue
                else:
                    for fld in self.tableFieldsInfo.Fields:
                        if fld._index == sub_main_pk_index:
                            fn_lst.append(fld.FieldName)
                            v_lst.append(main_pk_value)
                            continue
                        if fld.IsPrimarykey:
                            if not fld.Auto_Increment:
                                errStr = "子表主键字段'{}'只能为自增加类型!"
                                raise ValueError(
                                    errStr.format(t_main.PrimarykeyFieldName))
                            else:
                                continue
                        fn_lst.append(fld.FieldName)
                        v_lst.append(fld.sqlValue(row.Datas[fld._index]))
                    sqls.append(sql_i.format(','.join(fn_lst),
                                             ','.join(v_lst)))

        elif self.EditMode == self.Edit:
            for row in self.tableFieldsInfo.RowsData:
                fn_lst = []
                v_lst = []
                r_st = row.State
                if (r_st == JPTabelRowData.OriginalValue
                        or r_st == JPTabelRowData.New_None):
                    continue
                else:
                    if r_st == JPTabelRowData.New:
                        for fld in self.tableFieldsInfo.Fields:
                            if fld._index == sub_main_pk_index:
                                fn_lst.append(fld.FieldName)
                                v_lst.append(main_pk_value)
                                continue
                            if fld.IsPrimarykey:
                                if not fld.Auto_Increment:
                                    errStr = "子表主键字段'{}'只能为自增加类型!"
                                    raise ValueError(
                                        errStr.format(
                                            t_main.PrimarykeyFieldName))
                                else:
                                    continue
                            fn_lst.append(fld.FieldName)
                            v_lst.append(fld.sqlValue(row.Datas[fld._index]))
                        sqls.append(
                            sql_i.format(','.join(fn_lst), ','.join(v_lst)))
                    if r_st == JPTabelRowData.Update:
                        for fld in self.tableFieldsInfo.Fields:
                            if fld._index == sub_main_pk_index:
                                fn_lst.append(fld.FieldName)
                                v_lst.append(main_pk_value)
                                continue
                            if fld.IsPrimarykey:
                                sub_pk_name = fld.FieldName
                                sub_pk_value = fld.sqlValue(
                                    row.Datas[fld._index])
                                continue
                            fn_lst.append(fld.FieldName)
                            v_lst.append(fld.sqlValue(row.Datas[fld._index]))
                            temp = [
                                '{}={}'.format(n, v)
                                for n, v in zip(fn_lst, v_lst)
                            ]
                        sqls.append(
                            sql_u.format(','.join(temp), sub_pk_name,
                                         sub_pk_value))
        return sqls


class JPFormModelMainSub(JPEditFormDataMode):
    dataChanged = pyqtSignal([QModelIndex], [JPWidgets.QWidget])
    firstHasDirty = pyqtSignal()

    def __init__(self, Ui, subTableView: QTableView):
        super().__init__()
        self.mainModel = JPFormModelMain(Ui)
        self.mainModel.setFormModelMainSub(self)
        self.tableView = subTableView
        self.subModel = _JPFormModelSub()
        self.subModel.setFormModelMainSub(self)
        self.__dirty = False

    def __setdirty(self, state: bool = True):
        # 第一次存在脏数据时，发送一个信号
        if self.__dirty is False and state is True:
            self.__dirty = True
            self.firstHasDirty.emit()

    @property
    def dirty(self) -> bool:
        """返回模型中是否有脏数据"""
        return self.__dirty

    def setUi(self, ui):
        self.mainModel.setUi(ui)

    def _emitDataChange(self, arg):
        if isinstance(arg, QModelIndex):
            self.dataChanged[QModelIndex].emit(arg)
        if isinstance(arg, JPWidgets.QWidget):
            self.dataChanged[JPWidgets.QWidget].emit(arg)
        self.__setdirty()

    def setTabelInfo(self, tabelName):
        self.tableView = tabelName

    def getSqls(self, pk_role: int = None):
        if (self.mainModel.dirty is False and self.subModel.dirty is False):
            raise ValueError("未输入数据或不存在未保存数据")
        sql_m = self.mainModel.getSqls()
        sql_s = self.subModel.getSqls()
        if pk_role:
            newPKSQL = JPDb().NewPkSQL(pk_role)
            sqls = newPKSQL[0:2] + sql_m + sql_s + newPKSQL[2:]
            return sqls
        else:
            return sql_m + sql_s

    def setEditState(self, can_edit: bool = False):
        self.mainModel.setEditState(can_edit)
        self.subModel.setEditState(can_edit)

    def show(self, edit_mode, pk_value: str = None):
        # 处理子窗体

        self.mainModel.EditMode = edit_mode
        self.subModel.EditMode = edit_mode
        self.subModel.readData(self.tableView)
        self.subModel.MainModel = self.mainModel
        self.mainModel.readData()
        self.mainModel.dataChanged.connect(self._emitDataChange)
        self.subModel._model.dataChanged.connect(self._emitDataChange)
        # 设置更新数据后计算重载方法
        t = self.subModel_AfterSetDataBeforeInsterRowEvent
        self.subModel._model.AfterSetDataBeforeInsterRowEvent = t

    def subModel_AfterSetDataBeforeInsterRowEvent(self, row_data,
                                                  Index: QModelIndex) -> True:
        '''子窗体更新数据后,执行此事件，可重载，返回值必须为逻辑值
        不重载时，默认不增加行，返回True时增加行
        '''
        return False
