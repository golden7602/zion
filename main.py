#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
sys.path.append(os.getcwd())
from datetime import datetime

import pymysql
from Ui import Ui_mainform
from lib.funcform_process import clsmyStackedWidget
from lib.globalVar import pub
from PyQt5.QtCore import QSettings, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                             QProgressBar, QSplitter, QStackedWidget,
                             QTreeWidgetItem)


class MyThreadReadTree(QThread):  # 加载功能树的线程类
    def __init__(self, root, items):
        super(MyThreadReadTree, self).__init__()
        self.root = root
        self.items = items

    def run(self):  # 线程执行函数
        def additemtotree(parent, nmid, items, begin=0):
            for i in range(begin, len(items) - 1):
                if items[i]["fParentId"] == nmid and int(
                        items[i]["fIsCommandButton"]) == 0:
                    item = QTreeWidgetItem(parent)
                    item.setText(0, items[i]["fMenuText"])
                    path=os.getcwd()+"\\res\\ico\\"+ items[i]["fIcon"]
                    item.setIcon(
                        0,
                        QIcon(path))
                    item.jpData = items[i]
                    item.FullPath = parent.FullPath + \
                        '\\' + items[i]["fMenuText"]
                    additemtotree(item, items[i]["fNMID"], items, i)
                    item.setExpanded(1)

        additemtotree(self.root, 1, self.items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_mainform.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label_logo.setPixmap(QPixmap(os.getcwd()+"\\res\\Zions_100.png"))
    #MainWindow.setStyleSheet(pub.readQss(
    #    "C:\\Users\\Administrator\\Desktop\\newPYprj\\res\\blackwhite.css"))
    ui.stackedWidget.removeWidget(ui.page)
    ui.stackedWidget.removeWidget(ui.page_2)
    MainWindow.showMaximized()
    funcFrm = clsmyStackedWidget(ui.stackedWidget, MainWindow)
    funcFrm.TreeViewItemClicked(None)
    ui.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
        funcFrm.TreeViewItemClicked)
    root = QTreeWidgetItem(ui.treeWidget)
    root.setText(0, "Function")
    root.FullPath = "Function"
    items = pub.getDict(
        "select fNMID,fMenuText,fParentId,fCommand,fObjectName,fIcon,fIsCommandButton+0 as fIsCommandButton  from sysnavigationmenus where fEnabled=1 and  fNMID>1 order by fDispIndex"
    )
    tr = MyThreadReadTree(root, items)
    tr.run()
    MainWindow.Label = QLabel("")
    MainWindow.ProgressBar = QProgressBar()
    MainWindow.statusBar().addPermanentWidget(MainWindow.Label)
    MainWindow.statusBar().addPermanentWidget(MainWindow.ProgressBar)
    MainWindow.ProgressBar.hide()
    root.setExpanded(1)
    sys.exit(app.exec_())
