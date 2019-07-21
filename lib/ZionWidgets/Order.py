from os import getcwd
from sys import path as jppath
jppath.append(getcwd())


from functools import reduce

from PyQt5.QtCore import Qt,QModelIndex,pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox,QWidget
from PyQt5.QtPrintSupport import QPrinter

from lib.JPPrintReport import JPPrintSectionType, JPReport
from lib.ZionPublc import JPPub
from lib.ZionWidgets.FuncFormBase import JPFunctionForm


class JPFuncForm_Order(JPFunctionForm):
    def __init__(self, MainForm):
        super().__init__(MainForm)
        sql_1 = """
                SELECT fOrderID as 订单号码OrderID,
                        fOrderDate as 日期OrderDate,
                        fCustomerName as 客户名Cliente,
                        fCity as 城市City,
                        fSubmited1 as 提交Submited,
                        fSubmit_Name as 提交人Submitter,
                        fAmount as 金额SubTotal,
                        fRequiredDeliveryDate as 交货日期RDD,
                        fDesconto as 折扣Desconto,
                        fTax as 税金IVA,
                        fPayable as `应付金额Valor a Pagar`,
                        fContato as 联系人Contato,
                        fCelular as 手机Celular,
                        cast(fSubmited as SIGNED) AS fSubmited
                FROM v_order AS o
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                        AND (fSubmited={}
                        OR fSubmited={})
                        AND fOrderDate{}
                ORDER BY  forderID DESC"""
        sql_2 = """
                SELECT fOrderID as 订单号码OrderID,
                        fOrderDate as 日期OrderDate,
                        fCustomerName as 客户名Cliente,
                        fCity as 城市City,
                        fSubmited1 as 提交Submited,
                        fSubmit_Name as 提交人Submitter,
                        fAmount as 金额SubTotal,
                        fRequiredDeliveryDate as 交货日期RDD,
                        fDesconto as 折扣Desconto,
                        fTax as 税金IVA,
                        fPayable as `应付金额Valor a Pagar`,
                        fContato as 联系人Contato,
                        fCelular as 手机Celular,
                        cast(fSubmited as SIGNED) AS fSubmited
                FROM v_order AS o
                WHERE fCanceled=0
                        AND left(fOrderID,2)='CP'
                ORDER BY  forderID DESC"""
        self.backgroundWhenValueIsTrueFieldName = ['fSubmited']
        self.checkBox_1.setText('UnSubmited')
        self.checkBox_2.setText('Submited')
        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(False)
        super().setSQL(sql_1, sql_2)
        self.tableView.setColumnHidden(13, True)

    def but_click(self, name):
        for n, fun in JPFuncForm_Order.__dict__.items():
            if n.upper() == 'BTN{}CLICKED'.format(name.upper()):
                fun(self)

    def getCurrentCustomerID(self):
        index = self.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.model.TabelFieldInfo.getOnlyData([index.row(),0])

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
        print("CMDBROWSE被下",cu_id)



def showEditForm_Order(MainForm, edit_mode, PKValue=None):
    from Ui.Ui_FormOrderMob import Ui_Form
    pb = JPPub()
    Form = QDialog(MainForm)
    Form.setWindowModality(Qt.WindowModal)
    ui = Ui_Form()
    ui.setupUi(Form)
    curPK = PKValue
    m_sql = """
            SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate
                , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax
                , fPayable, fDesconto, fNote
            FROM t_order
            WHERE fOrderID = '{}'
            """.format(curPK)
    s_sql = """
            SELECT fID, fOrderID, fQuant AS '数量Qtd', 
                fProductName AS '名称Descrição', 
                fLength AS '长Larg.', fWidth AS '宽Comp.', 
                fPrice AS '单价P. Unitario', fAmount AS '金额Total'
            FROM t_order_detail
            WHERE fOrderID = '{}'    
            """.format(curPK)

    # 继承模型，为了设置重载方法，必要要时也可以用动态绑定到函数
    class myMainMode(JPFormModelMainSub):
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

    tv = ui.tableView
    MF = myMainMode(Form, tv)
    MF.setUi(ui)
    MF_S = MF.subModel
    MF_M = MF.mainModel
    MF_M.setFieldsRowSource([('fCustomerID', pb.getCustomerList()),
                             ('fVendedorID', pb.getEnumList(10))])
    MF_M.setTabelInfo(m_sql, 1)
    MF_S.setColumnsHidden(0, 1)
    MF_S.setColumnWidths(0, 0, 60, 300, 100, 100, 100, 100)
    MF_S.setColumnsReadOnly(7)
    MF_S.setTabelInfo(s_sql)
    MF_S.setFormula(
        7,
        "JPRound(JPRound({2}) * JPRound({4}) * JPRound({5}) * JPRound({6}))")

    def butSave():
        try:
            MF.subModel.GetSQLS()
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()

    def cusChange(r):
        obj = ui.fCustomerID
        row = obj.RowSource[r]
        ui.fNUIT.setText(row[2])
        ui.fCity.setText(row[3])

    def Cacu(*args):
        M = MF.mainModel
        v_sum = MF.subModel._model.getColumnSum(7)
        fDesconto = M.getObjectValue("fDesconto")
        fTax = (v_sum - fDesconto) * 0.17
        fPayable = v_sum - fDesconto + fTax
        M.setObjectValue('fAmount', v_sum)
        M.setObjectValue("fTax", fTax)
        M.setObjectValue("fPayable", fPayable)

    ui.fCustomerID.currentIndexChanged.connect(cusChange)
    ui.butSave.clicked.connect(butSave)
    MF.dataChanged[QModelIndex].connect(Cacu)
    MF.dataChanged[QWidget].connect(Cacu)

    MF.show(edit_mode)





