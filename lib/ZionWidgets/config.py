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
        self.exec_()

    def accept(self):
        txt = self.ui.Note_PrintingOrder.text()
        txt = txt if txt else ''
        try:
            JPDb().saveConfigVale('Note_PrintingOrder', txt, str)
        except Exception as e:
            pass