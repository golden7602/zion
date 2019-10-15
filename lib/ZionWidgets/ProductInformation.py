from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLineEdit, QWidget

from lib.JPPublc import JPDb, JPPub
from Ui.Ui_FormProductList import Ui_Form as UiFormProductList
from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPMvc.JPModel import JPTableViewModelReadOnly


class myJPTableViewModelReadOnly(JPTableViewModelReadOnly):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def data(self, index, role=Qt.DisplayRole):
    #     c = index.column()
    #     if c == 9 and role == Qt.DisplayRole:
    #         return ''
    #     else:
    #         return super().data(index, role)


class Form_ProductList(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.ui = UiFormProductList()
        self.ui.setupUi(self)
        self.MainForm = mainform
        mainform.addForm(self)
        self.list_sql = """
            select 
            fID as `序号NO.`, 
            fProductName as `产品名称Descrição do produto`, 
            fCurrentQuantity as 当前库存Quantidade ,
            fMinimumStock as 最低库存MinimumStock,
            fSpesc as  `规格Especificação`, 
            fWidth as 宽Largura, 
            fLength as 长Longo, 
            fUint 单位Unidade, 
            fNote as 备注Observações
            from t_product_information 
            where fCancel=0 and fProductName like '%{key}%' 
            order by  fID
            """
        medit_sql = """
            select 
            fCustomerID as `ID`, 
            fCustomerName as `客户名称Cliente`, 
            fNUIT as `税号NUIT`, 
            fEndereco,
            fCity,
            fContato,
            fCelular,
            fEmail,
            fNote,
            fFax,
            fTaxRegCer
            from  t_customer
            where fCustomerID={} 
            order by fCustomerName"""

        icon = QIcon(JPPub().MainForm.icoPath.format("search.png"))
        action = self.ui.lineEdit.addAction(icon, QLineEdit.TrailingPosition)
        self.ui.lineEdit.returnPressed.connect(self.actionClick)
        self.ui.lineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)
        action.triggered.connect(self.actionClick)

        self.SQL_EditForm_Main = medit_sql
        self.actionClick()
        self.dispAlertStock()
        self.pub = JPPub()
        #self.pub.UserSaveData.connect(self.UserSaveData)

    def actionClick(self):
        txt = self.ui.lineEdit.text()
        txt = txt if txt else ''
        sql = self.list_sql.format(key=txt)
        tv = self.ui.tableView
        self.dataInfo = JPTabelFieldInfo(sql)
        self.mod = myJPTableViewModelReadOnly(tv, self.dataInfo)
        tv.setModel(self.mod)
        # de = MyButtonDelegate(tv, self.dataInfo)
        # tv.setItemDelegateForColumn(9, de)
        tv.resizeColumnsToContents()

    def dispAlertStock(self):
        sql = """select              
            fID as `序号NO.`, 
            fProductName as `产品名称Descrição do produto`, 
            fCurrentQuantity as 当前库存Quantidade ,
            fMinimumStock as 最低库存MinimumStock
            from t_product_information 
            where fCancel=0 and fCurrentQuantity<fMinimumStock
            order by  fID
            """
        tv = self.ui.tableView_low
        self.dataInfo_low = JPTabelFieldInfo(sql)
        self.mod_low = myJPTableViewModelReadOnly(tv, self.dataInfo_low)
        tv.setModel(self.mod_low)