from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormUser import Ui_Form
from PyQt5.QtWidgets import QMessageBox, QWidget, QTreeWidgetItem, QTreeWidgetItemIterator
from PyQt5.QtCore import (QDate, pyqtSlot, QThread, Qt, QAbstractItemModel,
                          QModelIndex)
from lib.JPDatabase.Query import JPTabelFieldInfo
from lib.JPDatabase.Database import JPDb
from PyQt5.QtGui import QIcon
from lib.JPMvc.JPModel import JPTableViewModelEditForm
from lib.JPFunction import JPDateConver
from lib.ZionPublc import JPUser


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


class Form_User(QWidget):
    def __init__(self, mainform):
        super().__init__(mainform)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        mainform.addForm(self)
        tr = self.ui.treeWidget
        tb = self.ui.tableView
        tr.setColumnCount(2)
        tr.setHeaderLabels(["权限分配 Permission Assignment", "Right"])
        tr.setColumnWidth(0, 300)
        tr.setColumnWidth(1, 100)
        tr.itemChanged.connect(self.onItemChanged)
        self.refreshTable()
    def refreshTable(self):
        self.SQL = """
            select 
                fUserID as `编号 ID`, 
                fUsername as `用户名Name`, 
                fNickname as `昵称Nickname`, 
                fDepartment as `部门Department`, 
                fNotes as `备注Note ` 
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

    def checkDirty(self):
        try:
            return self.ui.treeWidget.dirty
        except AttributeError:
            return False

    def onItemChanged(self, item):
        item.dirty = True
        self.ui.treeWidget.dirty = True

    def on_tableView_currentChanged(self, index1, index2):
        user = JPUser()
        a = user.currentUserRight()
        if self.checkDirty():
            self.saveRight(index2)
        uid = self.dataInfo.RowsData[index1.row()].Data(0)
        sql = """
            SELECT u.fUsername, m.*, ord(ur.fHasRight) AS fHasRight
            FROM sysnavigationmenus m
                LEFT JOIN sysuserright ur ON m.fNMID = ur.fRightID
                LEFT JOIN sysusers u ON ur.fUserID = u.fUserID
            WHERE ur.fUserID = {}
                AND ord(m.fEnabled) = 1
            ORDER BY fDispIndex
        """
        items = JPDb().getDict(sql.format(uid))
        loadTreeview(self.ui.treeWidget, items)

    def getCurrentUID(self, index=None):
        tr = self.ui.treeWidget
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

    @pyqtSlot()
    def on_CmdNew_clicked(self):
        db=JPDb()
        db.executeTransaction("insert into sysusers (fUsername,fPassword) Values ('New User','1234') ")
        self.refreshTable()

    @pyqtSlot()
    def on_CmdDelete_clicked(self):
        uid = self.getCurrentUID()
        if uid is None:
            return
        sql = "update sysusers set fEnabled='0' where fUserID={}"
        if QMessageBox.question(self, '提示', "确认要删除此用户？",
                                (QMessageBox.Yes | QMessageBox.No),
                                QMessageBox.Yes) == QMessageBox.Yes:
            return JPDb().executeTransaction(sql.format(uid))
            self.mod.removeRow(r.row())

    @pyqtSlot()
    def on_CmdEdit_clicked(self):
        uid = self.getCurrentUID()
        if uid is None:
            return
        
