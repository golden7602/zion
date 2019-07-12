import html
import math
import sys

from PyQt5.QtCore import QDate, QRectF, Qt
from PyQt5.QtGui import (QFont, QFontMetrics, QPainter, QPixmap,
                         QTextBlockFormat, QTextCharFormat, QTextCursor,
                         QTextDocument, QTextFormat, QTextOption,
                         QTextTableFormat)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog, QPrinterInfo, QPrintPreviewWidget
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QHBoxLayout,
                             QLabel, QMainWindow, QPushButton, QSizePolicy,
                             QTableWidget, QTableWidgetItem, QVBoxLayout)

################################################
#######打印文本---《心经》
################################################
the_text = '''
观自在菩萨，行深般若波罗蜜多时，照见五蕴皆空，度一切苦厄。
舍利子，色不异空，空不异色，色即是空，空即是色，受想行识亦复如是。
舍利子，是诸法空相，不生不灭，不垢不净，不增不减。
是故空中无色，无受想行识，无眼耳鼻舌身意，无色声香味触法，无眼界乃至无意识界，无无明亦无无明尽，乃至无老死，亦无老死尽，无苦集灭道，无智亦无得。
以无所得故，菩提萨埵，依般若波罗蜜多故，心无挂碍；无挂碍故，无有恐怖，远离颠倒梦想，究竟涅槃。
三世诸佛，依般若波罗蜜多故，得阿耨多罗三藐三菩提。
故知般若波罗蜜多，是大神咒，是大明咒，是无上咒，是无等等咒，能除一切苦，真实不虚。
故说般若波罗蜜多咒，即说咒曰：揭谛揭谛，波罗揭谛，波罗僧揭谛，菩提萨婆诃。
'''


class Statement(object):
    def __init__(self, company, contact, address):
        self.company = company
        self.contact = contact
        self.address = address
        self.transactions = []  # List of (QDate, float) two-tuples

    def balance(self):
        return sum([amount for date, amount in self.transactions])


DATE_FORMAT = "MMM d, yyyy"


################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(self.tr("打印功能"))

        # 创建文本框
        self.label = QLabel()
        self.label.setFont(QFont("Roman times", 12, QFont.Bold))
        self.label.setText(the_text)
        self.setCentralWidget(self.label)

        # 创建菜单栏
        self.createMenus()

    def createMenus(self):
        # 创建动作一
        self.printAction1 = QAction(self.tr("打印无预留"), self)
        self.printAction1.triggered.connect(self.on_printAction1_triggered)

        # 创建动作二
        self.printAction2 = QAction(self.tr("打印有预留"), self)
        self.printAction2.triggered.connect(self.on_printAction2_triggered)

        # 创建动作三
        self.printAction3 = QAction(self.tr("直接打印"), self)
        self.printAction3.triggered.connect(self.on_printAction3_triggered)

        # 创建动作四
        self.printAction4 = QAction(self.tr("打印到PDF"), self)
        self.printAction4.triggered.connect(self.on_printAction4_triggered)

        # 创建菜单，添加动作
        self.printMenu = self.menuBar().addMenu(self.tr("打印"))
        self.printMenu.addAction(self.printAction1)
        self.printMenu.addAction(self.printAction2)
        self.printMenu.addAction(self.printAction3)
        self.printMenu.addAction(self.printAction4)

    # 动作一：打印，无预览
    def on_printAction1_triggered(self):
        printer = QPrinter()
        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QDialog.Accepted:
            self.handlePaintRequest(printer)

    # 动作二：打印，有预览
    def on_printAction2_triggered(self):
        dialog = QPrintPreviewDialog()
        #dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.paintRequested.connect(self.printViaQPainter)
        dialog.setWindowTitle('fdgjksdfhgjklsdhfgjsdhfgsfdjgd')
        dialog.exec_()

    # 动作三：直接打印
    def on_printAction3_triggered(self):
        printer = QPrinter()
        self.handlePaintRequest(printer)

    # 动作四：打印到pdf
    def on_printAction4_triggered(self):
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("D:/pdf打印测试.pdf")
        self.handlePaintRequest(printer)

    ## 打印函数
    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertText(self.label.text())
        document.print(printer)

    def printItem(self, painter, x, y, w, h, font, text):
        painter.drawRect(x, y, w, h)
        painter.setFont(font)
        textTop = 0
        fm = QFontMetrics(font)
        topMargin = (y - fm.height()) / 2
        if topMargin > 0:
            textTop = y + fm.height()
        else:
            textTop = y + fm.height()
        painter.drawText(x, textTop, text)

    def printViaQPainter(self, printer):
        # dialog = QPrintDialog(self.printer, self)
        # if not dialog.exec_():
        #     return
        printer.setPageSize(QPrinter.B5)
        LeftMargin = 72
        sansFont = QFont("Helvetica", 10)
        sansLineHeight = QFontMetrics(sansFont).height()
        serifFont = QFont("Times", 11)
        fm = QFontMetrics(serifFont)
        s0 = '早在今年4月份，中国联通就在上海发布了相应的5G品牌\n标识“5G”以及相应主题口号。同时发布了“7+33+n”5G 试验网络部署，在北京、上海、广州、深圳、南京、杭州、雄安7座城市核心区域连续覆盖，并且在33座城市的热点区域和n座城市行业应用区域提供5G网络覆盖，从而推进5G技术的应用和相应的产业升级。这也是联通的“5G”的含义。'