def formatEvent(self):
    if (self.SectionType is JPPrintSectionType.PageHeader
            and self.Report.CurrentPage == 1):
        return True


class Order(JPReport):
    def __init__(self,
                 PaperSize=QPrinter.A5,
                 Orientation=QPrinter.Orientation(1)):
        super().__init__(PaperSize, Orientation)
        self.SetMargins(30, 60, 30, 30)
        self.Copys = 2
        self.PageHeader.OnFormat = formatEvent
        self.logo = QPixmap(
            "D:\\JinptConfig\\桌面2018\\newPYprj\\res\\Zions_100.png")
        self.FillColor = QColor(128, 128, 128)

        self.font_Algerian = QFont("Algerian")
        self.font_Algerian_11 = QFont(self.font_Algerian)
        self.font_Algerian_12 = QFont(self.font_Algerian)
        self.font_Algerian_11.setPointSize(11)
        self.font_Algerian_12.setPointSize(12)

        self.font_YaHei = QFont("微软雅黑")
        self.font_YaHei_8 = QFont(self.self.font_YaHei)
        self.font_YaHei_8.setPointSize(8)

        self.font_YaHei_10 = QFont(self.self.font_YaHei)
        self.font_YaHei_10.setPointSize(10)
        self.font_YaHei_10.setBold(True)

    def _init_ReportHeader(self,
                           title1="NOTA DE PAGAMENTO",
                           title2="(ESTE DOCUMENTO É DO USO INTERNO)"):
        RH = self.ReportHeader
        RH.AddItem(2, 0, 0, 274, 50, self.logo)
        RH.AddItem(1,
                   274,
                   0,
                   400,
                   25,
                   title1,
                   Font=self.font_Algerian_12,
                   AlignmentFlag=(Qt.AlignCenter),
                   Bolder=False)
        RH.AddItem(1,
                   274,
                   25,
                   400,
                   25,
                   title2,
                   Font=self.font_Algerian_11,
                   AlignmentFlag=(Qt.AlignTop | Qt.AlignHCenter
                                  | Qt.AlignHCenter),
                   Bolder=False)
        # 第1行
        RH.AddItem(1,
                   0,
                   55,
                   90,
                   20,
                   "订单日期Date",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   55,
                   90,
                   20,
                   "fOrderDate",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(1,
                   180,
                   55,
                   130,
                   20,
                   "交货日期Delivery date:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   310,
                   55,
                   90,
                   20,
                   "fRequiredDeliveryDate",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(1,
                   400,
                   55,
                   90,
                   20,
                   "订单号码Nº",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   55,
                   160,
                   20,
                   "fOrderID",
                   Font=self.font_YaHei_10,
                   AlignmentFlag=Qt.AlignCenter)
        # 第2行
        RH.AddItem(1,
                   0,
                   75,
                   90,
                   20,
                   "客户Cliente:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   75,
                   310,
                   20,
                   "fCustomerName",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   400,
                   75,
                   90,
                   20,
                   "销售Vendedor:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   75,
                   160,
                   20,
                   "fVendedor",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        # 第3行
        RH.AddItem(1,
                   0,
                   95,
                   90,
                   20,
                   "税号NUIT:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   95,
                   310,
                   20,
                   "fNUIT",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   400,
                   95,
                   90,
                   20,
                   "城市City:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   95,
                   160,
                   20,
                   "fCity",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        # 第4行
        RH.AddItem(1,
                   0,
                   115,
                   90,
                   20,
                   "地址Endereco:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   115,
                   400,
                   20,
                   "fEndereco",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(3,
                   490,
                   115,
                   160,
                   20,
                   "fSucursal",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft,
                   FormatString="Sucursal:{}")
        # 第5行
        RH.AddItem(1,
                   0,
                   135,
                   90,
                   20,
                   "联系人Contato:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   135,
                   90,
                   20,
                   "fContato",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   180,
                   135,
                   130,
                   20,
                   "手机Celular:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   310,
                   135,
                   90,
                   20,
                   "fCelular",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   400,
                   135,
                   90,
                   20,
                   "电话Tel:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   135,
                   160,
                   20,
                   "fTelefone",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        # 联次信息
        tempItem = RH.AddItem(1,
                              655,
                              60,
                              120,
                              20,
                              " CONT.  / PRDUCAO",
                              Bolder=False,
                              Transform=True,
                              Font=self.font_YaHei_8,
                              AlignmentFlag=Qt.AlignLeft)

        # 修改联次
        def OnBeforePrint_LianCi(*args):
            if args[0] == 2:
                return False, "第二联"
            else:
                return False, None

        tempItem.OnBeforePrint = OnBeforePrint_LianCi

    def _init_ReportHeader_Individualization(self):
        # 第6行 Order个性部分
        RH = self.ReportHeader
        RH.AddPrintLables(
            0,
            155,
            20, [
                "#", "数量Qtd", "名称Descrição", "长Larg.", "宽Comp.",
                "单价P. Unitario", "金额Total"
            ], [40, 50, 280, 60, 60, 80, 80], [
                Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter,
                Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter
            ],
            FillColor=self.FillColor,
            Font=self.font_YaHei_8)

    def _init_DetailAndPageHeader(self):
        PH = self.PageHeader
        PH.AddItem(2, 0, 0, 274, 50, self.logo)
        font_title = QFont("Algerian", 12)
        font_title.setBold(True)
        PH.AddItem(1,
                   274,
                   0,
                   400,
                   25,
                   "NOTA DE PAGAMENTO",
                   Font=self.font_Algerian_12,
                   AlignmentFlag=(Qt.AlignCenter),
                   Bolder=False)
        PH.AddItem(1,
                   274,
                   25,
                   400,
                   25,
                   "(ESTE DOCUMENTO É DO USO INTERNO)",
                   Font=self.font_Algerian_11,
                   AlignmentFlag=(Qt.AlignTop | Qt.AlignVCenter
                                  | Qt.AlignHCenter),
                   Bolder=False)
        # 第1行
        PH.AddItem(1,
                   0,
                   55,
                   90,
                   20,
                   "订单日期Date",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        PH.AddItem(3,
                   90,
                   55,
                   90,
                   20,
                   "fOrderDate",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        PH.AddItem(1,
                   180,
                   55,
                   130,
                   20,
                   "交货日期Delivery date:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        PH.AddItem(3,
                   310,
                   55,
                   90,
                   20,
                   "fRequiredDeliveryDate",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        self.fyh10.setBold(True)
        PH.AddItem(1,
                   400,
                   55,
                   90,
                   20,
                   "订单号码Nº",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        PH.AddItem(3,
                   490,
                   55,
                   160,
                   20,
                   "fOrderID",
                   Font=self.font_YaHei_10,
                   AlignmentFlag=Qt.AlignCenter)
        # 第2行
        PH.AddPrintLables(
            0,
            75,
            20, [
                "#", "数量Qtd", "名称Descrição", "长Larg.", "宽Comp.",
                "单价P. Unitario", "金额Total"
            ], [40, 50, 280, 60, 60, 80, 80], [
                Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter,
                Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter
            ],
            Font=self.font_YaHei_8,
            FillColor=self.FillColor)

        self.Detail.AddPrintFields(
            0,
            0,
            20, [
                "fQuant", "fQuant", "fProductName", "fLength", "fWidth",
                "fPrice"
            ], [40, 50, 280, 60, 60, 80], [
                Qt.AlignCenter, Qt.AlignCenter, Qt.AlignLeft, Qt.AlignCenter,
                (Qt.AlignRight | Qt.AlignVCenter),
                (Qt.AlignRight | Qt.AlignVCenter)
            ],
            Font=self.font_YaHei_8)
        self.Detail.AddItem(3,
                            40 + 50 + 280 + 60 + 60 + 80,
                            0,
                            80,
                            20,
                            "fAmountDetail",
                            Font=self.font_YaHei_8,
                            FormatString='{:,.2f}',
                            AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter))

    def _init_ReportFooter(self):
        RF = self.ReportFooter
        RF.AddItem(1,
                   430,
                   0,
                   140,
                   20,
                   "金额合计SubTotal:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignRight)
        RF.AddItem(3,
                   570,
                   0,
                   80,
                   20,
                   "fAmount",
                   FormatString='{:,.2f}',
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   20,
                   140,
                   20,
                   "折扣Desconto:",
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   570,
                   20,
                   80,
                   20,
                   "fDesconto",
                   AlignmentFlag=Qt.AlignRight,
                   FormatString='{:,.2f}',
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   40,
                   140,
                   20,
                   "税金IVA:",
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   570,
                   40,
                   80,
                   20,
                   "fTax",
                   FormatString='{:,.2f}',
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   60,
                   140,
                   20,
                   "应付金额Valor a Pagar:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignRight)
        RF.AddItem(3,
                   570,
                   60,
                   80,
                   20,
                   "fPayable",
                   FormatString='{:,.2f}',
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        pitem = RF.AddItem(
            3,
            0,
            0,
            390,
            100,
            "fNote",
            FormatString='Note:Esta cotação é válida por 7 dias.\n{}',
            Bolder=False,
            AlignmentFlag=(Qt.AlignLeft | Qt.TextWordWrap),
            Font=self.font_YaHei_8)
        # 签字部分
        RF.AddItem(1,
                   0,
                   110,
                   100,
                   20,
                   '制作人 Productor:',
                   Bolder=False,
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1, 100, 125, 100, 0, '')
        RF.AddItem(1,
                   220,
                   110,
                   100,
                   20,
                   '审核人 Aprovar:',
                   Bolder=False,
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1, 320, 125, 100, 0, '')
        RF.AddItem(1,
                   420,
                   110,
                   120,
                   20,
                   '会计Caixa:',
                   Bolder=False,
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)
        RF.AddItem(1, 540, 125, 100, 0, '')
        RF.AddItem(1,
                   0,
                   140,
                   100,
                   20,
                   '销售Vendedor:',
                   Bolder=False,
                   AlignmentFlag=Qt.AlignRight,
                   Font=self.font_YaHei_8)

        RF.AddItem(1, 100, 155, 100, 0, '')
        self.PageFooter.AddItem(4,
                                10,
                                0,
                                100,
                                20,
                                '',
                                FormatString='Page: {Page}/{Pages}',
                                Bolder=False,
                                AlignmentFlag=Qt.AlignLeft,
                                Font=self.font_YaHei_8)
        self.PageFooter.AddItem(5,
                                110,
                                0,
                                540,
                                20,
                                '',
                                FormatString="PrintTime: %Y-%m-%d %H:%M:%S",
                                Bolder=False,
                                AlignmentFlag=Qt.AlignRight,
                                Font=self.font_YaHei_8)

    def PrintCurrentReport(self, OrderID: str = "CP2019-0201000021"):
        SQL = "select o.*, d.fQuant,d.fProductName,d.fLength,d.fWidth,\
            d.fPrice,d.fAmount as fAmountDetail from  v_order as o right join t_order_detail \
                    as d on o.fOrderID=d.fOrderID  where d.fOrderID='{}'"

        # SQL = "select o.*, d.fQuant,d.fProductName,d.fLength,d.fWidth,\
        #     d.fPrice,d.fAmount as fAmountDetail from  v_order as o right join t_order_detail \
        #         as d on o.fOrderID=d.fOrderID  "
        data = pub.getDict(SQL.format(OrderID))
        data.sort(key=lambda x: (x['fCustomerName'], x['fCity'], x['fAmount']
                                 is None, x['fAmount']))
        self.DataSource = data
        self._init_ReportHeader()
        self._init_ReportHeader_Individualization()
        self._init_DetailAndPageHeader()
        self._init_ReportFooter()
        super().BeginPrint()