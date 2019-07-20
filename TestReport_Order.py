# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter, QPixmap, QColor
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QApplication

from lib.globalVar import pub
from lib.JPPrintReport import JPPrintSectionType, JPReport


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rep = Order()
    try:
        rep.BeginPrint()
    except Exception as e:
        print(e)
    sys.exit(app.exec_())
