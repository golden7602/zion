from functools import reduce
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from lib.JPDatabase.Database import JPDb
from lib.JPMvc.JPEditDialog import PopEditForm
from lib.JPMvc.JPFuncForm import JPFunctionForm
from lib.JPMvc.JPModel import JPEditFormDataMode, JPFormModelMainSub
from lib.JPPrintReport import JPPrintSectionType
from lib.ZionPublc import JPPub
from lib.ZionReport.OrderReportMob import Order_report_Mob
from Ui.Ui_FormOrderMob import Ui_Form


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
                        fSubmited AS fSubmited
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
                    , fPayable, fDesconto, fNote
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

    def getEditFormClass(self):
        return EditForm_Order

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


# 继承模型，为了设置重载方法，必要要时也可以用动态绑定到函数
class myMainSubMode(JPFormModelMainSub):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def subModel_AfterSetDataBeforeInsterRowEvent(self, row_data, Index):
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


class EditForm_Order(PopEditForm):
    def __init__(self,
                 mainSql,
                 subSql=None,
                 edit_mode=JPFormModelMainSub.ReadOnly,
                 pkValue=None):

        super().__init__(clsUi=Ui_Form,
                         edit_mode=edit_mode,
                         pkValue=pkValue,
                         mainSql=mainSql,
                         subSql=subSql)
        self.setPkRole(1)
        self.ui.label_logo.setPixmap(QPixmap(getcwd() +
                                             "\\res\\Zions_100.png"))

    def setSubFormFormula(self):
        fla = "JPRound(JPRound({2}) * JPRound({4},2) * "
        fla = fla + "JPRound({5},2) * JPRound({6},2),2)"
        return 7, fla

    def setSubFormColumnsHidden(self):
        return 0, 1

    def setSubFormColumnsReadOnly(self):
        return 7

    def setSubFormColumnWidths(self):
        return 0, 0, 60, 300, 100, 100, 100, 100

    def setMainFormFieldsRowSources(self):
        pub = JPPub()
        return [('fCustomerID', pub.getCustomerList()),
                ('fVendedorID', pub.getEnumList(10))]

    def getMainSubMode(self):
        return myMainSubMode

    def getPrintReport(self):
        return Order_report

    def afterDataChangedCalculat(self):
        if self.EditMode != JPEditFormDataMode.ReadOnly:
            v_sum = self.SubModle._model.getColumnSum(7)
            fDesconto = self.MainModle.getObjectValue("fDesconto")
            fTax = (v_sum - fDesconto) * 0.17
            fPayable = v_sum - fDesconto + fTax
            self.MainModle.setObjectValue('fAmount', v_sum)
            self.MainModle.setObjectValue("fTax", fTax)
            self.MainModle.setObjectValue("fPayable", fPayable)

    def afterSaveDate(self, data):
        self.ui.fOrderID.setText(data)


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
