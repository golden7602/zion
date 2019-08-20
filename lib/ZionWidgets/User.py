from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormUser import Ui_Form as Ui_Form_List
from PyQt5.QtWidgets import (QMessageBox, QWidget, QTreeWidgetItem,
                             QTreeWidgetItemIterator, QPushButton)
from PyQt5.QtCore import (QDate, pyqtSlot, QThread, Qt, QAbstractItemModel,
                          QModelIndex, QMetaObject)
from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPDatabase.Database import JPDb
from PyQt5.QtGui import QIcon, QPixmap
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.JPFunction import JPDateConver
from lib.ZionPublc import JPUser
from lib.JPFunction import setButtonIcon
from lib.JPMvc.JPDelegate import (JPDelegate_LineEdit, JPDelegate_ReadOnly)
from lib.JPMvc.JPFuncForm import JPFunctionForm
from Ui.Ui_FormUserEdit import Ui_Form as Ui_Form_Edit
from lib.JPMvc.JPEditFormModel import JPFormModelMain, JPEditFormDataMode


def loadTreeview(treeWidget, items, hasCommandButton=False):
    class MyThreadReadTree(QThread):  # 加载功能树的线程类
        def __init__(self, treeWidget, items):
            super().__init__()
            treeWidget.clear()
            tree_title = [
                "权限分配 Permission Assignment【{}】".format(items[0]['fUsername']),
                "Right"
            ]
            treeWidget.setHeaderLabels(tree_title)
            treeWidget.dirty = False
            root = QTreeWidgetItem(treeWidget)
            root.setText(0, "Function")
            root.FullPath = "Function"
            root.key = 1
            root.dirty = False
            treeWidget._rootItem = root
            self.root = root
            self.items = items
            self.icopath = getcwd() + "\\res\\ico\\"

        def addItems(self, parent, items):
            for r in items:
                item = QTreeWidgetItem(parent)
                item.setText(0, r["fMenuText"])
                item.setIcon(0, QIcon(self.icopath + r["fIcon"]))
                st = (Qt.Checked if r['fHasRight'] == 1 else Qt.Unchecked)
                if not r["fDefault"]:
                    item.setCheckState(1, st)
                item.jpData = r
                item.dirty = False
                item.FullPath = (parent.FullPath + '\\' + r["fMenuText"])
                self.addItems(
                    item,
                    [l for l in self.items if l["fParentId"] == r["fNMID"]])
                item.setExpanded(1)

        def run(self):  # 线程执行函数
            self.addItems(self.root,
                          [l for l in self.items if l["fParentId"] == 1])
            self.root.setExpanded(True)

        def getRoot(self):
            return

    _readTree = MyThreadReadTree(treeWidget, items)
    _readTree.run()


# class JPFuncForm_Order(JPFunctionForm):
#     def __init__(self, MainForm):
#         super().__init__(MainForm)
#         sql_0 = """
#             select
#                 fUserID as `编号 ID`,
#                 fUsername as `用户名Name`,
#                 fNickname as `昵称Nickname`,
#                 fDepartment as `部门Department`,
#                 fNotes as `备注Note `,
#                 fEnabled as 可用Enabled
#                 from sysusers
#             where  fUserID > 1"""
#         self.backgroundWhenValueIsTrueFieldName = ['fEnabled']
#         super().setListFormSQL(sql_0, sql_0)
#         m_sql = """
#             select fUserID ,fUsername ,fNickname ,fDepartment,
#                 fNotes, fEnabled
#                 from sysusers  WHERE fUserID = '{}'"""
#         self.setEditFormSQL(m_sql, None)

#     @pyqtSlot()
#     def on_CmdSubmit_clicked(self):
#         cu_id = self.getCurrentSelectPKValue()


