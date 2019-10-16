# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormProcuctEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        Form.resize(665, 482)
        Form.setMaximumSize(QtCore.QSize(665, 484))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setMinimumSize(QtCore.QSize(329, 60))
        self.label_logo.setMaximumSize(QtCore.QSize(329, 60))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../res/tmLogo100.png"))
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
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.fProductName = QtWidgets.QLineEdit(Form)
        self.fProductName.setMinimumSize(QtCore.QSize(0, 25))
        self.fProductName.setSizeIncrement(QtCore.QSize(0, 25))
        self.fProductName.setClearButtonEnabled(True)
        self.fProductName.setObjectName("fProductName")
        self.gridLayout.addWidget(self.fProductName, 1, 1, 1, 1)
        self.fLength = QtWidgets.QLineEdit(Form)
        self.fLength.setMinimumSize(QtCore.QSize(0, 25))
        self.fLength.setSizeIncrement(QtCore.QSize(0, 25))
        self.fLength.setClearButtonEnabled(True)
        self.fLength.setObjectName("fLength")
        self.gridLayout.addWidget(self.fLength, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        self.label_6.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setMinimumSize(QtCore.QSize(0, 25))
        self.label_15.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)
        self.fUint = QtWidgets.QLineEdit(Form)
        self.fUint.setMinimumSize(QtCore.QSize(0, 25))
        self.fUint.setSizeIncrement(QtCore.QSize(0, 25))
        self.fUint.setClearButtonEnabled(True)
        self.fUint.setObjectName("fUint")
        self.gridLayout.addWidget(self.fUint, 5, 1, 1, 1)
        self.fSpesc = QtWidgets.QLineEdit(Form)
        self.fSpesc.setMinimumSize(QtCore.QSize(0, 25))
        self.fSpesc.setSizeIncrement(QtCore.QSize(0, 25))
        self.fSpesc.setPlaceholderText("")
        self.fSpesc.setClearButtonEnabled(True)
        self.fSpesc.setObjectName("fSpesc")
        self.gridLayout.addWidget(self.fSpesc, 2, 1, 1, 1)
        self.fMinimumStock = QtWidgets.QLineEdit(Form)
        self.fMinimumStock.setMinimumSize(QtCore.QSize(0, 25))
        self.fMinimumStock.setObjectName("fMinimumStock")
        self.gridLayout.addWidget(self.fMinimumStock, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.fWidth = QtWidgets.QLineEdit(Form)
        self.fWidth.setMinimumSize(QtCore.QSize(0, 25))
        self.fWidth.setSizeIncrement(QtCore.QSize(0, 25))
        self.fWidth.setObjectName("fWidth")
        self.gridLayout.addWidget(self.fWidth, 3, 1, 1, 1)
        self.fID = QtWidgets.QLineEdit(Form)
        self.fID.setMinimumSize(QtCore.QSize(0, 25))
        self.fID.setSizeIncrement(QtCore.QSize(0, 25))
        self.fID.setReadOnly(True)
        self.fID.setClearButtonEnabled(True)
        self.fID.setObjectName("fID")
        self.gridLayout.addWidget(self.fID, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        self.label_9.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setMinimumSize(QtCore.QSize(0, 25))
        self.label_20.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.fNote = QtWidgets.QTextEdit(Form)
        self.fNote.setMinimumSize(QtCore.QSize(50, 0))
        self.fNote.setObjectName("fNote")
        self.gridLayout.addWidget(self.fNote, 9, 1, 1, 2)
        self.btn_SelectPic = QtWidgets.QPushButton(Form)
        self.btn_SelectPic.setObjectName("btn_SelectPic")
        self.gridLayout.addWidget(self.btn_SelectPic, 8, 2, 1, 1)
        self.label_Tax_Registration = QtWidgets.QLabel(Form)
        self.label_Tax_Registration.setMinimumSize(QtCore.QSize(200, 242))
        self.label_Tax_Registration.setMaximumSize(QtCore.QSize(200, 242))
        self.label_Tax_Registration.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.label_Tax_Registration.setScaledContents(True)
        self.label_Tax_Registration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tax_Registration.setObjectName("label_Tax_Registration")
        self.gridLayout.addWidget(self.label_Tax_Registration, 0, 2, 8, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fProductPic = QtWidgets.QLineEdit(Form)
        self.fProductPic.setEnabled(True)
        self.fProductPic.setObjectName("fProductPic")
        self.horizontalLayout.addWidget(self.fProductPic)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.butSave = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSave.setIcon(icon)
        self.butSave.setIconSize(QtCore.QSize(16, 16))
        self.butSave.setObjectName("butSave")
        self.horizontalLayout.addWidget(self.butSave)
        self.butCancel = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/ico/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butCancel.setIcon(icon1)
        self.butCancel.setIconSize(QtCore.QSize(16, 16))
        self.butCancel.setObjectName("butCancel")
        self.horizontalLayout.addWidget(self.butCancel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.fID, self.fProductName)
        Form.setTabOrder(self.fProductName, self.fSpesc)
        Form.setTabOrder(self.fSpesc, self.fWidth)
        Form.setTabOrder(self.fWidth, self.fLength)
        Form.setTabOrder(self.fLength, self.fUint)
        Form.setTabOrder(self.fUint, self.fMinimumStock)
        Form.setTabOrder(self.fMinimumStock, self.fNote)
        Form.setTabOrder(self.fNote, self.btn_SelectPic)
        Form.setTabOrder(self.btn_SelectPic, self.butSave)
        Form.setTabOrder(self.butSave, self.butCancel)
        Form.setTabOrder(self.butCancel, self.fProductPic)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Customer Inoformation"))
        self.label_18.setText(_translate("Form", "产品信息"))
        self.label_19.setText(_translate("Form", "Product Information"))
        self.label_13.setText(_translate("Form", "产品编号ID:"))
        self.label_7.setText(_translate("Form", "宽度Width:"))
        self.label_6.setText(_translate("Form", "客户名称ProductName:"))
        self.label_15.setText(_translate("Form", "备注Note:"))
        self.label_5.setText(_translate("Form", "最低警戒库存MinimumStock:"))
        self.label_10.setText(_translate("Form", "长度Length:"))
        self.label_9.setText(_translate("Form", "规格Spesc:"))
        self.label_20.setText(_translate("Form", "计量单位Uint:"))
        self.btn_SelectPic.setText(_translate("Form", "Select Pic"))
        self.label_Tax_Registration.setText(_translate("Form", "Tax Registration"))
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
