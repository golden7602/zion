from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormCustomer import Ui_Form
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot
from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.JPFunction import JPDateConver, setButtonIcon


class Form_User(Ui_Form):
    def __init__(self, mainform):
        super().__init__()
        self.Widget = QWidget()
        self.setupUi(self.Widget)
        mainform.addForm(self.Widget)
        self.SQL = """
            select 
                fUserID as `编号 ID`, 
                fUsername as `用户名Name`, 
                fNickname as `昵称Nickname`, 
                fDepartment as `部门Department`, 
                fNotes as `备注Note ` 
                from  sysusers 
            where  fUserID > 1
        """
        self.dataInfo = JPTabelFieldInfo(self.SQL)
        self.mod = JPTableViewModelEditForm(self.tableView, self.dataInfo)
        self.tableView.setModel(self.mod)
        self.tableView.resizeColumnsToContents()

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item[0])
            btn.setObjectName(item[2].upper())
            setButtonIcon(btn)
            self.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self.Widget)