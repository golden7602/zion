from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot, Qt, QModelIndex
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QMessageBox, QPushButton, QWidget, QLineEdit,
                             QAction)

from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPFunction import JPDateConver, setButtonIcon
from lib.JPMvc.JPEditFormModel import JPEditFormDataMode, JPFormModelMain
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.ZionPublc import JPDb,JPPub
from Ui.Ui_FormCustomer_Arrears import Ui_Form as Ui_Form_List
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPExcel.JPExportToExcel import JPExpExcelFromTabelFieldInfo


class Form_FormCustomer_Arrears(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.ui = Ui_Form_List()
        self.ui.setupUi(self)
        mainform.addForm(self)

        icon = QIcon(getcwd() + "\\res\\ico\\search.png")
        action = self.ui.lineEdit.addAction(icon, QLineEdit.TrailingPosition)
        action.triggered.connect(self.actionClick)

        self.actionClick()

    def actionClick(self):
        sql = """
            SELECT c.fCustomerID as `ID`, 
                c.fCustomerName as `客户名称Cliente`, 
                c.fNUIT as `税号NUIT`, 
                c.fCity as `城市City`,
                QDD.dd AS 订单金额OrderAmount,
                QSK.sk AS Aeceivables收款, 
                QDD.dd - QSK.sk AS Arrears欠款
            FROM t_customer c
                LEFT JOIN (
                    SELECT fCustomerID, SUM(fAmountCollected) AS sk
                    FROM t_receivables
                    GROUP BY fCustomerID
                ) QSK
                ON QSK.fCustomerID = c.fCustomerID
                LEFT JOIN (
                    SELECT fCustomerID, SUM(fAmount) AS dd
                    FROM t_order
                    WHERE fCanceled = 0
                        AND fConfirmed = 1
                    GROUP BY fCustomerID
                ) QDD
                ON QDD.fCustomerID = c.fCustomerID
            WHERE NOT (isnull(QDD.dd)
            AND isnull(QSK.sk)) AND c.fCustomerName like '%{}%'"""
        txt = self.ui.lineEdit.text()
        txt = txt if txt else ''
        sql = sql.format(txt)

        tv = self.ui.tableView
        self.dataInfo = JPTabelFieldInfo(sql)
        self.mod = JPTableViewModelEditForm(tv, self.dataInfo)
        tv.setModel(self.mod)
        tv.resizeColumnsToContents()

        tv.selectionModel(
        ).currentRowChanged[QModelIndex, QModelIndex].connect(self.refreshRec)
        tv.selectionModel(
        ).currentRowChanged[QModelIndex, QModelIndex].connect(
            self.refreshOrder)

    def __getUID(self):
        r = self.ui.tableView.currentIndex()
        if r:
            return self.dataInfo.DataRows[r.row()].Datas[0]
        else:
            return -1

    def refreshOrder(self):
        sql = """
        SELECT fOrderID,
            fOrderDate,
            fPrice,
            fQuant,
            fAmount,
            fDesconto,
            fTax,
            fPayable
        FROM t_order
        WHERE fCustomerID={uid}
        ORDER BY  fOrderDate Desc"""
        tv = self.ui.tableView_order
        sql = sql.format(uid=self.__getUID())
        self.dataInfo_order = JPTabelFieldInfo(sql)
        self.mod_order = JPTableViewModelEditForm(tv, self.dataInfo_order)
        tv.setModel(self.mod_order)
        tv.resizeColumnsToContents()

    def refreshRec(self):
        sql = """SELECT fID,
            fReceiptDate,
            e.fTitle AS 收款方式 ,
            fAmountCollected,
            u.fUsername
        FROM t_receivables AS r
        LEFT JOIN t_enumeration AS e
            ON r.fPaymentMethodID=e.fItemID
        LEFT JOIN sysusers AS u
            ON r.fPayeeID=u.fUserID
        WHERE r.fCustomerID={uid}
        ORDER BY  r.fReceiptDate desc"""
        tv = self.ui.tableView_rec
        sql = sql.format(uid=self.__getUID())
        self.dataInfo_rec = JPTabelFieldInfo(sql)
        self.mod_rec = JPTableViewModelEditForm(tv, self.dataInfo_rec)
        tv.setModel(self.mod_rec)
        tv.resizeColumnsToContents()

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item['fMenuText'])
            btn.setObjectName(item['fObjectName'])
            setButtonIcon(btn, item['fIcon'])
            btn.setEnabled(item['fHasRight'])
            self.ui.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_CmdExportToExcel_clicked(self):
        exp = JPExpExcelFromTabelFieldInfo(self.mod.TabelFieldInfo, JPPub().MainForm)
        exp.run()