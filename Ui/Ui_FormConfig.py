# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Zion\zion\Ui\FormConfig.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.layoutWidget = QtWidgets.QWidget(self.tab2)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 10, 430, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.colorpicker = QtWidgets.QPushButton(self.layoutWidget)
        self.colorpicker.setMinimumSize(QtCore.QSize(25, 0))
        self.colorpicker.setMaximumSize(QtCore.QSize(25, 16777215))
        self.colorpicker.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/color_picker.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorpicker.setIcon(icon)
        self.colorpicker.setObjectName("colorpicker")
        self.horizontalLayout_3.addWidget(self.colorpicker)
        self.Null_prompt_bac_color = QtWidgets.QWidget(self.layoutWidget)
        self.Null_prompt_bac_color.setMinimumSize(QtCore.QSize(100, 0))
        self.Null_prompt_bac_color.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.Null_prompt_bac_color.setObjectName("Null_prompt_bac_color")
        self.horizontalLayout_3.addWidget(self.Null_prompt_bac_color)
        self.tabWidget.addTab(self.tab2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Bill"))
        self.label_4.setText(_translate("Dialog", "空值提示文背景色Null prompt background color："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Dialog", "other"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
