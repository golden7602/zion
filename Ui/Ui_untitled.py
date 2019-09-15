# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\win10\Desktop\Zion\zion\Ui\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.dateEdit = myDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(80, 50, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM_dd"))

class myDateEdit(QtWidgets.QDateEdit):
    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)

    def setNull(self):
        edit=self.findChild(QtWidgets.QLineEdit,"qt_spinbox_lineedit")
        if edit.text(): 
            print(edit.text())
            edit.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.dateEdit.setNull()
    Dialog.show()
    sys.exit(app.exec_())

