from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormConfig import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from lib.ZionPublc import JPPub
from PyQt5.QtCore import Qt
from lib.JPDatabase.Database import JPDb


class Form_Config(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        pub = JPPub()
        super().__init__(parent=pub.MainForm, flags=flags)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        txt = JPDb().getOnConfigValue('Note_PrintingOrder', str)
        self.ui.Note_PrintingOrder.setText(txt)
        txt = JPDb().getOnConfigValue('Bank_Account', str)
        self.ui.Bank_Account.setText(txt)
        self.exec_()

    def accept(self):
        txt = self.ui.Note_PrintingOrder.toPlainText()
        txt = txt if txt else ''
        txt1 = self.ui.Note_PrintingOrder.toPlainText()
        txt1 = txt1 if txt else ''
        try:
            JPDb().saveConfigVale('Note_PrintingOrder', txt, str)
            JPDb().saveConfigVale('Bank_Account', txt1, str)
        except Exception as e:
            pass
