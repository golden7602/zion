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
from PyQt5.QtCore import QCoreApplication, QMetaObject, QSize, Qt, pyqtSlot
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPModel import JPFormModelMainSub, JPTableViewModelReadOnly
from lib.JPFunction import setButtonIcon
from lib.JPDatabase.Database import JPDb
from Ui.Ui_FuncFormMob import Ui_Form


class JPFunctionForm(QWidget):
    def __init__(self, parent, flags=Qt.WindowFlags()):
        super().__init__(parent, flags=flags)
        # 把本窗体加入主窗体
        parent.addForm(self)
        self.MainForm = parent
        self.DefauleParaSQL = ''
        self.DefauleBaseSQL = ''
        self.backgroundWhenValueIsTrueFieldName = []
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.comboBox = self.ui.comboBox
        self.checkBox_1 = self.ui.checkBox_1
        self.checkBox_2 = self.ui.checkBox_2
        self.tableView = self.ui.tableView
        self.__FormClass = None
        self.PrimarykeyFieldIndex = 0

        # 以下为初始化部分
        self.ui.comboBox.addItems(['Today', 'Last Month', 'Last Year', 'All'])
        self.ui.checkBox_1.clicked.connect(self.btnRefreshClick)
        self.ui.checkBox_2.clicked.connect(self.btnRefreshClick)
        self.ui.comboBox.activated['int'].connect(self.btnRefreshClick)
        # 行交错颜色
        self.ui.tableView.setAlternatingRowColors(True)

    def setSQL(self, sql_with_where, sql_base):
        '''
        setSQL(sql_without_para, where_string)\n
        sql_without_para: 不带Where子句的sql
        where_string： where子句，参数用{}表示
        '''
        self.DefauleParaSQL = sql_with_where
        self.DefauleBaseSQL = sql_base
        self.btnRefreshClick()

    def getModelClass(self):
        '''此类可以重写，改写Model的行为,必须返回一个模型类
        重写时可以在重载方法中内部定义模型类并继承自已有模型类，将该类返回
        '''
        return JPTableViewModelReadOnly

    def setFormClass(self, cls):
        self.__FormClass = cls

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
        if self.DefauleParaSQL:
            #self.ui.tableView.clear()
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
            sql = self.DefauleParaSQL.format(
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

    #@pyqtSlot()
    def on_CmdExportToExcel_clicked(self):
        print("父类的 CMDEXPORTTOEXCEL 请重新写")

    #@pyqtSlot()
    def on_CmdSearch_clicked(self):
        print(" 父类的 CMDSEARCH 请重新写")

    #@pyqtSlot()
    def on_CmdNew_clicked(self):
        form = self.getEditFormClass()(JPFormModelMainSub.New)
        form.exec_()

    #@pyqtSlot()
    def on_CmdEdit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        form = self.getEditFormClass()(JPFormModelMainSub.Edit, cu_id)
        form.exec_()

    #@pyqtSlot()
    def on_CmdBrowse_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        form = self.getEditFormClass()(JPFormModelMainSub.ReadOnly, cu_id)
        form.exec_()

    #@pyqtSlot()
    def on_CmdRefresh_clicked(self):
        self.btnRefreshClick()

    #@pyqtSlot()
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
                sql = sql.format(tn=self.TableName,
                                 pk_n=self.PrimarykeyFieldName,
                                 pk_v=cu_id)
                if db.executeTransaction(sql):
                    del_i = (
                        self.tableView.selectionModel().currentIndex().row())
                    info.deleteRow(del_i)

    #@pyqtSlot()
    def on_CmdSubmit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        db = JPDb()
        info = self.model.TabelFieldInfo
        if info.getOnlyData([
                self.tableView.selectionModel().currentIndex().row(),
                self.fSubmited_column
        ]) == 1:
            msg = '记录【{cu_id}】已经提交，不能重复提交!\nThe order [{cu_id}] '
            msg = msg + 'has been submitted, can not be repeated submission!'
            msg = msg.format(cu_id=cu_id)
            QMessageBox.warning(self, '提示', msg, QMessageBox.Ok,
                                QMessageBox.Ok)
            return
        msg = '提交后订单将不能修改！确定继续提交记录【{cu_id}】吗？\n'
        msg = msg + 'The order "{cu_id}" will not be modified after submission. '
        msg = msg + 'Click OK to continue submitting?'.format(cu_id=cu_id)
        if QMessageBox.question(self, '确认', msg, QMessageBox.Ok,
                                QMessageBox.Ok) != QMessageBox.Ok:
            return
        sql = "update {tn} set fSubmited=1 where {pk_n}='{pk_v}'"
        sql = sql.format(tn=self.TableName,
                         pk_n=self.PrimarykeyFieldName,
                         pk_v=cu_id)
        if db.executeTransaction(sql):
            self.btnRefreshClick()
