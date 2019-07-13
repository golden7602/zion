# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\win10\Desktop\Zion\zion\Ui\FormReport_Day.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import os
sys.path.append(os.getcwd())
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1106, 541)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
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
        self.cbo_year.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.cbo_year.setModelColumn(0)
        self.cbo_year.setObjectName("cbo_year")
        self.horizontalLayout_3.addWidget(self.cbo_year)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cbo_base = QtWidgets.QComboBox(Form)
        self.cbo_base.setMinimumSize(QtCore.QSize(100, 0))
        self.cbo_base.setObjectName("cbo_base")
        self.cbo_base.addItem("")
        self.cbo_base.addItem("")
        self.horizontalLayout_3.addWidget(self.cbo_base)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.butPrint = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butPrint.setIcon(icon)
        self.butPrint.setIconSize(QtCore.QSize(32, 32))
        self.butPrint.setObjectName("butPrint")
        self.horizontalLayout_3.addWidget(self.butPrint)
        self.butPDF = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/ico/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butPDF.setIcon(icon1)
        self.butPDF.setIconSize(QtCore.QSize(32, 32))
        self.butPDF.setObjectName("butPDF")
        self.horizontalLayout_3.addWidget(self.butPDF)
        self.butSave = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../res/ico/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSave.setIcon(icon2)
        self.butSave.setIconSize(QtCore.QSize(32, 32))
        self.butSave.setObjectName("butSave")
        self.horizontalLayout_3.addWidget(self.butSave)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setMinimumSize(QtCore.QSize(0, 250))
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setDefaultSectionSize(30)
        self.tableView.verticalHeader().setMinimumSectionSize(25)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Order"))
        self.label.setText(_translate("Form", "年度Year:"))
        self.label_3.setText(_translate("Form", "基于BasedOn:"))
        self.cbo_base.setItemText(0, _translate("Form", "Payment"))
        self.cbo_base.setItemText(1, _translate("Form", "Receivables"))
        self.butPrint.setText(_translate("Form", "Print"))
        self.butPDF.setText(_translate("Form", "PDF"))
        self.butSave.setText(_translate("Form", "Excel"))



if __name__ == "__main__":

    from lib.JPDatebase import jpGetDataListAndFields 
    from lib.JPMvc.JPModel import JPTableViewModelReadOnly
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)            

    class myMod(JPTableViewModelReadOnly):
        def __init__(self,*args):
            super().__init__(*args)
            self.f=QtGui.QFont()
            self.f.Black=True
            self.f.setBold(True)
        def data(self, Index,
             role: int = QtCore.Qt.DisplayRole):
            if Index.column()==0 and role == QtCore.Qt.TextAlignmentRole:
                return QtCore.Qt.AlignCenter
            if Index.column()==0 and role ==  QtCore.Qt.BackgroundColorRole:
                return QtGui.QColor(QtCore.Qt.gray)
            if Index.column()==0 and role ==  QtCore.Qt.FontRole:
                return self.f
            if Index.row()==(super().rowCount()-1) and role == QtCore.Qt.BackgroundColorRole:
                 return QtGui.QColor(QtCore.Qt.gray)
            if Index.row()==(super().rowCount()-1) and role == QtCore.Qt.FontRole:
                return self.f
            return super().data(Index,role)

    sql_receivables="""
        SELECT IF(ISNULL(Q3.d), 'Sum', Q3.d) AS Day0
            , M1, M2, M3, M4, M5, M6, M7, M8, M9, M10
            , M11, M12
        FROM (
            SELECT Q1.d
                , IF(Q1.m = 1, Q1.j1, NULL) AS M1
                , IF(Q1.m = 2, Q1.j1, NULL) AS M2
                , IF(Q1.m = 3, Q1.j1, NULL) AS M3
                , IF(Q1.m = 4, Q1.j1, NULL) AS M4
                , IF(Q1.m = 5, Q1.j1, NULL) AS M5
                , IF(Q1.m = 6, Q1.j1, NULL) AS M6
                , IF(Q1.m = 7, Q1.j1, NULL) AS M7
                , IF(Q1.m = 8, Q1.j1, NULL) AS M8
                , IF(Q1.m = 9, Q1.j1, NULL) AS M9
                , IF(Q1.m = 10, Q1.j1, NULL) AS M10
                , IF(Q1.m = 11, Q1.j1, NULL) AS M11
                , IF(Q1.m = 12, Q1.j1, NULL) AS M12
            FROM (
                SELECT MONTH(fReceiptDate) AS m, DAY(fReceiptDate) AS d
                    , SUM(fAmountCollected) AS j1
                FROM t_receivables
                WHERE YEAR(fReceiptDate) = {}
                GROUP BY MONTH(fReceiptDate), DAY(fReceiptDate)
            ) Q1
            GROUP BY Q1.d WITH ROLLUP
        ) Q3
        """
    sql_payment="""
        SELECT if(isnull(Q3.d), 'Sum', Q3.d) AS Day0
            , M1, M2, M3, M4, M5, M6, M7, M8, M9, M10
            , M11, M12
        FROM (
            SELECT Q1.d
                , IF(Q1.m = 1, Q1.j1, NULL) AS M1
                , IF(Q1.m = 2, Q1.j1, NULL) AS M2
                , IF(Q1.m = 3, Q1.j1, NULL) AS M3
                , IF(Q1.m = 4, Q1.j1, NULL) AS M4
                , IF(Q1.m = 5, Q1.j1, NULL) AS M5
                , IF(Q1.m = 6, Q1.j1, NULL) AS M6
                , IF(Q1.m = 7, Q1.j1, NULL) AS M7
                , IF(Q1.m = 8, Q1.j1, NULL) AS M8
                , IF(Q1.m = 9, Q1.j1, NULL) AS M9
                , IF(Q1.m = 10, Q1.j1, NULL) AS M10
                , IF(Q1.m = 11, Q1.j1, NULL) AS M11
                , IF(Q1.m = 12, Q1.j1, NULL) AS M12
            FROM (
                SELECT MONTH(fOrderDate) AS m, DAY(fOrderDate) AS d
                    , SUM(fPayable) AS j1
                FROM t_order
                WHERE (Year(fOrderDate) = {}
                    AND fCanceled = 0
                    AND fSubmited = 1
                    AND fConfirmed = 1)
                GROUP BY MONTH(fOrderDate), DAY(fOrderDate)
            ) Q1
            GROUP BY Q1.d WITH ROLLUP
        ) Q3
        """
    cbo_year,cbo_base=ui.cbo_year,ui.cbo_base
    JPdf=jpGetDataListAndFields
    def _search():
        if cbo_year.currentIndex()!=-1 and cbo_base.currentIndex()!=-1:
            sql=cbo_base.currentData()
            data,fields=JPdf(sql.format(cbo_year.currentText()))
            mod=myMod(ui.tableView,data,fields)
    year=JPdf('''select year(fOrderDate) as y  
                from t_order union select year(fReceiptDate) 
                as y from t_receivables''')[0]
    cbo_year.addItems([str(y[0]) for y in year if y[0]])
    cbo_year.setCurrentIndex(-1)
    cbo_base.clear()
    cbo_base.addItem('Payment',sql_payment)
    cbo_base.addItem('Receivables',sql_receivables)
    cbo_base.setCurrentIndex(-1)
    cbo_base.currentTextChanged.connect(_search)
    cbo_year.currentTextChanged.connect(_search)


    Form.show()
    sys.exit(app.exec_())

