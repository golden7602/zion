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
from lib.JPMvc.JPFuncForm import JPFunctionForm
from lib.ZionWidgets.Order import EditForm_Order
from lib.ZionPublc import JPDb


class JPFuncForm_Quotation(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_1 = """
                select 
                    fOrderID as `报价单号OrderID`, 
                    fOrderDate as `报价单日期OrderDate`, 
                    fCustomerName as `客户名Cliente`, 
                    fNUIT as `税号NUIT`, 
                    fCity as `城市City`, 
                    fConfirmed1 as `确认Confirmed`, 
                    fEntry_Name as `录入Entry`, 
                    fConfirm_Name as `fConfirm_Name`, 
                    fAmount as `金额SubTotal`, 
                    fTax as `税金IVA`, 
                    fPayable as `应付金额Valor a Pagar`, 
                    fDesconto as `折扣Desconto`, 
                    fContato as `联系人Contato`, 
                    fCelular as `手机Celular`, 
                    fTelefone as `fTelefone`, 
                    fConfirmed as `已确认Confirmed`, 
                    fCustomerID as `客户编号CustomerID` 
                from v_quotation 
                where  left(fOrderID,2)='QS'
                and fCanceled = 0 
                and fOrderDate{date}
                order by  fOrderID DESC"""
        sql_2 = """
                select 
                    fOrderID as `报价单号OrderID`, 
                    fOrderDate as `报价单日期OrderDate`, 
                    fCustomerName as `客户名Cliente`, 
                    fNUIT as `税号NUIT`, 
                    fCity as `城市City`, 
                    fConfirmed1 as `确认Confirmed`, 
                    fEntry_Name as `录入Entry`, 
                    fConfirm_Name as `fConfirm_Name`, 
                    fAmount as `金额SubTotal`, 
                    fTax as `税金IVA`, 
                    fPayable as `应付金额Valor a Pagar`, 
                    fDesconto as `折扣Desconto`, 
                    fContato as `联系人Contato`, 
                    fCelular as `手机Celular`, 
                    fTelefone as `fTelefone`, 
                    fConfirmed as `已确认Confirmed`, 
                    fCustomerID as `客户编号CustomerID` 
                from v_quotation 
                where  left(fOrderID,2)='QS'
                and fCanceled = 0 
                order by  fOrderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setHidden(True)
        self.checkBox_2.setHidden(True)
        super().setListFormSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)
        m_sql = """
                SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                    , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                    , fPayable, fDesconto, fNote,fEntryID,fSucursal
                FROM t_quotation
                WHERE fOrderID = '{}'
                """
        s_sql = """
                SELECT fID, fOrderID, fQuant AS '数量Qtd',
                    fProductName AS '名称Descrição',
                    fLength AS '长Larg.', fWidth AS '宽Comp.',
                    fPrice AS '单价P. Unitario', fAmount AS '金额Total'
                FROM t_quotation_detail
                WHERE fOrderID = '{}'
                """
        self.setEditFormSQL(m_sql, s_sql)

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        return Edit_Order_Quotation(sql_main=sql_main,
                                    edit_mode=edit_mode,
                                    sql_sub=sql_sub,
                                    PKValue=PKValue)

    @pyqtSlot()
    def on_CmdOrder_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        newPKSQL = JPDb().NewPkSQL(self.PKRole)
        sql = [
            """
        INSERT INTO t_order (fOrderID, fOrderDate, fVendedorID
            , fRequiredDeliveryDate, fCustomerID
            , fContato, fCelular, fTelefone, fAmount, fTax
            , fPayable, fDesconto, fNote, fEntryID, fSucursal)
        SELECT '@PK', fOrderDate, fVendedorID
            , fRequiredDeliveryDate, fCustomerID
            , fContato, fCelular, fTelefone, fAmount, fTax
            , fPayable, fDesconto, fNote, fEntryID, fSucursal
        FROM t_quotation
        WHERE fOrderID = '{fOrderID}'""".format(cu_id),
        """
        INSERT INTO t_order_detail (fOrderID, fQuant, fProductName
            , fLength, fWidth, fPrice, fAmount)
        SELECT '@PK', fQuant, fProductName, fLength, fWidth
            , fPrice, fAmount
        FROM t_quotation_detail
        WHERE fOrderID = '{fOrderID}'""".format(cu_id)
        ]
        sql = newPKSQL[0:2] + sql + newPKSQL[2:]
        try:
            isOK, result = JPDb().executeTransaction(sql)
            if isOK:
                info = '已经根据报价单生成了订单【{id}】，请修改此订单信息!\n'
                info = info + 'The order [{id}] has been generated according '
                info = info + 'to the quotation. Please modify the order information.'
                QMessageBox.information(self, info.format(result),
                                        QMessageBox.Yes, QMessageBox.Yes)
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()


class Edit_Order_Quotation(EditForm_Order):
    def __init__(self, sql_main, sql_sub=None, edit_mode=None, PKValue=None):
        super().__init__(sql_main,
                         sql_sub=sql_sub,
                         edit_mode=edit_mode,
                         PKValue=PKValue)
        self.setPkRole(6)
