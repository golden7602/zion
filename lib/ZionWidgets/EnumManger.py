import datetime
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtWidgets import QWidget, QAbstractItemView, QMenu
from PyQt5.QtCore import Qt
from Ui.Ui_FormEnum import Ui_Form
from lib.JPDatabase.Query import JPQueryFieldInfo, JPTabelFieldInfo
from lib.JPMvc.JPModel import JPTableViewModelReadOnly, JPTableViewModelEditForm


class _myReadOnlyMod(JPTableViewModelReadOnly):
    def __init__(self, tableView, tabelFieldInfo):
        super().__init__(tableView, tabelFieldInfo)

    def data(self, Index, role):
        if role == Qt.TextAlignmentRole and Index.column() == 0:
            return Qt.AlignCenter
        else:
            return super().data(Index, role)


class Form_EnumManger(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.CurrentTypeID = None
        ui = Ui_Form()
        ui.setupUi(self)
        sql1 = """SELECT fTypeID AS 'TypeID 类别ID', 
                    fTypeName AS 'TypeName 名称', 
                    fNote AS 'Note 说明'
                FROM t_enumeration_type
                ORDER BY fTypeID
        """
        self.UI = ui
        #ui.butSave.setHidden(True)
        self.tab1 = ui.tabelViewType
        self.tab2 = ui.tabelViewEnum
        self.mainform = mainform
        self.tab1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab1.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabinfo1 = JPQueryFieldInfo(sql1)
        self.mod1 = _myReadOnlyMod(self.tab1, self.tabinfo1)
        self.tab1.setModel(self.mod1)
        self.tab1.resizeColumnsToContents()
        mainform.addForm(self)
        self.tab1.selectionModel().currentRowChanged.connect(
            self.type_selected)

        self.setTab2Column()
        self.tab2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tab2.customContextMenuRequested.connect(self.custom_right_menu)
        self.refreshTabEnum()
        self.UI.butSave.clicked.connect(self.but_Save)

    def type_selected(self, index1, index2):
        self.CurrentTypeID = self.tabinfo1.getOnlyData([index1.row(), 0])
        self.refreshTabEnum(self.CurrentTypeID)

    def refreshTabEnum(self, type_id: int = -1):
        sql2 = """SELECT fItemID, fTypeID, 
            fTitle AS 'text条目文本', 
            fSpare1 AS 'Value1值1', 
            fSpare2 AS 'Value2值2',
            fNote AS 'Note说明'
        FROM t_enumeration
        WHERE fTypeID = {}
        """.format(type_id)
        self.tabinfo2 = JPTabelFieldInfo(sql2)
        self.mod2 = JPTableViewModelEditForm(self.tab2, self.tabinfo2)
        self.tab2.setModel(self.mod2)
        self.setTab2Column()

    def but_Save(self):
        print(self.tabinfo2.getSqlSubStatements(self.mainform, 1, self.CurrentTypeID))

    def custom_right_menu(self, pos):
        menu = QMenu()
        opt1 = menu.addAction("AddNew增加")
        opt2 = menu.addAction("Delete删除")
        action = menu.exec_(self.tab2.mapToGlobal(pos))
        if action == opt1:
            self.mod2.insertRows(len(self.tabinfo2.RowsData))
            return
        elif action == opt2:
            self.mod2.removeRows(
                self.tab2.selectionModel().currentIndex().row())
            return
        else:
            return

    def setTab2Column(self):
        self.tab2.setColumnHidden(0, True)
        self.tab2.setColumnHidden(1, True)
        self.tab2.setColumnWidth(2, 300)
        self.tab2.setColumnWidth(3, 100)
        self.tab2.setColumnWidth(4, 100)
        self.tab2.setColumnWidth(5, 300)
