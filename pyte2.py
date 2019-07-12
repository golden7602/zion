from PyQt5.QtCore import QMargins, QRect, Qt
from PyQt5.QtGui import QFont, QPainter, QPixmap, QTransform, QFontMetrics
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog

import datetime
s = "abs"


def BreakLine(str0: str, font: QFont, max_lenght: int) -> str:
    r = []
    fm = QFontMetrics(font)
    for line in str0.splitlines():
        for i in range(len(line)):
            print(fm.width('str0'))


#BreakLine(s, QFont("Microsoft YaHei", 8), 100)


for i in range(2):
    aa= False if i==0 else True
    print(aa)
fstr = "PrintTime: %Y-%m-%d %H:%M:%S"
print(datetime.datetime.now().strftime(fstr))