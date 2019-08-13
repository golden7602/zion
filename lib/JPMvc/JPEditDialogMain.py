from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtWidgets import (QDialog, QWidget, QMessageBox, QMenu)
from lib.JPMvc.JPModel import JPFormModelMain, JPEditFormDataMode
from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot, pyqtSignal
from lib.ZionPublc import JPPub
from lib.JPDatabase.Database import JPDb
from lib.JPPrintReport import JPReport


class JPEditDialogMain(QDialog):
    afterSaveData = pyqtSignal([str])

    def __init__(self,
                 clsUi=None,
                 edit_mode: JPEditFormDataMode = JPEditFormDataMode.ReadOnly,
                 pkValue=None,
                 mainSql=None,
                 flags=Qt.WindowFlags()):
        pub = JPPub()
        super().__init__(parent=pub.MainForm, flags=flags)
        self.ui = clsUi()
        self.ui.setupUi(self)
        self.EditMode = edit_mode
        if self.EditMode in (JPEditFormDataMode.New, JPEditFormDataMode.Edit):
            self.ui.butSave.setEnabled(False)
            self.ui.butPrint.setEnabled(False)
            self.ui.butPDF.setEnabled(False)
        self.curPK = pkValue if pkValue else ''
        self.mainSql = mainSql.format(self.curPK)
        self.__PKRole = None
        # if subSql:
        #     self.tv = self.ui.tableView
        #     self.MainModle = self.MainSubModle.mainModel
        #     self.MainModle.setFieldsRowSource(
        #         self.setMainFormFieldsRowSources())
        #     self.MainModle.setTabelInfo(self.mainSql)
        #     f = self.setSubFormFormula()
        #     if f:
        #         self.SubModle.setFormula(*f)
        #     h = self.__getList(self.setSubFormColumnsHidden())
        #     if h:
        #         self.SubModle.setColumnsHidden(*h)
        #     r = self.__getList(self.setSubFormColumnsReadOnly())
        #     if r:
        #         self.SubModle.setColumnsReadOnly(*r)
        #     w = self.__getList(self.setSubFormColumnWidths())
        #     if w:
        #         self.SubModle.setColumnWidths(*w)
        #     self.SubModle.setTabelInfo(self.subSql)
        #     self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        #     self.ui.tableView.customContextMenuRequested.connect(
        #         self.__right_menu)
        #     self.MainSubModle.firstHasDirty.connect(self.__firstDirty)
        #     self.MainSubModle.dataChanged[QModelIndex].connect(
        #         self._onDataChange)
        #     self.MainSubModle.dataChanged[QWidget].connect(self._onDataChange)
        #     self.MainSubModle.show(edit_mode)
        # else:
        self.MainModle = self.getMainMode()(self.ui)
        self.MainModle.setFieldsRowSource(
            self.setMainFormFieldsRowSources())
        self.MainModle.setTabelInfo(self.mainSql)
        self.MainModle.EditMode = edit_mode
        self.MainModle.firstHasDirty.connect(self.__firstDirty)
        self.MainModle.dataChanged[QWidget].connect(self._onDataChange)
        self.MainModle.readData()

    def __getList(self, r):
        if isinstance(r, list):
            return r
        if isinstance(r, tuple):
            return list(r)
        if r is None:
            return []
        a = []
        a.append(r)
        return a

    def setPkRole(self, role: int):
        self.__PKRole = role

    def __right_menu(self, pos):
        menu = QMenu()
        tv = self.ui.tableView
        mod = self.SubModle._model.tableFieldsInfo
        opt1 = menu.addAction("AddNew增加")
        opt2 = menu.addAction("Delete删除")
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

    def setListForm(self, FunctionForm):
        self.__FunctionForm = FunctionForm

    def getMainMode(self) -> JPFormModelMain:
        """返回主窗体处理子类，必须继承自JPFormModelMain"""
        return JPFormModelMain

    def getPrintReport(self) -> JPReport:
        """返回主窗体处理子类，必须继承自JPReport"""
        return JPReport()

    def setSubFormFormula(self):
        '''返回两个值col: int, Formula: str'''
        return

    def setSubFormColumnsHidden(self):
        return []

    def setSubFormColumnsReadOnly(self):
        return []

    def setSubFormColumnWidths(self):
        return []

    def setMainFormFieldsRowSources(self):
        return []

    def afterDataChangedCalculat(self, obj):
        """数据变化后执行该方法，请覆盖"""
        return

    def _onDataChange(self, obj):
        md = self.MainModle
        md.dataChanged[QWidget].disconnect(self._onDataChange)
        self.afterDataChangedCalculat(obj)
        md.dataChanged[QWidget].connect(self._onDataChange)

    def afterSaveDate(self, data):
        """保存数据后执行该方法，一般用于根据此参数修改窗口状态，请覆盖"""
        return

    def firstDirty(self):
        """当主表及子表存在脏数据（未保存数据时）执行该方法，请覆盖"""
        return

    def __firstDirty(self):
        self.ui.butSave.setEnabled(True)

    @pyqtSlot()
    def on_butSave_clicked(self):
        try:
            lst = self.MainModle.getSqls(self.__PKRole)
            isOK, result = JPDb().executeTransaction(lst)
            if isOK:
                self.afterSaveDate(result)
                self.ui.butSave.setEnabled(False)
                self.ui.butPrint.setEnabled(True)
                self.ui.butPDF.setEnabled(True)
                if self.subSql:
                    self.MainSubModle.setEditState(False)
                else:
                    self.MainModle.setEditState(False)
                self.afterSaveData.emit(result)
                self.__FunctionForm._locationRow(result)
                QMessageBox.information(self, '完成',
                                        '保存数据完成！\nSave data complete!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()

    @pyqtSlot()
    def on_butPrint_clicked(self):
        rpt = self.getPrintReport()()
        rpt.PrintCurrentReport(self.ui.fOrderID.text())