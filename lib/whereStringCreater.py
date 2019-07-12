# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog, QPushButton,QDialog,QHeaderView,QComboBox

from lib.Ui_WhereStringCreater import Ui_DlgSearch


class clsWhereStringCreater(Ui_DlgSearch):
    """本类是查询条件生成窗口的处理类"""
    SY_CHAR=(
        {"Sy":"`{0}` like '%{1}%'", "En1":1, "En2":0, "TiC":"包含", "Tie":"Include"},
        {"Sy":"`{0}`='{1}'", "En1":1, "En2":0, "TiC":"等于", "Tie":"Equal"},
        {"Sy":"`{0}`>'{1}'", "En1":1, "En2":0, "TiC":"大于", "Tie":"GreaterThan"},
        {"Sy":"`{0}`>='{1}'", "En1":1, "En2":0, "TiC":"大于或等于", "Tie":"GreaterOrEqual"},
        {"Sy":"`{0}`<'{1}'", "En1":1, "En2":0, "TiC":"小于", "Tie":"LessThan"},
        {"Sy":"`{0}`<='{1}'", "En1":1, "En2":0, "TiC":"小于或等于", "Tie":"LessOrEqual"},
        {"Sy":"`{0}`<>'{1}'", "En1":1, "En2":0, "TiC":"不等于", "Tie":"NotEqual"},
        {"Sy":"`{0}` like '{1}%'", "En1":1, "En2":0, "TiC":"开头是", "Tie":"BeginLike"},
        {"Sy":"Not `{0}` like '{1}%'", "En1":1, "En2":0, "TiC":"开头不是", "Tie":"NotBeginLike"},
        {"Sy":"`{0}` like '%{1}'", "En1":1, "En2":0, "TiC":"结束是", "Tie":"EndLike"},
        {"Sy":"Not `{0}` like '%{1}'", "En1":1, "En2":0, "TiC":"结束不是", "Tie":"NotEndLike"},
        {"Sy":"IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"为空", "Tie":"IsNull"},
        {"Sy":"Not IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"不为空", "Tie":"NotNull"},
        #Ext
        {"Sy":"LENGTH(`{0}`)={1}", "En1":1, "En2":0, "TiC":"长度为", "Tie":"LengthIs"},
        {"Sy":"LENGTH(`{0}`)>={1}", "En1":1, "En2":0, "TiC":"长度大于等于", "Tie":"LengthGreaterOrEqual"},
        {"Sy":"LENGTH(`{0}`)<={1}", "En1":1, "En2":0, "TiC":"长度小于等于", "Tie":"LengthLessOrEqual"},
        {"Sy":"LENGTH(`{0}`)>{1}", "En1":1, "En2":0, "TiC":"长度大于", "Tie":"LengthGreaterThan"},
        {"Sy":"LENGTH(`{0}`)<{1}", "En1":1, "En2":0, "TiC":"长度小于", "Tie":"LengthLessThan"},
        {"Sy":"`{0}`=''", "En1":0, "En2":0, "TiC":"为空字符", "Tie":"IsEmptyString"}
    )
    SY_BOOL=(
        {"Sy":"`{0}`=1", "En1":0, "En2":0, "TiC":"值为是", "Tie":"IsTrue"},
        {"Sy":"`{0}`=0", "En1":0, "En2":0, "TiC":"值为否", "Tie":"ISFalse"},
        {"Sy":"IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"为空", "Tie":"IsNull"},
        {"Sy":"Not IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"不为空", "Tie":"NotNull"}
    )
    SY_DATE=(
        {"Sy":"`{0}`<'{1}'", "En1":1, "En2":0, "TiC":"早于", "Tie":"EarluThan"},
        {"Sy":"`{0}`<='{1}'", "En1":1, "En2":0, "TiC":"早于等于", "Tie":"EarlyOrEqual"},
        {"Sy":"`{0}`>'{1}'", "En1":1, "En2":0, "TiC":"晚于", "Tie":"LaterThan"},
        {"Sy":"`{0}`>='{1}'", "En1":1, "En2":0, "TiC":"晚于等于", "Tie":"LaterOrEqual"},
        {"Sy":"`{0}`<>'{1}'", "En1":1, "En2":0, "TiC":"不等于", "Tie":"NotEqual"},
        {"Sy":"`{0}` Between '{1}' And '{2}'", "En1":1, "En2":1, "TiC":"在区间内", "Tie":"Between"},
        {"Sy":"Not (`{0}` Between '{1}' And '{2}')", "En1":1, "En2":1, "TiC":"不在区间内", "Tie":"NotBetween"},
        {"Sy":"IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"为空", "Tie":"IsNull"},
        {"Sy":"Not IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"不为空", "Tie":"NotNull"}
    )
    SY_NUM=(
        {"Sy":"`{0}`={1}", "En1":1, "En2":0, "TiC":"等于", "Tie":"Equal"},
        {"Sy":"`{0}`>{1}", "En1":1, "En2":0, "TiC":"大于", "Tie":"GreaterThan"},
        {"Sy":"`{0}`>={1}", "En1":1, "En2":0, "TiC":"大于或等于", "Tie":"GreaterOrEqual"},
        {"Sy":"`{0}`<{1}", "En1":1, "En2":0, "TiC":"小于", "Tie":"LessThan"},
        {"Sy":"`{0}`<={1}", "En1":1, "En2":0, "TiC":"小于或等于", "Tie":"LessOrEqual"},
        {"Sy":"`{0}`<>{1}", "En1":1, "En2":0, "TiC":"不等于", "Tie":"NotEqual"},
        {"Sy":"`{0}` Between {1} and {2}", "En1":1, "En2":1, "TiC":"在区间内", "Tie":"Between"},
        {"Sy":"Not (`{0}` Between {1} and {2})", "En1":1, "En2":1, "TiC":"不在区间内", "Tie":"NotBetween"},
        {"Sy":"IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"为空", "Tie":"IsNull"},
        {"Sy":"Not IsNull(`{0}`)", "En1":0, "En2":0, "TiC":"不为空", "Tie":"NotNull"}
    )
    SY={
        (1,3,8,246):SY_NUM,
        (7,10):SY_DATE,
        (16):SY_BOOL,
        (253,254):SY_CHAR
    }

    def  __init__(self,tableWidget,MainForm):
        self.ui=Ui_DlgSearch()
        self.Dlg=QDialog()
        self.ui.setupUi(self.Dlg)
        self.tab=self.ui.tableWidget
        self.dataTab=tableWidget
        self.tab.setRowCount(1)

        self.btnAddNew=QPushButton("+")
        self.btnAddNew.clicked.connect(self.btnAddNewClick)
        self.tab.setCellWidget(0,7,self.btnAddNew)
        self.Dlg.accepted.connect(self.createWhereString)
        self.FieldList=[]
        self.FieldType=[]
        for i in range(0,len(tableWidget.FieldDict)):
            self.FieldList.append(tableWidget.FieldDict[i].name)
            self.FieldType.append(tableWidget.FieldDict[i].type_code)
        self.comboBoxField=QComboBox()
        self.comboBoxField.addItems(self.FieldList)
        self.comboBoxField.setFixedWidth(True)
        self.tab.setCellWidget(0,6,self.comboBoxField)


    def createWhereString(self):
        pass
    def show(self):
        self.Dlg.setModal(True)
        self.Dlg.show()
    def btnAddNewClick(self):
        row=self.tab.rowCount()+1
        self.tab.setRowCount(row)
        self.tab.setCellWidget(row-1,7,self.btnAddNew)
