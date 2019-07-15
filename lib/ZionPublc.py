import os
import sys
sys.path.append(os.getcwd())

from lib.JPDatebase import JPMySqlSingleTableQuery as JPQ, JPDb, getDict
from lib.JPFunction import Singleton
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon


@Singleton
class _JPUser():
    Name = None
    ID = None
    __AllUser = []
    __AllRight = []

    @staticmethod
    def reFreshAllUser():
        return JPQ(
            "select fUserID,fUsername,fPassword from sysusers where fUserID>1"
        )()

    def __init__(self):
        self.__AllRight = JPQ(
            "select fID, fUserID,fRightID,fHasRight from sysuserright")()
        self.__AllUser = self.reFreshAllUser()

    def currentUserRight(self):
        rt = self.__AllRight
        if rt and self.ID:
            return [r for r in rt if r[0] == self.ID]
        else:
            return []

    def setCurrentUserID(self, user_id: int):
        self.ID = user_id
        self.Name = [r[1] for r in self.__AllUser][0]

    def getAllUserList(self) -> list:
        return [r[0:2] for r in self.__AllUser]

    def getAllUserEnumList(self) -> list:
        return [[r[1], r[0]] for r in self.__AllUser]

    def __bool__(self):
        return self.Name and self.ID


@Singleton
class JPPub():
    def __init__(self):
        self.user = _JPUser()
        self.customerList = JPQ('''select fCustomerName,fCustomerID,fNUIT,
                            fCity,fContato from t_customer''')()
        self.__allCustomerList = JPQ(
            'select fCustomerName,fCustomerID,fNUIT,fCity,fContato from t_customer'
        )()

        def getEnumDict() -> dict:
            cur = JPDb().currentConn.cursor()
            cur.execute('''select fTypeID,fTitle,fItemID,fSpare1,
                        fSpare2,fNote from t_enumeration''')
            return {
                k: [row1[1:] for row1 in cur._rows if row1[0] == k]
                for k in set(row[0] for row in cur._rows)
            }

        self.__EnumDict = getEnumDict()

        self.__sysNavigationMenusDict = getDict(
            """
            SELECT fNMID, fMenuText, fParentId, fCommand, fObjectName, fIcon,
                    cast(fIsCommandButton AS SIGNED) AS fIsCommandButton
            FROM sysnavigationmenus
            WHERE fEnabled=1 AND fNMID>1
            ORDER BY fDispIndex
            """)

    def getEnumList(self, enum_type_id: int):
        return self.__EnumDict[enum_type_id]

    def getCustomerList(self):
        return self.__allCustomerList

    def getSysNavigationMenusDict(self):
        return self.__sysNavigationMenusDict


def loadTreeview(treeWidget, items):
    class MyThreadReadTree(QThread):  # 加载功能树的线程类
        def __init__(self, treeWidget, items):
            super().__init__()
            root = QTreeWidgetItem(treeWidget)
            root.setText(0, "Function")
            root.FullPath = "Function"
            self.root = root
            self.items = items

        def run(self):  # 线程执行函数
            def additemtotree(parent, nmid, items, begin=0):
                for i in range(begin, len(items) - 1):
                    if items[i]["fParentId"] == nmid and int(
                            items[i]["fIsCommandButton"]) == 0:
                        item = QTreeWidgetItem(parent)
                        item.setText(0, items[i]["fMenuText"])
                        path = os.getcwd(
                        ) + "\\res\\ico\\" + items[i]["fIcon"]
                        item.setIcon(0, QIcon(path))
                        item.jpData = items[i]
                        item.FullPath = parent.FullPath + \
                            '\\' + items[i]["fMenuText"]
                        additemtotree(item, items[i]["fNMID"], items, i)
                        item.setExpanded(1)

            additemtotree(self.root, 1, self.items)
            self.root.setExpanded(True)

        def getRoot(self):
            return
    _readTree = MyThreadReadTree(treeWidget, items)
    _readTree.run()