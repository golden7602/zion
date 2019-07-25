#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import getcwd
from sys import path as jppath, argv, exit as sys_exit
jppath.append(getcwd())

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                             QProgressBar, QTreeWidgetItem, QWidget)
from PyQt5.QtGui import QIcon, QPixmap
from lib.ZionPublc import JPPub, loadTreeview, JPUser
from Ui import Ui_mainform
from lib.JPFunction import readQss, setButtonIconByName
from lib.JPDatabase.Database import JPDb, JPDbType
from lib.ZionWidgets.Background import Form_Background
from Ui.Ui_FormUserLogin import Ui_Dialog


class mianFormProcess():
    def __init__(self, MW):

        ui = Ui_mainform.Ui_MainWindow()
        ui.setupUi(MW)
        ui.label_Title.setText("Zion OrderM")
        setButtonIconByName(ui.ChangeUser)
        setButtonIconByName(ui.ChangePassword)

        ui.label_logo.setPixmap(QPixmap(getcwd() + "\\res\\Zions_100.png"))

        def addForm(form):
            st = ui.stackedWidget
            if st.count() > 0:
                temp = st.widget(0)
                st.removeWidget(temp)
                del temp
            st.addWidget(form)

        MW.addForm = addForm
        self.addForm = addForm

        def onUserChanged(args):
            ui.label_UserName.setText(args[1])
            ui.treeWidget.clear()
            loadTreeview(ui.treeWidget, objUser.currentUserRight())
            Form_Background(MW)

        pub = JPPub()
        objUser = JPUser()
        objUser.INIT()  #程序开始时只初始化一次
        objUser.userChange.connect(onUserChanged)
        objUser.currentUserID()
        # def onBtnUserClicked():
        #     objUser.changeUser()
        ui.ChangeUser.clicked.connect(objUser.changeUser)
        #MW.setStyleSheet(readQss(os.getcwd() + "\\res\\blackwhite.css"))
        # 堆叠布局调
        ui.stackedWidget.removeWidget(ui.page)
        ui.stackedWidget.removeWidget(ui.page_2)
        # 隐藏树标题
        ui.label_FunPath.setText('')
        ui.treeWidget.setHeaderHidden(True)

        # MW.Label = QLabel("")
        # MW.ProgressBar = QProgressBar()
        # MW.statusBar().addPermanentWidget(MW.Label)
        # MW.statusBar().addPermanentWidget(MW.ProgressBar)
        # MW.ProgressBar.hide()

        def treeViewItemClicked(item, i):
            ui.label_FunPath.setText(item.FullPath)
            getStackedWidget(MW, item.jpData)

        ui.treeWidget.itemClicked[QTreeWidgetItem, int].connect(
            treeViewItemClicked)


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
    elif menu_id == 22:
        from lib.ZionWidgets.Report_Day import Form_Repoet_Day
        Form_Repoet_Day(mainForm)
    elif menu_id == 9:
        from lib.ZionWidgets.payment import JPFuncForm_Payment
        widget = JPFuncForm_Payment(mainForm)
        widget.addButtons(buts)
    elif menu_id == 10:
        from lib.ZionWidgets.EnumManger import Form_EnumManger
        Form_EnumManger(mainForm)
    elif menu_id == 20:
        from lib.ZionWidgets.Receivables import Form_Receivables
        Form_Receivables(mainForm)
    elif menu_id == 72:
        from lib.ZionWidgets.PrintingOrder import JPFuncForm_PrintingOrder
        widget = JPFuncForm_PrintingOrder(mainForm)
        widget.addButtons(buts)
    elif menu_id == 73:
        from lib.ZionWidgets.Customer import Form_Customer
        widget = Form_Customer(mainForm)
        widget.addButtons(buts)
    elif menu_id == 13:
        from lib.ZionWidgets.User import Form_User
        widget = Form_User(mainForm)
        widget.addButtons(buts)
    elif menu_id == 15:
        from lib.ZionWidgets.Complete import JPFuncForm_Complete
        widget = JPFuncForm_Complete(mainForm)
        widget.addButtons(buts)
    elif menu_id == 18:
        from lib.ZionWidgets.Adjustment import JPFuncForm_Adjustment
        widget = JPFuncForm_Adjustment(mainForm)
        widget.addButtons(buts)
    elif menu_id == 56:
        from lib.ZionWidgets.Quotation import JPFuncForm_Quotation
        widget = JPFuncForm_Quotation(mainForm)
        widget.addButtons(buts)
    elif menu_id == 55:
        from lib.ZionWidgets.PrintingQuotation import JPFuncForm_PrintingQuotation
        widget = JPFuncForm_PrintingQuotation(mainForm)
        widget.addButtons(buts)
    else:
        Form_Background(mainForm)

    return


if __name__ == "__main__":
    app = QApplication(argv)
    db = JPDb()
    db.setDatabaseType(JPDbType.MySQL)
    MainWindow = QMainWindow()
    mianFormProcess(MainWindow)
    MainWindow.showMaximized()
    sys_exit(app.exec_())
