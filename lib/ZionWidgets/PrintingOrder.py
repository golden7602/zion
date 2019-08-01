from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from functools import reduce
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox,QAction,QLineEdit
from lib.JPPrintReport import JPPrintSectionType
from lib.ZionPublc import JPPub
from lib.JPMvc.JPFuncForm import JPFunctionForm
from Ui.Ui_FormPrintingOrder import Ui_Form
from lib.JPMvc.JPModel import JPFormModelMainSub, JPEditFormDataMode
from lib.JPDatabase.Database import JPDb
from lib.ZionReport.OrderReportMob import Order_report_Mob
from lib.JPMvc.JPEditDialog import PopEditForm
from PyQt5.QtGui import QIntValidator,QIcon,QPixmap


class JPFuncForm_Order(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_0 = """
                SELECT   fOrderID as `订单号码OrderID`, 
                    fCustomerName as `客户名Cliente`, 
                    fOrderDate as `日期OrderDate`, 
                    fRequiredDeliveryDate as `fRequiredDeliveryDate`, 
                    fSubmited1 as `提交Submited`, 
                    fSubmit_Name as `fSubmit_Name`, 
                    fEspecie as `类别Especie`, 
                    fAmount as `金额SubTotal`, 
                    fTax as `税金IVA`, 
                    fPayable as `应付金额Valor a Pagar`, 
                    fDesconto as `折扣Desconto`, 
                    fNumerBegin as `起始号码fNumerBegin`, 
                    fNumerEnd as `结束号码fNumerEnd`, 
                    fQuant as `数量fQuant`, 
                    fPagePerVolumn as `每本页数 Page/Vol`, 
                    fAvista as `每页序号Avista`, 
                    fTamanho as `尺寸Tamanho`, 
                    fVendedor as `联系人fVendedor`, 
                    fNrCopy as `联数Nr.Copy`, 
                    fContato as `联系人Contato`, 
                    fCelular as `手机Celular`, 
                    fTelefone as `fTelefone`, 
                    fEntry_Name as `录入Entry`, 
                    fCustomerID as `客户编号CustomerID`,  
                    cast(fSubmited as SIGNED) AS `fSubmited`
                FROM v_order AS o"""
        sql_1 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='TP'
                        AND (fSubmited={ch1}
                        OR fSubmited={ch2})
                        AND fOrderDate{date}
                ORDER BY  forderID DESC"""
        sql_2 = sql_0 + """
                WHERE fCanceled=0
                        AND left(fOrderID,2)='TP'
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
                SELECT fOrderID, fEndereco, fCelular, fRequiredDeliveryDate, fContato
                    , fTelefone, fVendedorID, fCustomerID, fOrderDate, fNUIT
                    , fCity, fSucursal, fQuant, fNumerBegin, fNumerEnd
                    , fPrice, fLogo, fEspecie, fAvista, fTamanho
                    , fNrCopy, fPagePerVolumn, fNote, fAmount, fDesconto
                    , fTax, fPayable
                FROM t_order
                WHERE fOrderID = '{}'
                """
        super().setEditFormSQL(m_sql)

    def getEditFormClass(self):
        return EditForm_PrintingOrder

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


class myMainSubMode(JPFormModelMainSub):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EditForm_PrintingOrder(PopEditForm):
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
        # 添加一个动作
        self.SearchAction=QAction()
        self.SearchAction.setIcon(QIcon(getcwd() + "\\res\\ico\\search.png"))
        self.ui.fNumerBegin.addAction(SearchAction,QLineEdit.LeadingPosition)
        self.SearchAction.setEnabled(False)


    def setMainFormFieldsRowSources(self):
        pub = JPPub()
        return [('fCustomerID', pub.getCustomerList()),
                ('fVendedorID', pub.getEnumList(10))]

    def getMainSubMode(self):
        return myMainSubMode

    def getPrintReport(self):
        return Order_Printingreport

    def afterDataChangedCalculat(self):
        # 计算起始号码，设定有效范围
        mod=self.MainModle
        if self.EditMode != JPEditFormDataMode.ReadOnly:
            fAvista = mod.getObjectValue("fAvista")
            fQuant = mod.getObjectValue("fQuant")
            fPagePerVolumn = mod.getObjectValue("fPagePerVolumn")
            v = fAvista * fQuant * fPagePerVolumn
            mod.setObjectValue('fNumerBegin', v)
            mod.ObjectDict['fNumerBegin'].setValidator(QIntValidator(v, v + 100000000))
            b=mod.getObjectValue("fNumerBegin")
            mod.ObjectDict['fNumerEnd'].setValidator(QIntValidator(b, b + 100000000))

    def afterSaveDate(self, data):
        self.ui.fOrderID.setText(data)


class Order_Printingreport(Order_report_Mob):
    def __init__(self):
        super().__init__()

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        if (SectionType == JPPrintSectionType.PageHeader and CurrentPage == 1):
            return True

    def PrintCurrentReport(self, OrderID: str):
        self.init_data(OrderID)
        self.init_ReportHeader_title(
            title1=" CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCc",
            title2="(ESTE DOCUMENTO É DO USO INTERNO)")
        self.init_ReportHeader()
        self.init_ReportHeader_Individualization()
        self.init_PageHeader()
        self.init_Detail()
        self.init_ReportFooter()
        super().BeginPrint()
