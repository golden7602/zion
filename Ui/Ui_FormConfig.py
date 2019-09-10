# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormConfig.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(971, 629)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(3, 3, -1, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Note_PrintingOrder = QtWidgets.QTextEdit(self.tab1)
        self.Note_PrintingOrder.setObjectName("Note_PrintingOrder")
        self.verticalLayout_2.addWidget(self.Note_PrintingOrder)
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Bank_Account = QtWidgets.QTextEdit(self.tab1)
        self.Bank_Account.setObjectName("Bank_Account")
        self.verticalLayout_2.addWidget(self.Bank_Account)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_BackColor = QtWidgets.QLabel(self.tab1)
        self.label_BackColor.setMinimumSize(QtCore.QSize(100, 0))
        self.label_BackColor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_BackColor.setText("")
        self.label_BackColor.setObjectName("label_BackColor")
        self.horizontalLayout_2.addWidget(self.label_BackColor)
        self.butBackColor = QtWidgets.QPushButton(self.tab1)
        self.butBackColor.setMaximumSize(QtCore.QSize(80, 16777215))
        self.butBackColor.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.butBackColor.setAutoFillBackground(False)
        self.butBackColor.setObjectName("butBackColor")
        self.horizontalLayout_2.addWidget(self.butBackColor)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Config "))
        self.label.setText(_translate("Dialog", "PrintOrder单据备注内容 PrintOrder Note："))
        self.label_2.setText(_translate("Dialog", "单据账账户信息Conta Bancaria："))
        self.label_3.setText(_translate("Dialog", "突出显示背景填充颜色Highlight background fill color:"))
        self.butBackColor.setText(_translate("Dialog", "Change"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Bill"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Dialog", "other"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

