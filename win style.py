import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class AppWidget(QWidget):
    def __init__(self, parent=None):
        super(AppWidget, self).__init__(parent)
        #水平布局
        Hloyout = QHBoxLayout()

        #实例化标签与列表控件
        self.styleLabel = QLabel('set Style')
        self.styleComboBox = QComboBox()

        #从QStyleFactory中增加多个显示样式到列表控件
        self.styleComboBox.addItems(QStyleFactory.keys())

        #选择当前窗口的风格
        index = self.styleComboBox.findText(QApplication.style().objectName(),
                                            Qt.MatchFixedString)

        #设置当前窗口的风格
        self.styleComboBox.setCurrentIndex(index)

        #通过combobox控件选择窗口风格
        self.styleComboBox.activated[str].connect(self.handlestyleChanged)

        #添加控件到布局，设置窗口布局
        Hloyout.addWidget(self.styleLabel)
        Hloyout.addWidget(self.styleComboBox)
        self.setLayout(Hloyout)

    #改变窗口风格
    def handlestyleChanged(self, style):
        QApplication.setStyle(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgetApp = AppWidget()
    widgetApp.show()
    sys.exit(app.exec_())
