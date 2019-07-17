# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\Ui\FormEnum.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 593)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 15))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tabelViewType = QtWidgets.QTableView(self.layoutWidget)
        self.tabelViewType.setObjectName("tabelViewType")
        self.verticalLayout_2.addWidget(self.tabelViewType)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 15))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tabelViewEnum = QtWidgets.QTableView(self.layoutWidget_2)
        self.tabelViewEnum.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabelViewEnum.setObjectName("tabelViewEnum")
        self.verticalLayout_3.addWidget(self.tabelViewEnum)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "类别Category:"))
        self.label_3.setText(_translate("Form", "选项Options:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

