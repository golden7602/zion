from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormCustomer import Ui_Form
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from lib.JPFunction import JPDateConver, setButtonIcon


class Form_Customer(Ui_Form):
    def __init__(self, mainform):
        super().__init__()
        self.Widget = QWidget()
        self.setupUi(self.Widget)
        mainform.addWidget(self.Widget)

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item[0])
            btn.setObjectName(item[2].upper())
            setButtonIcon(btn)
            self.widget_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)