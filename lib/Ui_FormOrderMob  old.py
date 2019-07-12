# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\newPYprj\Ui\FormOrderMob.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

if __name__ == "__main__":
    from JPValidator import JPValidator


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(966, 563)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.butSave = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(
                "C:\\Users\\Administrator\\Desktop\\newPYprj\\res\\ico\\save.png"
            ), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSave.setIcon(icon)
        self.butSave.setIconSize(QtCore.QSize(32, 32))
        self.butSave.setObjectName("butSave")
        self.horizontalLayout_3.addWidget(self.butSave)
        self.butPrint = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "C:\\Users\\Administrator\\Desktop\\newPYprj\\res\\ico\\printer.png"
            ), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butPrint.setIcon(icon1)
        self.butPrint.setIconSize(QtCore.QSize(32, 32))
        self.butPrint.setObjectName("butPrint")
        self.horizontalLayout_3.addWidget(self.butPrint)
        self.butPDF = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(
                "C:\\Users\\Administrator\\Desktop\\newPYprj\\res\\ico\\pdf.png"
            ), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butPDF.setIcon(icon2)
        self.butPDF.setIconSize(QtCore.QSize(32, 32))
        self.butPDF.setObjectName("butPDF")
        self.horizontalLayout_3.addWidget(self.butPDF)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        self.fOrderID.setObjectName("fOrderID")
        self.horizontalLayout.addWidget(self.fOrderID)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, -1, 0, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.fCity = QtWidgets.QLineEdit(Form)
        self.fCity.setMinimumSize(QtCore.QSize(0, 25))
        self.fCity.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCity.setObjectName("fCity")
        self.gridLayout.addWidget(self.fCity, 2, 6, 1, 1)
        self.fContato = QtWidgets.QLineEdit(Form)
        self.fContato.setMinimumSize(QtCore.QSize(0, 25))
        self.fContato.setSizeIncrement(QtCore.QSize(0, 25))
        self.fContato.setObjectName("fContato")
        self.gridLayout.addWidget(self.fContato, 3, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_11.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_12.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        self.label_9.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_9.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.fTelefone = QtWidgets.QLineEdit(Form)
        self.fTelefone.setMinimumSize(QtCore.QSize(0, 25))
        self.fTelefone.setSizeIncrement(QtCore.QSize(0, 25))
        self.fTelefone.setObjectName("fTelefone")
        self.gridLayout.addWidget(self.fTelefone, 3, 6, 1, 1)
        self.Sucursal = QtWidgets.QCheckBox(Form)
        self.Sucursal.setMinimumSize(QtCore.QSize(0, 25))
        self.Sucursal.setSizeIncrement(QtCore.QSize(0, 25))
        self.Sucursal.setObjectName("Sucursal")
        self.gridLayout.addWidget(self.Sucursal, 1, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        self.label_6.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.fRequiredDeliveryDate = QtWidgets.QDateEdit(Form)
        self.fRequiredDeliveryDate.setMinimumSize(QtCore.QSize(0, 25))
        self.fRequiredDeliveryDate.setSizeIncrement(QtCore.QSize(0, 25))
        self.fRequiredDeliveryDate.setCalendarPopup(True)
        self.fRequiredDeliveryDate.setObjectName("fRequiredDeliveryDate")
        self.gridLayout.addWidget(self.fRequiredDeliveryDate, 0, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_4.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)
        self.fVendedor = QtWidgets.QLineEdit(Form)
        self.fVendedor.setMinimumSize(QtCore.QSize(0, 25))
        self.fVendedor.setSizeIncrement(QtCore.QSize(0, 25))
        self.fVendedor.setObjectName("fVendedor")
        self.gridLayout.addWidget(self.fVendedor, 0, 4, 1, 1)
        self.fEndereco = QtWidgets.QLineEdit(Form)
        self.fEndereco.setMinimumSize(QtCore.QSize(0, 25))
        self.fEndereco.setSizeIncrement(QtCore.QSize(0, 25))
        self.fEndereco.setPlaceholderText("")
        self.fEndereco.setObjectName("fEndereco")
        self.gridLayout.addWidget(self.fEndereco, 2, 2, 1, 3)
        self.fCelular = QtWidgets.QLineEdit(Form)
        self.fCelular.setMinimumSize(QtCore.QSize(0, 25))
        self.fCelular.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCelular.setObjectName("fCelular")
        self.gridLayout.addWidget(self.fCelular, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_3.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.fCustomerName = QtWidgets.QLineEdit(Form)
        self.fCustomerName.setMinimumSize(QtCore.QSize(0, 25))
        self.fCustomerName.setSizeIncrement(QtCore.QSize(0, 25))
        self.fCustomerName.setObjectName("fCustomerName")
        self.gridLayout.addWidget(self.fCustomerName, 1, 2, 1, 1)
        self.fNUIT = QtWidgets.QLineEdit(Form)
        self.fNUIT.setMinimumSize(QtCore.QSize(0, 25))
        self.fNUIT.setSizeIncrement(QtCore.QSize(0, 25))
        self.fNUIT.setObjectName("fNUIT")
        self.gridLayout.addWidget(self.fNUIT, 1, 4, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_7.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.fOrderDate = QtWidgets.QDateEdit(Form)
        self.fOrderDate.setCalendarPopup(True)
        self.fOrderDate.setObjectName("fOrderDate")
        self.gridLayout.addWidget(self.fOrderDate, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 260))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("dfsgsdfg")
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
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setToolTipDuration(-1)
        self.textEdit.setStatusTip("")
        self.textEdit.setWhatsThis("")
        self.textEdit.setAccessibleName("")
        self.textEdit.setLineWidth(-1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.temp = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.temp.sizePolicy().hasHeightForWidth())
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
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing
                                | QtCore.Qt.AlignVCenter)
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
        self.label_13.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
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
        self.label_14.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
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
        self.label_15.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
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
        self.fPayable.setObjectName("fPayable")
        self.gridLayout_2.addWidget(self.fPayable, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.temp)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.AllEditTriggers)
        self.butSave.clicked.connect(self.butSaveClicked)
        self.butPrint.clicked.connect(self.butPrintClicked)

        self.tableWidget.cellActivated[int, int].connect(self.cellActivated)
        self.tableWidget.cellChanged[int, int].connect(self.cellActivated)
        self.tableWidget.cellEntered[int, int].connect(self.cellEntered)
        self.tableWidget.cellClicked[int, int].connect(self.cellClicked)
        self.tableWidget.cellPressed[int, int].connect(self.cellPressed)
        self.tableWidget.cellChanged[int, int].connect(self.cellChanged)
        self.tableWidget.setColumnWidth(0, 10)

        self.fOrderDate.setDate(QtCore.QDate.currentDate())
        self.fRequiredDeliveryDate.setDate(QtCore.QDate.currentDate())
        self.fCelular.setValidator(JPValidator.ValidatorCellPhoneNumber(self))

        CellEdit1 = QtWidgets.QLineEdit()
        CellEdit1.setValidator(JPValidator.ValidatorCellPhoneNumber(self))

        class MyDelegate(QtWidgets.QStyledItemDelegate):
            def __init__(self, parent=None):
                self.parent = parent
                super().__init__(parent)

            def createEditor(self, parent, option, index):
                wdgt = QtWidgets.QLineEdit(parent)
                wdgt.setValidator(JPValidator.ValidatorCellCurrency(2))
                return wdgt

            def setEditorData(self, editor, index):
                value = index.model().data(index)  #,Qt.DisplayRole)
                if value:
                    editor.setText(str(value))

            def setModelData(self, editor, model, index):
                model.setData(index, editor.text())

        md = MyDelegate(self.tableWidget)
        self.tableWidget.setItemDelegateForColumn(1, md)
        item = QtWidgets.QTableWidgetItem()
        item.setText("456")
        self.tableWidget.setItem(0, 1, item)

    def butSaveClicked(self):
        print("kkkkk")

    def butPrintClicked(self):
        self.fAmount.__dict__["SqlValue"] = 1
        print(self.fOrderDate.dateTime())
        print(self.tableWidget.item(1, 1).text())

    def cellPressed(self, r, c):
        print("cellPressed {},{}".format(r, c))

    def cellChanged(self, r, c):
        if c == 6:
            return
        tw = self.tableWidget
        if tw.item(r, 1) and tw.item(r, 3) and tw.item(r, 4) and tw.item(r, 5):
            v = float(tw.item(r, 1).text()) * float(tw.item(
                r, 3).text()) * float(tw.item(r, 4).text()) * float(
                    tw.item(r, 5).text())
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(v))
            self.tableWidget.setItem(r, 6, item)

            S=0.0
            for i in range(tw.rowCount()):
                try:
                    S += float(tw.item(i, 6).text())
                except:
                    pass
            self.fAmount.setText('{:,.2f}'.format(S))
            self.fAmount.__dict__["Value"]= S



    def cellActivated(self, r, c):
        print("cellActivated {},{}".format(r, c))

    def cellEntered(self, r, c):
        print("cellEntered {},{}".format(r, c))

    def cellClicked(self, r, c):
        # CellEdit1 = QtWidgets.QLineEdit()
        # CellEdit1.setValidator(JPValidator.ValidatorCellPhoneNumber(self))
        # self.tableWidget.setCellWidget(r, c, CellEdit1)
        print("cellClicked {},{}".format(r, c))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.butSave.setText(_translate("Form", "Save"))
        self.butPrint.setText(_translate("Form", "Print"))
        self.butPDF.setText(_translate("Form", "PDF"))
        self.label_2.setText(_translate("Form", "NO."))
        self.label_11.setText(_translate("Form", "联系人Contato:"))
        self.label_8.setText(_translate("Form", "城市City:"))
        self.label_12.setText(_translate("Form", "电话Tel:"))
        self.label_10.setText(_translate("Form", "手机Celular:"))
        self.label_9.setText(_translate("Form", "地址Endereco:"))
        self.Sucursal.setText(_translate("Form", "Sucursal"))
        self.label_6.setText(_translate("Form", "客户名Cliente:"))
        self.fRequiredDeliveryDate.setDisplayFormat(
            _translate("Form", "yyyy-MM-dd"))
        self.label_4.setText(_translate("Form", "交货日期Date:"))
        self.label_3.setText(_translate("Form", "日期Date:"))
        self.label_5.setText(_translate("Form", "销售Vendedor:"))
        self.fCustomerName.setPlaceholderText(
            _translate("Form", "Please select a cliente."))
        self.label_7.setText(_translate("Form", "税号NUIT:"))
        self.fOrderDate.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "数量Qtd"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "名称Descrição"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "长Larg."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "宽Comp."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "单价P. Unitario"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "金额Total"))
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

    from JPEditForm import JPEditForm
    aa = JPEditForm(Form)
    aa.mainTabelName = "t_order"

    Form.show()
    sys.exit(app.exec_())
