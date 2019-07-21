# -*- coding: utf-8 -*-

from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex, Qt, pyqtSignal
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QWidget, QDialog

from lib.JPDatabase.Database import JPDb
from lib.JPDatebase import JPMySqlSingleTableQuery as JPQ, JPTabelFieldInfo, JPQueryFieldInfo
from lib.JPFunction import NV, JPRound
from lib.JPMvc.JPModel import JPFormModelMainSub, JPTableViewModelReadOnly
from lib.JPPrintReport import JPReport
from lib.ZionPublc import JPPub
from PyQt5.QtGui import QIcon, QPixmap
from lib.JPDatabase.Query import JPQueryFieldInfo

def getFuncForm_Enum(mainform):
    from Ui.Ui_FormEnum import Ui_Form
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    mainform.addForm(Form)


def getFuncForm_FormReceivables(mainform):
    from Ui.Ui_FormReceivables import Ui_Form
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    mainform.addForm(Form)



