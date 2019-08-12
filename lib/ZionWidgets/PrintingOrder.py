from functools import reduce
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QIntValidator, QPixmap
from PyQt5.QtWidgets import QAction, QLineEdit, QMessageBox

from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPMvc.JPEditDialog import PopEditForm
from lib.JPMvc.JPFuncForm import JPFunctionForm
from lib.JPMvc.JPModel import JPEditFormDataMode, JPFormModelMainSub
from lib.JPPrintReport import JPPrintSectionType
from lib.ZionPublc import JPPub
from lib.ZionReport.OrderReportMob import Order_report_Mob
from Ui.Ui_FormPrintingOrder import Ui_Form


class JPFuncForm_PrintingOrder(JPFunctionForm):
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
        self.tableView.setColumnHidden(23, True)
        self.tableView.setColumnHidden(24, True)
        self.fSubmited_column = 13
        m_sql = """
                SELECT fOrderID, fCelular, fRequiredDeliveryDate, fContato
                    , fTelefone, fVendedorID, fCustomerID, fOrderDate
                    , fSucursal, fQuant, fNumerBegin, fNumerEnd
                    , fPrice, fLogo, fEspecieID, fAvistaID, fTamanhoID
                    , fNrCopyID, fPagePerVolumn, fNote, fAmount, fDesconto
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


# class myMainSubMode(JPFormModelMainSub):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


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
        self.setPkRole(5)
        self.ui.fAvistaID.BindingColumn = 2
        self.ui.fVendedorID.BindingColumn = 2
        self.ui.fEspecieID.BindingColumn = 2
        self.ui.fTamanhoID.BindingColumn = 2
        self.ui.fNrCopyID.BindingColumn = 2
        self.ui.fAvistaID.BindingColumn = 2
        self.NumTabelFieldInfo = None
        pix = QPixmap(getcwd() + "\\res\\Zions_100.png")
        self.ui.label_logo.setPixmap(pix)
        self.ui.fNumerEnd.setEnabled(False)
        # 添加一个动作,用于显示已经存在的同类单据号码
        self.SearchAction = QAction()
        self.SearchAction.setIcon(QIcon(getcwd() + "\\res\\ico\\search.png"))
        self.ui.fNumerBegin.addAction(self.SearchAction,
                                      QLineEdit.LeadingPosition)
        #新单据状态
        if edit_mode == JPFormModelMainSub.New:
            self.ui.fOrderID.setEnabled(False)
            self.MainModle._loadDdata = True
            self.__noneNum()
            self.MainModle._loadDdata = False

        self.ui.fCustomerID.currentIndexChanged[int].connect(self.cacuNum)
        self.ui.fEspecieID.currentIndexChanged[int].connect(self.cacuNum)
        self.ui.fAvistaID.currentIndexChanged[int].connect(self.cacuNum)

        self.SearchAction.setEnabled(False)
        f1 = "{fNumerEnd} = {fNumerBegin} + {fAvistaID} * {fQuant} * {fPagePerVolumn} - 1"
        f1 = f1 + " if all(({fNumerBegin},{fAvistaID}!=-1,{fQuant},{fPagePerVolumn} )) else None"
        f2 = '{fPayable} = {fAmount} - ({fAmount} - {fDesconto}) * 0.17 - {fDesconto}'
        self.MainModle.setFormulas(f1, f2)

    def setMainFormFieldsRowSources(self):
        pub = JPPub()
        return [('fCustomerID', pub.getCustomerList()),
                ('fVendedorID', pub.getEnumList(10)),
                ('fEspecieID', pub.getEnumList(2)),
                ('fAvistaID', pub.getEnumList(7)),
                ('fTamanhoID', pub.getEnumList(8)),
                ('fNrCopyID', pub.getEnumList(9))]

    def getMainMode(self):
        return super().getMainMode()

    def getPrintReport(self):
        return Order_Printingreport

    def __noneNum(self):
        self.ui.fNumerBegin.setEnabled(False)
        self.SearchAction.setEnabled(True)
        self.ui.fNumerBegin.setText('')
        self.ui.fNumerEnd.setText('')

    def afterDataChangedCalculat(self,obj):
        if obj.objectName() in ("fCustomerID","fEspecieID","fAvistaID"):
            # 没有选择类别，直接退出
            if self.ui.fEspecieID.currentIndex() == -1:
                self.__noneNum()
                return
            # 当选择了类别，且需要号码管理
            if self.ui.fEspecieID.currentData()[2] == '1':
                self.ui.fNumerBegin.setEnabled(True)
                sql = '''
                    SELECT fOrderID AS OrderID, 
                        fOrderDate as OrderDate,
                        CAST(e.fTitle AS char(20)) AS Especie, 
                        CAST(fNumerBegin AS SIGNED) AS NumerBegin, 
                        CAST(fNumerEnd AS SIGNED) AS NumerEnd
                    FROM t_order o
                        LEFT JOIN t_enumeration e ON o.fEspecieID = e.fItemID
                    WHERE fCustomerID ={fCustomerID}
                        AND fEspecieID = {fEspecieID}
                        {WhereID}
                    ORDER BY fNumerEnd DESC
                '''
                if self.ui.fCustomerID.currentIndex() == -1:
                    # 没有选择客户时，退出
                    self.ui.fNumerBegin.refreshValueNotRaiseEvent('')
                    self.ui.fNumerEnd.refreshValueNotRaiseEvent('')
                    return
                else:
                    WhereID = "AND fOrderID<>'{}'".format(
                        self.curPK) if self.curPK else ''
                    sql = sql.format(fCustomerID=self.ui.fCustomerID.Value(),
                                    fEspecieID=self.ui.fEspecieID.Value(),
                                    WhereID=WhereID)
                    tab = JPTabelFieldInfo(sql)
                    self.NumTabelFieldInfo = tab
                    # 选择了客户，当查询到有历史记录时
                    if len(tab.DataRows) > 0:
                        self.SearchAction.setEnabled(True)
                        tempV = tab.getOnlyData([0, 4])
                        self.MainModle.setObjectValue('fNumerBegin',
                                                    tempV + 1 if tempV else 1)
                    else:
                        self.SearchAction.setEnabled(False)
                        self.MainModle.setObjectValue('fNumerBegin', 1)
                    # mod = self.MainModle
                    # fNumerBegin = self.ui.fNumerBegin.Value()
                    # mod.ObjectDict['fNumerBegin'].setValidator(
                    #     QIntValidator(fNumerBegin, fNumerBegin + 100000000))
            else:
                self.__noneNum()
        if obj.objectName() in ("fQuant","fPrice"):

    # def afterDataChangedCalculat(self):
    #     self.cacuNum()
    #     return

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
            title1="NOTA DE PAGAMENTO",
            title2="(ESTE DOCUMENTO É DO USO INTERNO)")
        self.init_ReportHeader()
        self.init_ReportHeader_Individualization()
        self.init_PageHeader()
        self.init_Detail()
        self.init_ReportFooter()
        super().BeginPrint()
