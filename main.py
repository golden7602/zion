#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                             QProgressBar, QTreeWidgetItem, QWidget)
from PyQt5.QtGui import QIcon, QPixmap
from lib.ZionPublc import JPPub, loadTreeview
from lib.ZionWidgets import getStackedWidget
from Ui import Ui_mainform

# class clsmyStackedWidget(object):
#     """功能窗口的堆叠布局类"""
#     def __init__(self, StackedWidget, MainForm):
#         self.StackedWidget = StackedWidget
#         self.MainForm = MainForm
#         self.ui = None
#         self.objFuncform = None
#     def TreeViewItemClicked(self, info):
#         try:
#             frm = self.StackedWidget
#             if frm.count() == 1:
#                 frm.removeWidget(frm.currentWidget)
#             sql ="""
#                 SELECT fNMID,  fMenuText, fParentId
#                 FROM sysnavigationmenus
#                 WHERE fParentId={}
#                 ORDER BY  fDispIndex
#             """
#             items = pub.getDict(sql.format(info.jpData["fNMID"]))
#             tempWidget = QWidget()
#             # 新建立一个功能窗口对象
#             self.ui = Func_Ui_Form()
#             self.ui.setupUi(tempWidget)
#             self.ui.label_FuncFullPath.setText(info.FullPath)
#             objName = info.jpData["fObjectName"].upper()
#             if objName in self.clsFuncFormDict:
#                 self.objFuncform = self.clsFuncFormDict[objName](self.ui,
#                                                                  self.MainForm)
#             else:
#                 raise AttributeError
#             for i in range(0, len(items)):
#                 nm = items[i]["fMenuText"]
#                 # 添加按钮
#                 btn = QPushButton(nm)
#                 btn.setObjectName('btn' + nm)  # 使用setObjectName设置对象名称
#                 btn.tableWidget = self.ui.tableWidget
#                 btn.clicked.connect(self.objFuncform.AnybtnClick)
#                 self.ui.horizontalLayout_Button.addWidget(btn)
#             frm.addWidget(tempWidget)
#             frm.currentWidget = tempWidget
#             frm.setCurrentIndex(1)
#             self.objFuncform.btnRefreshClick()
#         except AttributeError as err:
#             print(err)
#             tempWidget = QWidget()
#             # tempWidget.setStyleSheet("background-color:rgb(255, 255, 255);")
#             self.StackedWidget.addWidget(tempWidget)
#             self.StackedWidget.currentWidget = tempWidget
#             self.StackedWidget.setCurrentIndex(1)
#         else:
#             return


class mianFormProcess():
    def __init__(self, MW):

        ui = Ui_mainform.Ui_MainWindow()
        ui.setupUi(MW)
        ui.label_logo.setPixmap(QPixmap(os.getcwd() + "\\res\\Zions_100.png"))
        #MW.setStyleSheet(pub.readQss(
        #    "C:\\Users\\Administrator\\Desktop\\newPYprj\\res\\blackwhite.css"))
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

        # funcFrm = clsmyStackedWidget(ui.stackedWidget, MW)
        # funcFrm.TreeViewItemClicked(None)
        # ui.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
        #     funcFrm.TreeViewItemClicked)
        pub = JPPub()
        self.sysNavigationMenus = pub.getSysNavigationMenusDict()
        loadTreeview(ui.treeWidget, self.sysNavigationMenus)
        MW.Label = QLabel("")
        MW.ProgressBar = QProgressBar()
        MW.statusBar().addPermanentWidget(MW.Label)
        MW.statusBar().addPermanentWidget(MW.ProgressBar)
        MW.ProgressBar.hide()

        def reeViewItemClicked(item, i):
            widget = getStackedWidget(self, item.jpData)
            if widget:
                ui.stackedWidget.addWidget(widget)
                ui.stackedWidget.currentWidget = widget
                ui.stackedWidget.setCurrentIndex(1)

        ui.treeWidget.itemClicked[QTreeWidgetItem, int].connect(
            reeViewItemClicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    mianFormProcess(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
