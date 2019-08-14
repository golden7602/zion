from os import getcwd
from sys import path as jppath
jppath.append(getcwd())


from PyQt5.QtPrintSupport import QPrinter
from lib.JPPrintReport import JPPrintSectionType, JPReport
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap
from PyQt5.QtCore import Qt
from lib.JPDatabase.Database import JPDb


class PrintOrder_report_Mob(JPReport):
    def __init__(self,
                 PaperSize=QPrinter.A5,
                 Orientation=QPrinter.Orientation(1)):
        super().__init__(PaperSize, Orientation)
        self.SetMargins(30, 60, 30, 30)
        self.Copys = 2
        self.logo = QPixmap(getcwd() + "\\res\\Zions_100.png")
        self.FillColor = QColor(128, 128, 128)

        self.font_Algerian = QFont("Algerian")
        self.font_Algerian_11 = QFont(self.font_Algerian)
        self.font_Algerian_12 = QFont(self.font_Algerian)
        self.font_Algerian_11.setPointSize(11)
        self.font_Algerian_12.setPointSize(12)

        self.font_YaHei = QFont("微软雅黑")
        self.font_YaHei_8 = QFont(self.font_YaHei)
        self.font_YaHei_8.setPointSize(8)

        self.font_YaHei_10 = QFont(self.font_YaHei)
        self.font_YaHei_10.setPointSize(10)
        self.font_YaHei_10.setBold(True)

    def init_ReportHeader_title(self,
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

    def init_ReportHeader(self):
        # 第1行
        RH = self.ReportHeader
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

    def init_ReportHeader_Individualization(self):
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

    def init_PageHeader(self,
                        title1="NOTA DE PAGAMENTO",
                        title2="(ESTE DOCUMENTO É DO USO INTERNO)"):
        PH = self.PageHeader
        PH.AddItem(2, 0, 0, 274, 50, self.logo)
        font_title = QFont("Algerian", 12)
        font_title.setBold(True)
        PH.AddItem(1,
                   274,
                   0,
                   400,
                   25,
                   title1,
                   Font=self.font_Algerian_12,
                   AlignmentFlag=(Qt.AlignCenter),
                   Bolder=False)
        PH.AddItem(1,
                   274,
                   25,
                   400,
                   25,
                   title2,
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
        self.font_YaHei_10.setBold(True)
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

    def init_Detail(self):
        D = self.Detail
        D.AddPrintFields(
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
        D.AddItem(3,
                  40 + 50 + 280 + 60 + 60 + 80,
                  0,
                  80,
                  20,
                  "fAmountDetail",
                  Font=self.font_YaHei_8,
                  FormatString='{:,.2f}',
                  AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter))

    def init_ReportFooter(self):
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
        RF.AddItem(
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

    def init_data(self, OrderID: str):
        SQL = "select o.*, d.fQuant,d.fProductName,d.fLength,d.fWidth,\
            d.fPrice,d.fAmount as fAmountDetail from  v_order as o right join t_order_detail \
                    as d on o.fOrderID=d.fOrderID  where d.fOrderID='{}'"

        db = JPDb()
        data = db.getDict(SQL.format(OrderID))
        data.sort(key=lambda x: (x['fCustomerName'], x['fCity'], x['fAmount']
                                 is None, x['fAmount']))
        self.DataSource = data
