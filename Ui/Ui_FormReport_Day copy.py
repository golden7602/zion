# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormReport_Day.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1106, 798)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cbo_year = QtWidgets.QComboBox(Form)
        self.cbo_year.setMinimumSize(QtCore.QSize(100, 0))
        self.cbo_year.setAutoFillBackground(False)
        self.cbo_year.setLocale(
            QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.cbo_year.setModelColumn(0)
        self.cbo_year.setObjectName("cbo_year")
        self.horizontalLayout_3.addWidget(self.cbo_year)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cbo_base = QtWidgets.QComboBox(Form)
        self.cbo_base.setMinimumSize(QtCore.QSize(100, 0))
        self.cbo_base.setObjectName("cbo_base")
        self.horizontalLayout_3.addWidget(self.cbo_base)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.CmdPrint = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CmdPrint.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/printer.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CmdPrint.setIcon(icon)
        self.CmdPrint.setIconSize(QtCore.QSize(16, 16))
        self.CmdPrint.setObjectName("CmdPrint")
        self.horizontalLayout_3.addWidget(self.CmdPrint)
        self.CmdPDF = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CmdPDF.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/ico/pdf.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CmdPDF.setIcon(icon1)
        self.CmdPDF.setIconSize(QtCore.QSize(16, 16))
        self.CmdPDF.setObjectName("CmdPDF")
        self.horizontalLayout_3.addWidget(self.CmdPDF)
        self.CmdExportToExcel = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CmdExportToExcel.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../res/ico/export.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CmdExportToExcel.setIcon(icon2)
        self.CmdExportToExcel.setIconSize(QtCore.QSize(16, 16))
        self.CmdExportToExcel.setObjectName("CmdExportToExcel")
        self.horizontalLayout_3.addWidget(self.CmdExportToExcel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setMinimumSize(QtCore.QSize(0, 250))
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setDefaultSectionSize(23)
        self.tableView.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout.addWidget(self.graphicsView_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Order"))
        self.label.setText(_translate("Form", "年度Year:"))
        self.label_3.setText(_translate("Form", "基于BasedOn:"))
        self.CmdPrint.setText(_translate("Form", "Print"))
        self.CmdPDF.setText(_translate("Form", "PDF"))
        self.CmdExportToExcel.setText(_translate("Form", "ExportToExcel"))

    def aaa(self):
        self.series_1 = QLineSeries()  #定义LineSerise，将类QLineSeries实例化
        self._1_point_0 = QPointF(0.00, 0.00)  #定义折线坐标点
        self._1_point_1 = QPointF(0.80, 6.00)
        self._1_point_2 = QPointF(2.00, 2.00)
        self._1_point_3 = QPointF(4.00, 3.00)
        self._1_point_4 = QPointF(1.00, 3.00)
        self._1_point_5 = QPointF(5.00, 3.00)
        self._1_point_list = [
            self._1_point_0, self._1_point_1, self._1_point_4, self._1_point_2,
            self._1_point_3, self._1_point_5
        ]  #定义折线点清单
        self.series_1.append(self._1_point_list)  #折线添加坐标点清单
        self.series_1.setName("折线一")  #折线命名
        self.x_Aix = QValueAxis()  #  定义x轴，实例化
        self.x_Aix.setRange(0.00, 5.00)  #设置量程
        self.x_Aix.setLabelFormat("%0.2f")  #设置坐标轴坐标显示方式，精确到小数点后两位
        self.x_Aix.setTickCount(6)  #设置x轴有几个量程
        self.x_Aix.setMinorTickCount(0)  #设置每个单元格有几个小的分级

        self.y_Aix = QValueAxis()  #定义y轴
        self.y_Aix.setRange(0.00, 6.00)
        self.y_Aix.setLabelFormat("%0.2f")
        self.y_Aix.setTickCount(7)
        self.y_Aix.setMinorTickCount(0)

        self.charView = QChartView(
            self.graphicsView)  #定义charView，父窗体类型为 Window
        g=self.graphicsView.geometry()
        self.charView.setGeometry(g.x(),g.y(),g.width(),g.height())
        #self.charView.setGeometry(0, 0, self.width(),
        #                           self.height())  #设置charView位置、大小
        self.charView.chart().addSeries(self.series_1)  #添加折线
        # self.charView.chart().addSeries(self.series_2)  #添加折线
        #		self.charView.chart().addSeries(self.series_3)  #添加折线
        self.charView.chart().setAxisX(self.x_Aix)  #设置x轴属性
        self.charView.chart().setAxisY(self.y_Aix)  #设置y轴属性
        #		self.charView.chart().createDefaultAxes() #使用默认坐标系
        self.charView.chart().setTitleBrush(QBrush(Qt.cyan))  #设置标题笔刷
        self.charView.chart().setTitle("双折线")  #设置标题

        #QCharView.setTheme(self.charView.ChartThemeBlueIcy)
        self.charView.show()  #显示charView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.aaa()
    Form.show()
    sys.exit(app.exec_())
