# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormReceivableEdit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from os import getcwd
from sys import path as jppath
jppath.append(getcwd())
from PyQt5 import QtCore, QtGui
from lib.JPMvc import JPWidgets as QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(886, 480)
        Form.setMaximumSize(QtCore.QSize(1000, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setMinimumSize(QtCore.QSize(329, 60))
        self.label_logo.setMaximumSize(QtCore.QSize(329, 60))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../res/tmLogo100.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_6.addWidget(self.label_logo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setMinimumSize(QtCore.QSize(0, 30))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setMinimumSize(QtCore.QSize(0, 30))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setMinimumSize(QtCore.QSize(0, 30))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_3.addWidget(self.label_25)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, -1, 0, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.fEndereco = QtWidgets.QLineEdit(Form)
        self.fEndereco.setMinimumSize(QtCore.QSize(0, 25))
        self.fEndereco.setSizeIncrement(QtCore.QSize(0, 25))
        self.fEndereco.setReadOnly(True)
        self.fEndereco.setPlaceholderText("")
        self.fEndereco.setClearButtonEnabled(False)
        self.fEndereco.setObjectName("fEndereco")
        self.gridLayout.addWidget(self.fEndereco, 1, 2, 1, 3)
        self.fPayeeID = QtWidgets.QComboBox(Form)
        self.fPayeeID.setObjectName("fPayeeID")
        self.gridLayout.addWidget(self.fPayeeID, 4, 4, 1, 1)
        self.fSucursal = QtWidgets.QCheckBox(Form)
        self.fSucursal.setEnabled(False)
        self.fSucursal.setMinimumSize(QtCore.QSize(0, 25))
        self.fSucursal.setSizeIncrement(QtCore.QSize(0, 25))
        self.fSucursal.setText("")
        self.fSucursal.setObjectName("fSucursal")
        self.gridLayout.addWidget(self.fSucursal, 1, 6, 1, 1)
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setMinimumSize(QtCore.QSize(0, 25))
        self.label_18.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 4, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        self.label_9.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 5, 1, 1)
        self.fAmountPayable = QtWidgets.QLineEdit(Form)
        self.fAmountPayable.setMinimumSize(QtCore.QSize(0, 25))
        self.fAmountPayable.setMaximumSize(QtCore.QSize(130, 16777215))
        self.fAmountPayable.setSizeIncrement(QtCore.QSize(0, 25))
        self.fAmountPayable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fAmountPayable.setClearButtonEnabled(False)
        self.fAmountPayable.setObjectName("fAmountPayable")
        self.gridLayout.addWidget(self.fAmountPayable, 3, 2, 1, 1)
        self.fReceiptDate = QtWidgets.QDateEdit(Form)
        self.fReceiptDate.setCalendarPopup(True)
        self.fReceiptDate.setObjectName("fReceiptDate")
        self.gridLayout.addWidget(self.fReceiptDate, 4, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        self.label_6.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setMinimumSize(QtCore.QSize(0, 25))
        self.label_19.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 5, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setMinimumSize(QtCore.QSize(0, 25))
        self.label_13.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setMinimumSize(QtCore.QSize(0, 25))
        self.label_17.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 1)
        self.fCity = QtWidgets.QLineEdit(Form)
        self.fCity.setMinimumSize(QtCore.QSize(0, 25))
        self.fCity.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCity.setReadOnly(True)
        self.fCity.setClearButtonEnabled(False)
        self.fCity.setObjectName("fCity")
        self.gridLayout.addWidget(self.fCity, 0, 6, 1, 1)
        self.fPaymentMethodID = QtWidgets.QComboBox(Form)
        self.fPaymentMethodID.setObjectName("fPaymentMethodID")
        self.gridLayout.addWidget(self.fPaymentMethodID, 4, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setMinimumSize(QtCore.QSize(0, 25))
        self.label_14.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.fAmountPaid = QtWidgets.QLineEdit(Form)
        self.fAmountPaid.setMinimumSize(QtCore.QSize(0, 25))
        self.fAmountPaid.setSizeIncrement(QtCore.QSize(0, 25))
        self.fAmountPaid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fAmountPaid.setClearButtonEnabled(False)
        self.fAmountPaid.setObjectName("fAmountPaid")
        self.gridLayout.addWidget(self.fAmountPaid, 3, 4, 1, 1)
        self.fCustomerID = QtWidgets.QComboBox(Form)
        self.fCustomerID.setMaximumSize(QtCore.QSize(130, 16777215))
        self.fCustomerID.setObjectName("fCustomerID")
        self.gridLayout.addWidget(self.fCustomerID, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setMinimumSize(QtCore.QSize(0, 25))
        self.label_20.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.fNote = QtWidgets.QTextEdit(Form)
        self.fNote.setObjectName("fNote")
        self.gridLayout.addWidget(self.fNote, 6, 2, 1, 5)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setMinimumSize(QtCore.QSize(0, 25))
        self.label_21.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 6, 0, 1, 1)
        self.fAmountCollected = QtWidgets.QLineEdit(Form)
        self.fAmountCollected.setMinimumSize(QtCore.QSize(0, 100))
        self.fAmountCollected.setSizeIncrement(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fAmountCollected.setFont(font)
        self.fAmountCollected.setAlignment(QtCore.Qt.AlignCenter)
        self.fAmountCollected.setClearButtonEnabled(True)
        self.fAmountCollected.setObjectName("fAmountCollected")
        self.gridLayout.addWidget(self.fAmountCollected, 5, 2, 1, 5)
        self.fNUIT = QtWidgets.QLineEdit(Form)
        self.fNUIT.setMinimumSize(QtCore.QSize(0, 25))
        self.fNUIT.setSizeIncrement(QtCore.QSize(0, 25))
        self.fNUIT.setReadOnly(True)
        self.fNUIT.setObjectName("fNUIT")
        self.gridLayout.addWidget(self.fNUIT, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.fCelular = QtWidgets.QLineEdit(Form)
        self.fCelular.setMinimumSize(QtCore.QSize(0, 25))
        self.fCelular.setMaximumSize(QtCore.QSize(130, 16777215))
        self.fCelular.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCelular.setReadOnly(True)
        self.fCelular.setClearButtonEnabled(False)
        self.fCelular.setObjectName("fCelular")
        self.gridLayout.addWidget(self.fCelular, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 3, 1, 1)
        self.fTelefone = QtWidgets.QLineEdit(Form)
        self.fTelefone.setMinimumSize(QtCore.QSize(0, 25))
        self.fTelefone.setSizeIncrement(QtCore.QSize(0, 25))
        self.fTelefone.setReadOnly(True)
        self.fTelefone.setClearButtonEnabled(False)
        self.fTelefone.setObjectName("fTelefone")
        self.gridLayout.addWidget(self.fTelefone, 2, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setMinimumSize(QtCore.QSize(0, 25))
        self.label_15.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 5, 2, 1)
        self.fArrears = QtWidgets.QLineEdit(Form)
        self.fArrears.setMinimumSize(QtCore.QSize(0, 40))
        self.fArrears.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fArrears.setFont(font)
        self.fArrears.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fArrears.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fArrears.setReadOnly(True)
        self.fArrears.setClearButtonEnabled(False)
        self.fArrears.setObjectName("fArrears")
        self.gridLayout.addWidget(self.fArrears, 2, 6, 2, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fID = QtWidgets.QLineEdit(Form)
        self.fID.setMaximumSize(QtCore.QSize(30, 16777215))
        self.fID.setReadOnly(True)
        self.fID.setObjectName("fID")
        self.horizontalLayout_3.addWidget(self.fID)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.butSave = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSave.setIcon(icon)
        self.butSave.setIconSize(QtCore.QSize(16, 16))
        self.butSave.setObjectName("butSave")
        self.horizontalLayout_3.addWidget(self.butSave)
        self.butCancel = QtWidgets.QPushButton(Form)
        self.butCancel.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/ico/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butCancel.setIcon(icon1)
        self.butCancel.setIconSize(QtCore.QSize(16, 16))
        self.butCancel.setObjectName("butCancel")
        self.horizontalLayout_3.addWidget(self.butCancel)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Receivable"))
        self.label_23.setText(_translate("Form", "收款记录"))
        self.label_24.setText(_translate("Form", "Collection records"))
        self.label_25.setText(_translate("Form", "(ESTE DOCUMENTO É DO USO INTERNO)"))
        self.label_18.setText(_translate("Form", "收款人Payee:"))
        self.label_9.setText(_translate("Form", "地址Endereco:"))
        self.label_16.setText(_translate("Form", "Sucursal:"))
        self.label_6.setText(_translate("Form", "客户名Cliente:"))
        self.label_19.setText(_translate("Form", "收款日期Data de Pago"))
        self.label_13.setText(_translate("Form", "应付金额Valor a Pagar:"))
        self.label_17.setText(_translate("Form", "收款方式Modo Pago:"))
        self.label_14.setText(_translate("Form", "已付金额Amount Paid:"))
        self.label_7.setText(_translate("Form", "税号NUIT:"))
        self.label_20.setText(_translate("Form", "金额Amount:"))
        self.label_8.setText(_translate("Form", "城市City:"))
        self.label_21.setText(_translate("Form", "备注Note:"))
        self.fAmountCollected.setPlaceholderText(_translate("Form", "Amount"))
        self.label_10.setText(_translate("Form", "手机Celular:"))
        self.label_12.setText(_translate("Form", "电话Tel:"))
        self.label_15.setText(_translate("Form", "欠款金额Arrears:"))
        self.butSave.setText(_translate("Form", "Save"))
        self.butCancel.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
