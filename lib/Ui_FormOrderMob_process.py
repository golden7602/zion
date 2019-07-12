# -*- coding: utf-8 -*-

from functools import reduce

from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QIntValidator
#from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QTableWidget,
                             QTableWidgetItem, QWidget)

from globalVar import pub
from JPEditForm import (JPDelegate, JPEditForm, JPEditFormMode,
                        JPEditFormDataMode)
from JPFunction import JPRound
from Ui_FormOrderMob import Ui_Form

#from decimal import Decimal


def mySetText(ctl, f, formatstring):
    if f > 0:
        ctl.setText(formatstring.format(f))
        ctl.__dict__["NewValue"] = f
    else:
        ctl.setText('')
        ctl.__dict__["NewValue"] = 0


class MyFormOrderMobProcess(JPEditForm):
    """订单窗口模板的处理类"""

    def __init__(self, EditMode: JPEditFormDataMode):
        self.__Form = QWidget()
        ui = Ui_Form()
        ui.setupUi(self.__Form)
        super().__init__(UI=ui,
                         MainForm=self.__Form,
                         FormMode=JPEditFormMode.MainSub,
                         EditMode=EditMode,
                         MainTabelName='t_order',
                         ReadViewName='v_order',
                         AuToPkRoleID=1,
                         SubForm=ui.tableWidget,
                         SubTabelName="t_order_detail",
                         SubFormFieldsName=[
                             "fID", "fQuant", "fProductName", "fLength",
                             "fWidth", "fPrice", "fAmount"
                         ])
        tw = self.UI.tableWidget
        tw.setEditTriggers(QAbstractItemView.AllEditTriggers)
        tw.setColumnHidden(0, True)
        self.__AddRowInSubForm()
        dt_None = JPDelegate(tw, 0)
        dt_int = JPDelegate(tw, 2)
        dt_str = JPDelegate(tw, 1)
        dt_dec = JPDelegate(tw, 3)
        dts = [dt_None, dt_int, dt_str, dt_dec, dt_dec, dt_dec, dt_None]
        dt_int.editNext[QModelIndex].connect(self.__EditNext)
        dt_str.editNext[QModelIndex].connect(self.__EditNext)
        dt_dec.editNext[QModelIndex].connect(self.__EditNext)
        for i in range(7):
            tw.setItemDelegateForColumn(i, dts[i])
        wds = [20, 80, 300, 80, 80, 100, 100]
        for i in range(7):
            tw.setColumnWidth(i, wds[i])
        tw.cellChanged[int, int].connect(self.cellChanged)
        tw.cellPressed[int, int].connect(self.__AddRowInSubForm)

    def __EditNext(self, index):
        # 回车后向右
        self.SubForm.setCurrentCell(index.row(), index.column())

    def cellChanged(self, r, c):
        if c == 6:
            self.__AddRowInSubForm()
            return
        tw = self.SubForm
        cols = [
            tw.item(r, i).text().replace(',', '') if tw.item(r, i) else None
            for i in [1, 3, 4, 5]
        ]

        if all(cols):
            v = 0.0
            colsv = [JPRound(float(item), 2) for item in cols]
            v = reduce(lambda x, y: x * y, colsv)
            tw.item(r, 6).setText('{:,.2f}'.format(v))
            tw.item(r, 6).__dict__["NewValue"] = v
            Amount = 0.0
            for i in range(tw.rowCount()):
                if tw.item(r, 6):
                    try:
                        Amount += float(tw.item(i, 6).text().replace(',', ''))
                    except ValueError as e:
                        print(tw.item(i, 6).text().replace(',', ''))
            mySetText(self.UI.fAmount, Amount, '{:,.2f}')
            Desconto = JPRound(float(self.fDesconto.text().replace(',', '')),
                               2) if len(self.UI.fDesconto.text()) > 0 else 0
            Tax = JPRound((Amount - Desconto) * 0.17, 2)
            Payable = JPRound(Amount - Desconto - Tax, 2)
            mySetText(self.UI.fDesconto, Desconto, '{:,.2f}')
            mySetText(self.UI.fTax, Tax, '{:,.2f}')
            mySetText(self.UI.fPayable, Payable, '{:,.2f}')

    # def Show(self):
    #     pass

    #     self.__Form.show()

    def __AddRowInSubForm(self, *args):
        def addrow(tw):
            RV = Qt.AlignRight | Qt.AlignVCenter
            LV = Qt.AlignLeft | Qt.AlignVCenter
            align = [Qt.AlignCenter, RV, LV, RV, RV, RV, RV]
            tw.setRowCount(tw.rowCount() + 1)
            laseRow = tw.rowCount() - 1
            for i in range(7):
                item = QTableWidgetItem()
                item.setTextAlignment(align[i])
                tw.setItem(laseRow, i, item)

        tw = self.SubForm
        if tw.rowCount() == 0:
            addrow(tw)
            return
        if self.SubForm.item(tw.rowCount() - 1, 6).text():
            addrow(tw)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = MyFormOrderMobProcess(JPEditFormDataMode.ReadOnly)
    Form.Show("CP2019-0201000021")
    sys.exit(app.exec_())
