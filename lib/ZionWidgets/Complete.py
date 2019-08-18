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
from lib.ZionWidgets.ZionFunc import ZionFuncForm
from lib.JPMvc.JPModel import JPTableViewModelReadOnly

class _myMod(JPTableViewModelReadOnly):
    def __init__(self, *args):
        super().__init__(*args)
        self.f = QFont()
        self.f.Black = True
        self.f.setBold(True)
        self._getData=self.TabelFieldInfo.getOnlyData

    def data(self, Index, role: int = Qt.DisplayRole):
        if role == Qt.TextColorRole:
            if self._getData([Index.row(),12]) ==1:
                return QColor(Qt.blue)
        return super().data(Index, role)



class JPFuncForm_Complete(ZionFuncForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_0="""
                SELECT fOrderID as `订单号码OrderID`,
                    fOrderDate as `日期OrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fDelivered1 as `已完成fDelivered`,
                    fDeliverer_Name as `fDeliverer`,
                    fDelivered as `已完成fDelivered`,
                    fCity as `城市City`,
                    fEndereco as `fEndereco`,
                    fContato as `联系人Contato`,
                    fCelular as `手机Celular`,
                    fTelefone as `电话fTelefone`,
                    fDeliverViewed1 as `已查阅Viewed`,
                    fDeliverViewed
                FROM v_order AS o """
        sql_1 = sql_0 + """
                WHERE fConfirmed=1 AND fCanceled=0 And fOrderDate{date}
                        AND (fDelivered={ch1} OR fDelivered={ch2})
                ORDER BY  forderID DESC"""

        sql_2 = sql_0 +"""
                WHERE fConfirmed=1 AND fCanceled=0
                ORDER BY  forderID DESC"""


        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('Unfinished')
        self.checkBox_2.setText('Completed')
        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(False)
        self.setListFormSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(5, True)
        self.tableView.setColumnHidden(12, True)

    def getModelClass(self):
        return _myMod
