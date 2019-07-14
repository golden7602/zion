# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\Ui\FuncFormMob.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 300)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_FuncFullPath = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FuncFullPath.setFont(font)
        self.label_FuncFullPath.setObjectName("label_FuncFullPath")
        self.horizontalLayout_2.addWidget(self.label_FuncFullPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_Button = QtWidgets.QWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.widget_Button.setFont(font)
        self.widget_Button.setObjectName("widget_Button")
        self.horizontalLayout_Button = QtWidgets.QHBoxLayout(self.widget_Button)
        self.horizontalLayout_Button.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Button.setSpacing(0)
        self.horizontalLayout_Button.setObjectName("horizontalLayout_Button")
        self.horizontalLayout_3.addWidget(self.widget_Button)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.checkBox_1 = QtWidgets.QCheckBox(Form)
        self.checkBox_1.setObjectName("checkBox_1")
        self.horizontalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_FuncFullPath.setText(_translate("Form", "Function Path"))
        self.label_2.setText(_translate("Form", "Filter:"))
        self.checkBox_1.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

