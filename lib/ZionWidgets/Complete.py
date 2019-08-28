from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce

from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtPrintSupport import QPrinter

from lib.JPPrintReport import JPPrintSectionType, JPReport
from lib.ZionPublc import JPPub, JPDb, JPUser
from lib.ZionWidgets.ZionFunc import ZionFuncForm
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from lib.JPMvc.JPFuncForm import JPFunctionForm
from lib.JPMvc.JPEditFormModel import JPFormModelMain, JPFormModelMainHasSub

from Ui.Ui_FormPrintingOrder import Ui_Form as Ui_Form_PrintOrder
from Ui.Ui_FormOrderMob import Ui_Form as Ui_Form_Order


class _myMod(JPTableViewModelReadOnly):
    def __init__(self, *args):
        super().__init__(*args)
        self.f = QFont()
        self.f.Black = True
        self.f.setBold(True)
        self._getData = self.TabelFieldInfo.getOnlyData

    def data(self, Index, role: int = Qt.DisplayRole):
        if role == Qt.TextColorRole:
            if self._getData([Index.row(), 12]) == 1:
                return QColor(Qt.blue)
        return super().data(Index, role)


class _myFuncForm(JPFunctionForm):
    def __init__(self, parent):
        super().__init__(parent)
        self.CP_m_sql = """
                SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                    , fCustomerID, fNote,fEntryID,fSucursal
                    , fContato, fCelular  ,fTelefone
                    , fNUIT, fCity, fEndereco
                FROM v_order_readonly
                WHERE fOrderID = '{}'
                """
        self.CP_s_sql = """
                SELECT fQuant AS '数量Qtd',
                    fProductName AS '名称Descrição',
                    fLength AS '长Comp.', fWidth AS '宽Larg.'
                FROM t_order_detail
                WHERE fOrderID = '{}'
                """
        self.TP_m_sql = """
                SELECT fOrderID, fRequiredDeliveryDate, fVendedorID
                    , fCustomerID, fOrderDate
                    , fSucursal, fQuant, fNumerBegin, fNumerEnd, fPrice
                    , fLogo, fEspecieID, fAvistaID, fTamanhoID, fNrCopyID
                    , fPagePerVolumn, fNote, fEntryID, fContato, fCelular
                    , fTelefone, fNUIT, fCity, fEndereco
                FROM v_order_readonly
                WHERE fOrderID = '{}'
            """

    def onCurrentRowChanged(self, QModelIndex1, QModelIndex2):
        cur_tp = self.getCurrentSelectPKValue()[0:2]
        if cur_tp == 'CP':
            self.setEditFormSQL(self.CP_m_sql, self.CP_s_sql)
        elif cur_tp == 'TP':
            self.setEditFormSQL(self.TP_m_sql, None)