class EditForm_User(JPFormModelMain):
    def __init__(self, sql_main, PKValue, edit_mode, flags=Qt.WindowFlags()):
        super().__init__(Ui_Form_Edit(),
                         sql_main=sql_main,
                         PKValue=PKValue,
                         edit_mode=edit_mode,
                         flags=flags)
        pix = QPixmap(getcwd() + "\\res\\Zions_100.png")
        self.ui.label_logo.setPixmap(pix)
        # tr = self.ui.treeWidget
        # tr.setColumnCount(2)
        # tr.setHeaderLabels(["权限分配 Permission Assignment", "Right"])
        # tr.setColumnWidth(0, 400)
        # tr.setColumnWidth(1, 100)
        # tr.itemChanged.connect(self.onItemChanged)

    def checkDirty(self):
        try:
            return self.ui.treeWidget.dirty
        except AttributeError:
            return False

    def onItemChanged(self, item):
        item.dirty = True
        self.ui.treeWidget.dirty = True

    def on_tableView_currentChanged(self, index1, index2):
        if self.checkDirty():
            self.saveRight(index2)
        uid = self.dataInfo.DataRows[index1.row()].Data(0)
        ins_sql = """
            INSERT INTO sysuserright (fUserID, fRightID, fHasRight)
            SELECT {uid}, fNMID, fDefault
            FROM sysnavigationmenus
            WHERE fEnabled = 1
                AND NOT fNMID IN (
                    SELECT fRightID
                    FROM sysuserright
                    WHERE fUserID = {uid})"""
        sql = """
            SELECT u.fUsername, m.*, ord(ur.fHasRight) AS fHasRight
            FROM sysnavigationmenus m
                LEFT JOIN sysuserright ur ON m.fNMID = ur.fRightID
                LEFT JOIN sysusers u ON ur.fUserID = u.fUserID
            WHERE ur.fUserID = {}
                AND ord(m.fEnabled) = 1
            ORDER BY fDispIndex
        """
        db = JPDb()
        db.executeTransaction(ins_sql.format(uid=uid))
        items = db.getDict(sql.format(uid))
        loadTreeview(self.ui.treeWidget, items)

    def getCurrentUID(self, index=None):
        tr = self.ui.tableView
        r = index if index else tr.currentIndex()
        if r == -1:
            return
        index1 = self.mod.createIndex(r.row(), 0)
        return self.mod.data(index1, Qt.EditRole)

    def saveRight(self, index2):
        uid = self.getCurrentUID(index2)
        tr = self.ui.treeWidget
        # index = self.mod.createIndex(index2.row(), 0)
        # uid = self.mod.data(index, Qt.EditRole)
        cursor = QTreeWidgetItemIterator(tr)
        sql = """UPDATE sysuserright set fHasRight={} 
                where fUserID={} and fRightID={}"""
        lst = []
        while cursor.value():
            item = cursor.value()
            if item.dirty:
                st = 1 if item.checkState(1) == Qt.Checked else 0
                lst.append(sql.format(st, uid, item.jpData['fNMID']))
            cursor = cursor.__iadd__(1)
        if lst:
            if QMessageBox.question(self, '提示', "用户权限被修改，是否保存？",
                                    (QMessageBox.Yes | QMessageBox.No),
                                    QMessageBox.Yes) == QMessageBox.Yes:
                return JPDb().executeTransaction(lst)
            else:
                return True
        else:
            return True


