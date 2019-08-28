from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

#from lib.JPDatebase import JPMySqlSingleTableQuery as JPQ, JPDb, getDict
from lib.JPDatabase.Database import JPDb
from lib.JPFunction import Singleton
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox, QDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QObject
from PyQt5.QtGui import QIcon
from Ui.Ui_FormUserLogin import Ui_Dialog as Ui_Dialog_Login
from Ui.Ui_FormChangePassword import Ui_Dialog as Ui_Dialog_ChnPwd
from lib.JPFunction import md5_passwd, setWidgetIconByName


class Form_ChangePassword(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.ui = Ui_Dialog_ChnPwd()
        self.ui.setupUi(self)
        setWidgetIconByName(self.ui.Login_64)
        self.exec_()

    def accept(self):
        def msgbox(msg: str):
            QMessageBox.warning(self, '提示', msg, QMessageBox.Yes,
                                QMessageBox.Yes)

        old_pw = self.ui.OldPassword.text()
        new_pw = self.ui.NewPassowrd.text()
        new_pw2 = self.ui.ConfirmPassword.text()
        uid = JPUser().currentUserID()
        if not all((old_pw, new_pw, new_pw2)):
            msgbox("请完整输入！")
            return False
        sql = """
            select fUserID from sysusers
             where fUserName='{uid}' and fPassword='{pwd}'
             """.format(uid=uid, pwd=md5_passwd(old_pw))
        if not JPDb().getDataList(sql):
            msgbox("密码错误！")
            return False
        if new_pw != new_pw2:
            msgbox("两次输入新密码不一致！")
            return False
        sql = """
            update sysusers set fPassword='{pwd}' 
            where fUserName='{uid}'""".format(uid=uid, pwd=md5_passwd(new_pw))
        self.hide()


class Form_UserLogin(QDialog):
    def __init__(self, isLogin=True):
        super().__init__()
        self.ui = Ui_Dialog_Login()
        self.ui.setupUi(self)
        setWidgetIconByName(self.ui.Login_64)
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
        sql0 = """
            select fUserID from sysusers 
            where fUserName='{username}' and fPassword='{pwd}'"""
        sql1 = """
            select fUserID from sysusers 
            where fUserID='{uid}' and fPassword='{pwd}' 
                and ord(fEnabled)=1"""
        if all((pwd, uid)):
            isAdmin = 1 if uid.upper() == 'ADMIN' else 0
            if isAdmin:
                sql = sql0.format(pwd=md5_passwd(pwd), username=uid)
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
    FRM_PASSOWRD = None

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

    def changePassword(self):
        self.FRM_PASSOWRD = Form_ChangePassword()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def INIT(self):
        self.reFreshAllUser()
        #self.__refreshCurrentUserRight()

    def __refreshCurrentUserRight(self):
        db = JPDb()
        uid = self.currentUserID()
        sql = """
            SELECT ur.fUserID, n.fNMID, n.fDispIndex, n.fParentId, 
                n.fMenuText, n.fObjectName, n.fIcon, 
                ord(n.fIsCommandButton) AS fIsCommandButton, 
                ord(ur.fHasRight) as fHasRight
            FROM sysnavigationmenus n
                RIGHT JOIN (
                    SELECT *
                    FROM sysuserright
                    WHERE fUserID = {}
                ) ur
                ON n.fNMID = ur.fRightID
            WHERE ord(n.fEnabled) = 1
            ORDER BY n.fDispIndex
        """.format(uid)
        re = db.getDict(sql)
        menu = [r for r in re if r['fIsCommandButton'] == 0]
        for r in menu:
            r['btns'] = [
                b for b in re
                if b['fParentId'] == r['fNMID'] and b['fIsCommandButton'] == 1
            ]
        self.__CurrentUserRight = menu

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
class JPPub(QObject):
    MainForm = None

    def __init__(self):
        if self.MainForm is None:
            super().__init__()
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

    def getEnumList(self, enum_type_id: int):
        return self.__EnumDict[enum_type_id]

    def getCustomerList(self):
        return self.__allCustomerList

    def getSysNavigationMenusDict(self):
        return self.__sysNavigationMenusDict
