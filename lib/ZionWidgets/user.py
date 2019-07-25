from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormUser import Ui_Form
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot
from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPDatabase.Database import JPDb
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.JPFunction import JPDateConver, setButtonIcon
from lib.ZionPublc import loadTreeview


class Form_User(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        mainform.addForm(self)
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
        self.mod = JPTableViewModelEditForm(self.ui.tableView, self.dataInfo)
        self.ui.tableView.setModel(self.mod)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.selectionModel().currentChanged.connect(self.on_tableView_currentChanged)

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item[0])
            btn.setObjectName(item[2].upper())
            setButtonIcon(btn)
            self.ui.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)


    def on_tableView_currentChanged(self,index1, index2):
        uid = self.dataInfo.RowsData[index1.row()].Data(0)
        sql="""
            SELECT m.*, ord(u.fHasRight)
            FROM sysnavigationmenus m
                LEFT JOIN sysuserright u ON m.fNMID = u.fRightID
            WHERE u.fUserID = {} AND ord(m.fEnabled) = 1
        """
        items=JPDb().getDict(sql.format(uid))
        loadTreeview(self.ui.treeWidget,items)
