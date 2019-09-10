# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormCustomer_Arrears.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(868, 338)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_Button = QtWidgets.QWidget(Form)
        self.widget_Button.setObjectName("widget_Button")
        self.Layout_Button = QtWidgets.QHBoxLayout(self.widget_Button)
        self.Layout_Button.setContentsMargins(0, 0, 0, 0)
        self.Layout_Button.setSpacing(0)
        self.Layout_Button.setObjectName("Layout_Button")
        self.horizontalLayout_2.addWidget(self.widget_Button)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEdit.setSizeIncrement(QtCore.QSize(0, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tableView = QtWidgets.QTableView(self.splitter_2)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setDefaultSectionSize(25)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableView_order = QtWidgets.QTableView(self.splitter)
        self.tableView_order.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView_order.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_order.setObjectName("tableView_order")
        self.tableView_order.verticalHeader().setDefaultSectionSize(25)
        self.tableView_rec = QtWidgets.QTableView(self.splitter)
        self.tableView_rec.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView_rec.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_rec.setObjectName("tableView_rec")
        self.tableView_rec.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout.addWidget(self.splitter_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Find："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

