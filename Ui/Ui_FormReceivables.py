# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormReceivables.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1419, 736)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.frame_4 = QtWidgets.QFrame(self.splitter_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(500, 0))
        self.widget.setObjectName("widget")
        self.Layout_Button = QtWidgets.QHBoxLayout(self.widget)
        self.Layout_Button.setContentsMargins(0, 0, 0, 0)
        self.Layout_Button.setSpacing(2)
        self.Layout_Button.setObjectName("Layout_Button")
        self.horizontalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.SelectDate = QtWidgets.QDateEdit(self.frame_3)
        self.SelectDate.setMinimumSize(QtCore.QSize(0, 25))
        self.SelectDate.setCalendarPopup(True)
        self.SelectDate.setObjectName("SelectDate")
        self.horizontalLayout.addWidget(self.SelectDate)
        spacerItem1 = QtWidgets.QSpacerItem(1226, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabCurrentDayRec = QtWidgets.QTableView(self.splitter)
        self.tabCurrentDayRec.setMinimumSize(QtCore.QSize(0, 100))
        self.tabCurrentDayRec.setMaximumSize(QtCore.QSize(16777214, 500))
        self.tabCurrentDayRec.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabCurrentDayRec.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabCurrentDayRec.setObjectName("tabCurrentDayRec")
        self.tabCurrentDayRec.verticalHeader().setDefaultSectionSize(25)
        self.tabCurrentDayRec.verticalHeader().setMinimumSectionSize(25)
        self.SumPaymentMethod = QtWidgets.QTableView(self.splitter)
        self.SumPaymentMethod.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.SumPaymentMethod.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.SumPaymentMethod.setObjectName("SumPaymentMethod")
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.splitter_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 15))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.tabCustomerRecorder = QtWidgets.QTableView(self.layoutWidget)
        self.tabCustomerRecorder.setMinimumSize(QtCore.QSize(100, 0))
        self.tabCustomerRecorder.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabCustomerRecorder.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabCustomerRecorder.setObjectName("tabCustomerRecorder")
        self.tabCustomerRecorder.verticalHeader().setDefaultSectionSize(25)
        self.tabCustomerRecorder.verticalHeader().setMinimumSectionSize(25)
        self.verticalLayout_3.addWidget(self.tabCustomerRecorder)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setMinimumSize(QtCore.QSize(0, 15))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.tabCustomerArrearsList = QtWidgets.QTableView(self.layoutWidget1)
        self.tabCustomerArrearsList.setMinimumSize(QtCore.QSize(100, 0))
        self.tabCustomerArrearsList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabCustomerArrearsList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabCustomerArrearsList.setObjectName("tabCustomerArrearsList")
        self.tabCustomerArrearsList.verticalHeader().setDefaultSectionSize(25)
        self.tabCustomerArrearsList.verticalHeader().setMinimumSectionSize(25)
        self.verticalLayout_4.addWidget(self.tabCustomerArrearsList)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.splitter_2)
        self.verticalLayout_6.addWidget(self.splitter_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", " Daily Rreport:  "))
        self.SelectDate.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.label.setText(_translate("Form", "Receivables"))
        self.label_4.setText(_translate("Form", "Customer Recorder:"))
        self.label_2.setText(_translate("Form", "Customer Arrears:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

