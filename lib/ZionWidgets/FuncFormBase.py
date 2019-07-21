import datetime
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from dateutil.relativedelta import relativedelta
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QAbstractItemView, QCheckBox, QComboBox,
                             QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
                             QTableView, QVBoxLayout, QWidget, QPushButton)
from PyQt5.QtCore import QCoreApplication, QMetaObject,QSize,Qt,pyqtSlot
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPModel import JPFormModelMainSub, JPTableViewModelReadOnly


class JPFunctionForm(QWidget):
    def __init__(self, parent, flags=Qt.WindowFlags()):
        super().__init__(parent, flags=flags)
        # 把本窗体加入主窗体
        parent.addForm(self)
        self.MainForm = parent
        self.DefauleParaSQL = ''
        self.DefauleBaseSQL = ''
        self.backgroundWhenValueIsTrueFieldName = []

        self.setObjectName("Form")
        self.resize(742, 300)
        font = QFont()
        font.setFamily("Arial")
        self.setFont(font)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QSpacerItem(10, 20, QSizePolicy.Fixed,
                                 QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_FuncFullPath = QLabel(self)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FuncFullPath.setFont(font)
        self.label_FuncFullPath.setObjectName("label_FuncFullPath")
        self.horizontalLayout_2.addWidget(self.label_FuncFullPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_Button = QWidget(self)
        font = QFont()
        font.setPointSize(8)
        self.widget_Button.setFont(font)
        self.widget_Button.setObjectName("widget_Button")
        self.horizontalLayout_Button = QHBoxLayout(self.widget_Button)
        self.horizontalLayout_Button.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Button.setSpacing(0)
        self.horizontalLayout_Button.setObjectName("horizontalLayout_Button")
        self.horizontalLayout_3.addWidget(self.widget_Button)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QSpacerItem(20, 20, QSizePolicy.Fixed,
                                  QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QLabel(self)
        font = QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QComboBox(self)
        self.comboBox.setMinimumSize(QSize(100, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem2 = QSpacerItem(20, 20, QSizePolicy.Fixed,
                                  QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.checkBox_1 = QCheckBox(self)
        self.checkBox_1.setObjectName("checkBox_1")
        self.horizontalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QCheckBox(self)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                  QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView = QTableView(self)
        self.tableView.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setMinimumSectionSize(23)
        self.tableView.verticalHeader().setDefaultSectionSize(24)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(self)

        # 以下为初始化部分，不能删除
        self.comboBox.addItems(['Today', 'Last Month', 'Last Year', 'All'])
        self.checkBox_1.clicked.connect(self.btnRefreshClick)
        self.checkBox_2.clicked.connect(self.btnRefreshClick)
        self.comboBox.activated['int'].connect(self.btnRefreshClick)
        # 行交错颜色
        self.tableView.setAlternatingRowColors(True)

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
            #self.tableView.clear()
            self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
            ch1 = 1 if self.checkBox_1.isChecked() else 0
            ch2 = 0 if self.checkBox_2.isChecked() else 1
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
            sql = self.DefauleParaSQL.format(ch1, ch2,
                                             cb[self.comboBox.currentIndex()])
            info = JPQueryFieldInfo(sql)
            self.model = self.getModelClass()(self.tableView, info)
            self.tableView.setModel(self.model)
            self.tableView.resizeColumnsToContents()

    @pyqtSlot()
    def on_CMDEXPORTTOEXCEL_clicked(self):
        print("CMDEXPORTTOEXCEL 请重新写")

    @pyqtSlot()
    def on_CMDSEARCH_clicked(self):
        print("CMDSEARCH 请重新写")

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item[0])
            btn.setObjectName(item[2].upper())
            icon = QIcon()
            icon.addPixmap(QPixmap(getcwd() + "\\res\\ico\\" + item[1]),
                           QIcon.Normal, QIcon.Off)
            btn.setIcon(icon)
            self.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_FuncFullPath.setText(_translate("Form", "Function Path"))
        self.label_2.setText(_translate("Form", "Filter:"))
        self.checkBox_1.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
