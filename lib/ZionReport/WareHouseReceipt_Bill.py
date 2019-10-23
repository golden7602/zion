from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from lib.JPPrint.JPPrintReport import JPPrintSectionType, JPReport
from lib.ZionReport.PrintingOrderReportMob import PrintOrder_report_Mob
from PyQt5.QtCore import Qt
from lib.JPPublc import JPPub
from lib.JPDatabase.Database import JPDb
from PyQt5.QtGui import QFont
from lib.JPPrint.JPPrintReport import JPReport
from PyQt5.QtPrintSupport import QPrinter
from lib.JPFunction import JPGetDisplayText, JPDateConver


class WarehouseReceipt_Bill(JPReport):
    def __init__(self,
                 PaperSize=QPrinter.A5,
                 Orientation=QPrinter.Orientation(1)):
        super().__init__(PaperSize, Orientation)

        self.SetMargins(30, 60, 30, 30)
        self.CopyInfo = JPPub().getCopysInfo('BillCopys_WarehouseRreceipt')
        self.Copys = len(self.CopyInfo)
        self.logo = JPPub().MainForm.logoPixmap
        self.FillColor = JPPub().getConfigData(
        )['PrintHighlightBackgroundColor']

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
                                title1="Outbound Order",
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
                   AlignmentFlag=(Qt.AlignTop | Qt.AlignHCenter),
                   Bolder=False)

    def init_ReportHeader(self):
        # 第1行
        RH = self.ReportHeader
        RH.AddItem(1,
                   0,
                   55,
                   90,
                   20,
                   "入库单日期Date",
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
                   150,
                   20,
                   "入库日期WarehousingDate:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   330,
                   55,
                   70,
                   20,
                   "fWarehousingDate",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(1,
                   400,
                   55,
                   90,
                   20,
                   "入库单号Nº",
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
                   "客户Supplier:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   75,
                   310,
                   20,
                   "fSupplierName",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter,
                   FormatString=" {}")
        RH.AddItem(1,
                   400,
                   75,
                   90,
                   20,
                   "采购Purchaser:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   75,
                   160,
                   20,
                   "fPurchaserID",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter,
                   FormatString=" {}")
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
                   AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter,
                   FormatString=" {}")
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
                   AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter,
                   FormatString=" {}")

        # 第4行
        # RH.AddItem(1,
        #            0,
        #            115,
        #            90,
        #            20,
        #            " ",
        #            Font=self.font_YaHei_8,
        #            AlignmentFlag=Qt.AlignCenter)
        # RH.AddItem(1,
        #            90,
        #            115,
        #            400,
        #            20,
        #            " ",
        #            Font=self.font_YaHei_8,
        #            AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter)
        # RH.AddItem(3,
        #            490,
        #            115,
        #            160,
        #            20,
        #            "fSucursal1",
        #            Font=self.font_YaHei_8,
        #            AlignmentFlag=Qt.AlignLeft,
        #            FormatString="Sucursal:{}")
        # 第5行
        RH.AddItem(1,
                   0,
                   115,
                   90,
                   20,
                   "联系人Contato:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   115,
                   90,
                   20,
                   "fContato",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter,
                   FormatString=" {}")
        RH.AddItem(1,
                   180,
                   115,
                   130,
                   20,
                   "手机Celular:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   310,
                   115,
                   90,
                   20,
                   "fCelular",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter,
                   FormatString=" {}")
        RH.AddItem(1,
                   400,
                   115,
                   90,
                   20,
                   "电话Tel:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   115,
                   160,
                   20,
                   "fTelefone",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft | Qt.AlignVCenter,
                   FormatString=" {}")
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

    def init_ReportHeader_Individualization(self):
        # 第6行 Order个性部分
        RH = self.ReportHeader
        RH.AddPrintLables(
            0,
            135,
            20, ["#", "名称Descrição", "数量Qtd", "单价P. Unitario", "金额Total"],
            [40, 370, 80, 80, 80], [
                Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter,
                Qt.AlignCenter
            ],
            FillColor=self.FillColor,
            Font=self.font_YaHei_8)

    def init_PageHeader(self,
                        title1="Outbound Order",
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
                   "入库单日期Date",
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
                   "入库日期WarehousingDate:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        PH.AddItem(3,
                   310,
                   55,
                   90,
                   20,
                   "fWarehousingDate",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        self.font_YaHei_10.setBold(True)
        PH.AddItem(1,
                   400,
                   55,
                   90,
                   20,
                   "出库单号码Nº",
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
            20, ["#", "名称Descrição", "数量Qtd", "单价P. Unitario", "金额Total"],
            [40, 370, 80, 80, 80], [
                Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter, Qt.AlignCenter,
                Qt.AlignCenter
            ],
            Font=self.font_YaHei_8,
            FillColor=self.FillColor)

    def init_Detail(self):
        D = self.Detail
        D.AddPrintFields(0,
                         0,
                         20, ["fQuant", "fProductName"], [40, 370],
                         [Qt.AlignCenter, Qt.AlignLeft],
                         Font=self.font_YaHei_8)
        D.AddPrintFields(410,
                         0,
                         20, ["fQuant", "fPrice"], [80, 80],
                         [(Qt.AlignRight | Qt.AlignVCenter),
                          (Qt.AlignRight | Qt.AlignVCenter)],
                         Font=self.font_YaHei_8,
                         FormatString='{:,.3f} ')
        D.AddPrintFields(570,
                         0,
                         20, ["fAmount"], [80],
                         [(Qt.AlignRight | Qt.AlignVCenter)],
                         Font=self.font_YaHei_8,
                         FormatString='{:,.2f} ')
        # D.AddItem(3,
        #           40 + 50 + 280 + 60 + 60 + 80,
        #           0,
        #           80,
        #           20,
        #           "fAmountDetail",
        #           Font=self.font_YaHei_8,
        #           FormatString='{:,.3f} ',
        #           AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter))

    def init_ReportFooter(self):
        RF = self.ReportFooter
        RF.AddItem(1,
                   430,
                   0,
                   140,
                   20,
                   "金额合计SubTotal:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter))
        RF.AddItem(3,
                   570,
                   0,
                   80,
                   20,
                   "fAmount",
                   FormatString='{:,.2f} ',
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   20,
                   140,
                   20,
                   "折扣Desconto:",
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   570,
                   20,
                   80,
                   20,
                   "fDesconto",
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   FormatString='{:,.2f} ',
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   40,
                   140,
                   20,
                   "税金IVA:",
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   570,
                   40,
                   80,
                   20,
                   "fTax",
                   FormatString='{:,.2f} ',
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)
        RF.AddItem(1,
                   430,
                   60,
                   140,
                   20,
                   "应付金额Valor a Pagar:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter))
        RF.AddItem(3,
                   570,
                   60,
                   80,
                   20,
                   "fPayable",
                   FormatString='{:,.2f} ',
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)
        RF.AddItem(3,
                   0,
                   0,
                   430,
                   80,
                   "fNote1",
                   FormatString='备注Note:\n{}',
                   Bolder=True,
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
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)
        RF.AddItem(1, 100, 125, 100, 0, '')
        RF.AddItem(1,
                   220,
                   110,
                   100,
                   20,
                   '审核人 Aprovar:',
                   Bolder=False,
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)
        RF.AddItem(1, 320, 125, 100, 0, '')
        RF.AddItem(1,
                   420,
                   110,
                   120,
                   20,
                   '会计Caixa:',
                   Bolder=False,
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)

        RF.AddItem(1, 540, 125, 100, 0, '')
        RF.AddItem(1,
                   390,
                   140,
                   150,
                   20,
                   '库管Warehouse Managem:',
                   Bolder=False,
                   AlignmentFlag=(Qt.AlignRight | Qt.AlignVCenter),
                   Font=self.font_YaHei_8)

        RF.AddItem(1, 540, 155, 100, 0, '')

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
                                AlignmentFlag=(Qt.AlignRight
                                               | Qt.AlignVCenter),
                                Font=self.font_YaHei_8)

    # 修改联次
    def onBeforePrint(self, Copys, Sec, CurrentPrintDataRow, obj):
        title = self.CopyInfo[Copys - 1]['title']
        flag = self.CopyInfo[Copys - 1]['flag']
        if obj.PrintObject == " CONT.  / PRDUCAO":
            return False, title
        elif obj.PrintObject == 'fProductName':
            return False, self.getFullProductName(
                CurrentPrintDataRow['fProductID'])
        else:
            if obj.PrintObject in [
                    "fPrice", "fAmountDetail", "fAmount", "fDesconto", "fTax",
                    "fPayable"
            ]:
                return False, ' ' if flag is False else None
            return False, None

    def init_data(self, OrderID: str):
        SQL = f"""
            SELECT o.*,
                    d.fQuant,
                    d.fProductID,
                    d.fPrice ,
                    d.fAmount ,
                    if(isnull(o.fNote),
                    ' ',o.fNote) AS fNote1
            FROM v_product_warehousereceipt_order o
            RIGHT JOIN t_product_warehousereceipt_order_detail d
                ON o.fOrderID = d.fOrderID
            WHERE d.fOrderID='{OrderID}'
            """

        db = JPDb()
        data = db.getDict(SQL)
        data.sort(key=lambda x: (x['fSupplierName'], x['fCity'], x['fAmount']
                                 is None, x['fAmount']))
        self.DataSource = data

    def BeginPrint(self):
        # 大于9行自动更改纸型
        if len(self.DataSource) > 9:
            self.PaperSize = QPrinter.A4
            self.Orientation = QPrinter.Orientation(0)
        return super().BeginPrint()

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        if (SectionType == JPPrintSectionType.PageHeader and CurrentPage == 1):
            return True

    def PrintCurrentReport(self, OrderID: str):
        self.init_data(OrderID)
        self.init_ReportHeader_title(
            title1="入库单 Warehouse Receipt",
            title2="(ESTE DOCUMENTO É DO USO INTERNO)")
        self.init_ReportHeader()
        self.init_ReportHeader_Individualization()
        self.init_PageHeader()
        self.init_Detail()
        self.init_ReportFooter()
        super().BeginPrint()