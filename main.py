#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import getcwd
from sys import path as jppath, argv, exit as sys_exit
jppath.append(getcwd())

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                             QProgressBar, QTreeWidgetItem, QWidget)
from PyQt5.QtGui import QIcon, QPixmap
from lib.ZionPublc import JPPub, loadTreeview
from lib.ZionWidgets import getStackedWidget
from Ui import Ui_mainform
from lib.JPFunction import readQss


class mianFormProcess():
    def __init__(self, MW):

        ui = Ui_mainform.Ui_MainWindow()
        ui.setupUi(MW)
        ui.label_logo.setPixmap(QPixmap(getcwd() + "\\res\\Zions_100.png"))
        #MW.setStyleSheet(readQss(os.getcwd() + "\\res\\blackwhite.css"))
        # 堆叠布局调
        ui.stackedWidget.removeWidget(ui.page)
        ui.stackedWidget.removeWidget(ui.page_2)
        EF = QWidget()
        ui.empty = EF
        EF.horizontalLayout = QHBoxLayout(EF)
        EF.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        EF.horizontalLayout.setSpacing(0)
        EF.horizontalLayout.setObjectName("horizontalLayout")
        EF.label = QLabel(EF)
        EF.label.setStyleSheet(
            "background-color: rgb(255, 255, 255);border:0.5px solid rgb(127,127,127)"
        )
        EF.label.setText("")
        EF.label.setObjectName("label")
        EF.horizontalLayout.addWidget(EF.label)
        ui.stackedWidget.addWidget(EF)
        ui.stackedWidget.currentWidget = EF
        # 隐藏树标题
        ui.treeWidget.setHeaderHidden(True)
        pub = JPPub()
        self.sysNavigationMenus = pub.getSysNavigationMenusDict()
        loadTreeview(ui.treeWidget, self.sysNavigationMenus)
        MW.Label = QLabel("")
        # MW.ProgressBar = QProgressBar()
        # MW.statusBar().addPermanentWidget(MW.Label)
        # MW.statusBar().addPermanentWidget(MW.ProgressBar)
        # MW.ProgressBar.hide()

        def addForm(form):
            st = ui.stackedWidget
            if st.count() > 0:
                st.removeWidget(st.widget(0))
                st.addWidget(form)

        MW.addForm = addForm

        def reeViewItemClicked(item, i):
            widget = getStackedWidget(MW, item.jpData)
            if widget:
                ui.stackedWidget.addWidget(widget)
                ui.stackedWidget.currentWidget = widget
                ui.stackedWidget.setCurrentIndex(1)

        ui.treeWidget.itemClicked[QTreeWidgetItem, int].connect(
            reeViewItemClicked)


if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QMainWindow()
    mianFormProcess(MainWindow)
    MainWindow.showMaximized()
    sys_exit(app.exec_())
