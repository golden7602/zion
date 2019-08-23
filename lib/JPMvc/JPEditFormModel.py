import abc
import datetime
import re
from decimal import Decimal
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import (QDate, QModelIndex, QObject, Qt, QVariant,
                          pyqtSignal, pyqtSlot)
from PyQt5.QtWidgets import (QAbstractItemView, QDialog, QMenu, QMessageBox,
                             QTableView)

import lib.JPMvc.JPDelegate as myDe
from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Query import (JPQueryFieldInfo, JPTabelFieldInfo,
                                  JPTabelRowData)
from lib.JPFunction import JPRound
from lib.JPMvc import JPWidgets
from lib.JPMvc.JPModel import (JPTableViewModelEditForm,
                               JPTableViewModelReadOnly)
from lib.JPPrintReport import JPReport
from lib.ZionPublc import JPPub
from lib.JPException import JPExceptionFieldNull, JPExceptionRowDataNull


class JPEditFormDataMode():
    """本类为编辑窗口数据类型的枚举"""
    Edit = 1
    ReadOnly = 2
    New = 3


class JPFormModelMain(QDialog):
    afterSaveData = pyqtSignal([str])

    def __init__(self,
                 Ui,
                 sql_main: str = None,
                 PKValue=None,
                 edit_mode=JPEditFormDataMode.ReadOnly,
                 flags=Qt.WindowFlags()):
        pub = JPPub()
        super().__init__(parent=pub.MainForm, flags=flags)
        self.ui = Ui
        self.ui.setupUi(self)
        self.mainSQL = sql_main
        self.PKRole = None
        self.__dirty = False
        self.__Formulas = []
        self.__ReadOnlyFieldsName = []
        self._loadDdata = None
        self.__ObjectDict = {}
        self.__formulas = []
        self.EditMode = edit_mode
        self.PKValue = PKValue
        self.ui.butSave.setEnabled(False)
        if self.EditMode != JPEditFormDataMode.ReadOnly:
            self.ui.butSave.setEnabled(False)
            self.ui.butPrint.setEnabled(False)
            self.ui.butPDF.setEnabled(False)

    def setPkRole(self, role: int):
        self.PKRole = role

    @property
    def ObjectDict(self) -> dict:
        dic = self.__ObjectDict
        if dic:
            return dic
        dic = self.findChildren(
            (JPWidgets.QLineEdit, JPWidgets.QDateEdit, JPWidgets.QComboBox,
             JPWidgets.QTextEdit, JPWidgets.QCheckBox))
        lst_field = [k for k in self.mainTableFieldsInfo.FieldsDict.keys()]
        dic = {
            obj.objectName(): obj
            for obj in dic if obj.objectName() in lst_field
        }
        if dic:
            self.__ObjectDict = dic
            return self.__ObjectDict
        else:
            raise ValueError("请检查UI文件有没有更换Qwidgets的引用！")

    @property
    def dirty(self) -> bool:
        """返回模型中是否有脏数据"""
        return self.__dirty

    def setListForm(self, FunctionForm):
        self.__FunctionForm = FunctionForm

    def onGetMainFormFieldsRowSources(self):
        """设置主窗体字段的数据源"""
        return []

    @property
    def isReadOnlyMode(self):
        return self.EditMode == JPEditFormDataMode.ReadOnly

    @property
    def isEditMode(self):
        return self.EditMode == JPEditFormDataMode.Edit

    @property
    def isNewMode(self):
        return self.EditMode == JPEditFormDataMode.New

    def setFormulas(self, *args):
        """setFormulas(str1...)
        设置计算公式，从个公式之间用逗号分开"""
    def onDateChangeEvent(self, obj, value):
        """窗体数据变更事件，obj是变更的控件"""
        return

    def cacuFormula(self, Formula: str):
        fa = Formula
        mt = re.match(r"\{(\S+)\}\s*=(.+)", fa, flags=(re.I))
        try:
            fLeft = mt.groups()[0]
            fRight = mt.groups()[1]
        except Exception:
            raise ValueError("公式解析错误")
        v = None
        values = {k: v.Value() for k, v in self.ObjectDict.items()}
        fa_v = fRight.format(**values)
        try:
            v = eval(fa_v)
        except Exception:
            pass
        finally:
            self.setObjectValue(fLeft, v)

    def _emitDataChange(self, obj, value):
        self.onDateChangeEvent(obj, value)
        # 第一次存在脏数据时，发送一个信号
        if self.__dirty is False:
            self.__dirty = True
            self.ui.butSave.setEnabled(True)
            self.onFirstHasDirty()

    def onFirstHasDirty(self):
        """第一次出现脏数据时引执行此事件，请覆盖"""
        return

    def setSQL(self, sql: str):
        self.mainSQL = sql

    def readData(self):
        self._loadDdata = True
        self.mainTableFieldsInfo = JPTabelFieldInfo(
            self.mainSQL.format(self.PKValue),
            (self.EditMode == JPEditFormDataMode.New))
        tf = self.mainTableFieldsInfo
        # 如果是新增模式，添加一行数据
        if self.EditMode == JPEditFormDataMode.New:
            tf.addRow()
        # 设置字段行来源
        temp = self.onGetFieldsRowSources()
        if isinstance(temp, (list, tuple)):
            for item in temp:
                tf.setFieldsRowSource(*item)
        fld_dict = tf.getRowFieldsInfoDict(0)
        if fld_dict:
            for k, v in self.ObjectDict.items():
                if k in fld_dict:
                    v.setRowsData(tf.DataRows[0])
                    v.setMainModel(self)
                    v.setFieldInfo(fld_dict[k])

        if self.EditMode == JPEditFormDataMode.ReadOnly:
            self.setEditState(False)
        else:
            self.setEditState(True)
            self.__setReadOnlyFields()
            self.__setFieldsDisabled()

    def __setReadOnlyFields(self):
        # 设置只读字段
        self.__ReadOnlyFieldsName = self.onGetReadOnlyFields()
        for n in self.__ReadOnlyFieldsName:
            if n in self.ObjectDict.keys():
                self.ObjectDict[n].setReadOnly(False)

    def __setFieldsDisabled(self):
        tp = (JPWidgets.QLineEdit, JPWidgets.QDateEdit, JPWidgets.QComboBox,
              JPWidgets.QTextEdit, JPWidgets.QCheckBox)
        self.__DisableFieldsName = self.onGetDisableFields()
        if self.isReadOnlyMode:
            for obj in self.ObjectDict.values():
                obj.setEnabled(False)
            return
        for n in self.__DisableFieldsName:
            obj = self.findChild(tp, n)
            if obj:
                obj.setEnabled(False)

    def setEditState(self, can_edit: bool = False):
        for obj in self.ObjectDict.values():
            obj.setReadOnly(not can_edit)
        self.__setReadOnlyFields()
        self.__setFieldsDisabled()

    def onGetReadOnlyFields(self) -> list:
        """设置主窗体只读字段"""
        return []

    def onGetFieldsRowSources(self) -> list:
        """设置主窗体字段行来源"""
        return []

    def onGetDisableFields(self) -> list:
        """设置主窗体禁用字段"""
        return []

    def setObjectValue(self, obj_name: str, value):
        """按名称设置一个控件的值"""
        if obj_name in self.ObjectDict:
            obj = self.ObjectDict[obj_name]
            obj.refreshValueNotRaiseEvent(value, True)
        else:
            raise KeyError(
                '字段[{}]不在主窗体中未找到，请检查主窗体控件名，或指定的对象名！\n主窗体中的控件有[{}]'.format(
                    obj_name, ','.join(self.ObjectDict.keys())))

    def getObjectValue(self, obj_name: str):
        """返回指定控件的实际值，可用于计算，数值型字段为None时，将返回0"""
        return self.ObjectDict[obj_name].Value()

    @abc.abstractmethod
    def onGetPrintReport(self) -> JPReport:
        """返回主窗体处理子类，必须继承自JPReport"""
        pass

    def onAfterSaveData(self, data):
        """保存数据后执行，请覆盖"""
        return

    @pyqtSlot()
    def on_butSave_clicked(self):
        try:
            lst = self.getSqls(self.PKRole)
            isOK, result = JPDb().executeTransaction(lst)
            if isOK:
                self.onAfterSaveData(result)
                self.ui.butSave.setEnabled(False)
                self.ui.butPrint.setEnabled(True)
                self.ui.butPDF.setEnabled(True)
                # self.MainModle.setEditState(False)
                self.afterSaveData.emit(result)
                QMessageBox.information(self, '完成',
                                        '保存数据完成！\nSave data complete!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()

    @pyqtSlot()
    def on_butPrint_clicked(self):
        return

    def getSqls(self, pk_role: int = None):
        """返回主表的SQL语句，如果有检查空值错误，则引发一个错误，错误信息中包含字段名"""
        sqls = []
        pb = JPPub()
        appform = pb.MainForm
        nm_lst = []
        v_lst = []
        mti = self.mainTableFieldsInfo
        ds = mti.DataRows[0].Datas
        st = self.EditMode
        # 空值检查
        # for fld in mti.Fields:
        #     if fld.IsPrimarykey or fld.Auto_Increment:
        #         continue
        #     if fld.NotNull:
        #         if self.ObjectDict[fld.FieldName].getSqlValue() == 'Null':
        #             raise ValueError(fld)
        #             msg = '字段【{fn}】的值不能为空！\n'
        #             msg = msg + 'Field [{fn}] cannot be empty!'.format(
        #                 fn=fld.FieldName)
        #             QMessageBox.warning(appform, '提示', msg, QMessageBox.Ok,
        #                                 QMessageBox.Ok)
        # # 空值检查完成
        TN = mti.TableName

        sql_i = 'INSERT INTO ' + TN + ' ({}) VALUES ({});\n'
        sql_u = 'UPDATE ' + TN + ' SET {} WHERE {}={};\n'
        row_st = mti.DataRows[0].State
        if (row_st == JPTabelRowData.New_None
                or row_st == JPTabelRowData.OriginalValue):
            return ''
        if st == JPEditFormDataMode.New:
            for fld in mti.Fields:
                if fld.IsPrimarykey:
                    if fld.Auto_Increment:
                        continue
                    else:
                        nm_lst.append(fld.FieldName)
                        v_lst.append('@PK')
                else:
                    nm_lst.append(fld.FieldName)
                    v_lst.append(self.ObjectDict[fld.FieldName].getSqlValue())
            sqls.append(sql_i.format(",".join(nm_lst), ",".join(v_lst)))
            if pk_role:
                newPKSQL = JPDb().NewPkSQL(pk_role)
                sqls = newPKSQL[0:2] + sqls + newPKSQL[2:]
            return sqls
        if st == JPEditFormDataMode.Edit:
            for fld in mti.Fields:
                if fld.IsPrimarykey:
                    r_pk_name = fld.FieldName
                    r_pk_v = fld.sqlValue(ds[fld._index])
                else:
                    nm_lst.append(fld.FieldName)
                    v_lst.append(self.ObjectDict[fld.FieldName].getSqlValue())
            temp = ['{}={}'.format(n, v) for n, v in zip(nm_lst, v_lst)]
            sqls.append(sql_u.format(",".join(temp), r_pk_name, r_pk_v))
            return sqls


class JPFormModelMainHasSub(JPFormModelMain):
    def __init__(self,
                 Ui,
                 sql_main=None,
                 PKValue=None,
                 sql_sub=None,
                 edit_mode=JPEditFormDataMode.ReadOnly,
                 flags=Qt.WindowFlags()):
        super().__init__(Ui,
                         sql_main=sql_main,
                         PKValue=PKValue,
                         edit_mode=edit_mode,
                         flags=flags)
        self.subSQL = sql_sub

    def setSQL(self, sql_main, sql_sub):
        super().setSQL(sql_main)
        self.subSQL = sql_sub

    def readData(self):
        super().readData()
        self.__readSubData()

    def setEditState(self, can_edit: bool = False):
        super().setEditState(can_edit)
        st = {
            True: QAbstractItemView.AllEditTriggers,
            False: QAbstractItemView.NoEditTriggers
        }
        self.ui.tableView.setEditTriggers(st[can_edit])

    def getSqls(self, pk_role=None):

        # 以下返回主表的保存语句
        mainSaveSQLs = super().getSqls(pk_role=pk_role)
        if mainSaveSQLs:
            sql2 = mainSaveSQLs[0:len(mainSaveSQLs) - 1]
            sql_r = mainSaveSQLs[len(mainSaveSQLs) - 1:]
        else:
            return
        subSaveSQls = self.__getSubSQLs()
        if pk_role:
            return sql2 + subSaveSQls + sql_r
        else:
            return mainSaveSQLs + subSaveSQls

    def __readSubData(self):
        tv = self.ui.tableView
        em = self.EditMode
        JFDM = JPEditFormDataMode
        if em is None:
            raise ValueError("没有指定子窗体的编辑模式！")
        # 建立子窗体模型
        # self.subTableFieldsInfo = JPTabelFieldInfo(
        #     self.subSQL, True if em == JFDM.New else None)
        # tfi = self.subTableFieldsInfo
        if self.isNewMode:
            tfi = JPTabelFieldInfo(self.subSQL, False)
            if len(tfi.DeleteRows) == 0:
                tfi.addRow()
            self.SubModel = JPTableViewModelEditForm(tv, tfi)
        if self.isReadOnlyMode:
            tfi = JPQueryFieldInfo(self.subSQL.format(self.PKValue))
            self.SubModel = JPTableViewModelReadOnly(tv, tfi)
        if self.isEditMode:
            tfi = JPTabelFieldInfo(self.subSQL.format(self.PKValue))
            self.SubModel = JPTableViewModelEditForm(tv, tfi)
        self.subTableFieldsInfo = tfi

        # if em == JFDM.New and len(tfi.DeleteRows) == 0:
        #     tfi.addRow()
        # if em == JFDM.ReadOnly:
        #     self.SubModel = JPTableViewModelReadOnly(tv, tfi)
        # if em in [JFDM.Edit, JFDM.New]:
        #     self.SubModel = JPTableViewModelEditForm(tv, tfi)

        smd = self.SubModel
        tv.setModel(smd)

        smd.dataChanged.connect(self._emitDataChange)
        # 设置子窗体可编辑状态
        self.setEditState(em != JFDM.ReadOnly)
        # 设置子窗体的输入委托控件及格式等

        self.__readOnlyColumns = self.onGetReadOnlyColumns()
        smd.setColumnsDetegate()
        for col in self.__readOnlyColumns:
            tv.setItemDelegateForColumn(col, myDe.JPDelegate_ReadOnly(tv))
        self.__hideColumns = self.onGetHiddenColumns()
        for col in self.__hideColumns:
            tv.setColumnHidden(col, True)
        self.__columnWidths = self.onGetColumnWidths()
        for i, w in enumerate(self.__columnWidths):
            tv.setColumnWidth(i, w)
        self.__columnsRowSources = self.onGetColumnRowSources()
        for field_key, data, bind_col in self.__columnsRowSources:
            smd.TabelFieldInfo.Fields[field_key].BindingColumn = bind_col
            smd.TabelFieldInfo.setFieldsRowSource(field_key, data)
        # 设置字段计算公式
        for i, f in self.onGetColumnFormulas():
            smd.TabelFieldInfo.Fields[i].Formula = f
        temp = self.AfterSetDataBeforeInsterRowEvent
        smd.AfterSetDataBeforeInsterRowEvent = temp
        # 添加右键菜单
        if self.EditMode != JFDM.ReadOnly:
            tv.setContextMenuPolicy(Qt.CustomContextMenu)
            tv.customContextMenuRequested.connect(self.__right_menu)

    def __right_menu(self, pos):
        menu = QMenu()
        tv = self.ui.tableView
        mod = self.SubModel
        opt1 = menu.addAction("AddNew增加")
        opt2 = menu.addAction("Delete删除")
        index =self.ui.tableView.selectionModel().currentIndex().row()
        opt1.setEnabled(False)
        opt2.setEnabled((index == -1
                         or index != (len(mod.TabelFieldInfo) - 1)))
        action = menu.exec_(tv.mapToGlobal(pos))
        if action == opt1:
            mod.insertRows(len(mod.DataRows))
            tv.selectRow(mod.rowCount() - 1)
            return
        elif action == opt2:
            mod.removeRows(tv.selectionModel().currentIndex().row())
            return
        else:
            return

    def getColumnSum(self, col: int):
        return self.SubModel.getColumnSum(col)

    def onGetColumnRowSources(self, *args):
        return []

    def onGetHiddenColumns(self, ):
        """设置隐藏列的列号，如有多个列，请设置一个列表"""
        return []

    def onGetColumnWidths(self, ):
        return []

    def onGetReadOnlyColumns(self):
        return []

    def onGetColumnFormulas(self):
        """
        设置子表计算公式 {字段名}代表一个值
        本公式也用于增加新行前的检查，也用于列间的运算
        key为列号或字段名;formula格式示例如下：
        {7}=(JPRound({1},2) + NV({2},float))/2
        列2的值转换成浮点数与列3的值转换成浮点数和的一半
        等号左边为目标字段值，右边为公式，遵照python语法
        如果可以保证公式右边字段值不包含0，也可以不使用NV函数
        NV函数为一个自定义函数，用于防止None值并转换成指定类型
        JPRound函数为一个自定义函数,四舍五入
        """
        return []

    def AfterSetDataBeforeInsterRowEvent(self, row_data,
                                         Index: QModelIndex) -> True:
        '''子窗体更新数据后,执行此事件，可重载，返回值必须为逻辑值
        不重载时，默认不增加行，返回True时增加行
        '''
        return False

    def __getSubSQLs(self):
        # 以下返回子表的保存数据用SQL语句"""
        appform = JPPub().MainForm
        # 计算主窗体键名、键名列及键值
        if self.isReadOnlyMode:
            return ''
        t_main = self.mainTableFieldsInfo
        tfi = self.subTableFieldsInfo
        sub_main_pk_index = None
        main_pk_value = None
        for fld in tfi.Fields:
            if fld.FieldName == t_main.PrimarykeyFieldName:
                sub_main_pk_index = fld._index
        if sub_main_pk_index is None:
            raise ValueError("主窗体模型中竟然没有找到主键名，或子窗体模型中没有找到主键名")
        if self.isEditMode:
            # 如果是编辑模式，则要取得主表的键值
            pk_i = t_main.PrimarykeyFieldIndex
            main_pk_value = t_main.Fields[pk_i].sqlValue(
                t_main.getOnlyData([0, pk_i]))
        else:
            main_pk_value = '@PK'
        if main_pk_value is None:
            raise ValueError("获取主表主键值失败！")
        # 检查空值
        for r in range(len(tfi)):
            for c in range(len(tfi.Fields)):
                fld = tfi.Fields[c]
                if fld.Auto_Increment or fld.IsPrimarykey:
                    continue
                else:
                    if tfi.DataRows[r].State == JPTabelRowData.New_None:
                        continue
                    if tfi.getOnlyData([r, c]) is None:
                        if fld.NotNull:
                            raise JPExceptionRowDataNull(
                                (r + 1, tfi.Fields[c].FieldName))

        # 开始生成SQL
        sqls = []
        TN = tfi.TableName
        sql_i = 'INSERT INTO ' + TN + ' ({}) VALUES ({});\n'
        sql_u = 'UPDATE ' + TN + ' SET {} WHERE {}={};\n'
        if self.isNewMode:
            for row in tfi.DataRows:
                fn_lst = []
                v_lst = []
                r_st = row.State
                if (r_st == JPTabelRowData.OriginalValue
                        or r_st == JPTabelRowData.New_None):
                    continue
                else:
                    for fld in tfi.Fields:
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

        elif self.isEditMode:
            for row in tfi.DataRows:
                fn_lst = []
                v_lst = []
                r_st = row.State
                if (r_st == JPTabelRowData.OriginalValue
                        or r_st == JPTabelRowData.New_None):
                    continue
                else:
                    if r_st == JPTabelRowData.New:
                        for fld in tfi.Fields:
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
                        for fld in tfi.Fields:
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

    @pyqtSlot()
    def on_butSave_clicked(self):
        try:
            lst = self.getSqls(self.PKRole)
            isOK, result = JPDb().executeTransaction(lst)
            if isOK:
                self.onAfterSaveData(result)
                self.ui.butSave.setEnabled(False)
                self.ui.butPrint.setEnabled(True)
                self.ui.butPDF.setEnabled(True)
                # self.MainModle.setEditState(False)
                self.afterSaveData.emit(result)
                QMessageBox.information(self, '完成',
                                        '保存数据完成！\nSave data complete!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()
