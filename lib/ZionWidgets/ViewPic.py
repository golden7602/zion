from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormViewPic import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from lib.ZionPublc import JPPub
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Form_ViewPic(QDialog):
    def __init__(self, parent=None, Pixmap='', flags=Qt.WindowFlags()):
        pub = JPPub()
        super().__init__(parent=pub.MainForm, flags=flags)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(Pixmap)
        self.exec_()
