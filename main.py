#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import getcwd
from sys import path as jppath, argv, exit as sys_exit
jppath.append(getcwd())

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                             QProgressBar, QTreeWidgetItem, QWidget)
from PyQt5.QtGui import QIcon, QPixmap
from lib.ZionPublc import JPPub, loadTreeview
#from lib.ZionWidgets import getStackedWidget
from Ui import Ui_mainform
from lib.JPFunction import readQss
from lib.JPDatabase.Database import JPDb,JPDbType


class mianFormProcess():
    def __init__(self, MW):

        ui = Ui_mainform.Ui_MainWindow()
        ui.setupUi(MW)
        ui.label_logo.setPixmap(QPixmap(getcwd() + "\\res\\Zions_100.png"))
        #MW.setStyleSheet(readQss(os.getcwd() + "\\res\\blackwhite.css"))
        # 堆叠布局调
        ui.stackedWidget.removeWidget(ui.page)
        ui.stackedWidget.removeWidget(ui.page_2)
        # EF = QWidget()
        # ui.empty = EF
        # EF.horizontalLayout = QHBoxLayout(EF)
        # EF.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # EF.horizontalLayout.setSpacing(0)
        # EF.horizontalLayout.setObjectName("horizontalLayout")
        # EF.label = QLabel(EF)
        # EF.label.setStyleSheet(
        #     "background-color: rgb(255, 255, 255);border:0.5px solid rgb(127,127,127)"
        # )
        # EF.label.setText("")
        # EF.label.setObjectName("label")
        # EF.horizontalLayout.addWidget(EF.label)
        # ui.stackedWidget.addWidget(EF)
        # ui.stackedWidget.currentWidget = EF
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
                temp=st.widget(0)
                st.removeWidget(temp)
                del temp
            st.addWidget(form)

        MW.addForm = addForm

        def reeViewItemClicked(item, i):
            print(item)
            widget = getStackedWidget(MW, item.jpData)
            if widget:
                ui.stackedWidget.addWidget(widget)
                ui.stackedWidget.currentWidget = widget
                ui.stackedWidget.setCurrentIndex(1)

        ui.treeWidget.itemClicked[QTreeWidgetItem, int].connect(
            reeViewItemClicked)


def getStackedWidget(mainForm, sysnavigationmenus_data):
    pub = JPPub()
    menus = pub.getSysNavigationMenusDict()
    menu_id = sysnavigationmenus_data['fNMID']
    buts = [[m['fMenuText'], m['fIcon'], m['fObjectName']] for m in menus
            if m['fParentId'] == menu_id and m['fIsCommandButton']]
    widget = None
    if menu_id == 2:  # Order
        from lib.ZionWidgets.Order import JPFuncForm_Order
        widget = JPFuncForm_Order(mainForm)
        widget.addButtons(buts)
    # elif menu_id == 22:  #Report_day
    #     from lib.ZionWidgets.Report_Day import
    #     getFuncForm_FormReport_Day(mainForm)
    elif menu_id == 10:
        from lib.ZionWidgets.EnumManger import Form_EnumManger
        Form_EnumManger(mainForm)
    # elif menu_id == 20:
    #     getFuncForm_FormReceivables(mainForm)
    return

if __name__ == "__main__":
    app = QApplication(argv)
    db = JPDb()
    db.setDatabaseType(JPDbType.MySQL)
    MainWindow = QMainWindow()
    mianFormProcess(MainWindow)
    MainWindow.showMaximized()
    sys_exit(app.exec_())
