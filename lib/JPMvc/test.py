# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\JinptConfig\桌面2018\newPYprj\Ui\testTabelView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1020, 596)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setEditTriggers(
            QtWidgets.QAbstractItemView.AllEditTriggers)

        self.tableView.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setDefaultSectionSize(25)
        #self.tableView.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_3.addWidget(self.tableView)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.butAddRow = QtWidgets.QPushButton(Dialog)
        self.butAddRow.setObjectName("butAddRow")
        self.horizontalLayout.addWidget(self.butAddRow)
        self.butDelRow = QtWidgets.QPushButton(Dialog)
        self.butDelRow.setObjectName("butDelRow")
        self.horizontalLayout.addWidget(self.butDelRow)
        self.butSqls = QtWidgets.QPushButton(Dialog)
        self.butSqls.setObjectName("butSqls")
        self.horizontalLayout.addWidget(self.butSqls)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel
                                          | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.butAddRow.setText(_translate("Dialog", "AddRow"))
        self.butDelRow.setText(_translate("Dialog", "DelRow"))
        self.butSqls.setText(_translate("Dialog", "Sqls"))







if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.getcwd())
    from lib.JPDatebase import JPDb
    from lib.JPMvc.JPModel import JPTableModelEditForm, JPTableModelReadOnly
    from lib.JPMvc.JPDelegate import JPDelegate_ComboBox, JPDelegate_LineEdit, JPDelegate_DateEdit
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    db = JPDb()
    customers = db.getRecordsTuple(
        "select fCustomerName,fCustomerID from t_customer")
    users = db.getRecordsTuple(
        "select fUsername,fUserID from sysusers where fUserID>1")
    enums = db.getEnumDict(
        "select fTypeID,fTitle,fItemID,fSpare1,fSpare2,fNote from t_enumeration"
    )
    fEspecieID = [row[0:2] for row in enums[2]]
    data, flds = db.getRecordsAndFieldInfoTuple(
        "select * from t_order limit 10")
    myModel = JPTableModelEditForm(ui.tableView, data, flds)
    myModel.setFieldsRowSource("fCustomerID", customers, "fSubmitID", users,
                               "fReviewerID", users, "fConfirmID", users,
                               "fDelivererID", users, "fCancelID", users,
                               "fEspecieID", fEspecieID, "fEntryID", users)
    ui.tableView.setModel(myModel)
    myModel.setColumnsDetegate(ui.tableView)

    def myAddRow():
        row = myModel.rowCount()
        myModel.insertRows(row)
        index = myModel.index(row, 0)
        ui.tableView = ui.tableView
        ui.tableView.setFocus()
        ui.tableView.setCurrentIndex(index)
        ui.tableView.edit(index)

    ui.butAddRow.clicked.connect(myAddRow)

    # for column in range(len(flds)):
    #                 ui.tableView.resizeColumnToContents(column)
    Dialog.show()
    sys.exit(app.exec_())