class Form_User(QWidget):
    def __init__(self, mainform):
        super().__init__(mainform)
        self.ui = Ui_Form_List()
        self.ui.setupUi(self)
        mainform.addForm(self)
        tr = self.ui.treeWidget
        #tb = self.ui.tableView
        tr.setColumnCount(2)
        tr.setHeaderLabels(["权限分配 Permission Assignment", "Right"])
        tr.setColumnWidth(0, 300)
        tr.setColumnWidth(1, 100)
        tr.itemChanged.connect(self.onItemChanged)
        self.refreshTable()
        # d_o = JPDelegate_ReadOnly(tb)
        # d_e = JPDelegate_LineEdit(tb)
        # self.ui.tableView.setItemDelegateForColumn(0, d_o)
        # self.ui.tableView.setItemDelegateForColumn(1, d_e)
        # self.ui.tableView.setItemDelegateForColumn(2, d_e)
        # self.ui.tableView.setItemDelegateForColumn(3, d_e)

    def refreshTable(self):
        self.SQL = """
            select
                fUserID as `编号 ID`,
                fUsername as `用户名Name`,
                fNickname as `昵称Nickname`,
                fDepartment as `部门Department`,
                fNotes as `备注Note `,
                fEnabled as 可用Enabled
                from  sysusers
            where  fUserID > 1
        """
        tr = self.ui.treeWidget
        tb = self.ui.tableView
        self.dataInfo = JPTabelFieldInfo(self.SQL)
        self.mod = JPTableViewModelEditForm(tb, self.dataInfo)
        tb.setModel(self.mod)
        tb.resizeColumnsToContents()
        tb.selectionModel().currentChanged.connect(
            self.on_tableView_currentChanged)
        self.SQL_EditForm_Main = """
            select fUserID ,fUsername ,fNickname ,fDepartment,
                fNotes, fEnabled
                from sysusers  WHERE fUserID = '{}'"""

    def checkDirty(self):
        try:
            return self.ui.treeWidget.dirty
        except AttributeError:
            return False

    def onItemChanged(self, item):
        item.dirty = True
        self.ui.treeWidget.dirty = True

    def on_tableView_currentChanged(self, index1, index2):
        if self.checkDirty():
            self.saveRight(index2)
        uid = self.dataInfo.DataRows[index1.row()].Data(0)
        ins_sql = """
            INSERT INTO sysuserright (fUserID, fRightID, fHasRight)
            SELECT {uid}, fNMID, fDefault
            FROM sysnavigationmenus
            WHERE fEnabled = 1
                AND NOT fNMID IN (
                    SELECT fRightID
                    FROM sysuserright
                    WHERE fUserID = {uid})"""
        sql = """
            SELECT u.fUsername, m.*, ord(ur.fHasRight) AS fHasRight
            FROM sysnavigationmenus m
                LEFT JOIN sysuserright ur ON m.fNMID = ur.fRightID
                LEFT JOIN sysusers u ON ur.fUserID = u.fUserID
            WHERE ur.fUserID = {}
                AND ord(m.fEnabled) = 1
            ORDER BY fDispIndex
        """
        db = JPDb()
        db.executeTransaction(ins_sql.format(uid=uid))
        items = db.getDict(sql.format(uid))
        loadTreeview(self.ui.treeWidget, items)

    def getCurrentUID(self, index=None):
        tr = self.ui.tableView
        r = index if index else tr.currentIndex()
        if r == -1:
            return
        index1 = self.mod.createIndex(r.row(), 0)
        return self.mod.data(index1, Qt.EditRole)

    def saveRight(self, index2):
        uid = self.getCurrentUID(index2)
        tr = self.ui.treeWidget
        index = self.mod.createIndex(index2.row(), 0)
        uid = self.mod.data(index, Qt.EditRole)
        cursor = QTreeWidgetItemIterator(tr)
        sql = """UPDATE sysuserright set fHasRight={}
                where fUserID={} and fRightID={}"""
        lst = []
        while cursor.value():
            item = cursor.value()
            if item.dirty:
                st = 1 if item.checkState(1) == Qt.Checked else 0
                lst.append(sql.format(st, uid, item.jpData['fNMID']))
            cursor = cursor.__iadd__(1)
        if lst:
            if QMessageBox.question(self, '提示', "用户权限被修改，是否保存？",
                                    (QMessageBox.Yes | QMessageBox.No),
                                    QMessageBox.Yes) == QMessageBox.Yes:
                return JPDb().executeTransaction(lst)
            else:
                return True
        else:
            return True

    def addButtons(self, btnNames: list):
        for item in btnNames:
            btn = QPushButton(item['fMenuText'])
            btn.setObjectName(item['fObjectName'])
            setButtonIcon(btn)
            btn.setEnabled(item['fHasRight'])
            self.ui.horizontalLayout_Button.addWidget(btn)
        QMetaObject.connectSlotsByName(self)

    # @pyqtSlot()
    # def on_CmdNew_clicked(self):
    #     db = JPDb()
    #     sql = "insert into sysusers (fUsername,fPassword) Values ('New User','1234')"
    #     db.executeTransaction(sql)
    #     self.refreshTable()

    # @pyqtSlot()
    # def on_CmdDelete_clicked(self):
    #     uid = self.getCurrentUID()
    #     if uid is None:
    #         return
    #     sql = "update sysusers set fEnabled=0 where fUserID={}"
    #     if QMessageBox.question(self, '提示', "确认要删除此用户？",
    #                             (QMessageBox.Yes | QMessageBox.No),
    #                             QMessageBox.Yes) == QMessageBox.Yes:
    #         JPDb().executeTransaction(sql.format(uid))
    #         self.mod.removeRow(
    #             self.ui.tableView.selectionModel().currentIndex().row())

    # @pyqtSlot()
    # def on_CmdEdit_clicked(self):
    #     uid = self.getCurrentUID()
    #     if uid is None:
    #         return
    def btnRefreshClick(self):
        self.ui.CmdSave.setEnabled(False)

    def getEditForm(self, sql_main, edit_mode, sql_sub, PKValue):
        return EditForm_User(sql_main=sql_main,
                             edit_mode=edit_mode,
                             PKValue=PKValue)

    def getCurrentSelectPKValue(self):
        index = self.ui.tableView.selectionModel().currentIndex()
        if index.isValid():
            return self.mod.TabelFieldInfo.getOnlyData(
                [index.row(), 0])

    @pyqtSlot()
    def on_CmdNew_clicked(self):
        self.__EditForm = None

        self.__EditForm = self.getEditForm(sql_main=self.SQL_EditForm_Main,
                                           sql_sub=None,
                                           edit_mode=JPEditFormDataMode.New,
                                           PKValue=None)
        self.__EditForm.setListForm(self)
        self.__EditForm.afterSaveData.connect(self.btnRefreshClick)
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
        self.__EditForm.afterSaveData.connect(self.btnRefreshClick)
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