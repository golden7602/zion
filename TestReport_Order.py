# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter, QPixmap, QColor
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QApplication

from lib.globalVar import pub
from lib.JPPrintReport import JPPrintSectionType, JPReport


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
            self.FillColor=self.FillColor,
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
            self.FillColor=self.FillColor)

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


class QuotationOrder(order):
    def __init__(self):
        super().__init__()

    def PrintCurrentReport(self, OrderID: str = "CP2019-0201000021"):
        SQL = "select o.*, d.fQuant,d.fProductName,d.fLength,d.fWidth,\
            d.fPrice,d.fAmount as fAmountDetail from  v_order as o right join t_order_detail \
                    as d on o.fOrderID=d.fOrderID  where d.fOrderID='{}'"

        data = pub.getDict(SQL.format(OrderID))
        data.sort(key=lambda x: (x['fCustomerName'], x['fCity'], x['fAmount']
                                 is None, x['fAmount']))
        self.DataSource = data
        self._init_ReportHeader("COTACAO", "")
        self._init_ReportHeader_Individualization()
        self._init_DetailAndPageHeader()
        self._init_ReportFooter()
        super().BeginPrint()


class PrintingOrder(Order):
    def __init__(self):
        super().__init__()

    def _init_PrintingOrder_Individualization(self):
        RH.AddItem(1,
                   0,
                   155,
                   90,
                   20,
                   "类别Especie:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   155,
                   90,
                   20,
                   "fCategory",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   180,
                   155,
                   130,
                   20,
                   "材料Materia:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   310,
                   155,
                   90,
                   20,
                   "fBrandMateria",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   400,
                   155,
                   90,
                   20,
                   "电话Tel:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   155,
                   160,
                   20,
                   "fTelefone",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)

    def __myinit(self):
        logo = QPixmap("D:\\JinptConfig\\桌面2018\\newPYprj\\res\\Zions_100.png")
        self.FillColor = QColor(128, 128, 128)
        (Qt.AlignRight | Qt.AlignVCenter) = (Qt.AlignRight | Qt.AlignVCenter)
        font = QFont("微软雅黑", 15)
        self.font_YaHei_8 = QFont("微软雅黑", 8)
        font.setBold(True)
        RH = self.ReportHeader
        # sec.AddItem(1,5010,15,5295,435,'NOTA DE PAGAMENTO',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,5099,453,5130,450,'(ESTE DOCUMENTO é DO USO INTERNO)',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6285,0,1485,295,'订单号码No',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6285,590,1485,295,'城市City:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,590,1440,295,'税号NUIT:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,295,1440,295,'客户Cliente:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,0,1440,295,'订单日期Date:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,295,4845,295,'fCustomerName',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7771,0,2460,295,'fOrderID',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,0,1395,295,'fOrderDate',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7771,590,2460,295,'fCity',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,590,4845,295,'fNUIT',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,10230,435,225,2259,'CONT.  / PRDUCAO
        # ',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,2835,0,2085,295,'交货日期Delivery date:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4920,0,1365,295,'fRequiredDeliveryDate',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6285,295,1485,295,'销售Vendedor:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7771,295,2460,295,'fVendedor',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,885,7050,340,'fEndereco',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,1565,1920,340,'fBrandMateria',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,2245,1920,340,'fNumerBegin',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7350,2245,2880,340,'fNumerEnd',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7701,1565,780,340,'fQuant',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,1225,1590,340,'fContato',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,1225,1920,340,'fCelular',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7701,1225,2528,340,'fTelefone',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,2245,720,340,'ATE',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,9516,1565,714,340,'fPrice',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,1565,1590,340,'fEspecie',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,1905,1590,340,'fAvista',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,2245,1590,340,'fTamanho',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,1905,1920,340,'fNrCopy',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7701,1905,780,340,'fPagePerVolumn',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,1225,1440,340,'联系人Contato:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,1565,1440,340,'类别Especie:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,1905,1440,340,'每页序号Avista:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,2245,1440,340,'尺寸Tamanho:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,1565,1680,340,'材料Materia:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,1225,1680,340,'手机Celular:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,2245,1680,340,'序号Numeracao:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,1905,1680,340,'联数Nr.Copy:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,1565,1071,340,'数量Quant:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,1225,1071,340,'电话Tel:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8481,1565,1035,340,'单价Price:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,1905,1071,340,'Page/Vol:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,885,1440,340,'地址Endereco:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8490,885,1740,340,'Sucursal:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8481,1905,1748,340,'Logo:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8208,3744,570,145,'fNote',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7488,3744,575,145,'Note:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,9072,3744,285,135,'Note:
        # Esta ordem sera entregue em 10 dias de trabalho, se esta for urgente,e necessario pagar mais 20%. Para que nao afecte os trrabalhos diarios da vossa empresa,por favor, encomendem a vossa ordem  o mais rapido possivel.',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6768,3744,576,145,'LianCi',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,2880,2295,295,'折扣Desconto:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,2880,1310,295,'fDesconto',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,3470,2295,295,'应付金额Valor a Pagar:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,3175,2295,295,'税金IVA:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,2585,2295,295,'金额合计SubTotal:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,3470,1310,295,'fPayable',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,3175,1310,295,'fTax',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,2585,1310,295,'fAmount',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,2592,6630,1585,'fNote1',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3750,315,6456,345,'TextPrintTime',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,0,1695,295,'制作人 Productor:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3630,0,1590,295,'审核人 Aprovar:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7200,0,1125,295,'会计Caixa:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,345,1695,280,'销售Vendedor:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)

    def BeginPrint(self, OrderID: str = "CP2019-0201000021"):
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
        self.__myinit()
        super().BeginPrint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rep = Order()
    try:
        rep.BeginPrint()
    except Exception as e:
        print(e)
    sys.exit(app.exec_())
