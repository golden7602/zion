from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

#from lib.JPDatebase import JPMySqlSingleTableQuery as JPQ, JPDb, getDict
from lib.JPDatabase.Database import JPDb
from lib.JPFunction import Singleton
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox, QDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QObject
from PyQt5.QtGui import QIcon
from Ui.Ui_FormUserLogin import Ui_Dialog
from lib.JPFunction import md5_passwd


class Form_UserLogin(QDialog):
    def __init__(self, isLogin=True):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.isLogin = isLogin
        us = JPUser()
        for r in [r for r in us.getAllUserList() if r[0] > 1]:
            self.ui.User.addItem('{} {}'.format(r[0], r[1]), r[0])
        self.ui.User.setCurrentIndex(-1)
        self.setWindowFlags(Qt.WindowTitleHint)
        if not isLogin:
            self.setWindowTitle("Change User")
            self.ui.label_Title.setText("Change User")
        self.exec_()

    def accept(self):
        def msgbox(msg: str):
            QMessageBox.warning(self, '提示', msg, QMessageBox.Yes,
                                QMessageBox.Yes)

        uid = self.ui.User.currentText()
        pwd = self.ui.Password.text()
        sql0 = "select fUserID from sysusers where fUserName='{uid}' and fPassword='{pwd}'"
        sql1 = "select fUserID from sysusers where fUserID='{uid}' and fPassword='{pwd}' and ord(fEnabled)=1"
        if all((pwd, uid)):
            isAdmin = 1 if uid.upper() == 'ADMIN' else 0
            if isAdmin:
                sql = sql0.format(pwd=md5_passwd(pwd), uid=uid)
            else:
                sql = sql1.format(pwd=md5_passwd(pwd),
                                  uid=self.ui.User.currentData())
            lst = JPDb().getDict(sql)
            if lst:
                JPUser().setCurrentUserID(lst[0]['fUserID'])
                self.hide()
            else:
                msgbox('用户名或密码错误！\nUsername or password incorrect!')
        else:
            msgbox('用名或密码没有输入！')

    def reject(self):
        if not self.isLogin:
            self.hide()
        else:
            exit()