class JPFuncForm_Complete(_myFuncForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_0 = """
                SELECT fOrderID as `订单号码OrderID`,
                    fOrderDate as `日期OrderDate`,
                    fCustomerName as `客户名Cliente`,
                    fDelivered1 as `已完成fDelivered1`,
                    fDeliverer_Name as `fDeliverer`,
                    fDelivered as `已完成fDelivered`,
                    fCity as `城市City`,
                    fEndereco as `fEndereco`,
                    fContato as `联系人Contato`,
                    fCelular as `手机Celular`,
                    fTelefone as `电话fTelefone`,
                    fDeliverViewed1 as `已查阅Viewed1`,
                    fDeliverViewed as `已查阅Viewed`
                FROM v_order AS o """
        sql_1 = sql_0 + """
                WHERE fConfirmed=1 AND fCanceled=0 And fOrderDate{date}
                        AND (fDelivered={ch1} OR fDelivered={ch2})
                ORDER BY  forderID DESC"""

        sql_2 = sql_0 + """
                WHERE fConfirmed=1 AND fCanceled=0
                ORDER BY  forderID DESC"""

        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('finished')
        self.checkBox_2.setText('UnCompleted')
        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(False)
        self.setListFormSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(5, True)
        self.tableView.setColumnHidden(12, True)

    def getModelClass(self):
        return _myMod

    @pyqtSlot()
    def on_CmdBrowse_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        sql = "update t_order set fDeliverViewed=1 where fOrderID='{}'"
        db = JPDb()
        db.executeTransaction(sql.format(cu_id))
        super().on_CmdBrowse_clicked()
        self.refreshListForm()

    @pyqtSlot()
    def on_CmdComplete_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        sql = "update t_order set fDeliverViewed=1,fDelivered=1,"
        sql = sql + "fDelivererID={uid} where fOrderID='{pk}'"
        db = JPDb()
        us = JPUser()
        sql = sql.format(pk=cu_id, uid=us.currentUserID())
        msg = '确认要交付记录【{cu_id}】吗？\n'
        msg = msg + 'Are you sure you want to deliver this order[{cu_id}]?'
        msg = msg.format(cu_id=cu_id)
        if QMessageBox.question(JPPub().MainForm, '确认', msg,
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:
            db.executeTransaction(sql)
            self.refreshListForm()

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        cur_tp = self.getCurrentSelectPKValue()[0:2]
        mycls = {'CP': EditForm_Order, 'TP': EditForm_PrintingOrder}
        C = mycls[cur_tp]
        F = C(sql_main=sql_main,
              edit_mode=edit_mode,
              sql_sub=sql_sub,
              PKValue=PKValue)
        # self.onAfterCreatedForm(cur_tp, F)
        return F


def hideObject(ui):
    ui.butSave.hide()
    ui.butPrint.hide()
    ui.butPDF.hide()
    ui.label.hide()
    ui.label_13.hide()
    ui.label_14.hide()
    ui.label_15.hide()
    ui.fAmount.hide()
    ui.fDesconto.hide()
    ui.fTax.hide()
    ui.fPayable.hide()
    ui.verticalLayout_2.hide()


class EditForm_Order(JPFormModelMainHasSub):
    def __init__(self,
                 sql_main,
                 PKValue,
                 sql_sub,
                 edit_mode,
                 flags=Qt.WindowFlags()):
        super().__init__(Ui_Form_Order(),
                         sql_main=sql_main,
                         PKValue=PKValue,
                         sql_sub=sql_sub,
                         edit_mode=edit_mode,
                         flags=flags)
        self.setPkRole(1)
        self.ui.label_logo.setPixmap(QPixmap(getcwd() +
                                             "\\res\\Zions_100.png"))
        hideObject(self.ui)
        self.readData()

    def onGetFieldsRowSources(self):
        pub = JPPub()
        u_lst = [[item[1], item[0]] for item in JPUser().getAllUserList()]
        return [('fCustomerID', pub.getCustomerList(), 1),
                ('fVendedorID', pub.getEnumList(10), 1),
                ('fEntryID', u_lst, 1)]


class EditForm_PrintingOrder(JPFormModelMain):
    def __init__(self, sql_main, sql_sub=None, edit_mode=None, PKValue=None):
        super().__init__(Ui_Form_PrintOrder(),
                         sql_main,
                         PKValue=PKValue,
                         edit_mode=edit_mode)
        pix = QPixmap(getcwd() + "\\res\\Zions_100.png")
        self.ui.label_logo.setPixmap(pix)
        hideObject(self.ui)
        self.readData()

    def onGetFieldsRowSources(self):
        pub = JPPub()
        u_lst = [[item[1], item[0]] for item in JPUser().getAllUserList()]
        return [('fCustomerID', pub.getCustomerList(), 1),
                ('fVendedorID', pub.getEnumList(10), 1),
                ('fEspecieID', pub.getEnumList(2), 1),
                ('fAvistaID', pub.getEnumList(7), 1),
                ('fTamanhoID', pub.getEnumList(8), 1),
                ('fNrCopyID', pub.getEnumList(9), 1), ('fEntryID', u_lst, 1)]
