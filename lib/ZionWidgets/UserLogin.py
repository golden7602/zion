from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from lib.JPDatabase.Database import JPDb
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtCore import Qt
from Ui.Ui_FormUserLogin import Ui_Dialog
from lib.JPFunction import md5_passwd
