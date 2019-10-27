# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormWarehouseReceipt.ui'
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
        Form.resize(913, 567)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
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
        self.label_Title_Chn = QtWidgets.QLabel(Form)
        self.label_Title_Chn.setMinimumSize(QtCore.QSize(0, 30))
        self.label_Title_Chn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Title_Chn.setFont(font)
        self.label_Title_Chn.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_Title_Chn.setObjectName("label_Title_Chn")
        self.horizontalLayout_5.addWidget(self.label_Title_Chn)
        self.label_Title_Eng = QtWidgets.QLabel(Form)
        self.label_Title_Eng.setMinimumSize(QtCore.QSize(0, 30))
        self.label_Title_Eng.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_Title_Eng.setFont(font)
        self.label_Title_Eng.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_Title_Eng.setObjectName("label_Title_Eng")
        self.horizontalLayout_5.addWidget(self.label_Title_Eng)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.label_Title_Note = QtWidgets.QLabel(Form)
        self.label_Title_Note.setMinimumSize(QtCore.QSize(0, 30))
        self.label_Title_Note.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.label_Title_Note.setFont(font)
        self.label_Title_Note.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_Title_Note.setObjectName("label_Title_Note")
        self.verticalLayout_3.addWidget(self.label_Title_Note)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.butSave = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSave.setIcon(icon)
        self.butSave.setIconSize(QtCore.QSize(16, 16))
        self.butSave.setObjectName("butSave")
        self.horizontalLayout_3.addWidget(self.butSave)
        self.butPrint = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/ico/Print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butPrint.setIcon(icon1)
        self.butPrint.setIconSize(QtCore.QSize(16, 16))
        self.butPrint.setObjectName("butPrint")
        self.horizontalLayout_3.addWidget(self.butPrint)
        self.butPDF = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../res/ico/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butPDF.setIcon(icon2)
        self.butPDF.setIconSize(QtCore.QSize(16, 16))
        self.butPDF.setDefault(True)
        self.butPDF.setObjectName("butPDF")
        self.horizontalLayout_3.addWidget(self.butPDF)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 4, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.fOrderID = QtWidgets.QLineEdit(Form)
        self.fOrderID.setMinimumSize(QtCore.QSize(300, 0))
        self.fOrderID.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fOrderID.setFont(font)
        self.fOrderID.setText("")
        self.fOrderID.setAlignment(QtCore.Qt.AlignCenter)
        self.fOrderID.setReadOnly(True)
        self.fOrderID.setObjectName("fOrderID")
        self.horizontalLayout.addWidget(self.fOrderID)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, -1, 0, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        self.label_6.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.fEndereco = QtWidgets.QLineEdit(Form)
        self.fEndereco.setMinimumSize(QtCore.QSize(0, 25))
        self.fEndereco.setSizeIncrement(QtCore.QSize(0, 25))
        self.fEndereco.setPlaceholderText("")
        self.fEndereco.setClearButtonEnabled(False)
        self.fEndereco.setObjectName("fEndereco")
        self.gridLayout.addWidget(self.fEndereco, 2, 2, 1, 3)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)
        self.fContato = QtWidgets.QLineEdit(Form)
        self.fContato.setMinimumSize(QtCore.QSize(0, 25))
        self.fContato.setSizeIncrement(QtCore.QSize(0, 25))
        self.fContato.setClearButtonEnabled(True)
        self.fContato.setObjectName("fContato")
        self.gridLayout.addWidget(self.fContato, 4, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 3, 1, 1)
        self.fEntryID = QtWidgets.QComboBox(Form)
        self.fEntryID.setMinimumSize(QtCore.QSize(0, 25))
        self.fEntryID.setObjectName("fEntryID")
        self.gridLayout.addWidget(self.fEntryID, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.fWarehousingDate = QtWidgets.QDateEdit(Form)
        self.fWarehousingDate.setMinimumSize(QtCore.QSize(0, 25))
        self.fWarehousingDate.setSizeIncrement(QtCore.QSize(0, 25))
        self.fWarehousingDate.setAlignment(QtCore.Qt.AlignCenter)
        self.fWarehousingDate.setCalendarPopup(True)
        self.fWarehousingDate.setObjectName("fWarehousingDate")
        self.gridLayout.addWidget(self.fWarehousingDate, 0, 6, 1, 1)
        self.fOrderDate = QtWidgets.QDateEdit(Form)
        self.fOrderDate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fOrderDate.setAlignment(QtCore.Qt.AlignCenter)
        self.fOrderDate.setCalendarPopup(True)
        self.fOrderDate.setObjectName("fOrderDate")
        self.gridLayout.addWidget(self.fOrderDate, 0, 2, 1, 1)
        self.fCelular = QtWidgets.QLineEdit(Form)
        self.fCelular.setMinimumSize(QtCore.QSize(0, 25))
        self.fCelular.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCelular.setClearButtonEnabled(True)
        self.fCelular.setObjectName("fCelular")
        self.gridLayout.addWidget(self.fCelular, 4, 4, 1, 1)
        self.fSupplierID = QtWidgets.QComboBox(Form)
        self.fSupplierID.setMinimumSize(QtCore.QSize(0, 0))
        self.fSupplierID.setSizeIncrement(QtCore.QSize(0, 25))
        self.fSupplierID.setObjectName("fSupplierID")
        self.gridLayout.addWidget(self.fSupplierID, 1, 2, 1, 3)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        self.label_9.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 5, 1, 1)
        self.fTelefone = QtWidgets.QLineEdit(Form)
        self.fTelefone.setMinimumSize(QtCore.QSize(0, 25))
        self.fTelefone.setObjectName("fTelefone")
        self.gridLayout.addWidget(self.fTelefone, 4, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 5, 1, 1)
        self.fNUIT = QtWidgets.QLineEdit(Form)
        self.fNUIT.setMinimumSize(QtCore.QSize(0, 25))
        self.fNUIT.setSizeIncrement(QtCore.QSize(0, 25))
        self.fNUIT.setObjectName("fNUIT")
        self.gridLayout.addWidget(self.fNUIT, 3, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 5, 1, 1)
        self.fCity = QtWidgets.QLineEdit(Form)
        self.fCity.setMinimumSize(QtCore.QSize(0, 25))
        self.fCity.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCity.setClearButtonEnabled(False)
        self.fCity.setObjectName("fCity")
        self.gridLayout.addWidget(self.fCity, 2, 6, 1, 1)
        self.fPurchaserID = QtWidgets.QComboBox(Form)
        self.fPurchaserID.setMinimumSize(QtCore.QSize(0, 25))
        self.fPurchaserID.setObjectName("fPurchaserID")
        self.gridLayout.addWidget(self.fPurchaserID, 1, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1)
        self.fEmail = QtWidgets.QLineEdit(Form)
        self.fEmail.setMinimumSize(QtCore.QSize(0, 25))
        self.fEmail.setSizeIncrement(QtCore.QSize(0, 25))
        self.fEmail.setReadOnly(True)
        self.fEmail.setClearButtonEnabled(False)
        self.fEmail.setObjectName("fEmail")
        self.gridLayout.addWidget(self.fEmail, 3, 2, 1, 3)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_7.addWidget(self.tableView)
        spacerItem5 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fNote = QtWidgets.QTextEdit(Form)
        self.fNote.setMinimumSize(QtCore.QSize(0, 100))
        self.fNote.setMaximumSize(QtCore.QSize(16777215, 100))
        self.fNote.setToolTipDuration(-1)
        self.fNote.setStatusTip("")
        self.fNote.setWhatsThis("")
        self.fNote.setAccessibleName("")
        self.fNote.setLineWidth(-1)
        self.fNote.setObjectName("fNote")
        self.verticalLayout.addWidget(self.fNote)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.temp = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy)
        self.temp.setObjectName("temp")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.temp)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.temp)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(150, 25))
        self.label.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.fAmount = QtWidgets.QLineEdit(self.temp)
        self.fAmount.setMinimumSize(QtCore.QSize(0, 25))
        self.fAmount.setMaximumSize(QtCore.QSize(150, 25))
        self.fAmount.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fAmount.setFont(font)
        self.fAmount.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.fAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fAmount.setReadOnly(True)
        self.fAmount.setObjectName("fAmount")
        self.gridLayout_2.addWidget(self.fAmount, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.temp)
        self.label_13.setMinimumSize(QtCore.QSize(0, 25))
        self.label_13.setMaximumSize(QtCore.QSize(150, 25))
        self.label_13.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.fDesconto = QtWidgets.QLineEdit(self.temp)
        self.fDesconto.setMinimumSize(QtCore.QSize(0, 25))
        self.fDesconto.setMaximumSize(QtCore.QSize(150, 25))
        self.fDesconto.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fDesconto.setFont(font)
        self.fDesconto.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.fDesconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fDesconto.setObjectName("fDesconto")
        self.gridLayout_2.addWidget(self.fDesconto, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.temp)
        self.label_14.setMinimumSize(QtCore.QSize(0, 25))
        self.label_14.setMaximumSize(QtCore.QSize(150, 25))
        self.label_14.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.fTax = QtWidgets.QLineEdit(self.temp)
        self.fTax.setMinimumSize(QtCore.QSize(0, 25))
        self.fTax.setMaximumSize(QtCore.QSize(150, 25))
        self.fTax.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fTax.setFont(font)
        self.fTax.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.fTax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fTax.setObjectName("fTax")
        self.gridLayout_2.addWidget(self.fTax, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.temp)
        self.label_15.setMinimumSize(QtCore.QSize(0, 25))
        self.label_15.setMaximumSize(QtCore.QSize(150, 25))
        self.label_15.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)
        self.fPayable = QtWidgets.QLineEdit(self.temp)
        self.fPayable.setMinimumSize(QtCore.QSize(0, 25))
        self.fPayable.setMaximumSize(QtCore.QSize(150, 25))
        self.fPayable.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fPayable.setFont(font)
        self.fPayable.setStyleSheet("border-width: 0.7px;border-style: solid")
        self.fPayable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fPayable.setReadOnly(True)
        self.fPayable.setObjectName("fPayable")
        self.gridLayout_2.addWidget(self.fPayable, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.temp)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.butSave, self.butPrint)
        Form.setTabOrder(self.butPrint, self.butPDF)
        Form.setTabOrder(self.butPDF, self.fOrderDate)
        Form.setTabOrder(self.fOrderDate, self.fEntryID)
        Form.setTabOrder(self.fEntryID, self.fWarehousingDate)
        Form.setTabOrder(self.fWarehousingDate, self.fSupplierID)
        Form.setTabOrder(self.fSupplierID, self.fEndereco)
        Form.setTabOrder(self.fEndereco, self.tableView)
        Form.setTabOrder(self.tableView, self.fNote)
        Form.setTabOrder(self.fNote, self.fAmount)
        Form.setTabOrder(self.fAmount, self.fDesconto)
        Form.setTabOrder(self.fDesconto, self.fTax)
        Form.setTabOrder(self.fTax, self.fPayable)
        Form.setTabOrder(self.fPayable, self.fOrderID)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WarehousReceipt"))
        self.label_Title_Chn.setText(_translate("Form", "入库单"))
        self.label_Title_Eng.setText(_translate("Form", "Warehouse Receipt"))
        self.label_Title_Note.setText(_translate("Form", "(ESTE DOCUMENTO É DO USO INTERNO)"))
        self.butSave.setText(_translate("Form", "Save"))
        self.butPrint.setText(_translate("Form", "Print"))
        self.butPDF.setText(_translate("Form", "PDF"))
        self.label_2.setText(_translate("Form", "NO."))
        self.label_4.setText(_translate("Form", "入库日期WarehousingDate:"))
        self.label_6.setText(_translate("Form", "供应商Supplier:"))
        self.label_10.setText(_translate("Form", "手机Celular:"))
        self.label_17.setText(_translate("Form", "录入人Enter:"))
        self.label_3.setText(_translate("Form", "日期Date:"))
        self.fWarehousingDate.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.fOrderDate.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.fSupplierID.setToolTip(_translate("Form", "<html><head/><body><p>可输入客户名称或税号中的部分或全部进行快速过滤</p><p>Enter part or all of the customer name or tax number for quick filtering</p></body></html>"))
        self.fSupplierID.setProperty("placeholderText", _translate("Form", "Please select a cliente."))
        self.label_9.setText(_translate("Form", "地址Endereco:"))
        self.label_11.setText(_translate("Form", "联系人Contato:"))
        self.label_12.setText(_translate("Form", "电子邮件Email:"))
        self.label_16.setText(_translate("Form", "电话Telefone:"))
        self.label_7.setText(_translate("Form", "税号NUIT:"))
        self.label_8.setText(_translate("Form", "城市City:"))
        self.label_5.setText(_translate("Form", "采购员Purchaser:"))
        self.tableView.setToolTip(_translate("Form", "<html><head/><body><p>如果要输入单价为金额为0的订单，请在单价处输入0，但这时，明细表只能输入一行，如果要增加行，请先点击表格空白处（取消选中任何单元格），然后按 alt+d。</p><p>If you want to enter an order with a unit price of 0, please enter 0 at the unit price. But at this time, the detailed list can only enter one line. If you want to add more rows, please click on the blank of the table (cancel any cells), and then press Alt + D.</p></body></html>"))
        self.fNote.setPlaceholderText(_translate("Form", "Note："))
        self.label.setText(_translate("Form", "金额合计SubTota:"))
        self.label_13.setText(_translate("Form", "折扣Desconto:"))
        self.label_14.setText(_translate("Form", "税金IVA:"))
        self.label_15.setText(_translate("Form", "应付金额Valor a Pagar:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
