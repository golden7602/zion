import datetime
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from dateutil.relativedelta import relativedelta
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QAbstractItemView, QCheckBox, QComboBox,
                             QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
                             QTableView, QVBoxLayout, QWidget, QPushButton)
from PyQt5.QtCore import QCoreApplication, QMetaObject, QSize, Qt, pyqtSlot
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPModel import JPFormModelMainSub, JPTableViewModelReadOnly
from lib.JPFunction import setButtonIcon
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
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.comboBox=self.ui.comboBox
        self.checkBox_1=self.ui.checkBox_1
        self.checkBox_2=self.ui.checkBox_2
        self.tableView=self.ui.tableView

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

    def btnRefreshClick(self):
        if self.DefauleParaSQL:
            #self.ui.tableView.clear()
            self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
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

    @pyqtSlot()
    def on_CmdExportToExcel_clicked(self):
        print("CMDEXPORTTOEXCEL 请重新写")

    @pyqtSlot()
    def on_CmdSearch_clicked(self):
        print("CMDSEARCH 请重新写")
