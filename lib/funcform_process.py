# -*- coding: utf-8 -*-
"""
功能窗体各具体处理功能的汇总包
"""

import sys
import os
sys.path.append(os.getcwd())


import datetime

from dateutil.relativedelta import relativedelta
from PyQt5.QtCore import QMetaObject, Qt, QThread, pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QDialog, QMessageBox, QPushButton, QTableWidget,
                             QTableWidgetItem, QWidget)

#from Ui.Ui_FuncFormMob import Ui_Form as Func_Ui_Form
from lib.globalVar import pub
from lib.JPExcel.JPExportToExcel import clsExportToExcelFromTableWidget
#from lib.whereStringCreater import clsWhereStringCreater



class clsmyStackedWidget(object):
    """功能窗口的堆叠布局类"""

    def __init__(self, StackedWidget, MainForm):
        self.StackedWidget = StackedWidget
        self.MainForm = MainForm
        self.ui = None
        self.objFuncform = None
        # 设置一个用于创建功能窗体处理类的字典，键为对象名,值为对应的类名
        self.clsFuncFormDict = {
            'F_ORDER': funcform_Order,
            'F_PRINTINGORDER': funcform_PrintingOrder,
            'F_PAYMENTORDER': funcform_PaymentOrder
        }

    def TreeViewItemClicked(self, info):
        try:
            frm = self.StackedWidget
            if frm.count() == 1:
                frm.removeWidget(frm.currentWidget)
            sql = "select fNMID,fMenuText,fParentId from sysnavigationmenus \
                where fParentId={} order by fDispIndex"

            items = pub.getDict(sql.format(info.jpData["fNMID"]))
            tempWidget = QWidget()
            # 新建立一个功能窗口对象
            self.ui = Func_Ui_Form()
            self.ui.setupUi(tempWidget)
            self.ui.label_FuncFullPath.setText(info.FullPath)
            objName = info.jpData["fObjectName"].upper()
            if objName in self.clsFuncFormDict:
                self.objFuncform = self.clsFuncFormDict[objName](self.ui,
                                                                 self.MainForm)
            else:
                raise AttributeError
            for i in range(0, len(items)):
                nm = items[i]["fMenuText"]
                # 添加按钮
                btn = QPushButton(nm)
                btn.setObjectName('btn' + nm)  # 使用setObjectName设置对象名称
                btn.tableWidget = self.ui.tableWidget
                btn.clicked.connect(self.objFuncform.AnybtnClick)
                self.ui.horizontalLayout_Button.addWidget(btn)
            frm.addWidget(tempWidget)
            frm.currentWidget = tempWidget
            frm.setCurrentIndex(1)
            self.objFuncform.btnRefreshClick()
        except AttributeError as err:
            print(err)
            tempWidget = QWidget()
            # tempWidget.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.StackedWidget.addWidget(tempWidget)
            self.StackedWidget.currentWidget = tempWidget
            self.StackedWidget.setCurrentIndex(1)
        else:
            return


class MyThreadReadTable(QThread):
    """加载数据到列表的线程类"""

    def __init__(self, tableWidget, MainForm):
        self.tableWidget = tableWidget
        self.MainForm = MainForm

    def addItemToTabel(self, FieldType, FieldValue, item):
        left = (Qt.AlignLeft | Qt.AlignVCenter)
        center = (Qt.AlignCenter | Qt.AlignVCenter)
        right = (Qt.AlignRight | Qt.AlignVCenter)
        if FieldType in (1, 3, 8):  # TinyInt,Int
            item.setText(str(FieldValue))
            item.setTextAlignment(right)
        elif FieldType in (7, 10):  # TS,DATE
            item.setText(str(FieldValue))
            item.setTextAlignment(center)
        elif FieldType == 16:  # Bit
            item.setText(str(ord(FieldValue)))
            item.setTextAlignment(center)
        elif FieldType == 246:  # Decimal
            item.setText('{:,.2f}'.format(FieldValue))
            item.setTextAlignment(right)
        elif FieldType in (253, 254):  # VChar,Char
            item.setText(str(FieldValue))
            item.setTextAlignment(left)
        else:  # other
            item.setText(str(FieldValue))
            item.setTextAlignment(left)

    def run(self, sql, backgroundWhenValueIsTrueFieldName):
        clr = QColor(200, 200, 200)
        cur = pub.GetDatabase().cursor()
        cur.execute("select * from (" + sql + ") as a__a limit 0")
        flds = cur._result.fields
        fldsType_Colde = []
        fieldIndex = None
        for i in range(0, len(flds)):
            if flds[i].name == backgroundWhenValueIsTrueFieldName:
                fieldIndex = i
                break
        self.tableWidget.setColumnCount(len(flds))
        self.tableWidget.FieldDict = flds  #把字段属性字典存入表对象
        self.MainForm.Label.setText('准备数据中')
        self.MainForm.ProgressBar.show()
        for i in range(0, len(flds)):
            fldsType_Colde.append(flds[i].type_code)
            item = QTableWidgetItem(flds[i].name)
            self.tableWidget.setHorizontalHeaderItem(i, item)
        cur.execute(sql)
        self.tableWidget.setRowCount(cur.rowcount)
        self.MainForm.ProgressBar.setRange(0, cur.rowcount)
        for j in range(0, cur.rowcount):
            row = cur.fetchone()
            self.MainForm.ProgressBar.setValue(j + 1)
            for k in range(0, len(row)):
                item = QTableWidgetItem()
                if row[k]:
                    self.addItemToTabel(flds[k].type_code, row[k], item)
                    self.tableWidget.setItem(j, k, item)
                else:
                    self.tableWidget.setItem(j, k, item)
                if row[fieldIndex]:
                    item.setForeground(clr)
        self.MainForm.Label.setText('')
        self.MainForm.ProgressBar.hide()


