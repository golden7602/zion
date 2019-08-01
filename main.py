#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import getcwd
from sys import path as jppath, argv, exit as sys_exit
jppath.append(getcwd())

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow,
                             QTreeWidgetItem, QWidget,
                             QPushButton)
from PyQt5.QtGui import QIcon, QPixmap
from lib.ZionPublc import JPPub, JPUser
from Ui import Ui_mainform
from lib.JPFunction import readQss, setButtonIconByName
from lib.JPDatabase.Database import JPDb, JPDbType
from lib.ZionWidgets.Background import Form_Background
from Ui.Ui_FormUserLogin import Ui_Dialog
from lib.JPFunction import setButtonIconByName, setButtonIcon
from PyQt5.QtCore import QThread, QMetaObject, Qt



def loadTreeview(treeWidget, items):
    class MyThreadReadTree(QThread):  # 加载功能树的线程类
        def __init__(self, treeWidget, items):
            super().__init__()
            treeWidget.clear()
            root = QTreeWidgetItem(treeWidget)
            root.setText(0, "Function")
            root.FullPath = "Function"
            self.root = root
            self.items = items
            self.icopath = getcwd() + "\\res\\ico\\"

        def addItems(self, parent, items):
            for r in items:
                item = QTreeWidgetItem(parent)
                item.setText(0, r["fMenuText"])
                item.setIcon(0, QIcon(self.icopath + r["fIcon"]))
                item.jpData = r
                item.FullPath = (parent.FullPath + '\\' + r["fMenuText"])
                self.addItems(
                    item,
                    [l for l in self.items if l["fParentId"] == r["fNMID"]])
                item.setExpanded(1)

        def run(self):  # 线程执行函数
            self.addItems(self.root,
                          [l for l in self.items if l["fParentId"] == 1])
            self.root.setExpanded(True)

        def getRoot(self):
            return

    _readTree = MyThreadReadTree(treeWidget, items)
    _readTree.run()


class JPMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        JPPub().MainForm = self
        self.ui = Ui_mainform.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_Title.setText("Zion OrderM")
        setButtonIconByName(self.ui.ChangeUser)
        setButtonIconByName(self.ui.ChangePassword)
        self.ui.label_logo.setPixmap(QPixmap(getcwd() +
                                             "\\res\\Zions_100.png"))

        def onUserChanged(args):
            self.ui.label_UserName.setText(args[1])
            loadTreeview(self.ui.treeWidget, objUser.currentUserRight())
            Form_Background(self)

        objUser = JPUser()
        objUser.INIT()  # 程序开始时只初始化一次
        objUser.userChange.connect(onUserChanged)
        objUser.currentUserID()
        self.ui.ChangeUser.clicked.connect(objUser.changeUser)
        self.ui.ChangePassword.clicked.connect(objUser.changePassword)
        # MW.setStyleSheet(readQss(os.getcwd() + "\\res\\blackwhite.css"))
        # 堆叠布局调
        self.ui.stackedWidget.removeWidget(self.ui.page)
        self.ui.stackedWidget.removeWidget(self.ui.page_2)
        # 隐藏树标题
        self.ui.label_FunPath.setText('')
        self.ui.treeWidget.setHeaderHidden(True)

        # MW.Label = QLabel("")
        # MW.ProgressBar = QProgressBar()
        # MW.statusBar().addPermanentWidget(MW.Label)
        # MW.statusBar().addPermanentWidget(MW.ProgressBar)
        # MW.ProgressBar.hide()

        def treeViewItemClicked(item, i):
            self.ui.label_FunPath.setText(item.FullPath)
            self.getStackedWidget(item.jpData)

        self.ui.treeWidget.itemClicked[QTreeWidgetItem, int].connect(
            treeViewItemClicked)

    def addForm(self, form):
        st = self.ui.stackedWidget
        if st.count() > 0:
            temp = st.widget(0)
            st.removeWidget(temp)
            del temp
        st.addWidget(form)

    def addButtons(self):
        widget = self.ui.stackedWidget.widget(0)
        layout = widget.findChild((QHBoxLayout, QWidget), 'Layout_Button')
        if not (layout is None):
            for m in self.btns:
                widget.ui.btn = QPushButton(m['fMenuText'])
                widget.ui.btn.NMID = m['fNMID']
                widget.ui.btn.setObjectName(m['fObjectName'])
                setButtonIcon(widget.ui.btn)
                widget.ui.btn.setEnabled(m['fHasRight'])
                layout.addWidget(widget.ui.btn)
            QMetaObject.connectSlotsByName(widget)

    def getStackedWidget(self, sysnavigationmenus_data):
        self.btns = sysnavigationmenus_data['btns']
        self.menu_id = sysnavigationmenus_data['fNMID']
        if self.menu_id == 2:  # Order
            from lib.ZionWidgets.Order import JPFuncForm_Order
            JPFuncForm_Order(self)
        elif self.menu_id == 9:
            from lib.ZionWidgets.Payment import JPFuncForm_Payment
            JPFuncForm_Payment(self)
        elif self.menu_id == 22:
            from lib.ZionReport.Report_Day import Form_Repoet_Day
            Form_Repoet_Day(self)
        elif self.menu_id == 10:
            from lib.ZionWidgets.EnumManger import Form_EnumManger
            Form_EnumManger(self)
        elif self.menu_id == 20:
            from lib.ZionWidgets.Receivables import Form_Receivables
            Form_Receivables(self)
        elif self.menu_id == 72:
            from lib.ZionWidgets.PrintingOrder import JPFuncForm_PrintingOrder
            JPFuncForm_PrintingOrder(self)
        elif self.menu_id == 73:
            from lib.ZionWidgets.Customer import Form_Customer
            Form_Customer(self)
        elif self.menu_id == 13:
            from lib.ZionWidgets.User import Form_User
            Form_User(self)
        elif self.menu_id == 15:
            from lib.ZionWidgets.Complete import JPFuncForm_Complete
            JPFuncForm_Complete(self)
        elif self.menu_id == 18:
            from lib.ZionWidgets.Adjustment import JPFuncForm_Adjustment
            JPFuncForm_Adjustment(self)
        elif self.menu_id == 56:
            from lib.ZionWidgets.Quotation import JPFuncForm_Quotation
            JPFuncForm_Quotation(self)
        elif self.menu_id == 55:
            from lib.ZionWidgets.PrintingQuotation import JPFuncForm_PrintingQuotation
            JPFuncForm_PrintingQuotation(self)
        else:
            Form_Background(self)

        return


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(argv)
    db = JPDb()
    db.setDatabaseType(JPDbType.MySQL)
    MainWindow = JPMainWindow()
    icon = QIcon()
    icon.addPixmap(
        QPixmap(getcwd() + "\\res\\ico\\medical_invoice_information.png"))
    MainWindow.setWindowIcon(icon)
    MainWindow.showMaximized()
    sys_exit(app.exec_())
