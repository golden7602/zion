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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.tab2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Null_prompt_bac_color = QtWidgets.QWidget(self.frame)
        self.Null_prompt_bac_color.setMinimumSize(QtCore.QSize(100, 0))
        self.Null_prompt_bac_color.setStyleSheet(
            "background-color: rgb(255, 0, 255);\n"
            "border: 1px inset   ;\n"
            "border-color: rgb(194, 194, 194);\n"
            "")
        self.Null_prompt_bac_color.setObjectName("Null_prompt_bac_color")
        self.horizontalLayout_3.addWidget(self.Null_prompt_bac_color)
        self.colorpicker = QtWidgets.QPushButton(self.frame)
        self.colorpicker.setMinimumSize(QtCore.QSize(25, 0))
        self.colorpicker.setMaximumSize(QtCore.QSize(25, 16777215))
        self.colorpicker.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ico/color_picker.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorpicker.setIcon(icon)
        self.colorpicker.setObjectName("colorpicker")
        self.horizontalLayout_3.addWidget(self.colorpicker)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.PrintHighlightBackgroundColor = QtWidgets.QWidget(self.frame)
        self.PrintHighlightBackgroundColor.setMinimumSize(QtCore.QSize(100, 0))
        self.PrintHighlightBackgroundColor.setStyleSheet(
            "background-color: rgb(255, 0, 255);\n"
            "border: 1px inset   ;\n"
            "border-color: rgb(194, 194, 194);\n"
            "")
        self.PrintHighlightBackgroundColor.setObjectName(
            "PrintHighlightBackgroundColor")
        self.horizontalLayout_6.addWidget(self.PrintHighlightBackgroundColor)
        self.colorpicker_2 = QtWidgets.QPushButton(self.frame)
        self.colorpicker_2.setMinimumSize(QtCore.QSize(25, 0))
        self.colorpicker_2.setMaximumSize(QtCore.QSize(25, 16777215))
        self.colorpicker_2.setText("")
        self.colorpicker_2.setIcon(icon)
        self.colorpicker_2.setObjectName("colorpicker_2")
        self.horizontalLayout_6.addWidget(self.colorpicker_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_AutoEllipsis = QtWidgets.QRadioButton(self.widget)
        self.radioButton_AutoEllipsis.setObjectName("radioButton_AutoEllipsis")
        self.horizontalLayout_5.addWidget(self.radioButton_AutoEllipsis)
        self.radioButton_AutoShrinkFonts = QtWidgets.QRadioButton(self.widget)
        self.radioButton_AutoShrinkFonts.setObjectName(
            "radioButton_AutoShrinkFonts")
        self.horizontalLayout_5.addWidget(self.radioButton_AutoShrinkFonts)
        self.horizontalLayout_4.addWidget(self.widget)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 429,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.frame)
        self.tabWidget.addTab(self.tab2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel
                                          | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Config "))
        self.label.setText(
            _translate("Dialog", "PrintOrder单据备注内容 PrintOrder Note："))
        self.label_2.setText(_translate("Dialog", "单据账户信息Conta Bancaria："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1),
                                  _translate("Dialog", "Bill"))
        self.label_4.setText(
            _translate("Dialog", "空值提示文背景色Null Prompt Background Color："))
        self.label_5.setText(
            _translate("Dialog", "打印突出显示背景色Print Highlight Background Color："))
        self.label_3.setText(
            _translate(
                "Dialog",
                "文本宽度超边界时打印方式 Printing Policy When Text Width is Extra Width:")
        )
        self.radioButton_AutoEllipsis.setText(
            _translate("Dialog", "自动省略Auto ellipsis"))
        self.radioButton_AutoShrinkFonts.setText(
            _translate("Dialog", "自动缩小字体Auto shrink fonts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2),
                                  _translate("Dialog", "other"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
