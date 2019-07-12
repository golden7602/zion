# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\newPYprj\Ui\WhereStringCreater.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgSearch(object):
    def setupUi(self, DlgSearch):
        DlgSearch.setObjectName("DlgSearch")
        DlgSearch.resize(629, 373)
        self.verticalLayout = QtWidgets.QVBoxLayout(DlgSearch)
        self.verticalLayout.setContentsMargins(3, 3, 3, 10)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(DlgSearch)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgSearch)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DlgSearch)
        self.buttonBox.accepted.connect(DlgSearch.accept)
        self.buttonBox.rejected.connect(DlgSearch.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgSearch)

    def retranslateUi(self, DlgSearch):
        _translate = QtCore.QCoreApplication.translate
        DlgSearch.setWindowTitle(_translate("DlgSearch", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DlgSearch", "关系"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DlgSearch", "("))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DlgSearch", "字段"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DlgSearch", "运算"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("DlgSearch", "值"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("DlgSearch", "结束值"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("DlgSearch", ")"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DlgSearch = QtWidgets.QDialog()
    ui = Ui_DlgSearch()
    ui.setupUi(DlgSearch)
    DlgSearch.show()
    sys.exit(app.exec_())

