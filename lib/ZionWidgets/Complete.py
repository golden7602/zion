from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtPrintSupport import QPrinter

from lib.JPPrintReport import JPPrintSectionType, JPReport
from lib.ZionPublc import JPPub
from lib.ZionWidgets.FuncFormBase import JPFunctionForm
from lib.JPMvc.JPModel import JPTableViewModelReadOnly

class _myMod(JPTableViewModelReadOnly):
    def __init__(self, *args):
        super().__init__(*args)
        self.f = QFont()
        self.f.Black = True
        self.f.setBold(True)

    def data(self, Index, role: int = Qt.DisplayRole):
        if role == Qt.TextColorRole:
            return QColor(Qt.blue)
        return super().data(Index, role)



class JPFuncForm_Complete(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_1 = """
                SELECT fOrderID as `订单号码OrderID`,
                    fOrderDate as `日期OrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fDelivered1 as `fDelivered`,
                    fDeliverer_Name as `fDeliverer`,
                    fDelivered as `fDelivered`,
                    fCity as `城市City`,
                    fEndereco as `fEndereco`,
                    fContato as `联系人Contato`,
                    fCelular as `手机Celular`,
                    fTelefone as `fTelefone`,
                    fDeliverReaded
                FROM v_order AS o
                WHERE fConfirmed=1 AND fCanceled=0 And fOrderDate{date}
                        AND (fDelivered={ch1} OR fDelivered={ch2})
                ORDER BY  forderID DESC"""

        sql_2 = """
                SELECT fOrderID as `订单号码OrderID`,
                    fOrderDate as `日期OrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fDelivered1 as `fDelivered`,
                    fDeliverer_Name as `fDeliverer`,
                    fDelivered as `fDelivered`,
                    fCity as `城市City`,
                    fEndereco as `fEndereco`,
                    fContato as `联系人Contato`,
                    fCelular as `手机Celular`,
                    fTelefone as `fTelefone`,
                    fDeliverReaded
                FROM v_order AS o
                WHERE fConfirmed=1 AND fCanceled=0
                ORDER BY  forderID DESC"""


        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('Unfinished')
        self.checkBox_2.setText('Completed')
        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(False)
        super().setSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)

    def getModelClass(self):
        return _myMod

    def but_click(self, name):
        for n, fun in JPFuncForm_Complete.__dict__.items():
            if n.upper() == 'BTN{}CLICKED'.format(name.upper()):
                fun(self)

    def getCurrentCustomerID(self):
        index = self.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.model.TabelFieldInfo.getOnlyData([index.row(), 0])

    @pyqtSlot()
    def on_CMDEXPORTTOEXCEL_clicked(self):
        print('单击了CMDEXPORTTOEXCEL按钮')

    @pyqtSlot()
    def on_CMDNEW_clicked(self):
        print("CMDNEW被下")
        #showEditForm_Order(self.MainForm, JPFormModelMainSub.New)

    @pyqtSlot()
    def on_CMDBROWSE_clicked(self):
        cu_id = self.getCurrentCustomerID()
        if not cu_id:
            return
        #showEditForm_Order(self.MainForm, JPFormModelMainSub.ReadOnly, cu_id)
        print("CMDBROWSE被下", cu_id)