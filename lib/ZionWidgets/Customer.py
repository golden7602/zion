from os import getcwd
from sys import path as jppath
jppath.append(getcwd())


from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget

from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPFunction import JPDateConver, setButtonIcon
from lib.JPMvc.JPEditFormModel import JPEditFormDataMode, JPFormModelMain
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.ZionPublc import JPDb
from Ui.Ui_FormCustomer import Ui_Form as Ui_Form_List
from Ui.Ui_FormCustomerEdit import Ui_Form as Ui_Form_Edit


class Form_Customer(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.UI = Ui_Form_List()
        self.UI.setupUi(self)
        mainform.addForm(self)
        self.SQL = """
            select 
                fCustomerID as `ID`, 
                fCustomerName as `客户名称Cliente`, 
                fNUIT as `税号NUIT`, 
                fCity as `城市City`, 
                fContato as `联系人Contato`, 
                fCelular as `手机Celular`, 
                fTelefone as `电话Telefone`, 
                fEmail as `电子邮件Email`, 
                fWeb as `主页Web`, 
                fEndereco as `地址Endereco`, 
                fFax as `传真Fax` 
            from  t_customer 
        """
        self.SQL_EditForm_Main=self.SQL + " where fCustomerID={}"
        self.refreshTable()

    def refreshTable(self):
        cbo = self.UI.comboBox
        cbo.DisabledEvent = True
        sql = self.SQL if (
            cbo.currentIndex() == -1
        ) else self.SQL + " where fCustomerID={}".format(cbo.currentIndex())
        self.dataInfo = JPTabelFieldInfo(sql)
        self.mod = JPTableViewModelEditForm(self.UI.tableView, self.dataInfo)
        self.UI.tableView.setModel(self.mod)
        self.UI.tableView.resizeColumnsToContents()
        lst = [[item.Datas[1], item.Datas[0]]
               for item in self.dataInfo.DataRows]
        cbo.setEditable(True)
        for r in lst:
            cbo.addItem(r[0], r[1])
        cbo.setCurrentIndex(-1)
        cbo.DisabledEvent = False

    def on_comboBox_currentIndexChanged(self, index):
        if self.UI.comboBox.DisabledEvent:
            return
        self.on_CMDREFRESH_clicked()

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item['fMenuText'])
            btn.setObjectName(item['fObjectName'])
            setButtonIcon(btn)
            btn.setEnabled(item['fHasRight'])
            self.UI.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        return EditForm_User(sql_main=sql_main,
                             edit_mode=edit_mode,
                             PKValue=PKValue)

    def getCurrentSelectPKValue(self):
        index = self.ui.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.mod.TabelFieldInfo.getOnlyData([index.row(), 0])

    @pyqtSlot()
    def on_CmdNew_clicked(self):
        self.__EditForm = None

        self.__EditForm = self.getEditForm(sql_main=self.SQL_EditForm_Main,
                                           sql_sub=None,
                                           edit_mode=JPEditFormDataMode.New,
                                           PKValue=None)
        self.__EditForm.setListForm(self)
        self.__EditForm.afterSaveData.connect(self.refreshTable)
        self.__EditForm.exec_()

    @pyqtSlot()
    def on_CmdEdit_clicked(self):
        cu_id = self.getCurrentSelectPKValue()
        if not cu_id:
            return
        self.__EditForm = None
        self.__EditForm = self.getEditForm(sql_main=self.SQL_EditForm_Main,
                                           sql_sub=None,
                                           edit_mode=JPEditFormDataMode.Edit,
                                           PKValue=cu_id)
        self.__EditForm.setListForm(self)
        self.__EditForm.afterSaveData.connect(self.refreshTable)
        self.__EditForm.exec_()

    @pyqtSlot()
    def on_CmdDelete_clicked(self):
        uid = self.getCurrentUID()
        if uid is None:
            return
        sql = "update sysusers set fEnabled=0 where fUserID={}"
        if QMessageBox.question(self, '提示', "确认要删除此用户？",
                                (QMessageBox.Yes | QMessageBox.No),
                                QMessageBox.Yes) == QMessageBox.Yes:
            JPDb().executeTransaction(sql.format(uid))
            self.mod.removeRow(
                self.ui.tableView.selectionModel().currentIndex().row())


class EditForm_User(JPFormModelMain):
    def __init__(self, sql_main, PKValue, edit_mode, flags=Qt.WindowFlags()):
        super().__init__(Ui_Form_Edit(),
                         sql_main=sql_main,
                         PKValue=PKValue,
                         edit_mode=edit_mode,
                         flags=flags)
        pix = QPixmap(getcwd() + "\\res\\Zions_100.png")
        self.ui.label_logo.setPixmap(pix)
        self.readData()
        self.ui.butPrint.hide()
        self.ui.butPDF.hide()
        self.ui.fCustomerID.setEnabled(False)

    def onFirstHasDirty(self):
        self.ui.butSave.setEnabled(True)

    @pyqtSlot()
    def on_butSave_clicked(self):
        try:
            lst = self.getSqls(self.PKRole)
            isOK, result = JPDb().executeTransaction(lst)
            if isOK:
                self.ui.butSave.setEnabled(False)
                self.afterSaveData.emit(result)
                QMessageBox.information(self, '完成',
                                        '保存数据完成！\nSave data complete!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()
