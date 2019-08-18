from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from lib.JPMvc.JPFuncForm import JPFunctionForm
from lib.ZionWidgets.Order import EditForm_Order
from lib.ZionWidgets.PrintingOrder import EditForm_PrintingOrder
from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex

class ZionFuncForm(JPFunctionForm):
    def __init__(self, parent):
        super().__init__(parent)
        self.CP_m_sql = """
                SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                    , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                    , fPayable, fDesconto, fNote,fEntryID,fSucursal
                FROM t_order
                WHERE fOrderID = '{}'
                """
        self.CP_s_sql = """
                SELECT fID, fOrderID, fQuant AS '数量Qtd',
                    fProductName AS '名称Descrição',
                    fLength AS '长Larg.', fWidth AS '宽Comp.',
                    fPrice AS '单价P. Unitario', fAmount AS '金额Total'
                FROM t_order_detail
                WHERE fOrderID = '{}'
                """
        self.TP_m_sql = """
            SELECT fOrderID, fCelular, fRequiredDeliveryDate, fContato
                , fTelefone, fVendedorID, fCustomerID, fOrderDate
                , fSucursal, fQuant, fNumerBegin, fNumerEnd
                , fPrice, fLogo, fEspecieID, fAvistaID, fTamanhoID
                , fNrCopyID, fPagePerVolumn, fNote, fAmount, fDesconto
                , fTax, fPayable,fEntryID
            FROM t_order
            WHERE fOrderID = '{}'
            """

    def onCurrentRowChanged(self, QModelIndex1, QModelIndex2):
        cur_tp = self.getCurrentSelectPKValue()[0:2]
        if cur_tp == 'CP':
            self.setEditFormSQL(self.CP_m_sql, self.CP_s_sql)
        elif cur_tp == 'TP':
            self.setEditFormSQL(self.TP_m_sql, None)

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        cur_tp = self.getCurrentSelectPKValue()[0:2]
        mycls = {'CP': EditForm_Order, 'TP': EditForm_PrintingOrder}
        C = mycls[cur_tp]
        F = C(sql_main=sql_main,
              edit_mode=edit_mode,
              sql_sub=sql_sub,
              PKValue=PKValue)
        self.onAfterCreatedForm(cur_tp,F)
        return F

    def onAfterCreatedForm(self, cur_tp, form):
        return
