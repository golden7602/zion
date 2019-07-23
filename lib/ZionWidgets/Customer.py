from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormCustomer import Ui_Form
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot
from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.JPFunction import JPDateConver, setButtonIcon


class Form_Customer(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.UI = Ui_Form()
        self.UI.setupUi(self)
        mainform.addForm(self)
        self.SQL = """
            select 
                fCustomerID as `ID`, 
                fCustomerName as `客户名称Cliente`, 
                fNUIT as `税号NUIT`, 
                fCity as `城市City`, 
                fContato as `联系人Contato`, 
                fCelular as `手机Celular`, 
                fTelefone as `电话Telefone`, 
                fEmail as `电子邮件Email`, 
                fWeb as `主页Web`, 
                fEndereco as `地址Endereco`, 
                fFax as `传真Fax` 
            from  t_customer 
        """
        
        self.on_CMDREFRESH_clicked()

    def on_CMDREFRESH_clicked(self):
        cbo = self.UI.comboBox
        cbo.DisabledEvent = True
        sql = self.SQL if (
            cbo.currentIndex() == -1
        ) else self.SQL + " where fCustomerID={}".format(cbo.currentIndex())
        self.dataInfo = JPTabelFieldInfo(sql)
        self.mod = JPTableViewModelEditForm(self.UI.tableView, self.dataInfo)
        self.UI.tableView.setModel(self.mod)
        self.UI.tableView.resizeColumnsToContents()
        lst = [[item.Datas[1], item.Datas[0]]
               for item in self.dataInfo.RowsData]
        cbo.setEditable(True)
        for r in lst:
            cbo.addItem(r[0], r[1])
        cbo.setCurrentIndex(-1)
        cbo.DisabledEvent = False

    def on_comboBox_currentIndexChanged(self, index):
        if self.UI.comboBox.DisabledEvent:
            return
        self.on_CMDREFRESH_clicked()

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item[0])
            btn.setObjectName(item[2].upper())
            print(item[2].upper())
            setButtonIcon(btn)
            self.UI.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)