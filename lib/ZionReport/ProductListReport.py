from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import Qt,QDate
from PyQt5.QtGui import QFont
from PyQt5.QtPrintSupport import QPrinter

from lib.JPDatabase.Database import JPDb
from lib.JPPrint.JPPrintReport import JPPrintSectionType, JPReport
from lib.JPPublc import JPPub
from lib.ZionReport.PrintingOrderReportMob import PrintOrder_report_Mob
from lib.JPFunction import JPGetDisplayText, JPDateConver


class FormReport_ProductInfo(JPReport):
    def __init__(self,
                 PaperSize=QPrinter.A4,
                 Orientation=QPrinter.Orientation(1)):
        super().__init__(PaperSize, Orientation)
        self.configData = JPPub().getConfigData()
        self.font_YaHei = QFont("Microsoft YaHei")
        self.font_YaHei_8 = QFont(self.font_YaHei)
        self.font_YaHei_8.setPointSize(8)
        self.font_YaHei_10 = QFont(self.font_YaHei)
        self.font_YaHei_10.setPointSize(20)
        self.font_YaHei_10.setBold(True)
        self.BackColor = JPPub().getConfigData(
        )['PrintHighlightBackgroundColor']

        self.title_detail = [
            '序号\nID', '产品名称\nProductName', '规格\nSpesc', '宽\nWidth',
            '长\nLength', '计量单位\nUint', '剩余库存\nCurrentQuantity',
            '预警库存\nMinimumStock', '备注\nNote'
        ]

        self.fns = [
            'fID', 'fProductName', 'fSpesc', 'fWidth', 'fLength', 'fUint',
            'fNote', 'fCurrentQuantity', 'fMinimumStock'
        ]
        self.sql = """
        select fID,fProductName,fSpesc,fWidth,fLength,fUint,fNote,
        fCurrentQuantity,fMinimumStock 
        from t_product_information 
        where fCancel=0       
        order by fID
        """
        self.logo = JPPub().MainForm.logoPixmap
        self.title = 'Product Information List 产品信息明细表'

    def initItem(self):
        rpt = self
        rpt.PageHeader.AddItem(2, 0, 0, 274, 50, self.logo)
        rpt.PageHeader.AddItem(1,
                               274,
                               0,
                               746,
                               60,
                               self.title,
                               Bolder=False,
                               AlignmentFlag=(Qt.AlignCenter),
                               Font=self.font_YaHei_10)

        rpt.PageHeader.AddItem(1,
                               0,
                               50,
                               1020,
                               20,
                               'Date:{}'.format(
                                   JPDateConver(QDate.currentDate(), str)),
                               Bolder=False,
                               AlignmentFlag=(Qt.AlignRight),
                               Font=self.font_YaHei_8)

        cols = len(self.title_detail)
        al_c = Qt.AlignCenter
        al_r = (Qt.AlignVCenter | Qt.AlignRight)
        al_l = (Qt.AlignVCenter | Qt.AlignLeft)
        rpt.SetMargins(30, 30, 30, 30)
        title_height = 20
        rpt.ReportHeader.AddPrintLables(
            0,
            72,
            40,
            Texts=self.title_detail,
            Widths=[40, 470, 60, 60, 60, 60, 90, 90, 90],
            Aligns=[al_c] * cols)
        rpt.Detail.addPrintRowCountItem(0,
                                        0,
                                        40,
                                        20,
                                        AlignmentFlag=al_c,
                                        Font=self.font_YaHei_8)
        rpt.Detail.AddItem(
            3,
            40,
            0,
            470,
            20,
            self.fns[1],
            FormatString='{}',
            AlignmentFlag=al_l,
            # 超出长度省略
            AutoShrinkFont=self.configData['AutoShrinkFonts'],
            AutoEllipsis=self.configData['AutoEllipsis'],
            Font=self.font_YaHei_8)
        rpt.Detail.AddPrintFields(510,
                                  0,
                                  20,
                                  self.fns[2:], [60, 60, 60, 60, 90, 90, 90],
                                  [al_c] * 7,
                                  FormatString=' {}',
                                  Font=self.font_YaHei_8)

        # 页脚
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
                                100,
                                0,
                                920,
                                20,
                                '',
                                FormatString="PrintTime: %Y-%m-%d %H:%M:%S",
                                Bolder=False,
                                AlignmentFlag=Qt.AlignRight,
                                Font=self.font_YaHei_8)
        self.DataSource = JPDb().getDict(self.sql)

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        return False


