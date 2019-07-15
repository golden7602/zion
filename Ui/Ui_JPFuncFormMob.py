# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\Ui\FuncFormMob.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt


class Ui_Form(QtWidgets.QWidget):
    OneButtonClicked = pyqtSignal(str)

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setObjectName("Form")
        self.resize(742, 300)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_FuncFullPath = QtWidgets.QLabel(self)
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
        self.horizontalLayout_Button = QtWidgets.QHBoxLayout(
            self.widget_Button)
        self.horizontalLayout_Button.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Button.setSpacing(0)
        self.horizontalLayout_Button.setObjectName("horizontalLayout_Button")
        self.horizontalLayout_3.addWidget(self.widget_Button)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.checkBox_1 = QtWidgets.QCheckBox(self)
        self.checkBox_1.setObjectName("checkBox_1")
        self.horizontalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setEditTriggers(
            QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def addButtons(self, btnNames: list):
        class _myButton(QtWidgets.QPushButton):
            buttonClicked = pyqtSignal(str)

            def __init__(self, *arg, **kwarg):
                super().__init__(*arg, **kwarg)

            def mousePressEvent(self, event):

                self.buttonClicked[str].emit(self.text())

        def _click(name):
            print(name)
            self.OneButtonClicked[str].emit(name)

        for item in btnNames:
            btn = _myButton(item)
            btn.buttonClicked.connect(_click)
            self.horizontalLayout_Button.addWidget(btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_FuncFullPath.setText(_translate("Form", "Function Path"))
        self.label_2.setText(_translate("Form", "Filter:"))
        self.checkBox_1.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.addButtons(["aaa", "aaassdgsdg"])
    ui.show()
    sys.exit(app.exec_())
