from functools import reduce
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from lib.JPDatabase.Database import JPDb
from lib.JPMvc.JPEditFormModel import JPFormModelMainHasSub, JPEditFormDataMode
from lib.JPMvc.JPFuncForm import JPFunctionForm
#from lib.JPMvc.JPModel import JPEditFormDataMode, JPFormModelMainSub
from lib.JPPrintReport import JPPrintSectionType
from lib.ZionPublc import JPPub, JPUser
from lib.ZionReport.OrderReportMob import Order_report_Mob
from Ui.Ui_FormOrderMob import Ui_Form
from lib.JPFunction import JPRound


class JPFuncForm_Order(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_0 = """
                SELECT fOrderID as 订单号码OrderID,
                        fOrderDate as 日期OrderDate,
                        fCustomerName as 客户名Cliente,
                        fCity as 城市City,
                        fSubmited1 as 提交Submited,
                        fSubmit_Name as 提交人Submitter,
                        fRequiredDeliveryDate as 交货日期RequiredDeliveryDate,
                        fAmount as 金额SubTotal,
                        fDesconto as 折扣Desconto,
                        fTax as 税金IVA,
                        fPayable as `应付金额Valor a Pagar`,
                        fContato as 联系人Contato,
                        fCelular as 手机Celular,
                        fSubmited AS fSubmited,
                        fEntry_Name as 录入Entry
                FROM v_order AS o"""
        sql_1 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                        AND (fSubmited={ch1}
                        OR fSubmited={ch2})
                        AND fOrderDate{date}
                ORDER BY  forderID DESC"""
        sql_2 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                ORDER BY  forderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('UnSubmited')
        self.checkBox_2.setText('Submited')
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(True)
        super().setListFormSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)
        self.fSubmited_column = 13
        m_sql = """
                SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                    , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                    , fPayable, fDesconto, fNote,fEntryID
                FROM t_order
                WHERE fOrderID = '{}'
                """
        s_sql = """
                SELECT fID, fOrderID, fQuant AS '数量Qtd',
                    fProductName AS '名称Descrição',
                    fLength AS '长Larg.', fWidth AS '宽Comp.',
                    fPrice AS '单价P. Unitario', fAmount AS '金额Total'
                FROM t_order_detail
                WHERE fOrderID = '{}'
                """
        super().setEditFormSQL(m_sql, s_sql)

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        return EditForm_Order(sql_main=sql_main,
                              edit_mode=edit_mode,
                              sql_sub=sql_sub,
                              PKValue=PKValue)

    @pyqtSlot()
    def on_CmdSubmit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        db = JPDb()
        info = self.model.TabelFieldInfo
        submitted = info.getOnlyData([
            self.tableView.selectionModel().currentIndex().row(),
            self.fSubmited_column
        ])
        if submitted == 1:
            msg = '记录【{cu_id}】已经提交，不能重复提交!\nThe order [{cu_id}] '
            msg = msg + 'has been submitted, can not be repeated submission!'
            msg = msg.replace("{cu_id}", str(cu_id))
            QMessageBox.warning(self, '提示', msg, QMessageBox.Ok,
                                QMessageBox.Ok)
            return
        msg = '提交后订单将不能修改！确定继续提交记录【{cu_id}】吗？\n'
        msg = msg + 'The order "{cu_id}" will not be modified after submission. '
        msg = msg + 'Click OK to continue submitting?'
        msg = msg.replace("{cu_id}", str(cu_id))
        if QMessageBox.question(self, '确认', msg, QMessageBox.Ok,
                                QMessageBox.Ok) == QMessageBox.Ok:
            sql = "update {tn} set fSubmited=1 where {pk_n}='{pk_v}';"
            sql1 = "select '{pk_v}';"
            sql = sql.format(tn=self.EditFormMainTableName,
                             pk_n=self.EditFormPrimarykeyFieldName,
                             pk_v=cu_id)
            if db.executeTransaction([sql, sql1.format(pk_v=cu_id)]):
                self.btnRefreshClick()


# #继承模型，为了设置重载方法，必要要时也可以用动态绑定到函数
# class myMainSubMode(JPFormModelMainSub):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def subModel_AfterSetDataBeforeInsterRowEvent(self, row_data, Index):
#         if row_data is None:
#             return False
#         if row_data[7] is None:
#             return False
#         data = row_data
#         if data[7] == 0:
#             return False
#         lt = [data[2], data[4], data[5], data[6], data[7]]
#         lt = [float(str(i)) if i else 0 for i in lt]
#         return int(lt[4] * 100) == int(
#             reduce(lambda x, y: x * y, lt[0:4]) * 100)


class EditForm_Order(JPFormModelMainHasSub):
    def __init__(self,
                 sql_main=None,
                 PKValue=None,
                 sql_sub=None,
                 edit_mode=JPEditFormDataMode.ReadOnly,
                 flags=Qt.WindowFlags()):
        super().__init__(Ui_Form(),
                         sql_main=sql_main,
                         PKValue=PKValue,
                         sql_sub=sql_sub,
                         edit_mode=edit_mode,
                         flags=flags)
        self.setPkRole(1)
        self.cacuTax = True
        self.ui.label_logo.setPixmap(QPixmap(getcwd() +
                                             "\\res\\Zions_100.png"))
        self.ui.fTax.keyPressEvent = self.__onTaxKeyPress
        self.readData(self.ui.tableView)
        if self.isNewMode:
            self.ObjectDict['fEntryID'].refreshValueNotRaiseEvent(
                JPUser().currentUserID())
        if self.EditMode != JPEditFormDataMode.New:
            self.__refreshBeginNum()
        fla = "JPRound(JPRound({2}) * JPRound({4},2) * "
        fla = fla + "JPRound({5},2) * JPRound({6},2),2)"
        self.setFormula(7, fla)

    def __onTaxKeyPress(self, KeyEvent):
        if (KeyEvent.modifiers() == Qt.AltModifier
                and KeyEvent.key() == Qt.Key_Delete):
            self.ObjectDict['fTax'].refreshValueRaiseEvent(None, True)
            self.cacuTax = False
        elif (KeyEvent.modifiers() == Qt.AltModifier
              and KeyEvent.key() == Qt.Key_T):
            self.cacuTax = True

    def onGetHiddenColumns(self):
        return [0, 1]

    def onGetReadOnlyColumns(self):
        return [7]

    def onGetColumnWidths(self):
        return [0, 0, 60, 300, 100, 100, 100, 100]

    def onGetFieldsRowSources(self):
        pub = JPPub()
        u_lst = [[item[1], item[0]] for item in JPUser().getAllUserList()]
        return [('fCustomerID', pub.getCustomerList(), 1),
                ('fVendedorID', pub.getEnumList(10), 1),
                ('fEntryID', u_lst, 1)]

    def onGetReadOnlyFields(self):
        return ['fOrderID', "fEntryID", 'fAmount', 'fPayable', 'fTax']

    def getPrintReport(self):
        return Order_report

    def onDateChangeEvent(self, obj, value):
        if (self.EditMode != JPEditFormDataMode.ReadOnly
                and isinstance(obj, QModelIndex)):
            if obj.column() == 7:
                fAmount = self.getColumnSum(7)
                temp_fDesconto = self.ui.fDesconto.Value()
                fDesconto = temp_fDesconto if temp_fDesconto else 0
                self.ui.fAmount.refreshValueNotRaiseEvent(fAmount, True)
                if fAmount is None:
                    self.ui.fTax.refreshValueNotRaiseEvent(None, True)
                    self.ui.fPayable.refreshValueNotRaiseEvent(None, True)
                    return

        if not isinstance(obj, QModelIndex):
            if obj.objectName() == "fTax":
                temp_fTax = self.ui.fTax.Value()
                fTax = temp_fTax if temp_fTax else 0
            else:
                fTax = JPRound((fAmount - fDesconto) * 0.17) if fAmount else 0
        if self.cacuTax:
            self.self.ui.fTax.refreshValueNotRaiseEvent(fTax, True)
        else:
            fTax = 0
        fPayable = fAmount + fTax - fDesconto
        self.ui.fPayable.refreshValueNotRaiseEvent(fPayable, True)

    def afterSaveDate(self, data):
        self.ui.fOrderID.setText(data)

    def AfterSetDataBeforeInsterRowEvent(self, row_data, Index):
        if row_data is None:
            return False
        if row_data[7] is None:
            return False
        data = row_data
        if data[7] == 0:
            return False
        lt = [data[2], data[4], data[5], data[6], data[7]]
        lt = [float(str(i)) if i else 0 for i in lt]
        return int(lt[4] * 100) == int(
            reduce(lambda x, y: x * y, lt[0:4]) * 100)


class Order_report(Order_report_Mob):
    def __init__(self):
        super().__init__()

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        if (SectionType == JPPrintSectionType.PageHeader and CurrentPage == 1):
            return True

    def PrintCurrentReport(self, OrderID: str):
        self.init_data(OrderID)
        self.init_ReportHeader_title(
            title1=" NOTA DE ORDEM",
            title2="(ESTE DOCUMENTO É DO USO INTERNO)")
        self.init_ReportHeader()
        self.init_ReportHeader_Individualization()
        self.init_PageHeader()
        self.init_Detail()
        self.init_ReportFooter()
        super().BeginPrint()