class FormReport_ProductInfo_low(FormReport_ProductInfo):
    def __init__(self,
                 PaperSize=QPrinter.A4,
                 Orientation=QPrinter.Orientation(1)):
        super().__init__(PaperSize=QPrinter.A4,
                         Orientation=QPrinter.Orientation(1))
        self.title = 'Inventory Warning List 低库存产品信息表'
        self.sql = """
        select fID,fProductName,fSpesc,fWidth,fLength,fUint,fNote,
        fCurrentQuantity,fMinimumStock 
        from t_product_information 
        where fCancel=0  and   fCurrentQuantity< fMinimumStock 
        order by fID
        """


class FormReport_ProductInfo_Detail(JPReport):
    def __init__(self,
                 PaperSize=QPrinter.A4,
                 Orientation=QPrinter.Orientation(0)):
        super().__init__(PaperSize, Orientation)
        self.configData = JPPub().getConfigData()
        self.font_YaHei = QFont("Microsoft YaHei")
        self.font_YaHei_8 = QFont(self.font_YaHei)
        self.font_YaHei_8.setPointSize(8)
        self.font_YaHei_12 = QFont(self.font_YaHei)
        self.font_YaHei_12.setPointSize(12)
        self.font_YaHei_10 = QFont(self.font_YaHei)
        self.font_YaHei_10.setPointSize(20)
        self.font_YaHei_10.setBold(True)
        self.BackColor = JPPub().getConfigData(
        )['PrintHighlightBackgroundColor']
        self.title_detail = [
            '序号ID', '日期OrderDate', '单据号码OrderID', '入库In', '出库Out'
        ]
        self.fns = ['fOrderDate', 'fOrderDate', 'fOrderID', 'ksmc', 'rk', 'ck']
        self.logo = JPPub().MainForm.logoPixmap
        self.title = 'Warehouse in/out Details\n出入库明细表'
        self.beginDate = None
        self.endDate = None

    def initItem(self):
        rpt = self
        rpt.PageHeader.AddItem(2, 0, 0, 274, 50, self.logo)
        rpt.PageHeader.AddItem(1,
                               274,
                               0,
                               376,
                               60,
                               self.title,
                               Bolder=False,
                               AlignmentFlag=(Qt.AlignCenter),
                               Font=self.font_YaHei_12)

        rpt.PageHeader.AddItem(1,
                               0,
                               50,
                               650,
                               20,
                               'Date:{}'.format(
                                   JPDateConver(self.beginDate, str) + "--" +
                                   JPDateConver(self.endDate, str)),
                               Bolder=False,
                               AlignmentFlag=(Qt.AlignRight),
                               Font=self.font_YaHei_8)

        cols = len(self.title_detail)
        al_c = Qt.AlignCenter
        al_r = (Qt.AlignVCenter | Qt.AlignRight)
        al_l = (Qt.AlignVCenter | Qt.AlignLeft)
        rpt.SetMargins(30, 30, 30, 30)
        title_height = 20
        rpt.ReportHeader.AddPrintLables(0,
                                        72,
                                        20,
                                        Texts=self.title_detail,
                                        Widths=[60, 100, 250, 120, 120],
                                        Aligns=[al_c] * cols)
        rpt.Detail.addPrintRowCountItem(0,
                                        0,
                                        60,
                                        20,
                                        AlignmentFlag=al_c,
                                        Font=self.font_YaHei_8)
        rpt.Detail.AddPrintFields(60,
                                  0,
                                  20,
                                  self.fns[1:3], [100, 250], [al_c] * 2,
                                  FormatString=' {}',
                                  Font=self.font_YaHei_8)

        rpt.Detail.AddPrintFields(410,
                                  0,
                                  20,
                                  self.fns[4:], [120, 120], [al_r] * 2,
                                  FormatString='{} ',
                                  Font=self.font_YaHei_8)

        # 页脚
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
                                0,
                                0,
                                650,
                                20,
                                '',
                                FormatString="PrintTime: %Y-%m-%d %H:%M:%S",
                                Bolder=False,
                                AlignmentFlag=Qt.AlignRight,
                                Font=self.font_YaHei_8)
        self.DataSource = JPDb().getDict(self.sql)

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        return False