Qt.TextWordWrap
        def BreakLine(S0, FontMetrics, MaxWidth, *args):
            arr = S0.split('\n')
            for j in range(len(arr)):
                R = []
                begin = 0
                S = arr[j]
                for i in (range(len(S))):
                    if FontMetrics.width(S[begin:i]) > MaxWidth:
                        R.append(S[begin:i])
                        begin = i
                if begin < len(S):
                    R.append(S[begin:i])
                arr[j] = '\n'.join(R)
            return '\n'.join(arr)

        print(BreakLine(s0, fm, 300))

        DateWidth = fm.width(" September 99, 2999 ")
        CreditWidth = fm.width(" Credit ")
        AmountWidth = fm.width(" W999999.99 ")
        serifLineHeight = fm.height()
        logo = QPixmap(
            "C:\\Users\\Administrator\\Desktop\\newPYprj\\res\\Zions_100.png")
        painter = QPainter(printer)
        pageRect = printer.pageRect()

        y = LeftMargin
        x = LeftMargin
        # painter.drawRect(x, y, CreditWidth, 70)
        # painter.drawPixmap(x, 0, logo)
        # y += logo.height() + sansLineHeight
        # painter.setFont(sansFont)
        # painter.drawText(x, y, "Greasy Hands Ltd.")
        # y += sansLineHeight
        # painter.drawText(x, y, "New Lombard Street")
        # y += sansLineHeight
        # painter.drawText(x, y, "London")
        # y += sansLineHeight
        # painter.drawText(x, y, "WC13 4PX")
        # y += sansLineHeight

        painter.drawPixmap(x, 0, 274, 50, logo)

        aa = ("测试字符串1", "8875", "9999", "item4")
        for i in range(1, 100):
            self.printItem(painter, x, y, 100, 30,
                           QFont("Microsoft Yahei", 12), "item" + str(i))
            y += 30

        for item in aa:
            self.printItem(painter, x, y, 100, 30,
                           QFont("Microsoft Yahei", 12), item)
            x = x + 100
            printer.newPage()

        # page = 1
        # self.generateFakeStatements()
        # for statement in self.statements:
        #     painter.save()
        #     y = 0
        #     x = pageRect.width() - logo.width() - LeftMargin
        #     painter.drawPixmap(x, 0, logo)
        #     y += logo.height() + sansLineHeight
        #     painter.setFont(sansFont)
        #     painter.drawText(x, y, "Greasy Hands Ltd.")
        #     y += sansLineHeight
        #     painter.drawText(x, y, "New Lombard Street")
        #     y += sansLineHeight
        #     painter.drawText(x, y, "London")
        #     y += sansLineHeight
        #     painter.drawText(x, y, "WC13 4PX")
        #     y += sansLineHeight
        #     painter.drawText(x, y,
        #             QDate.currentDate().toString(DATE_FORMAT))
        #     y += sansLineHeight
        #     painter.setFont(serifFont)
        #     x = LeftMargin
        #     for line in statement.address.split(", "):
        #         painter.drawText(x, y, line)
        #         y += serifLineHeight
        #     y += serifLineHeight
        #     painter.drawText(x, y, "Dear {0},".format(statement.contact))
        #     y += serifLineHeight

        #     balance = statement.balance()
        #     painter.drawText(x, y, "The balance of your account is $ {0:,.2f}".format(float(balance)))
        #     y += serifLineHeight
        #     if balance < 0:
        #         painter.setPen(Qt.red)
        #         text = "Please remit the amount owing immediately."
        #     else:
        #         text = ("We are delighted to have done business "
        #                 "with you.")
        #     painter.drawText(x, y, text)
        #     painter.setPen(Qt.black)
        #     y += int(serifLineHeight * 1.5)
        #     painter.drawText(x, y, "Transactions:")
        #     y += serifLineHeight

        #     option = QTextOption(Qt.AlignRight|Qt.AlignVCenter)
        #     for date, amount in statement.transactions:
        #         x = LeftMargin
        #         h = int(fm.height() * 1.3)
        #         painter.drawRect(x, y, DateWidth, h)
        #         painter.drawText(
        #                 QRectF(x + 3, y + 3, DateWidth - 6, h - 6),
        #                 date.toString(DATE_FORMAT), option)
        #         x += DateWidth
        #         painter.drawRect(x, y, CreditWidth, h)
        #         text = "Credit"
        #         if amount < 0:
        #             text = "Debit"
        #         painter.drawText(
        #                 QRectF(x + 3, y + 3, CreditWidth - 6, h - 6),
        #                 text, option)
        #         x += CreditWidth
        #         painter.drawRect(x, y, AmountWidth, h)
        #         if amount < 0:
        #             painter.setPen(Qt.red)
        #         painter.drawText(
        #                 QRectF(x + 3, y + 3, AmountWidth - 6, h - 6),
        #                 "$ {0:,.2f}".format(float(amount)),
        #                 option)
        #         painter.setPen(Qt.black)
        #         y += h
        #     y += serifLineHeight
        #     x = LeftMargin
        #     painter.drawText(x, y, "We hope to continue doing "
        #                            "business with you,")
        #     y += serifLineHeight
        #     painter.drawText(x, y, "Yours sincerely")
        #     y += serifLineHeight * 3
        #     painter.drawText(x, y, "K. Longrey, Manager")
        #     x = LeftMargin
        #     y = pageRect.height() - 72
        #     painter.drawLine(x, y, pageRect.width() - LeftMargin, y)
        #     y += 2
        #     font = QFont("Helvetica", 9)
        #     font.setItalic(True)
        #     painter.setFont(font)
        #     option = QTextOption(Qt.AlignCenter)
        #     option.setWrapMode(QTextOption.WordWrap)
        #     painter.drawText(
        #             QRectF(x, y, pageRect.width() - 2 * LeftMargin, 31),
        #             "The contents of this letter are for information "
        #             "only and do not form part of any contract.",
        #             option)
        #     page += 1
        #     # if page <= len(self.statements):
        #     #     printer.newPage()
        #     painter.restore()


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
