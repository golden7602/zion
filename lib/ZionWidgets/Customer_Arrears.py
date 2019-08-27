from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget

from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPFunction import JPDateConver, setButtonIcon
from lib.JPMvc.JPEditFormModel import JPEditFormDataMode, JPFormModelMain
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.ZionPublc import JPDb
from Ui.Ui_FormCustomer_Arrears import Ui_Form as Ui_Form_List
from lib.JPDatabase.Query import JPQueryFieldInfo


class Form_FormCustomer_Arrears(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.ui = Ui_Form_List()
        self.ui.setupUi(self)
        mainform.addForm(self)
        self.SQL = """
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
            AND isnull(QSK.sk))"""
        self.refreshTable()
        self.refreshCombobox()

    def refreshCombobox(self):
        sql = """select fCustomerName,fCustomerID
                from  t_customer order by fCustomerName"""
        tab = JPTabelFieldInfo(sql)
        lst=[r.Datas for r in tab.DataRows]
        tab.Fields[1].RowSource=lst
        cbo = self.ui.comboBox.setFieldInfo(tab.Fields[1])

        # cbo.DisabledEvent = True
        # cbo.clear()
        # lst = [[item.Datas[1], item.Datas[0]] for item in tab.DataRows]
        # cbo.setEditable(True)
        # cbo.clear()
        # for r in lst:
        #     cbo.addItem(r[0], r[1])
        # cbo.setCurrentIndex(-1)
        # cbo.DisabledEvent = False

    def refreshTable(self):
        cbo = self.ui.comboBox
        tv = self.ui.tableView
        cid = cbo.currentIndex()
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
                    WHERE fCustomerID={cid}
                    GROUP BY fCustomerID
                ) QSK
                ON QSK.fCustomerID = c.fCustomerID
                LEFT JOIN (
                    SELECT fCustomerID, SUM(fAmount) AS dd
                    FROM t_order
                    WHERE fCanceled = 0
                        AND fConfirmed = 1
                        AND fCustomerID={cid}
                    GROUP BY fCustomerID
                ) QDD
                ON QDD.fCustomerID = c.fCustomerID
            WHERE c.fCustomerID={cid} AND NOT (isnull(QDD.dd)
            AND isnull(QSK.sk))"""

        sql = self.SQL if cid == -1 else sql.format(cid=cid)
        self.dataInfo = JPTabelFieldInfo(sql)
        self.mod = JPTableViewModelEditForm(tv, self.dataInfo)
        tv.setModel(self.mod)
        tv.resizeColumnsToContents()

    def on_comboBox_currentIndexChanged(self, index):
        # if self.ui.comboBox.DisabledEvent:
        #     return
        self.refreshTable()

    def addButtons(self, btnNames: list):
        return