@Singleton
class JPUser(QObject):
    __Name = None
    __ID = None
    __AllUser = []
    __CurrentUserRight = []
    userChange = pyqtSignal(list)
    FRM_LOGIN = None

    def reFreshAllUser(self):
        db = JPDb()
        sql = """select fUserID,fUsername from sysusers where fUserID=1 or ord(fEnabled)=1"""
        self.__AllUser = db.getDataList(sql)

    def currentUserID(self):
        if self.__ID:
            return self.__ID
        self.FRM_LOGIN = Form_UserLogin()

    def changeUser(self):
        self.FRM_LOGIN = Form_UserLogin(False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def INIT(self):
        self.reFreshAllUser()
        #self.__refreshCurrentUserRight()

    def __refreshCurrentUserRight(self):
        db = JPDb()
        uid = self.currentUserID()
        sql = '''
            SELECT n.*
            FROM (
            SELECT {} AS `fUserID`, t.*
            FROM sysnavigationmenus AS t where t.fIsCommandButton=0) AS n
            LEFT JOIN sysuserright AS r ON n.fNMID=r.fRightID AND n.fUserID=r.fUserID 
            WHERE r.fHasRight=1
            ORDER BY n.fDispIndex'''.format(uid)
        self.__CurrentUserRight = db.getDict(sql)
        pass

    def currentUserRight(self):
        return self.__CurrentUserRight

    def setCurrentUserID(self, user_id: int):
        self.__ID = user_id
        self.Name = [r[1] for r in self.__AllUser if r[0] == self.__ID][0]
        self.__refreshCurrentUserRight()
        self.userChange.emit([self.__ID, self.Name])

    def getAllUserList(self) -> list:
        return [r[0:2] for r in self.__AllUser]

    def getAllUserEnumList(self) -> list:
        return [[r[1], r[0]] for r in self.__AllUser]

    def __bool__(self):
        return self.Name and self.__ID


@Singleton
class JPPub():
    def __init__(self):
        self.user = JPUser()
        db = JPDb()
        sql = '''select fCustomerName,fCustomerID,fNUIT,
                fCity,fContato from t_customer'''
        self.customerList = db.getDataList(sql)
        sql = '''select fCustomerName,fCustomerID,
            fNUIT,fCity,fContato from t_customer'''
        self.__allCustomerList = db.getDataList(sql)

        def getEnumDict() -> dict:
            sql = '''select fTypeID,fTitle,fItemID,fSpare1,
                    fSpare2,fNote from t_enumeration'''
            rows = db.getDataList(sql)
            return {
                k: [row1[1:] for row1 in rows if row1[0] == k]
                for k in set(row[0] for row in rows)
            }

        self.__EnumDict = getEnumDict()
        sql = """
            SELECT fNMID, fMenuText, fParentId, fCommand, fObjectName, fIcon,
                    cast(fIsCommandButton AS SIGNED) AS fIsCommandButton
            FROM sysnavigationmenus
            WHERE fEnabled=1 AND fNMID>1
            ORDER BY fDispIndex
            """
        self.__sysNavigationMenusDict = db.getDict(sql)
        a = [
            row for row in self.__sysNavigationMenusDict if row["fNMID"] == 13
        ]

    def getEnumList(self, enum_type_id: int):
        return self.__EnumDict[enum_type_id]

    def getCustomerList(self):
        return self.__allCustomerList

    def getSysNavigationMenusDict(self):
        return self.__sysNavigationMenusDict


def loadTreeview(treeWidget, items, hasCommandButton=False):
    class MyThreadReadTree(QThread):  # 加载功能树的线程类
        def __init__(self, treeWidget, items):
            super().__init__()
            root = QTreeWidgetItem(treeWidget)
            root.setText(0, "Function")
            root.FullPath = "Function"
            self.root = root
            self.items = items
            self.hasCommandButton = 1 if hasCommandButton else 0
            self.icopath = getcwd() + "\\res\\ico\\"

        def addItems(self, parent, items):
            for r in items:
                item = QTreeWidgetItem(parent)
                item.setText(0, r["fMenuText"])
                item.setIcon(0, QIcon(self.icopath + r["fIcon"]))
                item.jpData = r
                item.FullPath = (parent.FullPath + '\\' + r["fMenuText"])
                self.addItems(
                    item,
                    [l for l in self.items if l["fParentId"] == r["fNMID"]])
                item.setExpanded(1)

        def run(self):  # 线程执行函数
            self.addItems(self.root, 
                          [l for l in self.items if l["fParentId"] == 0])
            self.root.setExpanded(True)

        def getRoot(self):
            return

    _readTree = MyThreadReadTree(treeWidget, items)
    _readTree.run()


# def loadTreeview(treeWidget, items, hasCommandButton=False):
#     class MyThreadReadTree(QThread):  # 加载功能树的线程类
#         def __init__(self, treeWidget, items):
#             super().__init__()
#             root = QTreeWidgetItem(treeWidget)
#             root.setText(0, "Function")
#             root.FullPath = "Function"
#             self.root = root
#             self.items = items
#             self.hasCommandButton = 1 if hasCommandButton else 0

#         def run(self):  # 线程执行函数
#             def additemtotree(parent, nmid, items, begin=0):
#                 for i in range(begin, len(items)):
#                     if items[i]["fParentId"] == nmid and items[i][
#                             "fIsCommandButton"] == self.hasCommandButton:
#                         item = QTreeWidgetItem(parent)
#                         item.setText(0, items[i]["fMenuText"])
#                         item.setIcon(
#                             0,
#                             QIcon(getcwd() + "\\res\\ico\\" +
#                                   items[i]["fIcon"]))
#                         item.jpData = items[i]
#                         item.FullPath = (parent.FullPath + '\\' +
#                                          items[i]["fMenuText"])
#                         additemtotree(item, items[i]["fNMID"], items, i)
#                         item.setExpanded(1)

#             additemtotree(self.root, 1, self.items)
#             self.root.setExpanded(True)

#         def getRoot(self):
#             return

#     _readTree = MyThreadReadTree(treeWidget, items)
#     _readTree.run()