class Funcform(object):
    """
    此类是功能窗口通用功能的基类，不能直接实例化，应该实例化其子类
    """
    backgroundWhenValueIsTrueFieldName = ''

    def __init__(self, ui, MainForm):
        self.ui = ui
        self.tableWidget = ui.tableWidget
        self.MainForm = MainForm
        self.DefauleParaSQL = ''
        self.MainTableName = ''
        self.SubTableName = ''
        self.whereDlg = None
        self.btnProcessDict = {
            "SEARCH": self.btnSearchClick,
            "REFRESH": self.btnRefreshClick,
            "EXPORTTOEXCEL": self.btnExportToExcel
        }
        self.comboBox = ui.comboBox
        self.comboBox.addItems(['Today', 'Last Month', 'Last Year', 'All'])
        self.checkBox1 = ui.checkBox_1
        self.checkBox2 = ui.checkBox_2
        self.checkBox1.clicked.connect(self.btnRefreshClick)
        self.checkBox2.clicked.connect(self.btnRefreshClick)
        self.comboBox.activated['int'].connect(self.btnRefreshClick)

    def btnSearchClick(self):
        self.whereDlg = clsWhereStringCreater(self.tableWidget, self.MainForm)
        self.whereDlg.show()

    def btnRefreshClick(self):
        if self.DefauleParaSQL:
            self.tableWidget.clear()
            thr = MyThreadReadTable(self.tableWidget, self.MainForm)
            ch1 = int(not self.ui.checkBox_1.isChecked())
            ch2 = int(self.ui.checkBox_2.isChecked())
            cb = {
                0:
                '=CURRENT_DATE()',
                1: (datetime.date.today() -
                    relativedelta(months=1)).strftime(">='%Y-%m-%d'"),
                2: (datetime.date.today() -
                    relativedelta(years=1)).strftime(">='%Y-%m-%d'"),
                3:
                '=fOrderDate'
            }
            thr.run(
                self.DefauleParaSQL.format(
                    ch1, ch2, cb[self.ui.comboBox.currentIndex()]),
                self.backgroundWhenValueIsTrueFieldName)
            self.ui.tableWidget.resizeColumnsToContents()

    def btnExportToExcel(self):
        exp = clsExportToExcelFromTableWidget(self.tableWidget, self.MainForm)
        exp.run()

    def AnybtnClick(self):  # ,btnCpation):
        btnName = self.MainForm.sender().text().upper()
        if btnName in self.btnProcessDict:
            self.btnProcessDict[btnName]()
        print(self.MainForm.sender().text())


class funcform_Order(Funcform):
    def __init__(self, ui, MainForm):
        super().__init__(ui, MainForm)
        self.tableWidget = ui.tableWidget
        self.MainForm = MainForm
        self.DefauleParaSQL = "Select * from v_order where (fCanceled=0 and left(fOrderID,2)='CP' \
            and (fSubmited={} or fSubmited={}) and fOrderDate{})"

        self.backgroundWhenValueIsTrueFieldName = 'fSubmited'
        ui.checkBox_1.setText('UnSubmited')
        ui.checkBox_2.setText('Submited')
        ui.checkBox_1.setChecked(True)
        ui.checkBox_2.setChecked(False)

    def btnNewClicked(self):
        pass

    def btnBrowseClicked(self):
        pass


class funcform_PrintingOrder(Funcform):
    def __init__(self, ui, MainForm):
        super().__init__(ui, MainForm)
        self.tableWidget = ui.tableWidget
        self.MainForm = MainForm
        self.DefauleParaSQL = "Select * from v_order where (fCanceled=0 and left(fOrderID,2)='TP' \
            and (fSubmited={} or fSubmited={}) and fOrderDate{})"

        super().backgroundWhenValueIsTrueFieldName = 'fSubmited'
        ui.checkBox_1.setText('UnSubmited')
        ui.checkBox_2.setText('Submited')
        ui.checkBox_1.setChecked(True)
        ui.checkBox_2.setChecked(False)

    def btnNewClicked(self):
        pass

    def btnBrowseClicked(self):
        pass


class funcform_PaymentOrder(Funcform):
    def __init__(self, ui, MainForm):
        super().__init__(ui, MainForm)
        self.tableWidget = ui.tableWidget
        self.MainForm = MainForm
        self.DefauleParaSQL = "Select * from v_order where (fCanceled=0 and (fConfirmed={} or fConfirmed={}) and fOrderDate{})"
        self.backgroundWhenValueIsTrueFieldName = 'fConfirmed'
        ui.checkBox_1.setText('UnConfirmed')
        ui.checkBox_2.setText('Confirmed')
        ui.checkBox_1.setChecked(True)
        ui.checkBox_2.setChecked(False)

    def btnBrowseClicked(self):
        pass
