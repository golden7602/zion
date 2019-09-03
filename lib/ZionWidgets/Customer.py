from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import QDate, QMetaObject, pyqtSlot, Qt, QModelIndex
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QLineEdit

from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPFunction import JPDateConver, setButtonIcon
from lib.JPMvc.JPEditFormModel import JPEditFormDataMode, JPFormModelMain
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from lib.ZionPublc import JPDb
from Ui.Ui_FormCustomer import Ui_Form as Ui_Form_List
from Ui.Ui_FormCustomerEdit import Ui_Form as Ui_Form_Edit
from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPSearch import Form_Search

# class myJPTableViewModelReadOnly(JPTableViewModelReadOnly):
#     def __init__(self, tableView, tabelFieldInfo):
#         super().__init__(tableView, tabelFieldInfo)

#     def data(self, Index, role=Qt.DisplayRole):
#         r = Index.row()
#         if role == Qt.TextColorRole and self.TabelFieldInfo.DataRows[r].Datas[
#                 5] == "Non":
#             return QColor(Qt.red)

#         return super().data(Index, role)


class Form_Customer(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.ui = Ui_Form_List()
        self.ui.setupUi(self)
        mainform.addForm(self)
        self.list_sql = """
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
            {wherestring}
            order by fCustomerName
            """
        medit_sql = """
            select 
            fCustomerID as `ID`, 
            fCustomerName as `客户名称Cliente`, 
            fNUIT as `税号NUIT`, 
            fCity,
            fContato,
            fCelular,
            fTelefone, 
            fEmail,
            fWeb,
            fEndereco,
            fFax, 
            fAreaCode
            from  t_customer
            where fCustomerID={} 
            order by fCustomerName"""
        icon = QIcon(getcwd() + "\\res\\ico\\search.png")
        action = self.ui.lineEdit.addAction(icon, QLineEdit.TrailingPosition)
        action.triggered.connect(self.actionClick)

        self.SQL_EditForm_Main = medit_sql
        self.actionClick()


    def __getUID(self):
        r = self.ui.tableView.currentIndex()
        if r:
            return self.dataInfo.DataRows[r.row()].Datas[0]
        else:
            return -1

    def actionClick(self, where_sql=None):
        #wherestring = "where fCustomerName like '%{key}%' or fNUIT like '%{key}%'"
        wherestring = """where (
            fCustomerName like '%{key}%' or
            fNUIT like '%{key}%' or
            fCity like '%{key}%' or
            fContato like '%{key}%' or
            fCelular like '%{key}%' or
            fTelefone like '%{key}%' or
            fEmail like '%{key}%' or
            fWeb like '%{key}%' or
            fEndereco like '%{key}%' or
            fFax like '%{key}%' 
        )"""
        txt = self.ui.lineEdit.text()
        txt = txt if txt else ''
        wherestring = wherestring.format(key=txt)
        sql = where_sql if where_sql else self.list_sql.format(
            wherestring=wherestring)

        tv = self.ui.tableView
        self.dataInfo = JPTabelFieldInfo(sql)
        self.mod = JPTableViewModelReadOnly(tv, self.dataInfo)
        tv.setModel(self.mod)
        tv.resizeColumnsToContents()

    def refreshTable(self):
        self.ui.lineEdit.setText(None)
        self.actionClick()

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item['fMenuText'])
            btn.setObjectName(item['fObjectName'])
            setButtonIcon(btn, item['fIcon'])
            btn.setEnabled(item['fHasRight'])
            self.ui.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        return EditForm_Customer(sql_main=sql_main,
                                 edit_mode=edit_mode,
                                 PKValue=PKValue)

    def getCurrentSelectPKValue(self):
        index = self.ui.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.mod.TabelFieldInfo.getOnlyData([index.row(), 0])

    @pyqtSlot()
    def on_CmdSearch_clicked(self):
        frm = Form_Search(self.dataInfo, self.list_sql.format(wherestring=''))
        frm.whereStringCreated.connect(self.actionClick)
        frm.exec_()

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
        uid = self.getCurrentSelectPKValue()
        if uid is None:
            return
        sql0 = """
            SELECT fCustomerID
            FROM (
                SELECT fCustomerID
                FROM v_order
                UNION ALL
                SELECT fCustomerID
                FROM v_quotation
            ) Q
            WHERE Q.fCustomerID = {}
            LIMIT 1"""
        tab = JPQueryFieldInfo(sql0.format(uid))
        if len(tab):
            txt = '该客户已经存在订单，无法删除!\n'
            txt = txt + "The customer already has an order and can not delete it!"
            QMessageBox.warning(self, '提示', txt, QMessageBox.Cancel,
                                QMessageBox.Cancel)
            return
        del_txt = '确认要删除此客户？\n'
        del_txt = del_txt + 'Are you sure you want to delete this customer?'
        sql = "DELETE FROM t_customer WHERE fCustomerID = {}"
        if QMessageBox.question(self, '提示', del_txt,
                                (QMessageBox.Yes | QMessageBox.No),
                                QMessageBox.Yes) == QMessageBox.Yes:
            JPDb().executeTransaction(sql.format(uid))
            self.refreshTable()


class EditForm_Customer(JPFormModelMain):
    def __init__(self, sql_main, PKValue, edit_mode, flags=Qt.WindowFlags()):
        super().__init__(Ui_Form_Edit(),
                         sql_main=sql_main,
                         PKValue=PKValue,
                         edit_mode=edit_mode,
                         flags=flags)
        pix = QPixmap(getcwd() + "\\res\\tmLogo100.png")
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
                                        '保存数据完成！\nSave data complete!')
        except Exception as e:
            msgBox = QMessageBox(QMessageBox.Critical, u'提示', str(e))
            msgBox.exec_()
