import datetime
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from dateutil.relativedelta import relativedelta
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QAbstractItemView, QCheckBox, QComboBox,
                             QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
                             QTableView, QVBoxLayout, QWidget, QPushButton,
                             QMessageBox)
from PyQt5.QtCore import QCoreApplication, QSize, Qt, pyqtSlot
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPModel import JPFormModelMainSub, JPTableViewModelReadOnly
from lib.JPFunction import setButtonIcon
from lib.JPDatabase.Database import JPDb
from Ui.Ui_FuncFormMob import Ui_Form
import re


class JPFunctionForm(QWidget):
    def __init__(self, parent, flags=Qt.WindowFlags()):
        super().__init__(parent, flags=flags)
        # 把本窗体加入主窗体
        parent.addForm(self)
        self.MainForm = parent
        self.SQL_ListForm_Para = ''
        self.SQL_ListForm_Base = ''
        self.backgroundWhenValueIsTrueFieldName = []
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        parent.addButtons()
        self.comboBox = self.ui.comboBox
        self.checkBox_1 = self.ui.checkBox_1
        self.checkBox_2 = self.ui.checkBox_2
        self.tableView = self.ui.tableView
        self.__FormClass = None
        self.PrimarykeyFieldIndex = 0
        self.__EditFormClass = self.getEditFormClass()
        self.__EditForm = None
        self.EditFormMainTableName = None
        self.EditFormPrimarykeyFieldName = None
        self.EditFormSubTableName = None

        # 以下为初始化部分
        self.ui.comboBox.addItems(['Today', 'Last Month', 'Last Year', 'All'])
        self.ui.checkBox_1.clicked.connect(self.btnRefreshClick)
        self.ui.checkBox_2.clicked.connect(self.btnRefreshClick)
        self.ui.comboBox.activated['int'].connect(self.btnRefreshClick)
        # 行交错颜色
        self.ui.tableView.setAlternatingRowColors(True)
        self.SQL_EditForm_Main = None
        self.SQL_EditForm_Sub = None

    def setListFormSQL(self, sql_with_where, sql_base):
        '''
        setSQL(sql_without_para, where_string)\n
        sql_without_para: 不带Where子句的sql
        where_string： where子句，参数用{}表示
        '''
        self.SQL_ListForm_Para = sql_with_where
        self.SQL_ListForm_Base = sql_base
        self.btnRefreshClick()

    def __getTableNameInfo(self, sql, errType=1):
        # 返回一个指定SQL语句的表名和条件字段名
        sql = re.sub(r'^\s', '', re.sub(r'\s+', ' ', re.sub(r'\n', '', sql)))
        sel_p = r"SELECT\s+.*from\s(\S+)\s(as\s\S+){0,1}where\s(\S+)\s*=.*"
        mt = re.match(sel_p, sql, flags=(re.I))
        if mt:
            return mt.groups()[0], mt.groups()[2]
        else:
            errStr = "主窗体" if errType == 1 else "子窗体"
            errStr = errStr + 'SQL语句格式有误,必须类似以下格式：\n'
            errStr = errStr + "SELECT fieldsList from tab where fld={}\n"
            errStr = errStr + '而当前设定语句为:\n'
            errStr = errStr + sql
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', errStr)
            msgBox.exec_()

    def setEditFormSQL(self, sql_main: str, sql_sub: str = None):
        if sql_main:
            self.SQL_EditForm_Main = sql_main
            a, b = self.__getTableNameInfo(sql_main)
            self.EditFormMainTableName = a
            self.EditFormPrimarykeyFieldName = b
        if sql_sub:
            self.SQL_EditForm_Sub = sql_sub
            self.EditFormSubTableName = self.__getTableNameInfo(sql_sub)

    def getModelClass(self):
        '''此类可以重写，改写Model的行为,必须返回一个模型类
        重写时可以在重载方法中内部定义模型类并继承自已有模型类，将该类返回
        '''
        return JPTableViewModelReadOnly

    def setFormClass(self, cls):
        self.__FormClass = cls

    # def _locationRow(self, id)
    #     datas=self.TabelFieldInfo.
    def getEditFormClass(self):
        if self.__FormClass is None:
            strErr = "没有设置JPFunctionForm的setFormClass属性，或重写getEditFormClass方法"
            raise AttributeError(strErr)
        else:
            return self.__FormClass

    def beforeDeleteRow(self, delete_ID):
        '''删除行之前查检用方法，可重载'''
        return True

    def btnRefreshClick(self):
        if self.SQL_ListForm_Para:
            self.ui.tableView.setSelectionMode(
                QAbstractItemView.SingleSelection)
            ch1 = 1 if self.ui.checkBox_1.isChecked() else 0
            ch2 = 0 if self.ui.checkBox_2.isChecked() else 1
            cb = {
                0:
                '=CURRENT_DATE()',
                1: (datetime.date.today() -
                    relativedelta(months=1)).strftime(">='%Y-%m-%d'"),
                2: (datetime.date.today() -
                    relativedelta(years=1)).strftime(">='%Y-%m-%d'"),
                3:
                '=fOrderDate'
            }
            sql = self.SQL_ListForm_Para.format(
                ch1=ch1, ch2=ch2, date=cb[self.ui.comboBox.currentIndex()])
            info = JPQueryFieldInfo(sql)
            self.model = self.getModelClass()(self.ui.tableView, info)
            self.ui.tableView.setModel(self.model)
            self.ui.tableView.resizeColumnsToContents()

    def getCurrentSelectPKValue(self):
        index = self.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.model.TabelFieldInfo.getOnlyData(
                [index.row(), self.PrimarykeyFieldIndex])

    # 定位到某一行
    def _locationRow(self, id):
        tab = self.model.TabelFieldInfo
        c = self.PrimarykeyFieldIndex
        for r in range(len(tab.DataRows)):
            print("{}={}".format(tab.getOnlyData([r, c]), id))
            if tab.getOnlyData([r, c]) == id:
                index = self.model.createIndex(r, c)
                self.ui.tableView.setCurrentIndex(index)
                return

    @pyqtSlot()
    def on_CmdExportToExcel_clicked(self):
        print("父类的 CMDEXPORTTOEXCEL 请重新写")

    @pyqtSlot()
    def on_CmdSearch_clicked(self):
        print(" 父类的 CMDSEARCH 请重新写")

    @pyqtSlot()
    def on_CmdNew_clicked(self):
        self.__EditForm = None
        f = self.__EditFormClass(self.SQL_EditForm_Main, self.SQL_EditForm_Sub,
                                 JPFormModelMainSub.New)
        f.setListForm(self)
        self.__EditForm = f
        self.__EditForm.afterSaveData.connect(self.btnRefreshClick)
        self.__EditForm.exec_()

    @pyqtSlot()
    def on_CmdEdit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        self.__EditForm = None
        f = self.__EditFormClass(self.SQL_EditForm_Main, self.SQL_EditForm_Sub,
                                 JPFormModelMainSub.Edit, cu_id)
        f.setListForm(self)
        self.__EditForm = f
        self.__EditForm.exec_()

    @pyqtSlot()
    def on_CmdBrowse_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        self.__EditForm = None
        f = self.__EditFormClass(self.SQL_EditForm_Main, self.SQL_EditForm_Sub,
                                 JPFormModelMainSub.ReadOnly, cu_id)
        f.setListForm(self)
        self.__EditForm = f
        self.__EditForm.exec_()

    @pyqtSlot()
    def on_CmdRefresh_clicked(self):
        self.btnRefreshClick()

    @pyqtSlot()
    def on_CmdDelete_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        if self.beforeDeleteRow(cu_id):
            msg = "确认要删除记录【{}】吗？".format(cu_id)
            if QMessageBox.question(self, '确认', msg, QMessageBox.Yes,
                                    QMessageBox.Yes) == QMessageBox.Yes:
                db = JPDb()
                info = self.model.TabelFieldInfo
                sql = "delete from {tn} where {pk_n}='{pk_v}'"
                sql = sql.format(tn=self.EditFormMainTableName,
                                 pk_n=self.EditFormPrimarykeyFieldName,
                                 pk_v=cu_id)
                if db.executeTransaction(sql):
                    del_i = (
                        self.tableView.selectionModel().currentIndex().row())
                    info.deleteRow(del_i)
