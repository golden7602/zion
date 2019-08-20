# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\Ui\FormCustomerEdit.ui'
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
        Form.resize(661, 308)
        Form.setMaximumSize(QtCore.QSize(661, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setMinimumSize(QtCore.QSize(329, 60))
        self.label_logo.setMaximumSize(QtCore.QSize(329, 60))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../res/Zions_100.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_2.addWidget(self.label_logo)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setMinimumSize(QtCore.QSize(0, 30))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setMinimumSize(QtCore.QSize(0, 30))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fCity = QtWidgets.QComboBox(Form)
        self.fCity.setMinimumSize(QtCore.QSize(0, 25))
        self.fCity.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCity.setProperty("clearButtonEnabled", True)
        self.fCity.setObjectName("fCity")
        self.gridLayout.addWidget(self.fCity, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.fAreaCode = QtWidgets.QLineEdit(Form)
        self.fAreaCode.setMinimumSize(QtCore.QSize(0, 25))
        self.fAreaCode.setSizeIncrement(QtCore.QSize(0, 25))
        self.fAreaCode.setClearButtonEnabled(True)
        self.fAreaCode.setObjectName("fAreaCode")
        self.gridLayout.addWidget(self.fAreaCode, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.fCustomerID = QtWidgets.QLineEdit(Form)
        self.fCustomerID.setMinimumSize(QtCore.QSize(0, 25))
        self.fCustomerID.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCustomerID.setReadOnly(True)
        self.fCustomerID.setClearButtonEnabled(True)
        self.fCustomerID.setObjectName("fCustomerID")
        self.gridLayout.addWidget(self.fCustomerID, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setMinimumSize(QtCore.QSize(0, 25))
        self.label_14.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)
        self.fCustomerName = QtWidgets.QLineEdit(Form)
        self.fCustomerName.setMinimumSize(QtCore.QSize(0, 25))
        self.fCustomerName.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCustomerName.setClearButtonEnabled(True)
        self.fCustomerName.setObjectName("fCustomerName")
        self.gridLayout.addWidget(self.fCustomerName, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)
        self.fCelular = QtWidgets.QLineEdit(Form)
        self.fCelular.setMinimumSize(QtCore.QSize(0, 25))
        self.fCelular.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCelular.setClearButtonEnabled(True)
        self.fCelular.setObjectName("fCelular")
        self.gridLayout.addWidget(self.fCelular, 3, 3, 1, 1)
        self.fContato = QtWidgets.QLineEdit(Form)
        self.fContato.setMinimumSize(QtCore.QSize(0, 25))
        self.fContato.setSizeIncrement(QtCore.QSize(0, 25))
        self.fContato.setClearButtonEnabled(True)
        self.fContato.setObjectName("fContato")
        self.gridLayout.addWidget(self.fContato, 2, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        self.label_9.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.fEndereco = QtWidgets.QLineEdit(Form)
        self.fEndereco.setMinimumSize(QtCore.QSize(0, 25))
        self.fEndereco.setSizeIncrement(QtCore.QSize(0, 25))
        self.fEndereco.setPlaceholderText("")
        self.fEndereco.setClearButtonEnabled(True)
        self.fEndereco.setObjectName("fEndereco")
        self.gridLayout.addWidget(self.fEndereco, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        self.label_6.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.fEmail = QtWidgets.QLineEdit(Form)
        self.fEmail.setMinimumSize(QtCore.QSize(0, 25))
        self.fEmail.setSizeIncrement(QtCore.QSize(0, 25))
        self.fEmail.setClearButtonEnabled(True)
        self.fEmail.setObjectName("fEmail")
        self.gridLayout.addWidget(self.fEmail, 4, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setMinimumSize(QtCore.QSize(0, 25))
        self.label_20.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 2, 1, 1)
        self.fNUIT = QtWidgets.QLineEdit(Form)
        self.fNUIT.setMinimumSize(QtCore.QSize(0, 25))
        self.fNUIT.setSizeIncrement(QtCore.QSize(0, 25))
        self.fNUIT.setObjectName("fNUIT")
        self.gridLayout.addWidget(self.fNUIT, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setMinimumSize(QtCore.QSize(0, 25))
        self.label_15.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)
        self.fWeb = QtWidgets.QLineEdit(Form)
        self.fWeb.setMinimumSize(QtCore.QSize(0, 25))
        self.fWeb.setSizeIncrement(QtCore.QSize(0, 25))
        self.fWeb.setClearButtonEnabled(True)
        self.fWeb.setObjectName("fWeb")
        self.gridLayout.addWidget(self.fWeb, 5, 1, 1, 1)
        self.fTelefone = QtWidgets.QLineEdit(Form)
        self.fTelefone.setMinimumSize(QtCore.QSize(0, 25))
        self.fTelefone.setSizeIncrement(QtCore.QSize(0, 25))
        self.fTelefone.setClearButtonEnabled(True)
        self.fTelefone.setObjectName("fTelefone")
        self.gridLayout.addWidget(self.fTelefone, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setMinimumSize(QtCore.QSize(0, 25))
        self.label_16.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 2, 1, 1)
        self.fFax = QtWidgets.QLineEdit(Form)
        self.fFax.setMinimumSize(QtCore.QSize(0, 25))
        self.fFax.setSizeIncrement(QtCore.QSize(0, 25))
        self.fFax.setClearButtonEnabled(True)
        self.fFax.setObjectName("fFax")
        self.gridLayout.addWidget(self.fFax, 5, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.butPDF = QtWidgets.QPushButton(Form)
        self.butPDF.setObjectName("butPDF")
        self.horizontalLayout.addWidget(self.butPDF)
        self.butPrint_2 = QtWidgets.QPushButton(Form)
        self.butPrint_2.setObjectName("butPrint_2")
        self.horizontalLayout.addWidget(self.butPrint_2)
        self.butSave = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSave.setIcon(icon)
        self.butSave.setIconSize(QtCore.QSize(16, 16))
        self.butSave.setObjectName("butSave")
        self.horizontalLayout.addWidget(self.butSave)
        self.butPrint = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/ico/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butPrint.setIcon(icon1)
        self.butPrint.setIconSize(QtCore.QSize(16, 16))
        self.butPrint.setObjectName("butPrint")
        self.horizontalLayout.addWidget(self.butPrint)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Order"))
        self.label_18.setText(_translate("Form", "客户信息"))
        self.label_19.setText(_translate("Form", "Customer Information"))
        self.label_5.setText(_translate("Form", "城市City:"))
        self.label_13.setText(_translate("Form", "客户编号CustomerID:"))
        self.label_11.setText(_translate("Form", "联系人Contato:"))
        self.label_14.setText(_translate("Form", "区号AreaCode:"))
        self.label_10.setText(_translate("Form", "手机Celular:"))
        self.label_9.setText(_translate("Form", "地址Endereco:"))
        self.label_7.setText(_translate("Form", "税号NUIT:"))
        self.label_6.setText(_translate("Form", "客户名称CustomerName:"))
        self.label_20.setText(_translate("Form", "电子邮件Email:"))
        self.label_15.setText(_translate("Form", "网址Web:"))
        self.label_12.setText(_translate("Form", "电话Tel:"))
        self.label_16.setText(_translate("Form", "传真Fax:"))
        self.butPDF.setText(_translate("Form", "PushButton"))
        self.butPrint_2.setText(_translate("Form", "PushButton"))
        self.butSave.setText(_translate("Form", "Save"))
        self.butPrint.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
